"""Maintenance hub + 6 sub-pages."""
from build import IMG, hero, cta_section, breadcrumb_html, feature_split, image_band

def maintenance_hub():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Maintenance", None)]) + '</div>'
    body += hero(
        badge="🛠 Maintenance Intelligence",
        headline_html='Concierge maintenance programs keep Texas arrays <span class="hl">efficient and storm-ready</span>.',
        lede="Whether we built your system or inherited it, Hart Beat Energy's statewide technicians and analysts manage everything — cleanings, inspections, repairs, storm response, and 24/7 Know TrueUp® monitoring. We service every major brand.",
        cta_primary="View membership plans", cta_primary_href="{BASE}membership.html",
        cta_secondary="Schedule service", cta_secondary_href="{BASE}contact.html",
        stats=[("24/7", "Monitoring &amp; dispatch"), ("&lt;4 hr", "Emergency response"), ("All brands", "Certified to service")],        bg_image=IMG["hero_maintenance"],

    )
    body += '''
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Our Services</span><h2>Six services that cover the full lifecycle of your array.</h2></div>
    <div class="grid grid-3">
      <a href="{BASE}maintenance/cleaning.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">🧹</div><h3 class="card__title">Panel Cleaning</h3><p class="card__desc">Certified cleaning protocols. Deionized water. Up to 30% production boost.</p><span class="card__link">Learn more →</span></a>
      <a href="{BASE}maintenance/repairs.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">🔧</div><h3 class="card__title">Repairs &amp; Troubleshooting</h3><p class="card__desc">4-hour emergency dispatch. On-truck inventory. Every major brand.</p><span class="card__link">Learn more →</span></a>
      <a href="{BASE}maintenance/monitoring.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">📊</div><h3 class="card__title">Know TrueUp® Monitoring</h3><p class="card__desc">24/7 predictive analytics. Weather-normalized benchmarks. Mobile app.</p><span class="card__link">Learn more →</span></a>
      <a href="{BASE}maintenance/critter-guard.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">🦔</div><h3 class="card__title">Critter Guard</h3><p class="card__desc">Pest &amp; debris protection from $399. Protects panels from squirrels, birds, rodents.</p><span class="card__link">Learn more →</span></a>
      <a href="{BASE}maintenance/inspection.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">🔍</div><h3 class="card__title">50-Point Inspection</h3><p class="card__desc">Annual comprehensive system inspection with thermal imaging &amp; documentation.</p><span class="card__link">Learn more →</span></a>
      <a href="{BASE}maintenance/audit.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">📋</div><h3 class="card__title">System Audit</h3><p class="card__desc">Comprehensive 40-page report. Production vs. design. ROI tracking.</p><span class="card__link">Learn more →</span></a>
    </div>
  </div>
</section>

'''
    body += image_band(IMG["maint_monitoring"], overlay_text="Know TrueUp® — 24/7 eyes on every panel.")
    body += '''
<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Why Hart Beat Energy</span><h2>Three things that set our maintenance apart.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">Dedicated account managers</h3><p class="card__desc">One point of contact for home and commercial portfolios — no call centers, no ticket loops.</p></div>
      <div class="card"><h3 class="card__title">Rapid storm response</h3><p class="card__desc">Emergency crews on standby for Texas weather events. Typical dispatch under 48 hours post-storm.</p></div>
      <div class="card"><h3 class="card__title">Certified for every platform</h3><p class="card__desc">We service every major solar and storage brand — regardless of who installed it. Bring us your orphaned system.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section(
        "Own a solar system? Get it on a Hart Beat Energy membership plan.",
        "Scheduled cleanings, priority repairs, Know TrueUp® monitoring, and storm response — for a predictable monthly rate.",
        "View membership plans", "{BASE}membership.html",
        "Call our team", "tel:3463302550",
    )
    return body

def cleaning():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Maintenance","maintenance/index.html"),("Panel Cleaning", None)]) + '</div>'
    body += hero(
        badge="🧹 Panel Cleaning",
        headline_html='Professional solar panel cleaning for <span class="hl">peak production</span> in every Texas season.',
        lede="Hart Beat Energy cleaning crews use deionized water systems and solar-safe agents to restore output. Manufacturer-approved methods protect your panel warranty and add 25–30% average production lift on dust-loaded arrays.",
        cta_primary="Schedule cleaning visit", cta_primary_href="{BASE}contact.html",
        cta_secondary="Add to membership plan", cta_secondary_href="{BASE}membership.html",
        stats=[("25–30%", "Avg production lift"), ("≤90 min", "Standard appointment"), ("All 254", "Counties covered")],        bg_image=IMG["maint_cleaning"],

    )
    body += '''
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Why It Matters</span>
      <h2>DIY cleaning costs more than it saves.</h2>
      <p>Texas heat, pollen, and storms coat panels faster than most homeowners expect. Our technicians follow manufacturer-approved protocols that restore peak output without damaging panel coatings or voiding warranties.</p>
      <ul class="check-list">
        <li><strong>Boost production by up to 30%</strong> — remove pollen, dust, and debris so every ray translates into usable kWh</li>
        <li><strong>Protect panel warranties</strong> — manufacturer-approved methods prevent micro-scratches and hot spots</li>
        <li><strong>Maintain ROI certainty</strong> — consistent cleaning ensures production forecasts stay accurate year over year</li>
        <li><strong>Two-person crews</strong> finish most homes in under 90 minutes with zero chemical runoff</li>
      </ul>
    </div>
    <div>
      <div class="card card--feature">
        <span class="eyebrow">What to Expect</span>
        <h3>Every visit, start to finish</h3>
        <ul class="check-list" style="margin-top:16px">
          <li>Baseline inspection with thermal and production reading</li>
          <li>Foamless, deionized water pre-rinse to lift abrasive particles</li>
          <li>Biodegradable surfactant application tailored to Texas dust loads</li>
          <li>Soft-bristle brush agitation with panel-safe equipment</li>
          <li>Spot-free rinse and edge detailing to prevent streaking</li>
          <li>Final production verification and photo documentation to Know TrueUp®</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Recommended Cadence</span><h2>Customized to your property type.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">Residential</h3><p class="card__desc">2–3 cleanings per year. Quarterly recommended for properties with heavy tree cover or near construction zones.</p></div>
      <div class="card"><h3 class="card__title">Commercial Roofs</h3><p class="card__desc">3–4 cleanings per year. Monthly rinse cycles for industrial zones with heavy airborne particulates.</p></div>
      <div class="card"><h3 class="card__title">Agricultural &amp; Oilfield</h3><p class="card__desc">4–6 cleanings per year. High dust and airborne particle environments require the most frequent service.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section("Proof of performance — every visit.","Before/after photos, production deltas, and full documentation added to your Know TrueUp® dashboard after every cleaning.","Request preferred date","{BASE}contact.html","Add to membership","{BASE}membership.html")
    return body

