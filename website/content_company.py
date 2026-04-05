"""Company pages: about, contact, reviews, faq, case-studies, warranty, storm-claims, referral, careers, membership."""
from build import IMG, hero, cta_section, breadcrumb_html

def about():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("About", None)]) + '</div>'
    body += hero(
        badge="About Hart Beat Energy",
        headline_html='Texas-owned, Texas-run, serving <span class="hl">every county</span> for over a decade.',
        lede="Hart Beat Energy was founded in Houston in 2014 by engineers and installers who were tired of watching solar customers get abandoned after install-day. We built the company we wish had existed — design, install, and maintain for life.",
        cta_primary="See our work", cta_primary_href="{BASE}case-studies.html",
        cta_secondary="Contact us", cta_secondary_href="{BASE}contact.html",
        stats=[("2014", "Founded"), ("5,000+", "Systems installed"), ("420+", "Commercial clients")],        bg_image=IMG["hero_about"],

    )
    body += '''
<section class="section">
  <div class="container" style="max-width:820px">
    <span class="eyebrow">Our Story</span>
    <h2>Why "Hart Beat"?</h2>
    <p>Because a solar system should beat steadily — day in, day out, for 25+ years — just like a healthy heart. And because our founder, an Army veteran who came home to Texas with a background in field diagnostics, believed every homeowner and business deserved a solar partner that monitored performance <em>for them</em>, not just handed over a login and wished them luck.</p>
    <p>Ten years later, that philosophy runs through everything we do. Every install comes with Know TrueUp® monitoring. Every membership includes proactive maintenance. Every customer gets a dedicated account manager who answers the phone.</p>

    <h2 class="mt-4">What we believe</h2>
    <ul class="check-list">
      <li><strong>Honesty wins.</strong> If solar isn't right for your roof or your budget, we'll say so. We turn down ~15% of leads for this reason.</li>
      <li><strong>Maintenance is design.</strong> A system you can't clean, inspect, or repair isn't an investment — it's a liability.</li>
      <li><strong>Texas is home.</strong> We design for Texas heat, Texas hail, Texas storms, Texas utilities, and Texas grid events. Nobody else does this the way we do.</li>
      <li><strong>Data is clarity.</strong> Know TrueUp® exists because we got tired of customers asking "is my system actually working?"</li>
    </ul>

    <h2 class="mt-4">Leadership</h2>
    <div class="grid grid-3 mt-3">
      <div class="card"><h3 class="card__title">Founder &amp; CEO</h3><p class="card__desc">15+ years in renewable energy. NABCEP-certified. Veteran-owned business operator. Active across ERCOT, NAHB-Texas, and SEIA.</p></div>
      <div class="card"><h3 class="card__title">VP of Operations</h3><p class="card__desc">Oversees 40+ field technicians across five Texas regions. Former commercial roofing executive, brings structural rigor to every install.</p></div>
      <div class="card"><h3 class="card__title">Director of Engineering</h3><p class="card__desc">Electrical engineer, NABCEP PV Design Specialist. Built Know TrueUp® from the ground up and leads AI-assisted roof modeling.</p></div>
    </div>

    <h2 class="mt-4">Certifications &amp; partners</h2>
    <div class="flex mt-3" style="gap:16px">
      <span class="badge">NABCEP Certified</span>
      <span class="badge">Texas Licensed Contractor</span>
      <span class="badge">Tesla Certified Installer</span>
      <span class="badge">Enphase Platinum</span>
      <span class="badge">BBB A+ Rating</span>
      <span class="badge">SEIA Member</span>
      <span class="badge">OSHA 30 Certified</span>
      <span class="badge">Veteran-Owned</span>
    </div>
  </div>
</section>
'''
    body += cta_section("Want to work with a partner that sticks around?","10 years in Texas, 5,000+ installs, and a maintenance team on standby 24/7.","Get a quote","{BASE}contact.html","Read customer reviews","{BASE}reviews.html")
    return body

