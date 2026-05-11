#!/usr/bin/env python3
"""
Direct semantic mismatch detector:

Finds pages that claim specific assets in "Curated assets:" text
but don't actually surface downloadable links to those assets.

This detects the exact pattern:
- Page says "Curated assets: X, Y, Z"
- But only exposes subset in archive-list or links
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_curated_assets_claim(html_text: str) -> list[str]:
    """Extract what the page claims are 'Curated assets'."""
    pattern = r'Curated assets:\s*([^<]+)'
    match = re.search(pattern, html_text)
    if not match:
        return []
    
    claim_text = match.group(1)
    # Split by comma and clean up
    items = [item.strip() for item in claim_text.split(",")]
    # Also handle "and" separator
    result = []
    for item in items:
        parts = item.split(" and ")
        result.extend([p.strip() for p in parts])
    return result


def parse_exposed_assets(html_text: str) -> list[tuple[str, str]]:
    """Extract visible asset links: (label, href)."""
    # Find archive-item or direct links with text labels
    pattern = r'<a\s+[^>]*href="([^"]*)"[^>]*>.*?<strong>([^<]+)</strong>'
    matches = re.findall(pattern, html_text, re.DOTALL)
    return [(label.strip(), href.strip()) for href, label in matches]


def main() -> None:
    print("=== SEMANTIC MISMATCH: CLAIMED vs EXPOSED ASSETS ===\n")
    
    findings = []
    
    for page_path in sorted((ROOT / "supporting").glob("*.html")) + sorted((ROOT / "featured").glob("*.html")):
        if page_path.name == "index.html":
            continue
        
        html = page_path.read_text(errors="ignore")
        claimed = parse_curated_assets_claim(html)
        exposed = parse_exposed_assets(html)
        
        if not claimed:
            continue
        
        # Normalize for comparison (lowercase, singular/plural)
        claimed_normalized = {c.lower().rstrip("s").rstrip("e") for c in claimed}
        exposed_labels = {label.lower().rstrip("s").rstrip("e") for label, _ in exposed}
        
        # Find uncovered claims
        uncovered = claimed_normalized - exposed_labels
        
        if uncovered and len(exposed) < len(claimed):
            findings.append({
                "page": str(page_path.relative_to(ROOT)),
                "claimed": claimed,
                "claimed_count": len(claimed),
                "exposed_count": len(exposed),
                "exposed_labels": [label for label, _ in exposed],
                "uncovered": uncovered,
            })
    
    if findings:
        print(f"Found {len(findings)} pages with claimed vs exposed asset mismatches:\n")
        
        for finding in findings:
            print(f"📄 {finding['page']}")
            print(f"   Claims: {', '.join(finding['claimed'])}")
            print(f"   Exposed ({finding['exposed_count']}/{finding['claimed_count']}): {', '.join(finding['exposed_labels'])}")
            if finding["uncovered"]:
                print(f"   ⚠️  Not surfaced: {', '.join(finding['uncovered'])}")
            print()
    else:
        print("✅ All pages match claims with exposed assets.")


if __name__ == "__main__":
    main()