def repairs():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Maintenance","maintenance/index.html"),("Repairs", None)]) + '</div>'
    body += hero(
        badge="🔧 Repairs &amp; Troubleshooting",
        headline_html='Fast, reliable repair services to <span class="hl">get your solar system back</span> to peak performance.',
        lede="Our expert technicians diagnose and fix all types of solar system issues — with on-truck inventory so most repairs finish same-visit. 24/7 emergency line. Every major brand. Certified to service.",
        cta_primary="📞 Emergency Hotline: (346) 330-2550", cta_primary_href="tel:3463302550",
        cta_secondary="Schedule service", cta_secondary_href="{BASE}contact.html",
        stats=[("&lt;4 hr", "Emergency dispatch"), ("On-truck", "Parts inventory"), ("All brands", "Certified service")],        bg_image=IMG["maint_repairs"],

    )
    body += '''
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Our Repair Process</span><h2>Six steps from call to resolution.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">1. Initial Consultation</h3><p class="card__desc">Phone consultation and remote troubleshooting to identify the likely issue and dispatch priority.</p></div>
      <div class="card"><h3 class="card__title">2. On-Site Diagnostic</h3><p class="card__desc">Thermal imaging and production data analysis to pinpoint the root cause.</p></div>
      <div class="card"><h3 class="card__title">3. Transparent Quote</h3><p class="card__desc">Detailed repair quote and timeline — no surprises, no hidden fees.</p></div>
      <div class="card"><h3 class="card__title">4. Professional Repair</h3><p class="card__desc">Manufacturer-approved components and techniques, by NABCEP-certified techs.</p></div>
      <div class="card"><h3 class="card__title">5. System Verification</h3><p class="card__desc">Testing and production verification to confirm full restoration.</p></div>
      <div class="card"><h3 class="card__title">6. Follow-up Support</h3><p class="card__desc">Ongoing monitoring — all repairs logged in Know TrueUp®.</p></div>
    </div>
    <div class="callout callout--sun mt-4"><strong>Membership benefit:</strong> Members receive 20% off all repair services and priority scheduling over non-members. <a href="{BASE}membership.html">Learn about membership →</a></div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Common Issues We Fix</span><h2>Expert solutions for every problem.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">Inverter Failures</h3><p class="card__desc"><em>Error codes, shutdowns, or no power conversion.</em> Diagnostics, repair, or full replacement with updated units.</p></div>
      <div class="card"><h3 class="card__title">Panel Damage</h3><p class="card__desc"><em>Cracks, hot spots, or physical damage.</em> Thermal scan to identify underperformers, targeted panel repair or replacement.</p></div>
      <div class="card"><h3 class="card__title">Wiring Issues</h3><p class="card__desc"><em>Loose connections, corrosion, arc faults.</em> Full rewiring and connection restoration to manufacturer spec.</p></div>
      <div class="card"><h3 class="card__title">Monitoring Errors</h3><p class="card__desc"><em>Communication failures or data gaps.</em> System reset, reconfiguration, and portal sync to Know TrueUp®.</p></div>
      <div class="card"><h3 class="card__title">Ground Faults</h3><p class="card__desc"><em>Safety system triggers and shutdowns.</em> Precision fault location and repair to restore safe operation.</p></div>
      <div class="card"><h3 class="card__title">Low Production</h3><p class="card__desc"><em>System underperforming expectations.</em> Complete diagnostics and optimization to restore full yield.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Response Times</span><h2>Matched to the urgency.</h2></div>
    <div class="grid grid-4">
      <div class="card"><h3 class="card__title">🚨 Emergency Repairs</h3><p class="card__desc">24/7 emergency service for complete system failures.</p><span class="badge badge--sun">Within 4 hours</span></div>
      <div class="card"><h3 class="card__title">🔄 Component Replacement</h3><p class="card__desc">Panels, inverters, optimizers, and more.</p><span class="badge">Next day</span></div>
      <div class="card"><h3 class="card__title">⚡ Electrical Repairs</h3><p class="card__desc">Wiring, grounding, and connection fixes.</p><span class="badge badge--green">Same day</span></div>
      <div class="card"><h3 class="card__title">📋 Warranty Support</h3><p class="card__desc">Handle manufacturer warranty claims end-to-end.</p><span class="badge">Full support</span></div>
    </div>
  </div>
</section>
'''
    body += cta_section("Don't let problems get worse.","Quick repairs save money and prevent further damage. Call our emergency line now for immediate assistance.","Call Emergency Line","tel:3463302550","Schedule service","{BASE}contact.html")
    return body