def contact():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Contact", None)]) + '</div>'
    body += '''
<section class="hero" style="padding:80px 0 60px">
  <div class="container hero__inner">
    <div class="hero__badge">📞 Let's talk</div>
    <h1>Get your free Texas solar quote.</h1>
    <p class="lede">Tell us about your home or business. We'll model your roof, analyze your utility rate, and present lease, PPA, loan, and cash options side-by-side.</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div>
      <h2>Reach us directly</h2>
      <ul class="check-list">
        <li><strong>Phone:</strong> <a href="tel:3463302550">(346) 330-2550</a> — Mon–Fri 8a–6p, Sat 9a–3p</li>
        <li><strong>Email:</strong> <a href="mailto:info@hartbeat.solar">info@hartbeat.solar</a></li>
        <li><strong>Emergency line:</strong> <a href="tel:3463302550">24/7 for members</a></li>
        <li><strong>Office:</strong> 1200 Smith St, Suite 1600, Houston, TX 77002</li>
      </ul>
      <h2 class="mt-4">Service areas</h2>
      <p>All 254 Texas counties. Primary metros: Houston, Austin, San Antonio, Dallas, Fort Worth, El Paso, Corpus Christi. <a href="{BASE}locations/houston.html">See city pages →</a></p>
    </div>
    <div>
      <div class="card card--feature">
        <h3>Request a free quote</h3>
        <form class="form" data-form>
          <div class="form__row">
            <div><label class="form__label" for="c-name">Full name</label><input id="c-name" class="form__input" type="text" required></div>
            <div><label class="form__label" for="c-phone">Phone</label><input id="c-phone" class="form__input" type="tel" required></div>
          </div>
          <div><label class="form__label" for="c-email">Email</label><input id="c-email" class="form__input" type="email" required></div>
          <div class="form__row">
            <div><label class="form__label" for="c-zip">ZIP code</label><input id="c-zip" class="form__input" type="text" pattern="[0-9]{5}" required></div>
            <div><label class="form__label" for="c-type">Property type</label><select id="c-type" class="form__select"><option>Residential</option><option>Commercial</option><option>Agricultural / Ranch</option><option>Multi-site portfolio</option></select></div>
          </div>
          <div><label class="form__label" for="c-bill">Current monthly electric bill</label><select id="c-bill" class="form__select"><option>Under $100</option><option>$100 – $200</option><option>$200 – $400</option><option>$400 – $800</option><option>$800+</option></select></div>
          <div><label class="form__label" for="c-msg">What are you looking for?</label><textarea id="c-msg" class="form__textarea" placeholder="New install, storage, maintenance, orphaned system audit, etc."></textarea></div>
          <button type="submit" class="btn btn-primary btn-lg btn-block">Get my free quote</button>
          <p class="form__note">By submitting you agree to receive a callback. We do not share your info. <a href="{BASE}privacy.html">Privacy policy</a>.</p>
        </form>
        <div data-form-success style="display:none">
          <h3 style="color:#10b981">Thanks — we got it!</h3>
          <p>A Hart Beat Energy specialist will contact you within one business day. For urgent inquiries, call <a href="tel:3463302550">(346) 330-2550</a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''
    return body

def reviews():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Reviews", None)]) + '</div>'
    body += hero(
        badge="⭐ Customer Reviews",
        headline_html='Texas homeowners and businesses <span class="hl">rate us 4.9/5</span> across 287 verified reviews.',
        lede="Here's what clients across Houston, Austin, Dallas, San Antonio, and beyond say about working with Hart Beat Energy.",
        cta_primary="Get your free quote", cta_primary_href="{BASE}contact.html",
        stats=[("4.9/5", "Avg rating"), ("287", "Verified reviews"), ("A+", "BBB rating")],        bg_image=IMG["hero_contact"],

    )
    reviews_list = [
        ("Sarah Johnson","Houston, TX","Engineered a custom array and handled every permit. Their maintenance membership keeps production ~30% higher than my neighbor's panels. The Know TrueUp® dashboard is a game-changer."),
        ("Michael Chen","Austin, TX","From financing to installation, their team was proactive and responsive. The monitoring alerts give me peace of mind every day. Went with PPA — $0 down, immediate savings."),
        ("Robert Martinez","Dallas, TX","We have multiple commercial rooftops statewide and Hart Beat Energy manages all of them with consistent SLAs. Our cost-per-kWh dropped ~62% after they optimized our arrays."),
        ("Jennifer Nguyen","San Antonio, TX","They audited an old array we inherited when we bought the house — found two dead panels and a bad optimizer. Fixed everything under the original manufacturer warranty. Saved us thousands."),
        ("David Rodriguez","Fort Worth, TX","Hail storm last March took out four panels. Crew was on my roof in 26 hours with temp fix, full replacement in two weeks. Warranty claim handled entirely by them."),
        ("Amanda Lee","El Paso, TX","Lease was the right move for us — $0 down, maintenance included. Bill went from $340 to $89. Know TrueUp® shows us exactly what we're generating."),
        ("Carlos Herrera","Corpus Christi, TX","Hurricane-ready install. Rode through two named storms without a blip. Storage saved my fridge during the outage after Beryl. Worth every penny."),
        ("Megan Thompson","The Woodlands, TX","The consultation was honest — they told us our north-facing roof was sub-optimal and recommended a smaller system. Most companies would have oversold. We trust them."),
        ("James Wilson","Plano, TX","Commercial install for my office park. 3.2 year payback on the CAPEX model after ITC and MACRS. Quarterly reporting is beautiful — I send it to the board unedited."),
    ]
    body += '<section class="section"><div class="container"><div class="grid grid-3">'
    for name, loc, quote in reviews_list:
        body += f'<div class="testimonial"><div class="testimonial__stars">★★★★★</div><p class="testimonial__quote">"{quote}"</p><div class="testimonial__author">{name}</div><div class="testimonial__location">{loc}</div></div>'
    body += '</div></div></section>'
    body += cta_section("Ready to join 5,000+ Texas solar customers?","See why homeowners and businesses choose Hart Beat Energy — and stay.","Get your free quote","{BASE}contact.html","Call (346) 330-2550","tel:3463302550")
    return body

def faq():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("FAQ", None)]) + '</div>'
    body += hero(
        badge="❓ Frequently Asked Questions",
        headline_html='Everything Texans ask us about <span class="hl">going solar in 2026</span>.',
        lede="Honest, detailed answers — no sales fluff. If your question isn't here, call us.",
        cta_primary="Ask your question", cta_primary_href="{BASE}contact.html",        bg_image=IMG["hero_faq"],

    )
    body += '''
