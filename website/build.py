#!/usr/bin/env python3
"""
Hart Beat Energy — Static Site Generator
Generates a complete production-ready website from this single file.
Run: python3 build.py
"""
import json, os, pathlib, html, datetime

ROOT = pathlib.Path(__file__).parent
SITE_URL = "https://www.hartbeat.solar"
BUILD_YEAR = datetime.date.today().year

# ============================================================
# BRAND CONFIG
# ============================================================
BRAND = {
    "name": "Hart Beat Energy",
    "tagline": "Texas Solar Experts",
    "phone_display": "(346) 330-2550",
    "phone_raw": "+13463302550",
    "phone_href": "tel:3463302550",
    "email": "support@hartbeat.solar",
    "address": {
        "street": "",
        "city": "Houston",
        "region": "TX",
        "postal": "77002",
        "country": "US",
        "lat": 29.7604,
        "lng": -95.3698,
    },
    "hours": "Mo-Fr 08:00-18:00, Sa 09:00-15:00",
    "founded": 2014,
    "social": {
        "facebook": "https://www.facebook.com/hartbeatenergy",
        "instagram": "https://www.instagram.com/hartbeatenergy",
        "linkedin": "https://www.linkedin.com/company/hartbeat-energy",
        "youtube": "https://www.youtube.com/@hartbeatenergy",
        "tiktok": "https://www.tiktok.com/@hartbeatenergy",
        "x": "https://x.com/hartbeatenergy",
    },
    "service_area": "Texas",
    "price_range": "$$-$$$",
}

# ============================================================
# SCHEMA (JSON-LD) BUILDERS
# ============================================================
def schema_organization():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE_URL}/#organization",
        "name": BRAND["name"],
        "url": SITE_URL,
        "logo": f"{SITE_URL}/assets/images/logo.png",
        "telephone": BRAND["phone_raw"],
        "email": BRAND["email"],
        "foundingDate": str(BRAND["founded"]),
        "description": "Texas solar sales, design, installation, and concierge maintenance across all 254 counties.",
        "sameAs": list(BRAND["social"].values()),
        "address": {
            "@type": "PostalAddress",
            "streetAddress": BRAND["address"]["street"],
            "addressLocality": BRAND["address"]["city"],
            "addressRegion": BRAND["address"]["region"],
            "postalCode": BRAND["address"]["postal"],
            "addressCountry": BRAND["address"]["country"],
        },
    }

def schema_local_business():
    return {
        "@context": "https://schema.org",
        "@type": "SolarPowerStation",
        "@id": f"{SITE_URL}/#business",
        "name": BRAND["name"],
        "image": f"{SITE_URL}/assets/images/og-default.jpg",
        "url": SITE_URL,
        "telephone": BRAND["phone_raw"],
        "email": BRAND["email"],
        "priceRange": BRAND["price_range"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": BRAND["address"]["street"],
            "addressLocality": BRAND["address"]["city"],
            "addressRegion": BRAND["address"]["region"],
            "postalCode": BRAND["address"]["postal"],
            "addressCountry": BRAND["address"]["country"],
        },
        "geo": {"@type": "GeoCoordinates", "latitude": BRAND["address"]["lat"], "longitude": BRAND["address"]["lng"]},
        "openingHours": BRAND["hours"],
        "areaServed": {"@type": "State", "name": "Texas"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "287"},
        "sameAs": list(BRAND["social"].values()),
    }

def schema_website():
    return {
        "@context": "https://schema.org", "@type": "WebSite",
        "@id": f"{SITE_URL}/#website", "url": SITE_URL, "name": BRAND["name"],
        "publisher": {"@id": f"{SITE_URL}/#organization"},
        "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": f"{SITE_URL}/search?q={{search_term_string}}"}, "query-input": "required name=search_term_string"},
    }

