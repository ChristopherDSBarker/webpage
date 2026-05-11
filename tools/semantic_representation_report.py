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


ROOT = Path(__file__).resolve().parents[1]


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
    
    claim_text = match.group(1).replace(" and ", ", ")
    return [item.strip() for item in claim_text.split(",")]


def parse_exposed_assets(html_text: str) -> list[tuple[str, str]]:
    """Extract (label, href) for all exposed asset links."""
    pattern = r'<a\s+[^>]*href="([^"]*)"[^>]*>.*?<strong>([^<]+)</strong>'
    matches = re.findall(pattern, html_text, re.DOTALL)
    return [(label.strip(), href.strip()) for href, label in matches]


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


def analyze_page(page_path: Path) -> dict | None:
    """Full analysis of a project page."""
    html = page_path.read_text(errors="ignore")
    
    claimed = parse_curated_assets_claim(html)
    if not claimed:
        return None
    
    exposed = parse_exposed_assets(html)
    
    # Extract asset subdirectory from page references
    asset_refs = re.findall(r'href="\.\./(assets/[^"]+)"', html)
    asset_dirs = {ref.split("/")[1] for ref in asset_refs if "/" in ref}
    
    deployed = set()
    for asset_dir in asset_dirs:
        deployed.update(get_asset_dir_contents(asset_dir))
    
    return {
        "page": str(page_path.relative_to(ROOT)),
        "claimed": claimed,
        "exposed": exposed,
        "deployed_assets": deployed,
        "asset_dirs": asset_dirs,
    }


def format_recommendation(analysis: dict) -> str:
    """Generate human-readable recommendations."""
    claimed_count = len(analysis["claimed"])
    exposed_count = len(analysis["exposed"])
    deployed_count = len(analysis["deployed_assets"])
    
    lines = []
    lines.append(f"\n📋 BRANDING SYSTEM PAGE ANALYSIS")
    lines.append(f"━" * 50)
    lines.append(f"\n1️⃣  WHAT THE PAGE CLAIMS:")
    lines.append(f"   • {', '.join(analysis['claimed'])}")
    lines.append(f"   → {claimed_count} asset types mentioned")
    
    lines.append(f"\n2️⃣  WHAT'S ACTUALLY SURFACED:")
    if analysis["exposed"]:
        for label, href in analysis["exposed"]:
            lines.append(f"   ✅ {label} → {href}")
    else:
        lines.append(f"   ❌ No direct asset links")
    lines.append(f"   → {exposed_count} assets exposed")
    
    lines.append(f"\n3️⃣  WHAT'S DEPLOYED IN ASSETS:")
    if analysis["deployed_assets"]:
        for asset in sorted(analysis["deployed_assets"])[:10]:
            lines.append(f"   📦 {asset}")
        if len(analysis["deployed_assets"]) > 10:
            lines.append(f"   ... and {len(analysis['deployed_assets']) - 10} more")
    else:
        lines.append(f"   ❌ No assets found in deployed directory")
    lines.append(f"   → {deployed_count} files available")
    
    lines.append(f"\n4️⃣  SEMANTIC REPRESENTATION GAP:")
    if deployed_count > 0 and exposed_count < claimed_count:
        gap = claimed_count - exposed_count
        lines.append(f"   ⚠️  Claims {claimed_count} assets, exposes {exposed_count}")
        lines.append(f"   ⚠️  {gap} claimed asset types are NOT directly downloadable")
        lines.append(f"   ⚠️  But {deployed_count} files are available in assets/")
    elif deployed_count == 0 and exposed_count < claimed_count:
        lines.append(f"   🚨 CRITICAL: Page claims assets that don't exist")
        lines.append(f"   🚨 Source folder may not be tracked in Git")
    else:
        lines.append(f"   ✅ Representation matches exposure")
    
    lines.append(f"\n5️⃣  RECOMMENDATIONS:")
    if deployed_count > exposed_count:
        lines.append(f"   1. Add direct download links for {deployed_count - exposed_count} hidden assets")
        lines.append(f"   2. Update 'Curated assets' claim to reflect only exposed items")
        lines.append(f"   3. Or surface more assets as an 'Additional Assets' section")
        lines.append(f"   4. Archive unexposed assets as 'source materials (not deployed)'")
    else:
        lines.append(f"   1. Verify source folder path is correct")
        lines.append(f"   2. Check Git tracking: are source assets in .gitignore?")
        lines.append(f"   3. Update claim to reflect actual exposure")
    
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
        
        # Flag if claims don't match exposure
        if len(analysis["exposed"]) < len(analysis["claimed"]):
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
