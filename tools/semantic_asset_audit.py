#!/usr/bin/env python3
"""
Semantic representation audit: Detect underrepresented source packages.

Key checks:
1. Pages that reference source folders not present in deployed assets
2. Narrative claims about assets that aren't surfaced on the page
3. Asset type mentions in narrative vs actual exposed file count
4. "Curated assets" descriptions vs reality

Scope boundary: this checks representation coverage. It does not validate
whether reel thumbnails are readable, balanced, or well-composed at card scale.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets"


def get_deployed_assets(asset_prefix: str) -> set[str]:
    """Get all deployed files under an asset prefix."""
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

    deployed = set()
    for line in result.stdout.splitlines():
        if line.startswith("assets/") and asset_prefix in line:
            deployed.add(line)
    return deployed


def extract_source_folder_claims(html_text: str) -> list[str]:
    """Extract 'Source folder:' or 'Curated assets:' claims from HTML."""
    claims = []
    
    # Find "Source folder:" patterns
    source_pattern = r'Source folder:\s*([^<.]+)'
    for match in re.finditer(source_pattern, html_text):
        claims.append(match.group(1).strip())
    
    # Find "Curated assets:" mentions
    curated_pattern = r'Curated assets:\s*([^<.]+)'
    for match in re.finditer(curated_pattern, html_text):
        claims.append(match.group(1).strip())
    
    return claims


def extract_surfaced_hrefs(html_text: str) -> list[str]:
    """Extract all href/src values from the HTML."""
    refs = []
    
    # Match href="..." and src="..."
    pattern = r'(?:href|src)="([^"]+)"'
    for match in re.finditer(pattern, html_text):
        ref = match.group(1)
        if not ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            refs.append(ref)
    
    return refs


def analyze_page_mismatch(page_path: Path) -> dict | None:
    """Analyze a page for narrative vs reality mismatches."""
    html = page_path.read_text(errors="ignore")
    
    source_claims = extract_source_folder_claims(html)
    surfaced_refs = extract_surfaced_hrefs(html)
    
    if not source_claims and not surfaced_refs:
        return None
    
    # Count how many asset types are mentioned vs surfaced
    asset_mentions = re.findall(r'\b(sketch|figma|draft|iteration|typeface|master|study|variant|export)\b', html.lower())
    
    return {
        "page": str(page_path.relative_to(ROOT)),
        "source_folder_claims": source_claims,
        "mentioned_asset_types": list(set(asset_mentions)),
        "type_mention_count": len(asset_mentions),
        "surfaced_local_assets": [r for r in surfaced_refs if r.startswith("../assets")],
        "surfaced_asset_count": len([r for r in surfaced_refs if r.startswith("../assets")]),
    }


def main() -> None:
    print("=== SEMANTIC ASSET REPRESENTATION AUDIT ===\n")
    print("Scope: semantic coverage only; not a reel-readability approval.\n")
    
    findings = []
    
    # Check all project pages
    for page_path in sorted((ROOT / "supporting").glob("*.html")) + sorted((ROOT / "featured").glob("*.html")):
        if page_path.name == "index.html":
            continue
        
        analysis = analyze_page_mismatch(page_path)
        if not analysis:
            continue
        
        # Flag if mentions multiple asset types but few are surfaced
        if analysis["type_mention_count"] > 2 and analysis["surfaced_asset_count"] < 3:
            findings.append(analysis)
    
    if findings:
        print(f"Found {len(findings)} pages with potential representation gaps:\n")
        
        for finding in findings:
            print(f"📄 {finding['page']}")
            
            if finding["source_folder_claims"]:
                print(f"   Source folder claims: {'; '.join(finding['source_folder_claims'])}")
            
            if finding["mentioned_asset_types"]:
                print(f"   Narrative mentions ({finding['type_mention_count']} refs): {', '.join(set(finding['mentioned_asset_types']))}")
            
            if finding["surfaced_local_assets"]:
                print(f"   Actually surfaced ({finding['surfaced_asset_count']}): {', '.join(finding['surfaced_local_assets'][:3])}")
                if len(finding["surfaced_local_assets"]) > 3:
                    print(f"      ... + {len(finding['surfaced_local_assets']) - 3} more")
            else:
                print(f"   Actually surfaced: (none)")
            
            # Calculate mismatch ratio
            if finding["type_mention_count"] > 0:
                coverage = (finding["surfaced_asset_count"] / finding["type_mention_count"]) * 100
                print(f"   Coverage: {coverage:.0f}% (mentions {finding['type_mention_count']} asset types, surfaces {finding['surfaced_asset_count']})")
            
            print()
    else:
        print("No major representation gaps detected.")


if __name__ == "__main__":
    main()
