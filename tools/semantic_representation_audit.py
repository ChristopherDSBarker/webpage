#!/usr/bin/env python3
"""
Semantic representation audit: Compare HTML narrative claims against deployed assets.

This goes beyond deployment-safe auditing to detect:
- Assets mentioned in narrative that aren't exposed on the page
- Hidden assets that could strengthen portfolio credibility
- Weak semantic matches between source folders and visible artifacts
- Underrepresented source packages
- Reel thumbnails that exist but are likely weak at card scale
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
PROJECTS_PAGE = ROOT / "projects.html"

REEL_SECTIONS = {
    "featured-reel": "Featured Projects Reel",
    "supporting-reel": "Supporting Work Reel",
}

GAMEPLAY_UI_TERMS = {
    "game",
    "gameplay",
    "minesweeper",
    "battleship",
    "pixel",
    "resume",
    "portfolio",
    "ui",
    "app",
    "web",
}

ARTIFACT_DESIGN_TERMS = {
    "design",
    "poster",
    "spread",
    "publication",
    "typography",
    "package",
    "branding",
    "sticker",
    "env",
    "environment",
    "campaign",
    "documentary",
    "animation",
    "scene",
}

DOCUMENT_PAGE_TERMS = {
    "pdf preview",
    "poster",
    "publication",
    "magazine spread",
    "presentation",
    "title slide",
    "report",
    "full page",
    "page preview",
    "design board",
}

WEAK_FOCAL_TERMS = {
    "workflow card",
    "title slide",
    "full poster",
    "pdf preview",
}

GAMEPLAY_REVIEW_TERMS = {
    "minesweeper",
    "battleship",
    "csci 367",
}


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


def attr_value(attrs: str, name: str) -> str:
    """Extract a quoted HTML attribute from a small tag string."""
    match = re.search(rf'\b{name}="([^"]*)"', attrs)
    return match.group(1).strip() if match else ""


def strip_tags(text: str) -> str:
    """Return compact text from a small HTML fragment."""
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def classify_reel_category(card: dict) -> str:
    """Classify a reel card by intended visual composition, not project taxonomy."""
    haystack = " ".join(
        str(card.get(key, "")) for key in ("title", "href", "src", "alt", "body_text")
    ).lower()
    if any(term in haystack for term in ARTIFACT_DESIGN_TERMS):
        return "Artifact/Design"
    if any(term in haystack for term in GAMEPLAY_UI_TERMS):
        return "Gameplay/UI"
    return "Diagram/System"


def extract_reel_cards() -> list[dict]:
    """Extract visible card metadata from the projects page reels."""
    if not PROJECTS_PAGE.exists():
        return []

    html = PROJECTS_PAGE.read_text(errors="ignore")
    cards: list[dict] = []
    section_pattern = re.compile(
        r'<section[^>]*id="(?P<section>featured-reel|supporting-reel)"[^>]*>'
        r'(?P<body>.*?)</section>',
        re.DOTALL,
    )
    card_pattern = re.compile(
        r'<a\s+class="project-card"(?P<a_attrs>[^>]*)>(?P<body>.*?)</a>',
        re.DOTALL,
    )

    for section_match in section_pattern.finditer(html):
        section_id = section_match.group("section")
        for card_match in card_pattern.finditer(section_match.group("body")):
            body = card_match.group("body")
            a_attrs = card_match.group("a_attrs")
            img_match = re.search(r"<img(?P<img_attrs>[^>]*)>", body, re.DOTALL)
            fallback_match = re.search(
                r'<div\s+class="(?P<class>[^"]*\bvisual-thumb\b[^"]*)"',
                body,
                re.DOTALL,
            )
            title_match = re.search(r"<h3>(?P<title>.*?)</h3>", body, re.DOTALL)

            img_attrs = img_match.group("img_attrs") if img_match else ""
            src = attr_value(img_attrs, "src")
            alt = attr_value(img_attrs, "alt")
            classes = attr_value(img_attrs, "class")
            if fallback_match:
                classes = f"{classes} {fallback_match.group('class')}".strip()

            cards.append(
                {
                    "section": section_id,
                    "section_label": REEL_SECTIONS[section_id],
                    "href": attr_value(a_attrs, "href"),
                    "title": strip_tags(title_match.group("title")) if title_match else "(untitled card)",
                    "src": src,
                    "alt": alt,
                    "classes": classes,
                    "uses_image": bool(src),
                    "uses_fallback": bool(fallback_match) or not src,
                    "body_text": strip_tags(body),
                }
            )

    return cards


def reel_asset_exists(card: dict) -> bool:
    """Return whether a card's image source resolves locally."""
    src = card.get("src")
    if not src:
        return False
    target = (PROJECTS_PAGE.parent / src).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return False
    return target.exists()


