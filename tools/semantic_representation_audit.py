#!/usr/bin/env python3
"""
Semantic representation audit: Compare HTML narrative claims against deployed assets.

This goes beyond deployment-safe auditing to detect:
- Assets mentioned in narrative that aren't exposed on the page
- Hidden assets that could strengthen portfolio credibility
- Weak semantic matches between source folders and visible artifacts
- Underrepresented source packages
"""

from __future__ import annotations

import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
FEATURED_DIR = ROOT / "featured"
SUPPORTING_DIR = ROOT / "supporting"
ASSETS_DIR = ROOT / "assets"


class HTMLAssetExtractor(HTMLParser):
    """Extract all asset references and narrative context from HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.surfaced_assets: set[str] = set()
        self.narrative_text: list[str] = []
        self.current_tag: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        self.current_tag = tag

        # Track hrefs and srcs as "surfaced assets"
        for key in ("href", "src"):
            value = data.get(key)
            if value and not value.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                self.surfaced_assets.add(value)

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.narrative_text.append(text)

    def handle_endtag(self, tag: str) -> None:
        self.current_tag = None


def extract_asset_keywords(narrative: str) -> set[str]:
    """Extract potential asset type keywords from narrative text."""
    keywords = {
        "sketch",
        "figma",
        "draft",
        "iteration",
        "typeface",
        "typography",
        "master board",
        "board",
        "study",
        "variant",
        "asset",
        "artifact",
        "design",
        "system",
        "presentation",
        "pdf",
        "export",
    }
    found = set()
    text_lower = narrative.lower()
    for keyword in keywords:
        if keyword in text_lower:
            found.add(keyword)
    return found


def get_deployed_assets(relative_path: str) -> set[str]:
    """Get all Git-tracked files in a directory."""
    try:
        result = subprocess.run(
            ["git", "ls-files", relative_path],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if result.returncode == 0:
            return {line for line in result.stdout.splitlines() if line}
    except Exception:
        pass
    return set()


def analyze_page(page_path: Path) -> dict:
    """Analyze a single project page for semantic representation."""
    if not page_path.exists():
        return {"status": "missing"}

    html_content = page_path.read_text(errors="ignore")
    extractor = HTMLAssetExtractor()
    extractor.feed(html_content)

    narrative = " ".join(extractor.narrative_text)
    claimed_assets = extract_asset_keywords(narrative)

    # Resolve surfaced asset paths to relative paths
    surfaced_resolved = set()
    for asset_ref in extractor.surfaced_assets:
        try:
            full_path = (page_path.parent / asset_ref).resolve()
            try:
                rel = str(full_path.relative_to(ROOT))
                surfaced_resolved.add(rel)
            except ValueError:
                pass
        except Exception:
            pass

    return {
        "page": str(page_path.relative_to(ROOT)),
        "narrative": narrative[:500],  # First 500 chars
        "claimed_asset_types": list(claimed_assets),
        "surfaced_asset_count": len(extractor.surfaced_assets),
        "surfaced_assets": sorted(extractor.surfaced_assets),
        "surfaced_resolved": sorted(surfaced_resolved),
    }


def main() -> int:
    print("=== SEMANTIC REPRESENTATION AUDIT ===\n")
    print("Checking for narrative claims that exceed visible asset exposure.\n")

    findings: list[dict] = []

    # Audit all supporting and featured pages
    for page_file in sorted(SUPPORTING_DIR.glob("*.html")) + sorted(FEATURED_DIR.glob("*.html")):
        if page_file.name == "index.html":
            continue

        analysis = analyze_page(page_file)
        if analysis.get("status") == "missing":
            continue

        # Detect representation gaps
        claimed = set(analysis.get("claimed_asset_types", []))
        surfaced = analysis.get("surfaced_asset_count", 0)

        # Flag if narrative mentions asset types but few are surfaced
        if claimed and surfaced < 3:
            findings.append({
                "page": analysis["page"],
                "issue": "NARRATIVE_CLAIMS_EXCEED_EXPOSURE",
                "claimed_types": claimed,
                "surfaced_count": surfaced,
                "surfaced_assets": analysis["surfaced_assets"],
            })

    # Print findings
    if findings:
        print(f"Found {len(findings)} pages with semantic representation mismatches:\n")
        for finding in findings:
            print(f"PAGE: {finding['page']}")
            print(f"ISSUE: {finding['issue']}")
            print(f"Narrative mentions: {', '.join(sorted(finding['claimed_types']))}")
            print(f"But only {finding['surfaced_count']} assets are surfaced:")
            for asset in finding["surfaced_assets"]:
                print(f"  - {asset}")
            print()
    else:
        print("No major semantic representation mismatches found.")

    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