<section class="section">
  <div class="container" style="max-width:820px">
    <h2>Solar basics</h2>
    <div class="faq">
      <details><summary>Is solar worth it in Texas in 2026?</summary><div><p>For most Texas homeowners with a south, east, or west-facing roof and an electric bill over $120/month — yes. Lease and PPA programs currently offer $0-down with immediate bill savings of 15–25%. Commercial projects still qualify for the 30% ITC and MACRS depreciation, which typically creates 3–5 year paybacks.</p></div></details>
      <details><summary>What happened to the 30% federal tax credit?</summary><div><p>The <strong>residential</strong> Investment Tax Credit ended July 2025. Homeowners who install and pay cash or finance via loan no longer qualify for the 30% residential credit. However, the ITC <strong>still applies</strong> to commercial systems and to residential systems owned by a third-party (lease/PPA provider). That's why most Texas homeowners in 2026 go the lease/PPA route.</p></div></details>
      <details><summary>What direction does my roof need to face?</summary><div><p>South is optimal in Texas. East and west still produce ~85% of south-facing output. North-facing is rarely cost-effective. Ground-mount options are available for properties where roof isn't ideal.</p></div></details>
      <details><summary>How much does a system cost?</summary><div><p>Lease/PPA: $0 down, monthly payments roughly 70–80% of your current electric bill. Cash purchase: ~$1.80–$2.40/watt installed before incentives, so a typical 8 kW system lands $14,400–$19,200. Commercial projects vary widely by size and complexity.</p></div></details>
      <details><summary>How long does installation take?</summary><div><p>Most residential installs are completed in 1–2 days of on-roof work. Total project timeline including design, permits, HOA approval, utility interconnection, and install is 30–40 days typically.</p></div></details>
    </div>

    <h2 class="mt-4">Financing &amp; incentives</h2>
    <div class="faq">
      <details><summary>Do I need good credit to qualify for lease or PPA?</summary><div><p>Most lease/PPA providers require a FICO score of 640+. Some have programs down to 600. We work with multiple lenders and can match you to the right program.</p></div></details>
      <details><summary>What Texas incentives still apply to homeowners?</summary><div><p>(1) Texas property tax exemption on added home value, (2) Texas sales tax exemption on qualifying equipment, (3) Utility-specific rebates from Austin Energy, CPS Energy, Oncor, etc., (4) Net metering or buyback programs where available.</p></div></details>
      <details><summary>Can I still go solar if I don't owe federal tax?</summary><div><p>Yes — this is exactly who benefits most from lease/PPA. Since you don't need the tax credit to make the economics work (the provider claims it), your savings come straight from a lower monthly payment than your utility bill.</p></div></details>
      <details><summary>What if I can afford cash — should I still lease?</summary><div><p>Not necessarily. Cash purchase still delivers the highest lifetime savings if you have the capital. We model both paths and you pick.</p></div></details>
    </div>

    <h2 class="mt-4">System &amp; performance</h2>
    <div class="faq">
      <details><summary>What brands do you install?</summary><div><p>Panels: LONGi, REC, QCells. Inverters: Enphase, Tesla, SolarEdge, Schneider. Storage: Tesla Powerwall, Schneider, Enphase. We match the equipment to your roof, budget, and reliability priorities.</p></div></details>
      <details><summary>How long do solar panels last?</summary><div><p>Tier-1 panels carry 25-year production warranties, meaning they'll still produce at least 85–92% of original rated output at year 25. Actual lifespan often extends to 30–40 years with reduced output.</p></div></details>
      <details><summary>Do panels work on cloudy days?</summary><div><p>Yes — at reduced output. Panels produce roughly 10–25% of rated output on heavily cloudy days. Texas's high solar irradiance means even our cloudier months deliver strong production.</p></div></details>
      <details><summary>Will hail damage my panels?</summary><div><p>Tier-1 panels are tested to withstand 1-inch hail at 55 mph. Most Texas storms don't exceed that threshold. Larger hail events may damage panels — which is why we recommend storage + strong warranty coverage + homeowner insurance rider.</p></div></details>
      <details><summary>What is "Know TrueUp®"?</summary><div><p>Hart Beat Energy's proprietary monitoring platform. It tracks production minute-by-minute, benchmarks against weather-normalized expectations, alerts on anomalies, and predicts your utility true-up settlement before it hits.</p></div></details>
    </div>

    <h2 class="mt-4">Maintenance &amp; warranty</h2>
    <div class="faq">
      <details><summary>How often should I clean my panels?</summary><div><p>2–3x per year for most Texas homes. More often for properties near construction, heavy tree cover, or agricultural areas with dust.</p></div></details>
      <details><summary>What does the Hart Beat Energy warranty cover?</summary><div><p>25 years on panels (production), 25 years on workmanship, 10–25 years on inverters depending on manufacturer, 10 years on storage. See our <a href="{BASE}warranty.html">warranty page</a>.</p></div></details>
      <details><summary>Do you service systems you didn't install?</summary><div><p>Yes. We're certified on every major platform. Bring us your orphaned or abandoned system — we'll audit it, fix it, and put it on a membership plan.</p></div></details>
      <details><summary>What if I have a storm or hail claim?</summary><div><p>Call our emergency line 24/7. We'll document damage, work with your insurance, handle manufacturer warranty claims, and get you back up fast. See <a href="{BASE}storm-claims.html">storm &amp; hail claims</a>.</p></div></details>
    </div>
  </div>
