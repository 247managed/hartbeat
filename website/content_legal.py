"""Legal pages: privacy, terms, sitemap."""
from build import IMG, hero, breadcrumb_html

def privacy_page():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Privacy Policy", None)]) + '</div>'
    body += hero(
        badge="🔒 Privacy",
        headline_html='Privacy Policy',
        lede="Last updated: March 1, 2026. This policy describes how Hart Beat Energy collects, uses, and protects your personal information.",
        cta_primary="Contact Us", cta_primary_href="{BASE}contact.html",
    )
    body += '''
<section class="section"><div class="container prose">
<h2>1. Information We Collect</h2>
<p>When you request a quote, we collect: name, phone, email, service address, utility bill information, and roof details. When you browse our site, we collect anonymous analytics (pages viewed, referrer, device type) via Google Analytics.</p>

<h2>2. How We Use Information</h2>
<p>We use your information to: (a) generate your solar quote and design your system, (b) coordinate site surveys and installation, (c) handle utility interconnection and permitting on your behalf, (d) communicate project updates, and (e) offer relevant maintenance or upgrade services.</p>

<h2>3. Information Sharing</h2>
<p>We share information only with: (a) our installation crews and subcontractors under NDA, (b) financing partners you explicitly choose, (c) utilities and permitting authorities as required for your project, and (d) law enforcement when legally required. <strong>We do not sell your personal information.</strong></p>

<h2>4. Your Rights</h2>
<p>You may request access to, correction of, or deletion of your personal information at any time by emailing support@hartbeat.solar. Texas residents have additional rights under the Texas Data Privacy and Security Act.</p>

<h2>5. Do Not Call / Do Not Text</h2>
<p>If you would like to be removed from our call or text list, email support@hartbeat.solar with "REMOVE" in the subject line. We honor all such requests within 10 business days.</p>

<h2>6. Cookies</h2>
<p>We use essential cookies for site functionality and analytics cookies via Google Analytics. You may disable cookies in your browser settings.</p>

<h2>7. Security</h2>
<p>We use industry-standard encryption for data in transit (TLS 1.3) and at rest (AES-256). Our CRM and document systems are SOC 2 compliant.</p>

<h2>8. Contact</h2>
<p>Hart Beat Energy · 1200 Smith Street, Suite 1600, Houston, TX 77002 · support@hartbeat.solar · (346) 330-2550</p>
</div></section>
'''
    return body


def terms_page():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Terms of Service", None)]) + '</div>'
    body += hero(
        badge="📄 Terms",
        headline_html='Terms of Service',
        lede="Last updated: March 1, 2026. By using hartbeat.solar, you agree to these terms.",
        cta_primary="Contact Us", cta_primary_href="{BASE}contact.html",
    )
    body += '''
<section class="section"><div class="container prose">
<h2>1. Use of the Site</h2>
<p>You agree to use this site only for lawful purposes. You may not: (a) attempt to gain unauthorized access, (b) scrape or harvest data, (c) upload malicious code, or (d) use automated systems without written permission.</p>

<h2>2. Quote Accuracy</h2>
<p>Quotes generated from the site are preliminary estimates based on information you provide. Final pricing is subject to on-site survey, structural review, and utility interconnection assessment.</p>

<h2>3. Incentives & Tax Credits</h2>
<p>We provide information about tax credits and incentives as a courtesy. We are not tax advisors. Consult your CPA to determine how any tax credit applies to your specific situation.</p>

<h2>4. Warranties</h2>
<p>Specific system and workmanship warranties are documented in your installation contract. Nothing on this website creates a warranty outside that contract.</p>

<h2>5. Limitation of Liability</h2>
<p>Hart Beat Energy's liability is limited to the terms stated in your installation agreement. We are not liable for indirect, incidental, or consequential damages arising from website use.</p>

<h2>6. Governing Law</h2>
<p>These terms are governed by the laws of the State of Texas. Disputes will be resolved in the state or federal courts located in Harris County, Texas.</p>

<h2>7. Contact</h2>
<p>Hart Beat Energy · 1200 Smith Street, Suite 1600, Houston, TX 77002 · support@hartbeat.solar · (346) 330-2550</p>
</div></section>
'''
    return body


