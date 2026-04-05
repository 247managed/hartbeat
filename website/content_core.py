"""Content for homepage + core service pages."""
from build import IMG, hero, cta_section, breadcrumb_html, feature_split, image_band, schema_local_business, schema_organization, schema_website, schema_service, schema_faq, schema_breadcrumb

# ============================================================
# HOMEPAGE
# ============================================================
def homepage():
    body = hero(
        badge="⚡ Serving all 254 Texas counties",
        headline_html='Solar engineered for <span class="hl">Texas heat</span>, backed by concierge maintenance intelligence.',
        lede="Hart Beat Energy designs, finances, installs, and maintains solar ecosystems for homes and businesses across Texas. Every array includes Know TrueUp® predictive monitoring, rapid-response maintenance, and long-term yield optimization.",
        cta_primary="Design my system →",
        cta_primary_href="{BASE}contact.html",
        cta_secondary="Explore maintenance plans",
        cta_secondary_href="{BASE}membership.html",
        stats=[("5,000+", "Arrays installed & managed"), ("98%", "Customer satisfaction"), ("24/7", "Monitoring & response")],
        bg_image=IMG["hero_home"],
    )

    body += '''
<!-- 2026 policy callout -->
<section class="section" style="padding-top:40px;padding-bottom:0">
  <div class="container">
    <div class="callout callout--sun">
      <strong>📣 Important 2026 update:</strong> The 30% residential federal tax credit expired July 2025. Hart Beat Energy has shifted residential homeowners to <strong>$0-down solar lease and PPA programs</strong> — giving you immediate monthly bill savings with no upfront cost, no tax-credit paperwork, and maintenance included. Commercial projects still qualify for the full 30% ITC. <a href="{BASE}lease-vs-ppa.html"><strong>See your options →</strong></a>
    </div>
  </div>
</section>

<!-- Stats strip -->
<section class="section">
  <div class="container">
    <div class="stats">
      <div><div class="stat__n">5,000+</div><div class="stat__l">Systems engineered &amp; maintained</div></div>
      <div><div class="stat__n">254</div><div class="stat__l">Texas counties covered</div></div>
      <div><div class="stat__n">99.4%</div><div class="stat__l">Fleet uptime</div></div>
      <div><div class="stat__n">50M kWh</div><div class="stat__l">Offset annually</div></div>
    </div>
  </div>
</section>

<!-- Sales section -->
<section class="section section--alt">
  <div class="container split">
    <div>
      <span class="eyebrow">Sales &amp; Design Excellence</span>
      <h2>Solar sales done differently: data-rich insights, concierge onboarding.</h2>
      <p>Hart Beat Energy blends advanced modeling with practical field experience. We analyze your load profile, utility rate, roof geometry, and Texas weather patterns — then deliver a system tuned to your life or business.</p>
      <ul class="check-list">
        <li>Tier-one technology — LONGi, Tesla, and Schneider Electric matched to Texas climates</li>
        <li>Transparent economics — lease &amp; PPA programs starting $0-down with immediate bill savings</li>
        <li>AI-assisted precision modeling for every roof pitch, obstruction, and utility rate</li>
        <li>NABCEP-certified crews delivering turn-key systems in 30–40 days</li>
      </ul>
      <div class="btn-group mt-3">
        <a href="{BASE}residential.html" class="btn btn-primary">Residential solar →</a>
        <a href="{BASE}commercial.html" class="btn btn-outline">Commercial solar</a>
      </div>
    </div>
    <div>
      <div class="card card--feature">
        <span class="eyebrow">Texas Insights</span>
        <h3 style="margin-bottom:16px">Average homeowner outcomes</h3>
        <div class="grid grid-2">
          <div><div class="stat__n">6–8 yrs</div><div class="stat__l">Lease payback equivalent</div></div>
          <div><div class="stat__n">$1,540</div><div class="stat__l">Annual savings</div></div>
          <div><div class="stat__n">99.4%</div><div class="stat__l">Uptime</div></div>
          <div><div class="stat__n">25 yrs</div><div class="stat__l">Warranty coverage</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Services grid -->
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">What we do</span><h2>Four service lines, one accountable partner.</h2></div>
    <div class="grid grid-4">
      <div class="card"><div class="card__icon">🏠</div><h3 class="card__title">Residential Solar</h3><p class="card__desc">Custom home arrays optimized for your ZIP, utility rate, and roof geometry.</p><a href="{BASE}residential.html" class="card__link">Learn more →</a></div>
      <div class="card"><div class="card__icon">🏢</div><h3 class="card__title">Commercial Solar</h3><p class="card__desc">Large-scale portfolios with CAPEX, PPA, and lease structures for any business model.</p><a href="{BASE}commercial.html" class="card__link">Learn more →</a></div>
      <div class="card"><div class="card__icon">🔋</div><h3 class="card__title">Battery Storage</h3><p class="card__desc">Tesla Powerwall and Schneider storage keeping you online through Texas storms.</p><a href="{BASE}battery-storage.html" class="card__link">Get a quote →</a></div>
      <div class="card"><div class="card__icon">💰</div><h3 class="card__title">Financing</h3><p class="card__desc">$0-down lease &amp; PPA with specialists navigating utility and business incentives.</p><a href="{BASE}financing.html" class="card__link">Explore options →</a></div>
    </div>
  </div>
</section>

'''
    body += feature_split(
        IMG["feature_install"],
        eyebrow="Engineered install",
        headline="NABCEP-certified crews. 30–40 day turn-key install.",
        body_html="<p>Our in-house installation teams handle every step — permit submission, structural letters, utility interconnection, panel mount, inverter wiring, and final inspection. You get one project manager, one timeline, and one accountable contract.</p><ul class=\"check-list\"><li>Licensed master electricians on every job</li><li>Houston-based warehouse for same-day replacement parts</li><li>Drone roof survey + structural engineering included</li></ul>",
        cta_text="See the install process →", cta_href="{BASE}residential.html",
    )
    body += image_band(IMG["hero_battery"], overlay_text="Texas heat. Texas storms. Texas-ready solar.")
    body += '''
<!-- Maintenance -->
<section class="section section--navy">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow" style="color:#f5a623">Maintenance Intelligence</span><h2>Concierge maintenance programs keep Texas arrays efficient and storm-ready.</h2><p class="lede" style="margin:0 auto;color:rgba(255,255,255,.8)">Whether we built your system or inherited it, our statewide technicians and analysts manage everything — cleanings, inspections, repairs, storm response, 24/7 monitoring.</p></div>
    <div class="grid grid-4 mt-4">
      <div class="card card--dark"><div class="card__icon">🧹</div><h3 class="card__title">Panel Cleaning</h3><p class="card__desc">Certified protocols. Up to 30% production boost.</p><a href="{BASE}maintenance/cleaning.html" class="card__link">Learn more →</a></div>
      <div class="card card--dark"><div class="card__icon">🔧</div><h3 class="card__title">Repairs</h3><p class="card__desc">Rapid diagnostics. On-truck inventory. All brands.</p><a href="{BASE}maintenance/repairs.html" class="card__link">Learn more →</a></div>
      <div class="card card--dark"><div class="card__icon">📊</div><h3 class="card__title">Know TrueUp®</h3><p class="card__desc">24/7 predictive analytics for every array.</p><a href="{BASE}maintenance/monitoring.html" class="card__link">Learn more →</a></div>
      <div class="card card--dark"><div class="card__icon">🦔</div><h3 class="card__title">Critter Guard</h3><p class="card__desc">Custom pest &amp; debris protection from $399.</p><a href="{BASE}maintenance/critter-guard.html" class="card__link">Learn more →</a></div>
    </div>
    <div class="text-center mt-4"><a href="{BASE}membership.html" class="btn btn-primary">View membership plans →</a></div>
  </div>
</section>

<!-- Testimonials -->
<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Texas Voices</span><h2>Clients across the Lone Star State rely on Hart Beat Energy.</h2></div>
    <div class="grid grid-3">
      <div class="testimonial"><div class="testimonial__stars">★★★★★</div><p class="testimonial__quote">"Hart Beat Energy engineered a custom array and handled every permit. Their maintenance membership keeps production ~30% higher than my neighbor's panels."</p><div class="testimonial__author">Sarah Johnson</div><div class="testimonial__location">Houston, TX</div></div>
      <div class="testimonial"><div class="testimonial__stars">★★★★★</div><p class="testimonial__quote">"From financing to installation, their team was proactive and responsive. The Know TrueUp® monitoring alerts give me peace of mind every single day."</p><div class="testimonial__author">Michael Chen</div><div class="testimonial__location">Austin, TX</div></div>
      <div class="testimonial"><div class="testimonial__stars">★★★★★</div><p class="testimonial__quote">"We have multiple commercial rooftops statewide and Hart Beat Energy manages all of them with consistent SLAs. Our cost-per-kWh dropped ~62%."</p><div class="testimonial__author">Robert Martinez</div><div class="testimonial__location">Dallas, TX</div></div>
    </div>
    <div class="text-center mt-4"><a href="{BASE}reviews.html" class="btn btn-outline">Read all reviews →</a></div>
  </div>
</section>
'''
    body += cta_section(
        "Ready to unlock predictable energy costs for your Texas property?",
        "Book a strategy session. We'll model your roof, design the right system, and walk you through lease, PPA, and loan paths — no pressure, just clarity.",
        "Schedule strategy session", "{BASE}contact.html",
        "Call our team →", "tel:3463302550",
    )
    return body