</section>
'''
    body += cta_section("Still have questions?","Call us. Our consultations are free and we'll tell you exactly what makes sense for your roof.","Schedule a consultation","{BASE}contact.html","Call (346) 330-2550","tel:3463302550")
    return body

def case_studies():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Case Studies", None)]) + '</div>'
    body += hero(
        badge="📂 Case Studies",
        headline_html='Real Texas projects, <span class="hl">real Texas savings</span>.',
        lede="Every installation tells a story. Here are a few projects across the state that show what Hart Beat Energy delivers — from Houston homeowners to Dallas distribution centers.",
        cta_primary="Start your project", cta_primary_href="{BASE}contact.html",        bg_image=IMG["hero_cases"],

    )
    cases = [
        ("Houston Homeowner — 9.6 kW Lease", "Houston, TX", "Standard", "$0 down solar lease, south-facing roof, 24 panels, Enphase microinverters. Electric bill dropped from $287 to $94 average. Homeowner saves ~$2,300/year."),
        ("Austin Residential + Powerwall", "Austin, TX", "Premium", "11.4 kW Tesla solar + two Powerwalls. Rode through 6-hour outage after 2026 spring storm without interruption. Monthly payment fixed at $189; avg bill was $340."),
        ("Dallas Distribution Warehouse", "Dallas, TX", "Commercial", "680 kW rooftop solar on 112,000 sqft warehouse. 3.4 year payback with ITC + MACRS. $186k/year utility cost reduction. Integrated demand-response with Oncor."),
        ("San Antonio Medical Office", "San Antonio, TX", "Commercial", "92 kW carport-canopy solar. Covered staff parking. CPS Energy rebate stacked with ITC. 4.1 year payback. Patient-facing sustainability messaging drove new referrals."),
        ("Hill Country Ranch", "Fredericksburg, TX", "Residential + Storage", "18 kW ground-mount array with battery backup. Powers home + well pump + workshop. Homeowner went from $480/month to net-zero."),
        ("Multi-Site Retail Portfolio", "Texas statewide", "Commercial", "11 locations, 2.4 MW total. PPA structure with $0 CapEx. Blended kWh rate 38% below utility. Unified Know TrueUp® dashboard across all sites for facilities team."),
    ]
    body += '<section class="section"><div class="container"><div class="grid grid-3">'
    for title, loc, tag, desc in cases:
        body += f'<div class="card card--feature"><span class="badge badge--sun">{tag}</span><h3 class="card__title mt-2">{title}</h3><div class="testimonial__location">{loc}</div><p class="card__desc mt-2">{desc}</p></div>'
    body += '</div></div></section>'
    body += cta_section("Want to see more?","Request detailed case study PDFs for your industry or city.","Request case studies","{BASE}contact.html","See reviews","{BASE}reviews.html")
    return body

def warranty():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Warranty", None)]) + '</div>'
    body += hero(
        badge="🛡️ Warranty Coverage",
        headline_html='<span class="hl">25-year</span> production, performance, and workmanship assurance.',
        lede="Hart Beat Energy stands behind every system we install — and every system we take over. Here's exactly what's covered.",
        cta_primary="Ask about your warranty", cta_primary_href="{BASE}contact.html",        bg_image=IMG["hero_warranty"],

    )
    body += '''
