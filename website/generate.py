#!/usr/bin/env python3
"""Hart Beat Energy — Site Generator.
Runs all content modules, writes ~45 HTML files under /dist."""
import pathlib, shutil, datetime, os

from build import (
    page_html, SITE_URL, BRAND,
    schema_organization, schema_local_business, schema_website,
    schema_service, schema_faq, schema_breadcrumb, schema_article,
)
import content_core
import content_maintenance
import content_company
import content_locations
import content_industries
import content_blog
import content_legal

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"

# ---- FAQ data for FAQPage schema on homepage ----
HOMEPAGE_FAQS = [
    ("Does the 30% federal solar tax credit still exist?",
     "The residential 30% federal ITC expired July 4, 2025. However, the commercial 30% ITC remains through 2032. Texas homeowners today go solar through $0-down lease or PPA contracts, where a third-party owner claims the commercial ITC and passes savings through as lower monthly payments."),
    ("How much does solar cost in Texas in 2026?",
     "With $0-down lease or PPA, Texas homeowners typically pay $89-$198/month for solar — usually lower than their existing electric bill. Cash purchases range $2.50-$3.25 per watt installed. Commercial projects average $1.80-$2.40 per watt at scale."),
    ("How long does installation take?",
     "From signed contract to utility PTO (permission to operate), typical residential projects take 6-10 weeks. The install itself is 1-2 days on-site. Commercial projects run 8-16 weeks depending on scale and utility interconnection queue."),
    ("Do you work outside Houston?",
     "Yes — Hart Beat Energy serves all 254 Texas counties. We have crews operating from Houston, Austin, Dallas/Fort Worth, San Antonio, and El Paso."),
    ("What warranty do I get?",
     "25-year production warranty, 25-year panel warranty (Tier-1 manufacturers), 12-year inverter warranty, 10-year battery warranty, and 10-year workmanship warranty on all labor."),
]


def write(path, html):
    full = DIST / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(html, encoding="utf-8")
    print(f"  ✓ {path}")