# ============================================================
# RESIDENTIAL
# ============================================================
def residential():
    body = breadcrumb_html([("Residential Solar", None)])
    body = '<div class="container" style="padding-top:28px">' + body + '</div>'
    body += hero(
        badge="🏠 Residential Solar",
        headline_html='Design a Texas solar system that <span class="hl">lowers bills</span>, fortifies your home, and looks premium on day one.',
        lede="From Houston bungalows to Hill Country estates, Hart Beat Energy engineers residential solar systems for Texas roofs, Texas weather, and Texas utility rates. $0-down lease and PPA options start saving money on day one.",
        cta_primary="Book a residential consult", cta_primary_href="{BASE}contact.html",
        cta_secondary="See financing programs", cta_secondary_href="{BASE}financing.html",
        stats=[("$1,500+", "Average annual savings"), ("6–8 yrs", "Lease payback equivalent"), ("25 yrs", "Warranty coverage")],
        bg_image=IMG["hero_residential"],
    )
    body += '''
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">System Benefits</span>
      <h2>Tailored to your home's architecture and energy goals.</h2>
      <p>Every Hart Beat Energy design begins with structural modeling, utility rate analysis, and aesthetic planning. We look at your roof, your bills, your tree cover, and your 20-year plan — then engineer a system that pays you back faster.</p>
      <ul class="check-list">
        <li><strong>Raise property value</strong> — solar-equipped Texas homes sell for up to 4.1% more and close faster</li>
        <li><strong>Grid resilience</strong> — pair storage to ride through outages and peak pricing events</li>
        <li><strong>Texas-ready performance</strong> — engineered for high-heat, hail, and hurricane zones statewide</li>
        <li><strong>Sustainable impact</strong> — offset 4+ metric tons of CO₂ annually while supporting local grid stability</li>
      </ul>
    </div>
    <div>
      <div class="card card--feature">
        <span class="eyebrow" style="color:#f5a623">2026 Incentive Landscape</span>
        <h3>How Texas homeowners save today</h3>
        <ul class="check-list" style="margin-top:16px">
          <li><strong>$0-down lease &amp; PPA</strong> — immediate bill savings, maintenance included</li>
          <li>Utility rebates through Austin Energy, CPS Energy, Oncor, and more</li>
          <li>Texas property tax exemption on added home value</li>
          <li>Texas sales tax exemption on qualifying equipment</li>
          <li>HELOC &amp; solar loan options — all arranged in-house</li>
        </ul>
        <div class="callout callout--warn mt-3" style="font-size:.9rem">
          <strong>Heads up:</strong> The federal residential 30% tax credit expired July 2025. Our lease/PPA programs are designed for this new landscape.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">System Packages</span><h2>Pick the output that matches your lifestyle.</h2><p class="lede" style="margin:0 auto">Each package includes Tier-1 panels, microinverters, balance-of-system hardware, full permitting, and 25-year production warranty. Pricing reflects typical $0-down lease monthly payment in Texas markets.</p></div>
    <div class="pricing">
      <div class="plan"><div class="plan__name">Starter</div><div class="plan__sub">1–2 bedroom homes</div><div class="plan__price">~$89<small>/mo lease</small></div>
        <ul class="plan__features"><li>5.2 kW system size</li><li>~13 panels</li><li>~650 kWh/month production</li><li>30–40 days to install</li><li>25-yr warranty</li><li>Know TrueUp® included</li></ul>
        <a href="{BASE}contact.html" class="btn btn-outline btn-block">Get custom pricing</a>
      </div>
      <div class="plan plan--featured"><div class="plan__badge">Most Popular</div><div class="plan__name">Standard</div><div class="plan__sub">3–4 bedroom homes</div><div class="plan__price">~$135<small>/mo lease</small></div>
        <ul class="plan__features"><li>8.0 kW system size</li><li>~20 panels</li><li>~1,000 kWh/month production</li><li>30–40 days to install</li><li>25-yr warranty</li><li>Know TrueUp® included</li><li>Storm-ready engineering</li></ul>
        <a href="{BASE}contact.html" class="btn btn-primary btn-block">Get custom pricing</a>
      </div>
      <div class="plan"><div class="plan__name">Premium</div><div class="plan__sub">Large homes &amp; EV charging</div><div class="plan__price">~$198<small>/mo lease</small></div>
        <ul class="plan__features"><li>12.0 kW system size</li><li>~30 panels</li><li>~1,500 kWh/month production</li><li>30–40 days to install</li><li>25-yr warranty</li><li>Know TrueUp® included</li><li>EV-charging ready</li></ul>
        <a href="{BASE}contact.html" class="btn btn-outline btn-block">Get custom pricing</a>
      </div>
    </div>
    <p class="text-center mt-3" style="font-size:.85rem;color:#5a6578">Monthly payments are illustrative. Your exact payment depends on roof, utility, credit, and program — see <a href="{BASE}lease-vs-ppa.html">lease vs PPA</a> for details.</p>
  </div>
</section>

'''
    body += feature_split(
        IMG["feature_family"],
        eyebrow="Built for Texas families",
        headline="Immediate monthly savings. No upfront cost. 25-year peace of mind.",
        body_html="<p>Our $0-down lease and PPA structures let Texas homeowners lock in a lower-than-utility electric rate on day one — no tax credit paperwork, no loan underwriting, no capital outlay. Maintenance, monitoring, and production guarantees included for 25 years.</p><ul class=\"check-list\"><li>Monthly payment typically 10–25% below current electric bill</li><li>Predictable escalator or fixed-rate options</li><li>Fully transferable when you sell your home</li></ul>",
        cta_text="Compare lease vs. PPA →", cta_href="{BASE}lease-vs-ppa.html",
        reverse=True,
    )
    body += '''
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">From Consultation to Activation</span><h2>A guided six-step journey with one accountable partner.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">1. Discovery &amp; Analysis</h3><p class="card__desc">Virtual or in-home assessment, load analysis, and incentive mapping for your specific ZIP and utility.</p></div>
      <div class="card"><h3 class="card__title">2. Precision Design</h3><p class="card__desc">AI-assisted roof modeling with production forecasts, visual layouts, and shade analysis.</p></div>
      <div class="card"><h3 class="card__title">3. Permitting &amp; Approvals</h3><p class="card__desc">We manage HOA, utility interconnection, and city permitting end-to-end — nothing for you to chase.</p></div>
      <div class="card"><h3 class="card__title">4. Installation</h3><p class="card__desc">NABCEP-certified crews complete most residential projects in 1–2 days with minimal disruption.</p></div>
      <div class="card"><h3 class="card__title">5. Activation &amp; Training</h3><p class="card__desc">System commissioning plus Know TrueUp® dashboard walkthrough for your entire household.</p></div>
      <div class="card"><h3 class="card__title">6. Monitoring &amp; Maintenance</h3><p class="card__desc">24/7 analytics, routine inspections, and proactive cleanings keep your ROI on track for decades.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section(
        "Texas homeowners typically offset 60–90% of their energy usage.",
        "We model your net-metering or buyback program to maximize savings from day one — no upfront cost required.",
        "Request a tailored proposal", "{BASE}contact.html",
        "Explore financing options", "{BASE}financing.html",
    )
    return body

# ============================================================
# COMMERCIAL
# ============================================================
def commercial():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Commercial Solar", None)]) + '</div>'
    body += hero(
        badge="🏢 Commercial Solar",
        headline_html='Deploy <span class="hl">solar and storage portfolios</span> that lower OpEx, fortify operations, and advance ESG commitments.',
        lede="Hart Beat Energy engineers and maintains large-scale solar assets across Texas — from single facilities to multi-site portfolios. Commercial projects still qualify for the 30% federal ITC plus MACRS accelerated depreciation.",
        cta_primary="Schedule a portfolio review", cta_primary_href="{BASE}contact.html",
        cta_secondary="Speak with commercial lead", cta_secondary_href="tel:3463302550",
        stats=[("$2.3M+", "20-year savings potential"), ("3–5 yrs", "Typical payback range"), ("420+", "Facilities served")],
        bg_image=IMG["hero_commercial"],
    )
    body += '''
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Business Value</span>
      <h2>Operate smarter with energy assets designed for your business model.</h2>
      <p>We translate complex tariffs, incentives, and load profiles into turnkey projects layered with predictive monitoring. Your CFO gets cash-flow clarity. Your facilities team gets 24/7 performance data. Your board gets documented ESG progress.</p>
      <ul class="check-list">
        <li><strong>Stabilize operating costs</strong> — offset 50–90% of utility spend with predictable solar production</li>
        <li><strong>Maximize incentives</strong> — stack the 30% ITC, MACRS depreciation, demand-response rebates, and property abatements</li>
        <li><strong>Critical power resilience</strong> — pair solar with storage to harden against outages and peak demand charges</li>
        <li><strong>Accelerate ESG progress</strong> — documented emissions reductions and LEED pathways for investors and regulators</li>
      </ul>
    </div>
    <div>
      <div class="card card--feature">
        <h3>Federal + State Commercial Incentives</h3>
        <ul class="check-list" style="margin-top:16px">
          <li><strong>30% Federal ITC</strong> — Investment Tax Credit on eligible project cost</li>
          <li><strong>MACRS accelerated depreciation</strong> — 5-year recovery schedule, ~85% year-one deduction</li>
          <li><strong>Bonus depreciation</strong> — available in applicable tax years</li>
          <li><strong>Utility rebates &amp; demand response</strong> — ERCOT, CenterPoint, Oncor, CPS, Austin Energy programs</li>
          <li><strong>Property tax abatement</strong> — Texas Chapter 312/313 programs for qualifying installations</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Financing Structures</span><h2>Tailored to balance sheet goals.</h2></div>
    <div class="grid grid-3">
      <div class="card card--feature"><h3 class="card__title">Capital Purchase</h3><p class="card__desc">Access full incentives and depreciation. Highest net savings. Balance sheet asset with full ownership and 25+ year production warranty.</p></div>
      <div class="card card--feature"><h3 class="card__title">Power Purchase Agreement</h3><p class="card__desc">$0 CapEx — pay for delivered kWh. Immediate savings with escalator controls. Maintenance included. 15–25 year terms.</p></div>
      <div class="card card--feature"><h3 class="card__title">Custom Lease &amp; Loan Blends</h3><p class="card__desc">Align terms with cash-flow goals. Blend PACE, traditional debt, or operating leases. Flexible buyout structures.</p></div>
    </div>
  </div>