<section class="section">
  <div class="container" style="max-width:960px">
    <h2>Coverage matrix</h2>
    <div class="grid grid-2 mt-3">
      <div class="card"><h3 class="card__title">Panel Production Warranty</h3><p class="card__desc">25 years — Tier-1 panels guaranteed to produce at least 85–92% of rated output at year 25.</p></div>
      <div class="card"><h3 class="card__title">Panel Product Warranty</h3><p class="card__desc">25 years — coverage against defects in materials and workmanship.</p></div>
      <div class="card"><h3 class="card__title">Inverter Warranty</h3><p class="card__desc">10–25 years depending on manufacturer. Enphase and Tesla inverters carry 25-year warranties.</p></div>
      <div class="card"><h3 class="card__title">Storage Warranty</h3><p class="card__desc">10 years on Tesla Powerwall, Enphase IQ Battery, and Schneider Home batteries.</p></div>
      <div class="card"><h3 class="card__title">Workmanship Warranty</h3><p class="card__desc">25 years — Hart Beat Energy stands behind every install, mount, penetration, and wire run.</p></div>
      <div class="card"><h3 class="card__title">Roof Penetration Warranty</h3><p class="card__desc">10-year leak-free guarantee on every roof penetration we make.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section("Have a warranty question?","We handle manufacturer claims end-to-end. No phone-tree headaches.","File a warranty claim","{BASE}contact.html","Call (346) 330-2550","tel:3463302550")
    return body