def schema_service(name, desc, url, service_type="Solar energy service"):
    return {
        "@context": "https://schema.org", "@type": "Service",
        "name": name, "description": desc, "url": f"{SITE_URL}{url}",
        "provider": {"@id": f"{SITE_URL}/#organization"},
        "areaServed": {"@type": "State", "name": "Texas"},
        "serviceType": service_type,
    }

def schema_faq(items):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items],
    }

def schema_breadcrumb(items):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "item": f"{SITE_URL}{u}"} for i, (n, u) in enumerate(items)],
    }

def schema_article(title, desc, url, date, author="Hart Beat Energy"):
    return {
        "@context": "https://schema.org", "@type": "Article",
        "headline": title, "description": desc, "url": f"{SITE_URL}{url}",
        "datePublished": date, "dateModified": date,
        "author": {"@type": "Organization", "name": author},
        "publisher": {"@id": f"{SITE_URL}/#organization"},
        "image": f"{SITE_URL}/assets/images/og-default.jpg",
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE_URL}{url}"},
    }

# ============================================================
# TEMPLATE COMPONENTS
# ============================================================
def render_schema(schemas):
    if not schemas: return ""
    out = []
    for s in schemas:
        out.append(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>')
    return "\n".join(out)

LOGO_SVG = '''<img class="nav__logo-mark" src="{BASE}assets/images/hartbeat-logo.png" alt="Hart Beat Energy" width="52" height="52"><span class="nav__logo-text">Hart Beat<br>Energy</span>'''

# ============================================================
# IMAGE LIBRARY — Unsplash (solar photography) + local brand imagery
# ============================================================
IMG = {
    # Hero photography (Unsplash, from existing live site + expanded)
    "hero_home": "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1920&auto=format&fit=crop&q=80",  # rooftop solar panels sunset
    "hero_residential": "https://images.unsplash.com/photo-1611365892117-00bd9f9f2f38?w=1920&auto=format&fit=crop&q=80",  # home with solar
    "hero_commercial": "https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=1920&auto=format&fit=crop&q=80",  # commercial array
    "hero_battery": "https://images.unsplash.com/photo-1548337138-e87d889cc369?w=1920&auto=format&fit=crop&q=80",  # tesla powerwall / battery room
    "hero_maintenance": "https://images.unsplash.com/photo-1559302504-64aae6ca6b6d?w=1920&auto=format&fit=crop&q=80",  # worker on panels
    "hero_contact": "https://images.unsplash.com/photo-1497440001374-f26997328c1b?w=1920&auto=format&fit=crop&q=80",  # houston skyline
    "hero_about": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1920&auto=format&fit=crop&q=80",  # texas solar
    "hero_financing": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1920&auto=format&fit=crop&q=80",  # calculator + docs
    "hero_blog": "https://images.unsplash.com/photo-1497493292307-31c376b6e479?w=1920&auto=format&fit=crop&q=80",  # newspaper/reading
    "hero_faq": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1920&auto=format&fit=crop&q=80",  # texas home
    "hero_reviews": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=1920&auto=format&fit=crop&q=80",  # happy family home
    "hero_cases": "https://images.unsplash.com/photo-1558449028-b53a39d100fc?w=1920&auto=format&fit=crop&q=80",  # engineer + solar
    "hero_warranty": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=1920&auto=format&fit=crop&q=80",  # handshake
    "hero_storm": "https://images.unsplash.com/photo-1580193769210-b8d1c049a7d9?w=1920&auto=format&fit=crop&q=80",  # storm clouds
    "hero_referral": "https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1920&auto=format&fit=crop&q=80",  # handshake
    "hero_careers": "https://images.unsplash.com/photo-1521791055366-0d553872125f?w=1920&auto=format&fit=crop&q=80",  # team
    "hero_membership": "https://images.unsplash.com/photo-1581094288338-2314dddb7ece?w=1920&auto=format&fit=crop&q=80",  # worker service

    # Maintenance detail pages
    "maint_cleaning": "https://images.unsplash.com/photo-1592833159057-6faf31037c8c?w=1920&auto=format&fit=crop&q=80",
    "maint_repairs": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1920&auto=format&fit=crop&q=80",
    "maint_monitoring": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920&auto=format&fit=crop&q=80",  # dashboard
    "maint_critter": "https://images.unsplash.com/photo-1601758003122-53c40e686a19?w=1920&auto=format&fit=crop&q=80",
    "maint_inspection": "https://images.unsplash.com/photo-1615715616181-6ba3f61c7865?w=1920&auto=format&fit=crop&q=80",
    "maint_audit": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1920&auto=format&fit=crop&q=80",

    # Content imagery (feature sections, cards)
    "feature_home": "https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=1200&auto=format&fit=crop&q=80",  # house w/ panels
    "feature_savings": "https://images.unsplash.com/photo-1579621970795-87facc2f976d?w=1200&auto=format&fit=crop&q=80",  # cash savings
    "feature_install": "https://images.unsplash.com/photo-1605980413988-9ff24c537935?w=1200&auto=format&fit=crop&q=80",  # install crew
    "feature_team": "https://images.unsplash.com/photo-1529400971008-f566de0e6dfc?w=1200&auto=format&fit=crop&q=80",  # team meeting
    "feature_design": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&auto=format&fit=crop&q=80",  # blueprint/design
    "feature_roof": "https://images.unsplash.com/photo-1613665813446-82a78c468a1d?w=1200&auto=format&fit=crop&q=80",  # rooftop
    "feature_panel_closeup": "https://images.unsplash.com/photo-1513151233558-d860c5398176?w=1200&auto=format&fit=crop&q=80",
    "feature_family": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=1200&auto=format&fit=crop&q=80",
    "feature_sunrise": "https://images.unsplash.com/photo-1501084817091-a4f3d1d19e07?w=1200&auto=format&fit=crop&q=80",
    "feature_warehouse": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1200&auto=format&fit=crop&q=80",
    "feature_factory": "https://images.unsplash.com/photo-1513828583688-c52646db42da?w=1200&auto=format&fit=crop&q=80",
    "feature_retail": "https://images.unsplash.com/photo-1555529902-5261145633bf?w=1200&auto=format&fit=crop&q=80",
    "feature_farm": "https://images.unsplash.com/photo-1500595046743-cd271d694d30?w=1200&auto=format&fit=crop&q=80",
    "feature_hotel": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?w=1200&auto=format&fit=crop&q=80",
    "feature_hospital": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1200&auto=format&fit=crop&q=80",

    # Texas city imagery
    "city_houston": "https://images.unsplash.com/photo-1570193910014-8eb14e93b7aa?w=1920&auto=format&fit=crop&q=80",
    "city_austin": "https://images.unsplash.com/photo-1588862057-dabe9fe6a6d9?w=1920&auto=format&fit=crop&q=80",
    "city_dallas": "https://images.unsplash.com/photo-1531218150217-54595bc2b934?w=1920&auto=format&fit=crop&q=80",
    "city_sanantonio": "https://images.unsplash.com/photo-1612892010902-83c9f8e6b0e3?w=1920&auto=format&fit=crop&q=80",
    "city_fortworth": "https://images.unsplash.com/photo-1579033461380-adb47c3eb938?w=1920&auto=format&fit=crop&q=80",
    "city_elpaso": "https://images.unsplash.com/photo-1564419429444-f7e2a8f9a9c9?w=1920&auto=format&fit=crop&q=80",
}

def nav_html(active=""):
    depth_prefix = ""  # adjust at page level
    return f'''
<a href="#main" class="sr-only">Skip to content</a>
<div class="kicker-bar">⚡ Serving all 254 Texas counties — <a href="{{BASE}}contact.html">Get your $0-down solar quote →</a></div>
<nav class="nav" aria-label="Primary">
  <div class="container nav__inner">
    <a href="{{BASE}}index.html" class="nav__logo" aria-label="Hart Beat Energy home">{LOGO_SVG}</a>
    <ul class="nav__links" role="menubar">
      <li role="none"><a role="menuitem" href="{{BASE}}index.html">Home</a></li>
      <li role="none"><a role="menuitem" href="{{BASE}}residential.html">Residential</a>
        <div class="nav__dropdown">
          <a href="{{BASE}}residential.html">Residential Solar<small>Home systems designed for your roof</small></a>
          <a href="{{BASE}}battery-storage.html">Battery Storage<small>Tesla Powerwall + Schneider</small></a>
          <a href="{{BASE}}financing.html">Financing<small>Lease, PPA, loan, cash</small></a>
          <a href="{{BASE}}lease-vs-ppa.html">Lease vs PPA<small>Which path fits you?</small></a>
        </div>
      </li>
      <li role="none"><a role="menuitem" href="{{BASE}}commercial.html">Commercial</a>
        <div class="nav__dropdown">
          <a href="{{BASE}}commercial.html">Commercial Solar<small>Portfolios & single-site</small></a>
          <a href="{{BASE}}industries/manufacturing.html">Manufacturing<small>Peak-load shaving</small></a>
          <a href="{{BASE}}industries/logistics.html">Logistics &amp; Warehousing<small>Rooftop &amp; cold storage</small></a>
          <a href="{{BASE}}industries/retail.html">Retail &amp; Mixed-Use<small>Canopy &amp; demand charges</small></a>
        </div>
      </li>
      <li role="none"><a role="menuitem" href="{{BASE}}maintenance/index.html">Maintenance</a>
        <div class="nav__dropdown">
          <a href="{{BASE}}maintenance/index.html">All Maintenance Services</a>
          <a href="{{BASE}}maintenance/cleaning.html">Panel Cleaning<small>25–30% production lift</small></a>
          <a href="{{BASE}}maintenance/repairs.html">Repairs<small>4hr emergency dispatch</small></a>
          <a href="{{BASE}}maintenance/monitoring.html">Know TrueUp® Monitoring<small>24/7 analytics</small></a>
          <a href="{{BASE}}maintenance/critter-guard.html">Critter Guard<small>Pest &amp; debris protection</small></a>
          <a href="{{BASE}}maintenance/inspection.html">50-Point Inspection</a>
          <a href="{{BASE}}maintenance/audit.html">System Audit</a>
        </div>
      </li>
      <li role="none"><a role="menuitem" href="{{BASE}}membership.html">Membership</a></li>
      <li role="none"><a role="menuitem" href="{{BASE}}blog/index.html">Resources</a>
        <div class="nav__dropdown">
          <a href="{{BASE}}blog/index.html">Solar Blog</a>
          <a href="{{BASE}}faq.html">FAQ</a>
          <a href="{{BASE}}case-studies.html">Case Studies</a>
          <a href="{{BASE}}reviews.html">Reviews</a>
        </div>
      </li>
      <li role="none"><a role="menuitem" href="{{BASE}}about.html">About</a></li>
    </ul>
    <div class="nav__cta">
      <a href="{BRAND['phone_href']}" class="btn btn-ghost btn-sm" aria-label="Call Hart Beat Energy">📞 {BRAND['phone_display']}</a>
      <a href="{{BASE}}contact.html" class="btn btn-primary btn-sm">Get a Quote</a>
    </div>
    <button class="nav__toggle" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 6h18M3 12h18M3 18h18" stroke-linecap="round"/></svg></button>
  </div>
  <div class="nav__mobile" aria-label="Mobile menu">
    <a href="{{BASE}}index.html">Home</a>
    <a href="{{BASE}}residential.html">Residential Solar</a>
    <a href="{{BASE}}commercial.html">Commercial Solar</a>
    <a href="{{BASE}}battery-storage.html">Battery Storage</a>
    <a href="{{BASE}}financing.html">Financing</a>
    <a href="{{BASE}}lease-vs-ppa.html">Lease vs PPA</a>
    <a href="{{BASE}}maintenance/index.html">Maintenance</a>
    <a href="{{BASE}}membership.html">Membership</a>
    <a href="{{BASE}}case-studies.html">Case Studies</a>
    <a href="{{BASE}}reviews.html">Reviews</a>
    <a href="{{BASE}}faq.html">FAQ</a>
    <a href="{{BASE}}blog/index.html">Blog</a>
    <a href="{{BASE}}about.html">About</a>
    <a href="{{BASE}}contact.html" class="btn btn-primary btn-block">Get a Quote</a>
    <a href="{BRAND['phone_href']}" class="btn btn-outline btn-block" style="margin-top:10px">📞 {BRAND['phone_display']}</a>
  </div>
</nav>
'''

def footer_html():
    return f'''
<footer class="footer" role="contentinfo">
  <div class="container">
    <div class="footer__grid">
      <div>
        <div class="footer__brand"><img src="{{BASE}}assets/images/hartbeat-logo.png" alt="" width="44" height="44"><span>Hart Beat Energy</span></div>
        <p class="footer__about">Designing, installing, and maintaining solar ecosystems for Texas homes and businesses. All 254 counties. Know TrueUp® predictive monitoring included with every install.</p>
        <p style="color:rgba(255,255,255,.6);font-size:.88rem;margin-top:12px">
          <strong style="color:#fff">{BRAND['address']['street']}</strong><br>
          {BRAND['address']['city']}, {BRAND['address']['region']} {BRAND['address']['postal']}<br>
          <a href="{BRAND['phone_href']}">{BRAND['phone_display']}</a> · <a href="mailto:{BRAND['email']}">{BRAND['email']}</a>
        </p>
        <div class="footer__social" aria-label="Social media">
          <a href="{BRAND['social']['facebook']}" aria-label="Facebook" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 8h-3v4h3v12h5V12h3.642L18 8h-4V6.333C14 5.378 14.192 5 15.115 5H18V0h-3.808C10.596 0 9 1.583 9 4.615V8z"/></svg></a>
          <a href="{BRAND['social']['instagram']}" aria-label="Instagram" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.85.07 3.25.15 4.77 1.7 4.92 4.92.06 1.25.07 1.62.07 4.8s0 3.56-.07 4.8c-.15 3.22-1.66 4.77-4.92 4.92-1.25.06-1.62.07-4.85.07s-3.6 0-4.85-.07c-3.26-.15-4.77-1.7-4.92-4.92C2.16 15.56 2.15 15.2 2.15 12s0-3.55.07-4.8C2.38 3.98 3.9 2.43 7.15 2.28 8.4 2.22 8.77 2.2 12 2.2zm0 5.4a4.4 4.4 0 100 8.8 4.4 4.4 0 000-8.8zm0 7.27a2.87 2.87 0 110-5.74 2.87 2.87 0 010 5.74zm4.59-7.45a1.03 1.03 0 100 2.06 1.03 1.03 0 000-2.06z"/></svg></a>
          <a href="{BRAND['social']['linkedin']}" aria-label="LinkedIn" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8h4V24h-4V8zm7.5 0h3.8v2.2h.05c.53-1 1.82-2.2 3.75-2.2C19.64 8 21 10.4 21 14.1V24h-4V15c0-2.15-.04-4.9-3-4.9-3 0-3.45 2.33-3.45 4.75V24H7.5V8z"/></svg></a>
          <a href="{BRAND['social']['youtube']}" aria-label="YouTube" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 00-2.12-2.12C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.38.58A3 3 0 00.5 6.2C0 8.08 0 12 0 12s0 3.92.5 5.8a3 3 0 002.12 2.12C4.5 20.5 12 20.5 12 20.5s7.5 0 9.38-.58a3 3 0 002.12-2.12C24 15.92 24 12 24 12s0-3.92-.5-5.8zM9.75 15.58V8.42L15.82 12l-6.07 3.58z"/></svg></a>
          <a href="{BRAND['social']['tiktok']}" aria-label="TikTok" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.5 0h3.5c.2 1.8 1.2 3.3 2.8 4.2 1 .6 2.2.9 3.3.9v3.6c-1.9 0-3.8-.5-5.5-1.5v7.2c0 4.3-3.5 7.8-7.8 7.8S1 18.7 1 14.4s3.5-7.8 7.8-7.8c.4 0 .8 0 1.2.1v3.7c-.4-.1-.8-.2-1.2-.2-2.3 0-4.2 1.9-4.2 4.2S6.5 18.6 8.8 18.6s4.2-1.9 4.2-4.2V0h-.5z"/></svg></a>
        </div>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="{{BASE}}residential.html">Residential Solar</a></li>
          <li><a href="{{BASE}}commercial.html">Commercial Solar</a></li>
          <li><a href="{{BASE}}battery-storage.html">Battery Storage</a></li>
          <li><a href="{{BASE}}financing.html">Financing</a></li>
          <li><a href="{{BASE}}lease-vs-ppa.html">Lease vs PPA</a></li>
          <li><a href="{{BASE}}maintenance/cleaning.html">Panel Cleaning</a></li>
          <li><a href="{{BASE}}maintenance/repairs.html">Repairs</a></li>
          <li><a href="{{BASE}}maintenance/monitoring.html">Know TrueUp®</a></li>
        </ul>
      </div>
      <div>
        <h4>Texas Cities</h4>
        <ul>
          <li><a href="{{BASE}}locations/houston.html">Houston</a></li>
          <li><a href="{{BASE}}locations/austin.html">Austin</a></li>
          <li><a href="{{BASE}}locations/dallas.html">Dallas</a></li>
          <li><a href="{{BASE}}locations/san-antonio.html">San Antonio</a></li>
          <li><a href="{{BASE}}locations/fort-worth.html">Fort Worth</a></li>
          <li><a href="{{BASE}}locations/el-paso.html">El Paso</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{{BASE}}about.html">About Us</a></li>
          <li><a href="{{BASE}}careers.html">Careers</a></li>
          <li><a href="{{BASE}}case-studies.html">Case Studies</a></li>
          <li><a href="{{BASE}}reviews.html">Reviews</a></li>
          <li><a href="{{BASE}}faq.html">FAQ</a></li>
          <li><a href="{{BASE}}warranty.html">Warranty</a></li>
          <li><a href="{{BASE}}referral.html">Referral Program</a></li>
          <li><a href="{{BASE}}contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <div>© {BUILD_YEAR} {BRAND['name']}. All rights reserved. Licensed Texas solar contractor. NABCEP-certified crews.</div>
      <div>
        <a href="{{BASE}}privacy.html">Privacy</a>
        <a href="{{BASE}}terms.html">Terms</a>
        <a href="{{BASE}}sitemap.html">Sitemap</a>
      </div>
    </div>
  </div>
</footer>
'''

def page_html(title, description, canonical_path, body_html, schemas=None, og_image="og-default.jpg", depth=0):
    """Renders a complete HTML page. depth = number of ../ needed for subdir pages."""
    base = "../" * depth if depth else ""
    canonical = f"{SITE_URL}{canonical_path}"
    full_title = title if title == BRAND['name'] else f"{title} | {BRAND['name']}"
    schemas_out = render_schema(schemas) if schemas else ""
    nav = nav_html().replace("{BASE}", base)
    footer = footer_html().replace("{BASE}", base)
    body_html = body_html.replace("{BASE}", base)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0b1f3a">
<meta name="format-detection" content="telephone=yes">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND['name']}">
<meta property="og:image" content="{SITE_URL}/assets/images/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(full_title)}">
<meta name="twitter:description" content="{html.escape(description)}">
<meta name="twitter:image" content="{SITE_URL}/assets/images/{og_image}">
<link rel="icon" type="image/svg+xml" href="{base}assets/images/favicon.svg">
<link rel="icon" type="image/png" href="{base}assets/images/favicon.png">
<link rel="apple-touch-icon" href="{base}assets/images/apple-touch-icon.png">
<link rel="manifest" href="{base}manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{base}assets/css/styles.css">
{schemas_out}
</head>
<body>
{nav}
<main id="main" role="main">
{body_html}
</main>
{footer}
<script src="{base}assets/js/main.js" defer></script>
</body>
</html>
'''

# ============================================================
# REUSABLE UI SNIPPETS
# ============================================================
def hero(badge, headline_html, lede, cta_primary, cta_primary_href, cta_secondary=None, cta_secondary_href=None, stats=None, bg_image=None):
    stats_html = ""
    if stats:
        stats_html = '<div class="hero__stats">' + "".join(
            f'<div class="hero__stat"><div class="n">{n}</div><div class="l">{l}</div></div>' for n, l in stats
        ) + '</div>'
    secondary = f'<a href="{cta_secondary_href}" class="btn btn-outline btn-lg" style="color:#fff;border-color:rgba(255,255,255,.3)">{cta_secondary}</a>' if cta_secondary else ""
    cls = "hero"
    style = ""
    if bg_image:
        cls += " hero--bg"
        style = f' style="background-image:url(\'{bg_image}\')"'
    return f'''