</section>

'''
    body += feature_split(
        IMG["feature_warehouse"],
        eyebrow="Commercial at scale",
        headline="Turn 50,000+ sq ft of unused roof into a 20-year asset.",
        body_html="<p>Most Texas commercial properties host 500 kW–2 MW of solar capacity sitting idle overhead. We engineer roof-load, interconnection, and financing so your facility produces its own power while the 30% ITC + MACRS depreciation stack drives 5–7 year paybacks.</p>",
        cta_text="See commercial ROI →", cta_href="{BASE}commercial.html",
    )
    body += '''
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Industry Playbooks</span><h2>Texas-scale expertise crafted from 10+ years of projects.</h2></div>
    <div class="grid grid-3">
      <a href="{BASE}industries/manufacturing.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">🏭</div><h3 class="card__title">Manufacturing &amp; Industrial</h3><p class="card__desc">70% average offset. Peak-load shaving, process electrification support, and on-site storage integration.</p><span class="card__link">See industry page →</span></a>
      <a href="{BASE}industries/logistics.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">🚚</div><h3 class="card__title">Logistics &amp; Warehousing</h3><p class="card__desc">85% roof utilization. High-clearance arrays, dock electrification, and cold storage stabilization.</p><span class="card__link">See industry page →</span></a>
      <a href="{BASE}industries/retail.html" class="card" style="text-decoration:none;color:inherit"><div class="card__icon">🛍️</div><h3 class="card__title">Retail &amp; Mixed-Use</h3><p class="card__desc">75% energy reduction. Solar canopy parking, customer-facing sustainability, and demand charge mitigation.</p><span class="card__link">See industry page →</span></a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Enterprise-Grade Delivery</span><h2>Your dedicated project director keeps you in control at every stage.</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3 class="card__title">Portfolio Analysis</h3><p class="card__desc">Energy analytics, site audits, structural reviews, and incentive discovery for every property in your footprint.</p></div>
      <div class="card"><h3 class="card__title">Financial Modeling</h3><p class="card__desc">10- to 25-year cash-flow projections and board-ready business cases with multiple funding paths.</p></div>
      <div class="card"><h3 class="card__title">Engineering &amp; Permitting</h3><p class="card__desc">Stamped drawings, utility interconnection packages, AHJ coordination, and structural certification.</p></div>
      <div class="card"><h3 class="card__title">Installation &amp; Commissioning</h3><p class="card__desc">OSHA-compliant crews install with minimal downtime; we commission and train your facilities team.</p></div>
      <div class="card"><h3 class="card__title">Lifecycle Operations</h3><p class="card__desc">Dedicated commercial maintenance plans with 24/7 monitoring, inspections, and priority dispatch.</p></div>
      <div class="card"><h3 class="card__title">Quarterly Reporting</h3><p class="card__desc">Executive-level performance reviews with KPI dashboards and compliance documentation.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section(
        "From Gulf Coast petrochemical plants to DFW logistics hubs.",
        "Hart Beat Energy programs deliver measurable ROI and resilience for multi-site operators and single-facility businesses alike.",
        "Schedule a portfolio review", "{BASE}contact.html",
        "Request maintenance briefing", "{BASE}maintenance/index.html",
    )
    return body