def storm_claims():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Storm &amp; Hail Claims", None)]) + '</div>'
    body += hero(
        badge="⛈️ Storm &amp; Hail Claims",
        headline_html='Texas weather happens. <span class="hl">We handle it.</span>',
        lede="From Gulf hurricanes to North Texas hail, Hart Beat Energy storm teams document damage, work with your insurer, file manufacturer warranty claims, and get your system back online fast.",
        cta_primary="📞 Emergency: (346) 330-2550", cta_primary_href="tel:3463302550",
        cta_secondary="Report non-emergency damage", cta_secondary_href="{BASE}contact.html",
        stats=[("24/7", "Emergency line"), ("&lt;48 hr", "Typical dispatch"), ("Full", "Insurance support")],        bg_image=IMG["hero_storm"],

    )
    body += '''
<section class="section">
  <div class="container">
    <h2>How we handle storm damage</h2>
    <div class="grid grid-3 mt-3">
      <div class="card"><h3 class="card__title">1. Emergency assessment</h3><p class="card__desc">We dispatch within 48 hours of major storm events. Temporary stabilization if needed.</p></div>
      <div class="card"><h3 class="card__title">2. Damage documentation</h3><p class="card__desc">Photos, thermal imaging, production data — delivered as a report your insurer can act on.</p></div>
      <div class="card"><h3 class="card__title">3. Insurance coordination</h3><p class="card__desc">We speak the insurance language and handle adjuster calls so you don't have to.</p></div>
      <div class="card"><h3 class="card__title">4. Manufacturer warranty</h3><p class="card__desc">Where applicable, we file warranty claims with panel &amp; inverter manufacturers in parallel.</p></div>
      <div class="card"><h3 class="card__title">5. Repair &amp; restoration</h3><p class="card__desc">On-truck inventory, factory-trained crews, all major brands serviced.</p></div>
      <div class="card"><h3 class="card__title">6. Production verification</h3><p class="card__desc">Know TrueUp® verifies full restoration before we close the ticket.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section("Add storm protection to your membership.","Members get priority dispatch and 20% off repairs.","View membership plans","{BASE}membership.html","Call emergency line","tel:3463302550")
    return body

def referral():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Referral Program", None)]) + '</div>'
    body += hero(
        badge="🤝 Referral Program",
        headline_html='Refer a friend. <span class="hl">Get $500.</span> They save thousands.',
        lede="When you refer a new residential customer who installs a system, you get $500. They get a $500 install credit. Commercial referrals earn $2,500+.",
        cta_primary="Refer someone now", cta_primary_href="{BASE}contact.html",        bg_image=IMG["hero_referral"],

    )
    body += '''
<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="card card--feature"><h3 class="card__title">Residential Referral</h3><div class="stat__n">$500</div><p class="card__desc">To you + $500 install credit to your friend.</p></div>
      <div class="card card--feature"><h3 class="card__title">Commercial Referral</h3><div class="stat__n">$2,500+</div><p class="card__desc">Scales with project size. Capped at $10k.</p></div>
      <div class="card card--feature"><h3 class="card__title">Maintenance Referral</h3><div class="stat__n">$100</div><p class="card__desc">For every system added to our maintenance program.</p></div>
    </div>
  </div>
</section>
'''
    body += cta_section("Know someone who needs solar?","Send them to us. Everybody wins.","Submit a referral","{BASE}contact.html","Call us","tel:3463302550")
    return body

def careers():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Careers", None)]) + '</div>'
    body += hero(
        badge="💼 Careers",
        headline_html='Join a Texas solar team that <span class="hl">takes care of its own</span>.',
        lede="Hart Beat Energy is hiring across installation, sales, engineering, and maintenance. Competitive pay, full benefits, training stipends, and a crew culture that sticks together.",
        cta_primary="View open positions", cta_primary_href="{BASE}contact.html",        bg_image=IMG["hero_careers"],

    )
    body += '''