def sitemap_html_page():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Sitemap", None)]) + '</div>'
    body += hero(
        badge="🗺 Sitemap",
        headline_html='Sitemap',
        lede="Every page on hartbeat.solar, organized by section.",
        cta_primary="Contact Us", cta_primary_href="{BASE}contact.html",
    )
    sections = [
        ("Core", [
            ("Home", "index.html"),
            ("Residential Solar", "residential.html"),
            ("Commercial Solar", "commercial.html"),
            ("Battery Storage", "battery-storage.html"),
            ("Financing", "financing.html"),
            ("Lease vs PPA", "lease-vs-ppa.html"),
            ("Contact", "contact.html"),
        ]),
        ("Maintenance", [
            ("Maintenance Hub", "maintenance/index.html"),
            ("Panel Cleaning", "maintenance/cleaning.html"),
            ("Repairs", "maintenance/repairs.html"),
            ("Monitoring", "maintenance/monitoring.html"),
            ("Critter Guard", "maintenance/critter-guard.html"),
            ("50-Point Inspection", "maintenance/inspection.html"),
            ("40-Page Audit", "maintenance/audit.html"),
            ("Membership Plans", "membership.html"),
        ]),
        ("Company", [
            ("About", "about.html"),
            ("Reviews", "reviews.html"),
            ("FAQ", "faq.html"),
            ("Case Studies", "case-studies.html"),
            ("Warranty", "warranty.html"),
            ("Storm Claims", "storm-claims.html"),
            ("Referral Program", "referral.html"),
            ("Careers", "careers.html"),
        ]),
        ("Locations", [
            ("Houston", "locations/houston.html"),
            ("Austin", "locations/austin.html"),
            ("Dallas", "locations/dallas.html"),
            ("San Antonio", "locations/san-antonio.html"),
            ("Fort Worth", "locations/fort-worth.html"),
            ("El Paso", "locations/el-paso.html"),
        ]),
        ("Industries", [
            ("Manufacturing", "industries/manufacturing.html"),
            ("Logistics & Warehousing", "industries/logistics.html"),
            ("Retail & Multi-Site", "industries/retail.html"),
            ("Agriculture", "industries/agriculture.html"),
            ("Hospitality", "industries/hospitality.html"),
            ("Healthcare", "industries/healthcare.html"),
        ]),
        ("Blog", [
            ("Blog Home", "blog/index.html"),
            ("Texas Solar in 2026", "blog/texas-solar-2026-after-itc-expired.html"),
            ("Lease vs PPA Guide", "blog/solar-lease-vs-ppa-texas-homeowners.html"),
            ("ERCOT Storm Prep", "blog/ercot-storm-prep-solar-battery-homeowners.html"),
            ("Houston HOA Guide", "blog/houston-hoa-solar-approval-guide.html"),
            ("Commercial ITC + MACRS", "blog/commercial-solar-itc-macrs-2026.html"),
            ("Retail Buyback Plans", "blog/texas-solar-buyback-plans-retail-providers.html"),
        ]),
        ("Legal", [
            ("Privacy Policy", "privacy.html"),
            ("Terms of Service", "terms.html"),
            ("Sitemap", "sitemap.html"),
        ]),
    ]
    cols = ""
    for title, links in sections:
        items = "".join(f'<li><a href="{{BASE}}{h}">{t}</a></li>' for t, h in links)
        cols += f'<div><h3>{title}</h3><ul class="sitemap-list">{items}</ul></div>'
    body += f'''
<section class="section"><div class="container">
  <div class="grid grid-4">{cols}</div>
</div></section>
'''
    return body