def monitoring():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Maintenance","maintenance/index.html"),("Know TrueUp® Monitoring", None)]) + '</div>'
    body += hero(
        badge="📊 Know TrueUp® Monitoring",
        headline_html='Stay connected to your solar investment with <span class="hl">real-time data</span>, instant alerts, and detailed performance reports.',
        lede="Our proprietary Know TrueUp® software benchmarks production against weather-normalized expectations. You see your true ROI at every moment — and we catch issues before they cost you.",
        cta_primary="Get started with monitoring", cta_primary_href="{BASE}contact.html",
        cta_secondary="Request demo", cta_secondary_href="{BASE}contact.html",
        stats=[("24/7", "Live monitoring"), ("52/yr", "Weekly reports"), ("99.4%", "Fleet uptime")],        bg_image=IMG["maint_monitoring"],

    )
    body += '''
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Platform Features</span>
      <h2>Complete system visibility — never wonder how your array is performing.</h2>
      <ul class="check-list">
        <li><strong>Accurate TrueUp predictions</strong> — know your annual utility settlement before it arrives</li>
        <li><strong>Real-time production data</strong> — track energy generation minute by minute</li>
        <li><strong>Instant alert notifications</strong> — get notified immediately of any system issues or downtime</li>
        <li><strong>Weather correlation</strong> — production benchmarked against local weather so seasonal dips don't mask real problems</li>
        <li><strong>Mobile app access</strong> — monitor your system from anywhere with iOS and Android apps</li>
        <li><strong>ROI tracking</strong> — energy consumption vs production analysis and financial reporting</li>
      </ul>
    </div>
    <div>
      <div class="card card--feature">
        <span class="eyebrow">Know TrueUp® Live</span>
        <div class="grid grid-2 mt-3">
          <div><div class="stat__n">5.2 kW</div><div class="stat__l">Current output</div></div>
          <div><div class="stat__n">99.4%</div><div class="stat__l">Uptime today</div></div>
          <div><div class="stat__n">10,240 kWh</div><div class="stat__l">Annual production</div></div>
          <div><div class="stat__n">$1,540</div><div class="stat__l">Est. TrueUp credit</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Monitoring Plans</span><h2>Choose the right level of visibility.</h2></div>
    <div class="pricing">
      <div class="plan"><div class="plan__name">Basic Monitoring</div><div class="plan__price">Included<small>&nbsp;with every Hart Beat Energy install</small></div>
        <ul class="plan__features"><li>Daily production summaries</li><li>Monthly performance reports</li><li>Basic email alerts</li><li>Web portal access</li></ul>
        <a href="{BASE}contact.html" class="btn btn-outline btn-block">Get Started</a>
      </div>
      <div class="plan plan--featured"><div class="plan__badge">Recommended</div><div class="plan__name">Know TrueUp® Pro</div><div class="plan__price">$15<small>/mo</small></div><div class="plan__sub">or included free with any membership plan</div>
        <ul class="plan__features"><li>Real-time monitoring</li><li>Mobile app (iOS &amp; Android)</li><li>Advanced TrueUp analytics</li><li>Instant anomaly notifications</li><li>Weather correlation engine</li><li>API access for integrations</li></ul>
        <a href="{BASE}contact.html" class="btn btn-primary btn-block">Get Started</a>
      </div>
      <div class="plan"><div class="plan__name">Enterprise</div><div class="plan__price">Custom<small>&nbsp;multi-site portfolios</small></div>
        <ul class="plan__features"><li>Multi-site management dashboard</li><li>Custom KPI dashboards</li><li>Dedicated support team</li><li>Advanced compliance reporting</li><li>BMS / ERP integration</li><li>Uptime SLA guarantees</li></ul>
        <a href="{BASE}contact.html" class="btn btn-outline btn-block">Contact Sales</a>
      </div>
    </div>
  </div>
</section>
'''
    body += cta_section("Know TrueUp® is included free with all membership plans.","Combine predictive monitoring with scheduled cleanings and priority dispatch for complete solar protection.","Compare membership plans","{BASE}membership.html","Get started","{BASE}contact.html")
    return body