# ============================================================
# BATTERY STORAGE
# ============================================================
def battery_storage():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Battery Storage", None)]) + '</div>'
    body += hero(
        badge="🔋 Battery Storage",
        headline_html='Keep the lights on when <span class="hl">the Texas grid doesn\'t</span>.',
        lede="Pair your solar array with Tesla Powerwall or Schneider XW Pro storage to ride through outages, shave peak demand charges, and capture every kWh your roof produces. Hart Beat Energy engineers storage for Texas heat, hail, and hurricanes.",
        cta_primary="Get a storage quote", cta_primary_href="{BASE}contact.html",
        cta_secondary="See financing", cta_secondary_href="{BASE}financing.html",
        stats=[("13.5 kWh", "Powerwall capacity"), ("10+ hr", "Typical backup runtime"), ("$0 down", "Financing available")],
        bg_image=IMG["hero_battery"],
    )
    body += '''
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Why Storage</span>
      <h2>Resilience, self-consumption, and peak shaving — in one box.</h2>
      <p>A battery turns your solar array from a daytime bill-reducer into a 24-hour energy asset. During ERCOT outages, your essential loads keep running. During peak pricing windows, you discharge stored solar instead of paying premium rates.</p>
      <ul class="check-list">
        <li><strong>Whole-home or partial backup</strong> — choose critical circuits or full-home failover</li>
        <li><strong>Time-of-use optimization</strong> — discharge during expensive peak periods</li>
        <li><strong>Self-consumption boost</strong> — use every kWh your roof produces, day or night</li>
        <li><strong>Seamless switching</strong> — ~20ms automatic transfer when grid fails</li>
        <li><strong>Modular expansion</strong> — stack multiple units for larger energy needs</li>
      </ul>
    </div>
    <div>
      <div class="card card--feature">
        <h3>Storage Platforms We Install</h3>
        <div class="grid" style="gap:12px;margin-top:16px">
          <div class="callout" style="padding:16px"><strong>Tesla Powerwall 3</strong><br><small>13.5 kWh · Integrated inverter · App control · Storm Watch</small></div>
          <div class="callout" style="padding:16px"><strong>Schneider XW Pro + Schneider Home</strong><br><small>Whole-home energy ecosystem · Load panel integration</small></div>
          <div class="callout" style="padding:16px"><strong>Enphase IQ Battery</strong><br><small>Modular 3.5/10 kWh · Microinverter architecture</small></div>
        </div>
      </div>
    </div>
  </div>
</section>

'''
    body += image_band(IMG["feature_panel_closeup"], overlay_text="Every kWh stored. Every outage survived.")
    body += '''
<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><h2>Texas backup scenarios we engineer for.</h2></div>
    <div class="grid grid-3">
      <div class="card"><div class="card__icon">⛈️</div><h3 class="card__title">Hurricane &amp; Severe Weather</h3><p class="card__desc">Gulf Coast storms can drop grid service for days. Storage + solar keeps refrigeration, medical devices, and internet running.</p></div>
      <div class="card"><div class="card__icon">🥶</div><h3 class="card__title">Winter Storm Events</h3><p class="card__desc">After Uri, tens of thousands of Texans added storage. Keep heat circulating and pipes from freezing.</p></div>
      <div class="card"><div class="card__icon">⚡</div><h3 class="card__title">ERCOT Peak Pricing</h3><p class="card__desc">Summer afternoons push grid rates sky-high. Discharge stored solar during peak windows and buy back at night.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section(
        "Ready to take your home or business off-grid-capable?",
        "Our storage specialists will size the right system for your load profile, backup priorities, and budget.",
        "Get a storage quote", "{BASE}contact.html",
        "Call (346) 330-2550", "tel:3463302550",
    )
    return body

# ============================================================
# FINANCING
# ============================================================
def financing():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Financing", None)]) + '</div>'
    body += hero(
        badge="💰 Financing Options",
        headline_html='Make solar affordable with <span class="hl">flexible financing</span>. $0-down options with immediate savings.',
        lede="Our in-house financing specialists work with multiple lenders and program providers to find the right structure for your goals. Residential: lease, PPA, loan, or cash. Commercial: PPA, lease, loan, or capital purchase with full ITC access.",
        cta_primary="Check financing options", cta_primary_href="{BASE}contact.html",
        cta_secondary="Compare lease vs PPA", cta_secondary_href="{BASE}lease-vs-ppa.html",
        stats=[("$0", "Down payment on lease/PPA"), ("4.49%+", "Loan rates from"), ("25 yrs", "Max term available")],
        bg_image=IMG["hero_financing"],
    )
    body += '''