<section class="{cls}"{style}>
  <div class="container hero__inner">
    <div class="hero__badge">{badge}</div>
    <h1>{headline_html}</h1>
    <p class="lede">{lede}</p>
    <div class="hero__actions">
      <a href="{cta_primary_href}" class="btn btn-primary btn-lg">{cta_primary}</a>
      {secondary}
    </div>
    {stats_html}
  </div>
</section>
'''


def feature_split(img_url, eyebrow, headline, body_html, cta_text=None, cta_href=None, reverse=False):
    """Side-by-side image + text section."""
    rev = " feature-split--reverse" if reverse else ""
    cta = f'<p style="margin-top:24px"><a href="{cta_href}" class="btn btn-primary">{cta_text}</a></p>' if cta_text else ""
    return f'''
<section class="section">
  <div class="container">
    <div class="feature-split{rev}">
      <div class="feature-split__media"><img src="{img_url}" alt="" loading="lazy"></div>
      <div class="feature-split__body">
        <span class="eyebrow">{eyebrow}</span>
        <h2>{headline}</h2>
        {body_html}
        {cta}
      </div>
    </div>
  </div>
</section>
'''


def image_band(img_url, overlay_text=None):
    """Full-width image banner."""
    overlay = f'<div class="image-band__overlay"><h2>{overlay_text}</h2></div>' if overlay_text else ""
    return f'<section class="image-band"><img src="{img_url}" alt="" loading="lazy">{overlay}</section>'

def cta_section(heading, sub, btn1, btn1_href, btn2=None, btn2_href=None):
    b2 = f'<a href="{btn2_href}" class="btn btn-outline btn-lg">{btn2}</a>' if btn2 else ""
    return f'''
<section class="cta-section">
  <div class="container text-center">
    <h2 style="max-width:720px;margin:0 auto 16px">{heading}</h2>
    <p style="max-width:620px;margin:0 auto 28px;font-size:1.1rem">{sub}</p>
    <div class="btn-group" style="justify-content:center">
      <a href="{btn1_href}" class="btn btn-secondary btn-lg">{btn1}</a>
      {b2}
    </div>
  </div>
</section>
'''

def breadcrumb_html(items):
    out = '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="{BASE}index.html">Home</a>'
    for name, url in items:
        out += f'<span>›</span><a href="{{BASE}}{url}">{name}</a>' if url else f'<span>›</span>{name}'
    out += '</nav>'
    return out

print("Builder loaded. Imports okay.")