def critter_guard():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Maintenance","maintenance/index.html"),("Critter Guard", None)]) + '</div>'
    body += hero(
        badge="🦔 Critter Guard",
        headline_html='Keep squirrels, birds, and rodents <span class="hl">out of your solar array</span>.',
        lede="Texas wildlife loves the shade and warmth under solar panels — which leads to chewed wires, nests, and production loss. Critter Guard installs a custom steel mesh barrier around your array perimeter to keep pests out permanently. From $399.",
        cta_primary="Get Critter Guard quote", cta_primary_href="{BASE}contact.html",
        cta_secondary="Schedule inspection", cta_secondary_href="{BASE}contact.html",
        stats=[("$399+", "Starting price"), ("Permanent", "One-time install"), ("All panels", "Every major brand")],        bg_image=IMG["maint_critter"],

    )
    body += '''
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">The Problem</span>
      <h2>Why critters love your array.</h2>
      <p>Solar panels create a shaded, weather-protected cavity roughly 4 inches tall on your roof. That's prime real estate for squirrels, grackles, pigeons, rats, and raccoons — especially during Texas summers. Once they move in, you get:</p>
      <ul class="check-list">
        <li>Chewed DC wiring — fire risk and production loss</li>
        <li>Nests blocking ventilation — panels overheat, efficiency drops</li>
        <li>Droppings &amp; debris — shading &amp; corrosion</li>
        <li>Voided warranty claims — some manufacturers exclude rodent damage</li>
      </ul>
    </div>
    <div>
      <div class="card card--feature">
        <span class="eyebrow">The Solution</span>
        <h3>Custom steel mesh barrier</h3>
        <p style="margin-top:12px">Rigid galvanized steel mesh cut to your array's exact footprint, secured under panel clips with UV-stable fasteners. Invisible from ground level. Rated for 20+ years.</p>
        <ul class="check-list" style="margin-top:16px">
          <li>Same-day installation for most residential homes</li>
          <li>Works with any panel brand</li>
          <li>Doesn't void panel warranty</li>
          <li>Includes inspection &amp; debris clearing</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''
    body += cta_section("Stop wildlife damage before it costs you.","Get a free Critter Guard assessment with your next maintenance visit.","Get a quote","{BASE}contact.html","Call (346) 330-2550","tel:3463302550")
    return body

def inspection():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Maintenance","maintenance/index.html"),("50-Point Inspection", None)]) + '</div>'
    body += hero(
        badge="🔍 50-Point Inspection",
        headline_html='Annual comprehensive inspection — <span class="hl">catch issues before they cost you</span>.',
        lede="Our 50-point inspection combines thermal imaging, electrical testing, structural review, and documentation into one annual visit. Every finding photographed, logged in Know TrueUp®, and delivered in a shareable PDF report.",
        cta_primary="Schedule inspection", cta_primary_href="{BASE}contact.html",
        cta_secondary="Add to membership", cta_secondary_href="{BASE}membership.html",
        stats=[("50", "Inspection points"), ("Thermal", "Imaging included"), ("PDF", "Report delivered")],        bg_image=IMG["maint_inspection"],

    )
    body += '''
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">What's Covered</span><h2>Six inspection domains, 50 individual checkpoints.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">Structural</h3><p class="card__desc">Mounting, flashing, rails, attachment points, roof-penetration sealing.</p></div>
      <div class="card"><h3 class="card__title">Electrical</h3><p class="card__desc">DC/AC wiring integrity, torque checks, ground-fault verification, arc-fault detection.</p></div>
      <div class="card"><h3 class="card__title">Panels</h3><p class="card__desc">Thermal imaging, micro-crack detection, hot-spot identification, shading analysis.</p></div>
      <div class="card"><h3 class="card__title">Inverter / Optimizers</h3><p class="card__desc">Firmware, fan operation, error log review, efficiency testing.</p></div>
      <div class="card"><h3 class="card__title">Monitoring</h3><p class="card__desc">Data-link integrity, Know TrueUp® sync verification, reporting accuracy.</p></div>
      <div class="card"><h3 class="card__title">Safety</h3><p class="card__desc">Rapid-shutdown verification, signage, placards, disconnect labeling.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section("One inspection per year keeps warranties valid and production high.","Most homeowners save their first annual inspection fee many times over in caught problems.","Schedule an inspection","{BASE}contact.html","Join membership","{BASE}membership.html")
    return body