<section class="section">
  <div class="container">
    <h2>Open positions</h2>
    <div class="grid grid-2 mt-3">
      <div class="card"><h3 class="card__title">Solar Installer / Crew Lead</h3><p class="card__desc"><em>Houston, Austin, Dallas, San Antonio</em> · NABCEP preferred · Competitive base + per-install bonus.</p></div>
      <div class="card"><h3 class="card__title">Solar Sales Consultant</h3><p class="card__desc"><em>Statewide, remote-friendly</em> · Consultative sales, no high-pressure tactics. Base + commission.</p></div>
      <div class="card"><h3 class="card__title">Solar Designer / Engineer</h3><p class="card__desc"><em>Houston HQ</em> · PV design, AutoCAD, Helioscope, utility interconnection experience.</p></div>
      <div class="card"><h3 class="card__title">Maintenance Technician</h3><p class="card__desc"><em>Regional — all Texas metros</em> · Truck + tools provided. Cleaning, repairs, inspections.</p></div>
      <div class="card"><h3 class="card__title">Customer Success Manager</h3><p class="card__desc"><em>Houston HQ / remote</em> · Account management for residential + SMB customers. Know TrueUp® expert.</p></div>
      <div class="card"><h3 class="card__title">Commercial Project Director</h3><p class="card__desc"><em>Houston / Dallas</em> · End-to-end ownership of commercial portfolios from design to commissioning.</p></div>
    </div>
    <h2 class="mt-4">Why work here</h2>
    <ul class="check-list">
      <li>Full medical, dental, vision — 100% covered for you, 70% for family</li>
      <li>401(k) with 4% match</li>
      <li>Annual training &amp; certification stipend ($1,500)</li>
      <li>Truck / tool allowance for field crews</li>
      <li>Veteran-owned — veterans especially welcome</li>
    </ul>
  </div>
</section>
'''
    body += cta_section("Ready to join?","Send us a resume and tell us what you're great at.","Apply now","{BASE}contact.html","Email careers@hartbeat.solar","mailto:careers@hartbeat.solar")
    return body

def membership():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Membership Plans", None)]) + '</div>'
    body += hero(
        badge="⭐ Membership Plans",
        headline_html='One plan covers <span class="hl">cleaning, monitoring, repairs, and storm response</span>.',
        lede="Stop wondering if your panels are clean, if your inverter is alerting, or who to call after a storm. Hart Beat Energy membership bundles everything into one predictable monthly rate.",
        cta_primary="Join today", cta_primary_href="{BASE}contact.html",        bg_image=IMG["hero_membership"],

    )
    body += '''
<section class="section">
  <div class="container">
    <div class="pricing">
      <div class="plan"><div class="plan__name">Essential</div><div class="plan__price">$29<small>/mo</small></div><div class="plan__sub">Residential systems up to 10 kW</div>
        <ul class="plan__features"><li>Know TrueUp® Pro monitoring</li><li>2 annual cleanings</li><li>Annual 50-point inspection</li><li>10% off repairs</li><li>Email alerts</li></ul>
        <a href="{BASE}contact.html" class="btn btn-outline btn-block">Start Essential</a>
      </div>
      <div class="plan plan--featured"><div class="plan__badge">Most Popular</div><div class="plan__name">Complete</div><div class="plan__price">$59<small>/mo</small></div><div class="plan__sub">Residential systems any size</div>
        <ul class="plan__features"><li>Know TrueUp® Pro monitoring</li><li>3 annual cleanings</li><li>Annual 50-point inspection</li><li>20% off repairs</li><li>Priority dispatch (within 24hr)</li><li>Critter Guard included</li><li>Storm response priority</li></ul>
        <a href="{BASE}contact.html" class="btn btn-primary btn-block">Start Complete</a>
      </div>
      <div class="plan"><div class="plan__name">Commercial</div><div class="plan__price">Custom<small>&nbsp;/mo</small></div><div class="plan__sub">Commercial &amp; multi-site</div>
        <ul class="plan__features"><li>Enterprise Know TrueUp®</li><li>Quarterly cleanings</li><li>Bi-annual inspections</li><li>25% off repairs</li><li>4-hour emergency dispatch</li><li>Dedicated account manager</li><li>Quarterly executive reports</li><li>SLA guarantees</li></ul>
        <a href="{BASE}contact.html" class="btn btn-outline btn-block">Contact Sales</a>
      </div>
    </div>
  </div>
</section>
'''
    body += cta_section("Already have a Hart Beat Energy system?","Adding membership takes 2 minutes. Call us or request online.","Add membership","{BASE}contact.html","Call (346) 330-2550","tel:3463302550")
    return body