def visual_style(card: dict) -> str:
    """Return a coarse visual style for neighboring-card review leads."""
    if card.get("uses_fallback"):
        return "fallback"
    haystack = f"{card.get('title', '')} {card.get('src', '')} {card.get('alt', '')}".lower()
    if any(term in haystack for term in DOCUMENT_PAGE_TERMS):
        return "document"
    category = classify_reel_category(card)
    if category == "Gameplay/UI":
        return "gameplay-ui"
    if category == "Artifact/Design":
        return "artifact-design"
    return "diagram-system"


def add_reel_finding(findings: list[dict], card: dict, issue: str, detail: str) -> None:
    findings.append(
        {
            "section": card["section_label"],
            "title": card["title"],
            "category": classify_reel_category(card),
            "issue": issue,
            "detail": detail,
        }
    )


def analyze_reel_readability() -> list[dict]:
    """Surface likely reel-readability problems for human review.

    These are heuristic leads, not art-quality scores. They intentionally warn
    when an asset exists but likely behaves like a full artifact, raw document,
    generic fallback, or weak neighbor in the reel.
    """
    cards = extract_reel_cards()
    findings: list[dict] = []

    for card in cards:
        haystack = f"{card['title']} {card['href']} {card['src']} {card['alt']} {card['body_text']}".lower()
        visual_haystack = f"{card['title']} {card['src']} {card['alt']}".lower()
        category = classify_reel_category(card)

        if card["uses_image"] and not reel_asset_exists(card):
            add_reel_finding(
                findings,
                card,
                "MISSING_REEL_IMAGE",
                "Projects reel references an image that does not resolve locally.",
            )

        if card["uses_fallback"]:
            add_reel_finding(
                findings,
                card,
                "FALLBACK_REEL_REVIEW",
                "Intentional fallback is acceptable only when no honest screenshot, output, chart, or artifact crop exists.",
            )
            continue

        if category == "Artifact/Design" and any(term in haystack for term in DOCUMENT_PAGE_TERMS):
            add_reel_finding(
                findings,
                card,
                "DOCUMENT_PAGE_REEL_LEAD",
                "Likely raw poster/PDF/page treatment; review for one extracted composition moment.",
            )

        if category == "Diagram/System" and any(term in haystack for term in ("poster", "report", "presentation")):
            add_reel_finding(
                findings,
                card,
                "SYSTEM_FLOW_SIMPLIFICATION_LEAD",
                "Likely dense artifact compression; review for one readable system flow or result cluster.",
            )

        if category == "Gameplay/UI" and any(term in haystack for term in GAMEPLAY_REVIEW_TERMS):
            add_reel_finding(
                findings,
                card,
                "GAMEPLAY_SCALE_REVIEW",
                "Verify the crop shows an interaction moment, not an entire distant screen or empty interface.",
            )

        if any(term in visual_haystack for term in WEAK_FOCAL_TERMS):
            add_reel_finding(
                findings,
                card,
                "WEAK_FOCAL_HIERARCHY_LEAD",
                "Likely needs a clearer dominant shape or focal idea at reel scale.",
            )

    for index, card in enumerate(cards):
        if not card["uses_fallback"]:
            continue
        previous_style = visual_style(cards[index - 1]) if index > 0 else ""
        next_style = visual_style(cards[index + 1]) if index + 1 < len(cards) else ""
        if previous_style != "fallback" or next_style != "fallback":
            add_reel_finding(
                findings,
                card,
                "NEIGHBOR_BALANCE_REVIEW",
                "Fallback card may visually collapse next to artifact-heavy neighbors; preserve only if intentionally honest.",
            )

    return findings


def print_reel_findings(findings: list[dict]) -> None:
    """Print compact reel-readability leads."""
    print("=== REEL READABILITY REVIEW LEADS ===\n")
    print(
        "These are human-review leads. They warn when a reel card may be "
        "semantically represented but visually weak at card scale.\n"
    )
    if not findings:
        print("No likely reel-readability leads detected.")
        return

    print(f"Found {len(findings)} reel-readability lead(s):\n")
    for finding in findings:
        print(f"REEL: {finding['section']}")
        print(f"CARD: {finding['title']}")
        print(f"CATEGORY: {finding['category']}")
        print(f"ISSUE: {finding['issue']}")
        print(f"REVIEW: {finding['detail']}")
        print()


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

    print()
    reel_findings = analyze_reel_readability()
    print_reel_findings(reel_findings)

    return 0 if not findings and not reel_findings else 1


if __name__ == "__main__":
    sys.exit(main())