def audit():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Maintenance","maintenance/index.html"),("System Audit", None)]) + '</div>'
    body += hero(
        badge="📋 System Audit",
        headline_html='Comprehensive 40-page system audit — know <span class="hl">exactly what you own</span> and how it performs.',
        lede="If you inherited a solar array or suspect it's underperforming, our system audit delivers the definitive answer. Production vs. design baseline, warranty status, remaining life expectancy, optimization opportunities, and a prioritized action list.",
        cta_primary="Request an audit", cta_primary_href="{BASE}contact.html",
        stats=[("40-page", "Report deliverable"), ("All brands", "We audit anything"), ("Free", "For members")],        bg_image=IMG["maint_audit"],

    )
    body += '''
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">What You Get</span><h2>A decisive document you can act on.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">As-Built Documentation</h3><p class="card__desc">String diagrams, panel layout, inverter configuration, interconnection.</p></div>
      <div class="card"><h3 class="card__title">Production Analysis</h3><p class="card__desc">Actual vs. designed production, year-over-year degradation, shading impact.</p></div>
      <div class="card"><h3 class="card__title">Warranty Status</h3><p class="card__desc">Remaining coverage on panels, inverter, workmanship, and monitoring.</p></div>
      <div class="card"><h3 class="card__title">Component Health</h3><p class="card__desc">Thermal scan of every panel, inverter diagnostic, connection integrity.</p></div>
      <div class="card"><h3 class="card__title">Remaining Useful Life</h3><p class="card__desc">Estimated years-of-service on each major component.</p></div>
      <div class="card"><h3 class="card__title">Optimization Roadmap</h3><p class="card__desc">Prioritized list of repairs, upgrades, and maintenance items with ROI impact.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section("Stop guessing. Know what you own.","Free audit included with every Hart Beat Energy acquisition of an orphaned system.","Request an audit","{BASE}contact.html","Call (346) 330-2550","tel:3463302550")
    return body
