#!/usr/bin/env python3
"""
Comprehensive semantic representation audit with recommendations.

Generates a detailed report showing:
1. What the page claims vs what it exposes
2. What actually exists in deployed assets
3. Recommendations for truthful portfolio exposure
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from html.parser import HTMLParser


ROOT = Path(__file__).resolve().parents[1]


class ExposureParser(HTMLParser):
    """Collect links and images that a reviewer can actually see or open."""

    def __init__(self) -> None:
        super().__init__()
        self.exposures: list[tuple[str, str]] = []
        self._active_href: str | None = None
        self._active_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "a":
            self._active_href = data.get("href")
            self._active_text = []
        elif tag == "img":
            src = data.get("src")
            if src and is_asset_ref(src):
                self.exposures.append(((data.get("alt") or src).strip(), src.strip()))

    def handle_data(self, data: str) -> None:
        if self._active_href:
            text = data.strip()
            if text:
                self._active_text.append(text)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._active_href:
            label = " ".join(self._active_text).strip() or self._active_href
            if is_asset_ref(self._active_href):
                self.exposures.append((label, self._active_href.strip()))
            self._active_href = None
            self._active_text = []


def is_asset_ref(ref: str) -> bool:
    """Return true for concrete portfolio artifacts, not navigation links."""
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
        return False
    ref_lower = ref.lower()
    if any(part in ref_lower for part in ("/assets/", "/images/", "assets/", "images/")):
        return True
    return bool(re.search(r"\.(pdf|png|jpe?g|gif|webp|ipynb|py|java|pde|md|docx|zip|jar|r)$", ref_lower))


def get_deployed_assets(prefix: str) -> set[str]:
    """Get all deployed files matching a prefix."""
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        return set()

    assets = set()
    for line in result.stdout.splitlines():
        if prefix in line:
            assets.add(line)
    return assets


def parse_curated_assets_claim(html_text: str) -> list[str]:
    """Extract claimed 'Curated assets' from HTML."""
    pattern = r'Curated assets:\s*([^<]+)'
    match = re.search(pattern, html_text)
    if not match:
        return []
    
    claim_text = match.group(1)
    claim_sentences = []
    for sentence in re.split(r"(?<=\.)\s+", claim_text):
        lowered = sentence.lower()
        if "source/archive/internal" in lowered or "remains source" in lowered:
            continue
        claim_sentences.append(sentence)
    claim_text = " ".join(claim_sentences).replace(" and ", ", ")
    return [item.rstrip(".").strip() for item in claim_text.split(",") if item.rstrip(".").strip()]


def parse_exposed_assets(html_text: str) -> list[tuple[str, str]]:
    """Extract (label, href) for all exposed asset links."""
    parser = ExposureParser()
    parser.feed(html_text)
    return parser.exposures


def get_asset_dir_contents(asset_subdir: str) -> set[str]:
    """Get all files in a deployed asset subdirectory."""
    asset_path = ROOT / "assets" / asset_subdir
    if not asset_path.exists():
        return set()
    
    files = set()
    for file in asset_path.rglob("*"):
        if file.is_file():
            files.add(str(file.relative_to(ROOT)))
    return files


def normalize(text: str) -> str:
    """Normalize labels, hrefs, and claim phrases for fuzzy but concrete matching."""
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    noise = {
        "asset",
        "assets",
        "curated",
        "and",
        "or",
        "the",
        "a",
        "an",
        "png",
        "pdf",
        "jpg",
        "jpeg",
        "html",
        "file",
        "files",
    }
    return " ".join(part for part in text.split() if part not in noise)


def claim_is_exposed(claim: str, exposures: list[tuple[str, str]]) -> bool:
    count_match = re.search(r"\b(\d+)\s+(pdfs?|pngs?|jpe?gs?|gifs?|images?|files?)\b", claim.lower())
    if count_match:
        expected = int(count_match.group(1))
        kind = count_match.group(2)
        kind = kind.rstrip("s")
        if kind == "image":
            pattern = r"\.(png|jpe?g|gif|webp)$"
        elif kind == "file":
            pattern = r"\.[a-z0-9]+$"
        else:
            pattern = rf"\.{kind}$"
        return sum(1 for _, href in exposures if re.search(pattern, href.lower())) >= expected

    claim_norm = normalize(claim)
    if not claim_norm:
        return True

    for label, href in exposures:
        exposure_norm = normalize(f"{label} {href}")
        if claim_norm in exposure_norm or exposure_norm in claim_norm:
            return True
        claim_terms = set(claim_norm.split())
        exposure_terms = set(exposure_norm.split())
        if claim_terms and claim_terms.issubset(exposure_terms):
            return True
    return False


def analyze_page(page_path: Path) -> dict | None:
    """Full analysis of a project page."""
    html = page_path.read_text(errors="ignore")
    
    claimed = parse_curated_assets_claim(html)
    if not claimed:
        return None
    
    exposed = parse_exposed_assets(html)
    
    # Extract asset subdirectories from page references. Keep this page-specific:
    # assets/featured/env-design/x.png should scan assets/featured/env-design/,
    # not every file under assets/featured/.
    asset_refs = re.findall(r'href="\.\./(assets/[^"]+)"', html)
    asset_refs += re.findall(r'src="\.\./(assets/[^"]+)"', html)
    asset_dirs = {"/".join(ref.split("/")[:3]) for ref in asset_refs if len(ref.split("/")) >= 3}
    
    deployed = set()
    for asset_dir in asset_dirs:
        deployed.update(get_asset_dir_contents(asset_dir.removeprefix("assets/")))

    uncovered = [claim for claim in claimed if not claim_is_exposed(claim, exposed)]
    
    return {
        "page": str(page_path.relative_to(ROOT)),
        "claimed": claimed,
        "exposed": exposed,
        "deployed_assets": deployed,
        "asset_dirs": asset_dirs,
        "uncovered": uncovered,
    }


def format_recommendation(analysis: dict) -> str:
    """Generate human-readable recommendations."""
    claimed_count = len(analysis["claimed"])
    exposed_count = len(analysis["exposed"])
    deployed_count = len(analysis["deployed_assets"])
    uncovered_count = len(analysis["uncovered"])
    
    lines = []
    lines.append(f"\nPAGE ANALYSIS: {analysis['page']}")
    lines.append(f"━" * 50)
    lines.append(f"\n1. WHAT THE PAGE CLAIMS:")
    lines.append(f"   • {', '.join(analysis['claimed'])}")
    lines.append(f"   → {claimed_count} asset types mentioned")
    
    lines.append(f"\n2. WHAT'S ACTUALLY SURFACED:")
    if analysis["exposed"]:
        for label, href in analysis["exposed"][:12]:
            lines.append(f"   ✅ {label} → {href}")
        if len(analysis["exposed"]) > 12:
            lines.append(f"   ... and {len(analysis['exposed']) - 12} more page-visible refs")
    else:
        lines.append(f"   ❌ No direct asset links")
    lines.append(f"   → {exposed_count} assets exposed")
    
    lines.append(f"\n3. WHAT'S DEPLOYED IN THIS PAGE'S ASSET FOLDERS:")
    if analysis["deployed_assets"]:
        for asset in sorted(analysis["deployed_assets"])[:10]:
            lines.append(f"   📦 {asset}")
        if len(analysis["deployed_assets"]) > 10:
            lines.append(f"   ... and {len(analysis['deployed_assets']) - 10} more")
    else:
        lines.append(f"   ❌ No assets found in deployed directory")
    lines.append(f"   → {deployed_count} files available")
    
    lines.append(f"\n4. SEMANTIC REPRESENTATION GAP:")
    if uncovered_count:
        lines.append(f"   Warning lead: {uncovered_count} claimed asset type(s) were not matched to a visible link/image")
        lines.append(f"   Unmatched claims: {', '.join(analysis['uncovered'])}")
        if deployed_count:
            lines.append(f"   Some page-specific assets exist; verify whether these should be linked, shown, or classified as source/internal.")
    else:
        lines.append(f"   OK: curated asset wording is backed by visible links or images.")

    lines.append(f"\n5. RECOMMENDATIONS:")
    if uncovered_count:
        lines.append(f"   1. Tighten the claim, expose the missing item, or mark it source/archive/internal.")
        lines.append(f"   2. Prefer a visible screenshot, artifact link, or thumbnail-map entry over more process documentation.")
    else:
        lines.append(f"   1. No patch required from this warning.")
        lines.append(f"   2. If the page still feels weak, improve visual evidence rather than adding audit layers.")
    
    return "\n".join(lines)


def main() -> None:
    print("=== COMPREHENSIVE SEMANTIC REPRESENTATION AUDIT ===")
    print("Checking claimed vs exposed vs deployed assets...\n")
    
    findings = []
    
    for page_path in sorted((ROOT / "supporting").glob("*.html")) + sorted((ROOT / "featured").glob("*.html")):
        if page_path.name == "index.html":
            continue
        
        analysis = analyze_page(page_path)
        if not analysis:
            continue
        
        # Flag only if a claim cannot be matched to a visible link or image.
        if analysis["uncovered"]:
            findings.append(analysis)
    
    if not findings:
        print("✅ All project pages have matching claims and exposure.\n")
        return
    
    print(f"Found {len(findings)} pages with semantic representation gaps:\n")
    
    for analysis in findings:
        print(format_recommendation(analysis))
        print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