def build_all():
    DIST.mkdir(exist_ok=True)

    # copy assets dir (overwrite files individually — sandbox may block rmtree)
    assets_src = ROOT / "assets"
    assets_dst = DIST / "assets"
    if assets_src.exists():
        for src_file in assets_src.rglob("*"):
            if src_file.is_file():
                rel = src_file.relative_to(assets_src)
                dst_file = assets_dst / rel
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copy2(src_file, dst_file)
                except Exception as e:
                    print(f"  (asset copy warning: {rel} — {e})")

    # GitHub Pages custom domain + Jekyll bypass
    (DIST / "CNAME").write_text("www.hartbeat.solar\n", encoding="utf-8")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    print("  ✓ CNAME + .nojekyll")

    base_schemas = [schema_organization(), schema_local_business(), schema_website()]
    print("Building pages...")

    # ===== HOMEPAGE =====
    write("index.html", page_html(
        title="Texas Solar Installation & Maintenance",
        description="Hart Beat Energy: Texas solar sales, design, installation, and concierge maintenance. $0-down lease & PPA. Serving all 254 counties. Call (346) 330-2550.",
        canonical_path="/",
        body_html=content_core.homepage(),
        schemas=base_schemas + [schema_faq(HOMEPAGE_FAQS)],
    ))

    # ===== CORE PAGES =====
    write("residential.html", page_html(
        title="Residential Solar — $0 Down Lease & PPA",
        description="Texas home solar with $0-down lease or PPA. Monthly payments from $89. 25-year production warranty. Serving all 254 Texas counties.",
        canonical_path="/residential.html",
        body_html=content_core.residential(),
        schemas=base_schemas + [schema_service("Residential Solar", "Home solar design and install across Texas", "/residential.html")],
    ))
    write("commercial.html", page_html(
        title="Commercial Solar — 30% ITC + MACRS",
        description="Commercial solar for Texas businesses. 30% federal ITC + 5-year MACRS depreciation. Typical 5-7 year payback. All facility types.",
        canonical_path="/commercial.html",
        body_html=content_core.commercial(),
        schemas=base_schemas + [schema_service("Commercial Solar", "Commercial solar and storage for Texas businesses", "/commercial.html")],
    ))
    write("battery-storage.html", page_html(
        title="Battery Storage — Tesla Powerwall & Schneider",
        description="Backup power and self-consumption optimization with Tesla Powerwall 3 and Schneider XW Pro. Installed across Texas.",
        canonical_path="/battery-storage.html",
        body_html=content_core.battery_storage(),
        schemas=base_schemas + [schema_service("Battery Storage", "Tesla Powerwall 3 and Schneider battery installs", "/battery-storage.html")],
    ))
    write("financing.html", page_html(
        title="Solar Financing — Lease, PPA, Loan, Cash",
        description="Compare all four Texas solar financing paths: $0-down lease, PPA, solar loan, and cash purchase. Clear side-by-side math.",
        canonical_path="/financing.html",
        body_html=content_core.financing(),
        schemas=base_schemas,
    ))
    write("lease-vs-ppa.html", page_html(
        title="Solar Lease vs PPA — Which One Wins in Texas?",
        description="Detailed comparison of solar lease and PPA contracts for Texas homeowners. Escalators, buyouts, transfers, and real-world math.",
        canonical_path="/lease-vs-ppa.html",
        body_html=content_core.lease_vs_ppa(),
        schemas=base_schemas,
    ))

    # ===== MAINTENANCE =====
    write("maintenance/index.html", page_html(
        title="Solar Maintenance Services — Texas",
        description="Full-service Texas solar maintenance: cleaning, repairs, 24/7 monitoring, inspection, critter guard, and full system audits.",
        canonical_path="/maintenance/",
        body_html=content_maintenance.maintenance_hub(),
        schemas=base_schemas + [schema_service("Solar Maintenance", "Cleaning, monitoring, repairs, inspections", "/maintenance/")],
        depth=1,
    ))
    write("maintenance/cleaning.html", page_html(
        title="Solar Panel Cleaning — Texas",
        description="Professional solar panel cleaning delivers 25-30% production lift on neglected arrays. All-Texas crews, monthly to quarterly service.",
        canonical_path="/maintenance/cleaning.html",
        body_html=content_maintenance.cleaning(),
        schemas=base_schemas,
        depth=1,
    ))
    write("maintenance/repairs.html", page_html(
        title="Solar Repairs — 4hr Emergency Dispatch",
        description="24/7 solar repair dispatch across Texas. All brands serviced. Inverter, panel, string, wiring, monitoring, and roof-penetration repairs.",
        canonical_path="/maintenance/repairs.html",
        body_html=content_maintenance.repairs(),
        schemas=base_schemas,
        depth=1,
    ))
    write("maintenance/monitoring.html", page_html(
        title="Know TrueUp® Solar Monitoring",
        description="24/7 predictive solar monitoring with production guarantees, anomaly alerts, and monthly performance reports.",
        canonical_path="/maintenance/monitoring.html",
        body_html=content_maintenance.monitoring(),
        schemas=base_schemas,
        depth=1,
    ))
    write("maintenance/critter-guard.html", page_html(
        title="Critter Guard — Solar Panel Pest Protection",
        description="Stop squirrels, birds, and rodents from nesting under your solar panels. Lifetime critter guard mesh install from $399.",
        canonical_path="/maintenance/critter-guard.html",
        body_html=content_maintenance.critter_guard(),
        schemas=base_schemas,
        depth=1,
    ))
    write("maintenance/inspection.html", page_html(
        title="50-Point Solar System Inspection",
        description="Comprehensive 50-point solar inspection: electrical, mechanical, roof penetration, inverter health, and production verification.",
        canonical_path="/maintenance/inspection.html",
        body_html=content_maintenance.inspection(),
        schemas=base_schemas,
        depth=1,
    ))
    write("maintenance/audit.html", page_html(
        title="40-Page Solar System Audit",
        description="Forensic 40-page audit for underperforming systems. Identifies design flaws, shading, soiling, wiring losses, and financial recovery options.",
        canonical_path="/maintenance/audit.html",
        body_html=content_maintenance.audit(),
        schemas=base_schemas,
        depth=1,
    ))

    # ===== COMPANY =====
    write("about.html", page_html(
        title="About Hart Beat Energy",
        description="Founded 2014 in Houston. 5,000+ Texas solar installs. NABCEP-certified. Family-owned, veteran-led, all-Texas operations.",
        canonical_path="/about.html",
        body_html=content_company.about(),
        schemas=base_schemas,
    ))
    write("contact.html", page_html(
        title="Contact Hart Beat Energy — Free Quote",
        description="Get your free solar quote. Call (346) 330-2550 or fill out our form. Serving all 254 Texas counties.",
        canonical_path="/contact.html",
        body_html=content_company.contact(),
        schemas=base_schemas,
    ))
    write("reviews.html", page_html(
        title="Customer Reviews — Hart Beat Energy",
        description="4.9/5 average across 287 verified Texas homeowners and businesses. Real reviews from Houston, Austin, Dallas, and beyond.",
        canonical_path="/reviews.html",
        body_html=content_company.reviews(),
        schemas=base_schemas,
    ))
    write("faq.html", page_html(
        title="Solar FAQ — Texas Homeowners & Businesses",
        description="Answers to every question Texas homeowners and businesses ask about solar: cost, tax credits, financing, permits, HOA, warranty, and more.",
        canonical_path="/faq.html",
        body_html=content_company.faq(),
        schemas=base_schemas + [schema_faq(HOMEPAGE_FAQS)],
    ))
    write("case-studies.html", page_html(
        title="Solar Case Studies — Texas Projects",
        description="Six detailed solar case studies across Texas homes and businesses. Real systems, real costs, real savings.",
        canonical_path="/case-studies.html",
        body_html=content_company.case_studies(),
        schemas=base_schemas,
    ))
    write("warranty.html", page_html(
        title="Solar Warranty Coverage — Hart Beat Energy",
        description="25-year production, 25-year panel, 12-year inverter, 10-year battery, 10-year workmanship. Full warranty matrix.",
        canonical_path="/warranty.html",
        body_html=content_company.warranty(),
        schemas=base_schemas,
    ))
    write("storm-claims.html", page_html(
        title="Storm Damage Claims — Hail, Wind, Lightning",
        description="Texas solar storm damage inspection, insurance claim support, and rapid repair. Hail, hurricane, wind, and lightning specialists.",
        canonical_path="/storm-claims.html",
        body_html=content_company.storm_claims(),
        schemas=base_schemas,
    ))
    write("referral.html", page_html(
        title="Referral Program — $500 Residential, $2,500+ Commercial",
        description="Refer friends, family, or businesses to Hart Beat Energy and earn cash rewards. $500 per residential install, $2,500+ for commercial.",
        canonical_path="/referral.html",
        body_html=content_company.referral(),
        schemas=base_schemas,
    ))
    write("careers.html", page_html(
        title="Careers — Join Hart Beat Energy",
        description="Join a Texas-based solar team. Open positions in installation, electrical, sales, project management, and customer success.",
        canonical_path="/careers.html",
        body_html=content_company.careers(),
        schemas=base_schemas,
    ))
    write("membership.html", page_html(
        title="Solar Maintenance Membership — Essential, Complete, Commercial",
        description="Annual solar maintenance plans. Essential $29/mo, Complete $59/mo, Commercial custom. Cleaning, monitoring, repairs included.",
        canonical_path="/membership.html",
        body_html=content_company.membership(),
        schemas=base_schemas,
    ))

    # ===== LOCATIONS =====
    for slug in content_locations.CITIES:
        city_name = content_locations.CITIES[slug]["name"]
        write(f"locations/{slug}.html", page_html(
            title=f"{city_name} Solar Installation & Maintenance",
            description=f"Solar installation, financing, and maintenance in {city_name}, Texas. Local crews, fast response, full-service from Hart Beat Energy.",
            canonical_path=f"/locations/{slug}.html",
            body_html=content_locations.city_page(slug),
            schemas=base_schemas,
            depth=1,
        ))

    # ===== INDUSTRIES =====
    for slug in content_industries.INDUSTRIES:
        ind_name = content_industries.INDUSTRIES[slug]["name"]
        write(f"industries/{slug}.html", page_html(
            title=f"{ind_name} Solar — Commercial Solutions",
            description=f"Commercial solar for Texas {ind_name.lower()} facilities. 30% ITC + MACRS, 5-7 year payback. Design, install, and maintain.",
            canonical_path=f"/industries/{slug}.html",
            body_html=content_industries.industry_page(slug),
            schemas=base_schemas + [schema_service(f"{ind_name} Solar", f"Commercial solar for {ind_name.lower()}", f"/industries/{slug}.html")],
            depth=1,
        ))

    # ===== BLOG =====
    write("blog/index.html", page_html(
        title="Texas Solar Blog — Policy, Financing, How-To",
        description="Hart Beat Energy blog: Texas solar policy, lease vs PPA, ERCOT storm prep, HOA guides, and commercial case studies.",
        canonical_path="/blog/",
        body_html=content_blog.blog_index_page(),
        schemas=base_schemas,
        depth=1,
    ))
    for post in content_blog.POSTS:
        write(f"blog/{post['slug']}.html", page_html(
            title=post["title"],
            description=post["excerpt"],
            canonical_path=f"/blog/{post['slug']}.html",
            body_html=content_blog.blog_post_page(post["slug"]),
            schemas=base_schemas + [schema_article(post["title"], post["excerpt"], f"/blog/{post['slug']}.html", post["date"], post["author"])],
            depth=1,
        ))

    # ===== LEGAL =====
    write("privacy.html", page_html(
        title="Privacy Policy",
        description="Hart Beat Energy privacy policy — how we collect, use, and protect your personal information.",
        canonical_path="/privacy.html",
        body_html=content_legal.privacy_page(),
        schemas=base_schemas,
    ))
    write("terms.html", page_html(
        title="Terms of Service",
        description="Hart Beat Energy terms of service for hartbeat.solar website users.",
        canonical_path="/terms.html",
        body_html=content_legal.terms_page(),
        schemas=base_schemas,
    ))
    write("sitemap.html", page_html(
        title="Sitemap",
        description="Every page on hartbeat.solar, organized by section.",
        canonical_path="/sitemap.html",
        body_html=content_legal.sitemap_html_page(),
        schemas=base_schemas,
    ))

    # ===== ROBOTS + SITEMAP + MANIFEST =====
    write_robots()
    write_sitemap_xml()
    write_manifest()
    print(f"\n✅ Built site → {DIST}")


