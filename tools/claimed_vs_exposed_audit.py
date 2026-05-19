#!/usr/bin/env python3
"""
Direct semantic mismatch detector:

Finds pages that claim specific assets in "Curated assets:" text
but don't actually surface downloadable links to those assets.

This detects the exact pattern:
- Page says "Curated assets: X, Y, Z"
- But only exposes subset in links or visible images

Scope boundary: this checks truthful exposure, not reel readability. A passing
result does not approve thumbnail composition at card scale.
"""

from __future__ import annotations

import re
from pathlib import Path
from html.parser import HTMLParser


ROOT = Path(__file__).resolve().parents[1]


class ExposureParser(HTMLParser):
    """Collect page-visible assets and the text/alt labels that describe them."""

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
    """Return true for concrete portfolio artifacts, not nav/page chrome."""
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
        return False
    ref_lower = ref.lower()
    if any(part in ref_lower for part in ("/assets/", "/images/", "assets/", "images/")):
        return True
    return bool(re.search(r"\.(pdf|png|jpe?g|gif|webp|ipynb|py|java|pde|md|docx|zip|jar|r)$", ref_lower))


def parse_curated_assets_claim(html_text: str) -> list[str]:
    """Extract what the page claims are 'Curated assets'."""
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
    claim_text = " ".join(claim_sentences)

    # Split by comma and clean up
    items = [item.strip() for item in claim_text.split(",")]
    # Also handle "and" separator
    result = []
    for item in items:
        parts = item.split(" and ")
        result.extend([p.strip() for p in parts])
    return [item.rstrip(".").strip() for item in result if item.rstrip(".").strip()]


def parse_exposed_assets(html_text: str) -> list[tuple[str, str]]:
    """Extract visible asset links: (label, href)."""
    parser = ExposureParser()
    parser.feed(html_text)
    return parser.exposures


def normalize(text: str) -> str:
    """Normalize asset wording so 'Final PNG' can match a final png link/href."""
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
    """Return true when a claim is concretely represented by label, href, or alt."""
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


def main() -> None:
    print("=== SEMANTIC MISMATCH: CLAIMED vs EXPOSED ASSETS ===\n")
    print("Scope: asset exposure only; not a reel-composition approval.\n")
    
    findings = []
    
    for page_path in sorted((ROOT / "supporting").glob("*.html")) + sorted((ROOT / "featured").glob("*.html")):
        if page_path.name == "index.html":
            continue
        
        html = page_path.read_text(errors="ignore")
        claimed = parse_curated_assets_claim(html)
        exposed = parse_exposed_assets(html)
        
        if not claimed:
            continue
        
        uncovered = [claim for claim in claimed if not claim_is_exposed(claim, exposed)]

        if uncovered:
            findings.append({
                "page": str(page_path.relative_to(ROOT)),
                "claimed": claimed,
                "claimed_count": len(claimed),
                "exposed_count": len(exposed),
                "exposed_labels": [label for label, _ in exposed[:8]],
                "uncovered": uncovered,
            })
    
    if findings:
        print(f"Found {len(findings)} pages with claimed vs exposed asset mismatches:\n")
        
        for finding in findings:
            print(f"📄 {finding['page']}")
            print(f"   Claims: {', '.join(finding['claimed'])}")
            print(f"   Exposed ({finding['exposed_count']}/{finding['claimed_count']}): {', '.join(finding['exposed_labels'])}")
            if finding["uncovered"]:
                print(f"   Warning lead: not concretely surfaced: {', '.join(finding['uncovered'])}")
            print()
    else:
        print("✅ All pages match claims with exposed assets.")


if __name__ == "__main__":
    main()