<section class="section">
  <div class="container">
    <div class="callout callout--warn mb-4"><strong>2026 residential landscape:</strong> The federal 30% residential solar tax credit expired July 2025. Most Texas homeowners today choose $0-down solar <strong>leases or PPAs</strong> — which shift the tax-credit mechanics to the system owner and pass savings to you as lower monthly payments. <a href="{BASE}lease-vs-ppa.html">Learn how the two differ →</a></div>

    <div class="text-center mb-4"><span class="eyebrow">Compare Financing Options</span><h2>Four paths — find the right one for your budget.</h2></div>
    <div class="grid grid-2">
      <div class="card card--feature"><h3 class="card__title">📋 Solar Lease <span class="badge badge--sun">Most Popular 2026</span></h3><p class="card__desc">Rent the system with predictable fixed monthly payments. Maintenance included. $0 down. No tax-credit paperwork.</p>
        <ul class="check-list"><li>$0 down payment</li><li>Fixed monthly lease payment</li><li>Maintenance &amp; monitoring included</li><li>Production guarantee</li><li>Option to buy at end of term</li></ul>
        <p style="font-size:.88rem;color:#5a6578"><strong>Best for:</strong> Homeowners who want simplicity, no maintenance worries, and guaranteed savings.</p>
      </div>
      <div class="card card--feature"><h3 class="card__title">⚡ Power Purchase Agreement</h3><p class="card__desc">Pay only for the power your system generates, at a rate below your utility.</p>
        <ul class="check-list"><li>$0 upfront cost</li><li>Pay per kWh produced</li><li>Rate lower than utility</li><li>Maintenance included</li><li>Production-based billing</li></ul>
        <p style="font-size:.88rem;color:#5a6578"><strong>Best for:</strong> Homeowners &amp; businesses focused on immediate kWh-rate reduction with no capex.</p>
      </div>
      <div class="card"><h3 class="card__title">🏦 Solar Loan</h3><p class="card__desc">Finance the system with competitive rates. You own it from day one.</p>
        <ul class="check-list"><li>$0 down options available</li><li>Own system immediately</li><li>Eligible for residual incentives</li><li>Rates from 4.49% APR</li><li>Terms up to 25 years</li></ul>
        <p style="font-size:.88rem;color:#5a6578"><strong>Best for:</strong> Homeowners wanting ownership + long-term equity.</p>
      </div>
      <div class="card"><h3 class="card__title">💵 Cash Purchase</h3><p class="card__desc">Pay upfront for maximum lifetime savings and full ownership.</p>
        <ul class="check-list"><li>Highest lifetime ROI</li><li>No financing costs</li><li>Immediate ownership</li><li>Full warranty coverage</li><li>Eligible for residual incentives</li></ul>
        <p style="font-size:.88rem;color:#5a6578"><strong>Best for:</strong> Homeowners with available capital seeking maximum returns.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Savings Calculator</span><h2>See how the numbers work for your home.</h2></div>
    <div class="card card--feature" data-calc style="max-width:760px;margin:0 auto">
      <div class="form__row">
        <div><label class="form__label" for="calc-bill">Current monthly electric bill</label><input id="calc-bill" class="form__input" type="number" value="180" min="50" max="1500" data-calc-bill></div>
        <div><label class="form__label" for="calc-years">Time horizon (years)</label><input id="calc-years" class="form__input" type="number" value="20" min="5" max="25" data-calc-years></div>
      </div>
      <div class="grid grid-3 mt-3">
        <div><div class="stat__n" data-calc-out-bill>$144</div><div class="stat__l">Est. new monthly bill (w/ solar)</div></div>
        <div><div class="stat__n" data-calc-out-lease>$8,640</div><div class="stat__l">Lifetime lease savings</div></div>
        <div><div class="stat__n" data-calc-out-20>$58,000</div><div class="stat__l">Total utility cost w/o solar</div></div>
      </div>
      <p class="form__note mt-3">Illustrative based on 20% avg bill reduction and 3% annual utility escalator. Your actual savings depend on roof, utility, and program selected.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Texas-Specific Incentives</span><h2>Stack every benefit available to you.</h2></div>
    <div class="grid grid-4">
      <div class="card"><div class="stat__n" style="color:#f5a623">30%</div><div class="stat__l"><strong>Commercial Federal ITC</strong> — Investment Tax Credit applies to commercial &amp; business projects through 2032</div></div>
      <div class="card"><div class="stat__n" style="color:#f5a623">100%</div><div class="stat__l"><strong>Texas Property Tax Exemption</strong> — no property tax on added home value</div></div>
      <div class="card"><div class="stat__n" style="color:#f5a623">100%</div><div class="stat__l"><strong>Texas Sales Tax Exemption</strong> — on qualifying solar equipment</div></div>
      <div class="card"><div class="stat__n" style="color:#f5a623">85%</div><div class="stat__l"><strong>MACRS Depreciation</strong> — accelerated year-one for commercial projects</div></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Our Lending Partners</span><h2>Competitive rates from trusted capital providers.</h2></div>
    <div class="grid grid-4">
      <div class="card"><h3 class="card__title">GoodLeap</h3><div class="stat__n">From 4.99%</div><div class="stat__l">Up to 25-year terms</div></div>
      <div class="card"><h3 class="card__title">Mosaic</h3><div class="stat__n">From 5.49%</div><div class="stat__l">Up to 20-year terms</div></div>
      <div class="card"><h3 class="card__title">Sunlight Financial</h3><div class="stat__n">From 5.99%</div><div class="stat__l">Up to 25-year terms</div></div>
      <div class="card"><h3 class="card__title">Credit Unions</h3><div class="stat__n">From 4.49%</div><div class="stat__l">Up to 15-year terms</div></div>
    </div>
  </div>