def write_robots():
    body = f"""User-agent: *
Allow: /
Disallow: /assets/raw/

Sitemap: {SITE_URL}/sitemap.xml
"""
    (DIST / "robots.txt").write_text(body, encoding="utf-8")
    print("  ✓ robots.txt")


def write_sitemap_xml():
    today = datetime.date.today().isoformat()
    urls = [
        ("/", "1.0", "weekly"),
        ("/residential.html", "0.9", "monthly"),
        ("/commercial.html", "0.9", "monthly"),
        ("/battery-storage.html", "0.8", "monthly"),
        ("/financing.html", "0.8", "monthly"),
        ("/lease-vs-ppa.html", "0.8", "monthly"),
        ("/contact.html", "0.9", "monthly"),
        ("/about.html", "0.6", "monthly"),
        ("/reviews.html", "0.7", "weekly"),
        ("/faq.html", "0.7", "monthly"),
        ("/case-studies.html", "0.7", "monthly"),
        ("/warranty.html", "0.5", "yearly"),
        ("/storm-claims.html", "0.6", "monthly"),
        ("/referral.html", "0.5", "monthly"),
        ("/careers.html", "0.5", "monthly"),
        ("/membership.html", "0.7", "monthly"),
        ("/maintenance/", "0.8", "monthly"),
        ("/maintenance/cleaning.html", "0.7", "monthly"),
        ("/maintenance/repairs.html", "0.7", "monthly"),
        ("/maintenance/monitoring.html", "0.7", "monthly"),
        ("/maintenance/critter-guard.html", "0.6", "monthly"),
        ("/maintenance/inspection.html", "0.6", "monthly"),
        ("/maintenance/audit.html", "0.6", "monthly"),
        ("/blog/", "0.8", "weekly"),
        ("/privacy.html", "0.3", "yearly"),
        ("/terms.html", "0.3", "yearly"),
        ("/sitemap.html", "0.4", "monthly"),
    ]
    for slug in content_locations.CITIES:
        urls.append((f"/locations/{slug}.html", "0.8", "monthly"))
    for slug in content_industries.INDUSTRIES:
        urls.append((f"/industries/{slug}.html", "0.7", "monthly"))
    for post in content_blog.POSTS:
        urls.append((f"/blog/{post['slug']}.html", "0.7", "monthly"))

    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, priority, freq in urls:
        xml.append(f"  <url><loc>{SITE_URL}{path}</loc><lastmod>{today}</lastmod><changefreq>{freq}</changefreq><priority>{priority}</priority></url>")
    xml.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(xml), encoding="utf-8")
    print("  ✓ sitemap.xml")


def write_manifest():
    manifest = {
        "name": "Hart Beat Energy",
        "short_name": "Hart Beat",
        "description": "Texas Solar Experts",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0b1f3a",
        "theme_color": "#0b1f3a",
        "icons": [
            {"src": "/assets/images/favicon.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/images/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
        ],
    }
    import json
    (DIST / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("  ✓ manifest.json")


if __name__ == "__main__":
    build_all()