</section>
'''
    body += cta_section(
        "Ready to go solar with $0 down?",
        "Get pre-qualified in minutes. No impact to your credit score. Multiple financing options presented side-by-side so you can pick what fits.",
        "Check Financing Options", "{BASE}contact.html",
        "Talk to a finance expert →", "tel:3463302550",
    )
    return body

# ============================================================
# LEASE VS PPA
# ============================================================
def lease_vs_ppa():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Financing", "financing.html"), ("Lease vs PPA", None)]) + '</div>'
    body += hero(
        badge="📊 Lease vs PPA",
        headline_html='Lease or PPA? Here\'s <span class="hl">which $0-down path</span> fits your home.',
        lede="Both options cost nothing upfront. Both include maintenance. Both are designed for the 2026 Texas solar landscape. The difference is how you pay: fixed monthly (lease) or per-kWh produced (PPA). Here's what most Texas homeowners should know.",
        cta_primary="Get my personalized comparison", cta_primary_href="{BASE}contact.html",
        cta_secondary="All financing options", cta_secondary_href="{BASE}financing.html",
        bg_image=IMG["hero_financing"],
    )
    body += '''
<section class="section">
  <div class="container" style="max-width:960px">
    <span class="eyebrow">Quick Context</span>
    <h2>Why these two options matter more in 2026</h2>
    <p>The federal residential 30% Investment Tax Credit for homeowners expired July 2025. For homeowners, that removes a major chunk of the direct-ownership economics. But the 30% ITC <em>still applies</em> to systems owned by a third party — like a lease or PPA provider — who then passes those savings to you in the form of lower monthly payments or lower per-kWh rates.</p>
    <p><strong>Translation:</strong> in 2026, leases and PPAs are often the most cost-effective residential path, because the tax credit is still being captured by the system owner and flowing through to you.</p>

    <h2 class="mt-4">How each works</h2>
    <div class="grid grid-2 mt-3">
      <div class="card card--feature">
        <h3>Solar Lease</h3>
        <p><strong>What you pay:</strong> A fixed monthly lease payment, regardless of production.</p>
        <p><strong>What you get:</strong> Unlimited solar electricity the system produces, plus maintenance &amp; monitoring.</p>
        <p><strong>Best if:</strong> You want predictable budget-friendly monthly payments and production-risk protection.</p>
        <ul class="check-list">
          <li>Same lease payment every month (with optional escalator of 0–2.9%)</li>
          <li>Production guarantee — if system underperforms, you get a credit</li>
          <li>Maintenance included for full term</li>
          <li>Typical term: 20–25 years</li>
          <li>End of term: buy system, renew, or have it removed</li>
        </ul>
      </div>
      <div class="card card--feature">
        <h3>Power Purchase Agreement (PPA)</h3>
        <p><strong>What you pay:</strong> A per-kWh rate on the electricity your system produces.</p>
        <p><strong>What you get:</strong> A solar rate lower than your current utility rate, plus maintenance &amp; monitoring.</p>
        <p><strong>Best if:</strong> You want to see direct correlation between production and what you pay.</p>
        <ul class="check-list">
          <li>Pay only for kWh the system actually produces</li>
          <li>Rate locked in below your utility baseline</li>
          <li>Maintenance included for full term</li>
          <li>Typical term: 20–25 years</li>
          <li>End of term: buy system, renew, or have it removed</li>
        </ul>
      </div>
    </div>

    <h2 class="mt-4">Side-by-side comparison</h2>
    <div class="card" style="padding:0;overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:.94rem">
        <thead><tr style="background:#0b1f3a;color:#fff"><th style="padding:14px;text-align:left">Feature</th><th style="padding:14px;text-align:left">Lease</th><th style="padding:14px;text-align:left">PPA</th></tr></thead>
        <tbody>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>Upfront cost</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">$0</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">$0</td></tr>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>Monthly payment basis</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Fixed</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Per kWh produced</td></tr>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>Bill predictability</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Highest</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Moderate (tracks production)</td></tr>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>Production risk</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Owner (guaranteed)</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Owner (you pay only for what's made)</td></tr>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>Maintenance</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Included</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Included</td></tr>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>Monitoring</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Know TrueUp® included</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Know TrueUp® included</td></tr>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>Escalator</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">0–2.9% typical</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">0–2.9% typical</td></tr>
          <tr><td style="padding:14px;border-bottom:1px solid #e0e6ef"><strong>End of term options</strong></td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Buy / renew / remove</td><td style="padding:14px;border-bottom:1px solid #e0e6ef">Buy / renew / remove</td></tr>
          <tr><td style="padding:14px"><strong>Home sale transfer</strong></td><td style="padding:14px">Assumable by buyer</td><td style="padding:14px">Assumable by buyer</td></tr>
        </tbody>
      </table>
    </div>

    <h2 class="mt-4">Common questions</h2>
    <div class="faq" data-single>
      <details><summary>Does a lease or PPA hurt my home sale?</summary><div><p>No — when structured correctly, both are transferable to the buyer. Buyers typically see it as a plus: lower electric bills from day one with no capex. Our team handles transfer paperwork at closing. Over 90% of our lease/PPA transfers close without issue.</p></div></details>
      <details><summary>Who owns the solar panels?</summary><div><p>A third-party system owner (the lease/PPA provider) owns the panels for the duration of the term. They claim the 30% ITC and depreciation, which is how they're able to offer $0-down with lower-than-utility pricing.</p></div></details>
      <details><summary>What happens if I move before the term ends?</summary><div><p>Three options: (1) transfer the agreement to your home's buyer — most common, (2) pay the remaining buyout to own the system, or (3) have the system removed (rare). We support all three paths.</p></div></details>
      <details><summary>Can I buy the system outright later?</summary><div><p>Yes. Leases and PPAs both include buyout options — typically at specific year milestones (e.g., years 6, 10, 15) plus at end of term. Buyout prices are pre-disclosed in your contract.</p></div></details>
      <details><summary>What about maintenance if something breaks?</summary><div><p>Covered. The system owner is responsible for maintenance, repairs, and monitoring during the term. Hart Beat Energy provides the maintenance under most Texas lease/PPA programs we sell.</p></div></details>
    </div>
  </div>
</section>
'''
    body += cta_section(
        "Still not sure which fits?",
        "Get a side-by-side lease + PPA + loan comparison for your specific home — free, no obligation.",
        "Get my personalized comparison", "{BASE}contact.html",
        "Call our team", "tel:3463302550",
    )
    return body
