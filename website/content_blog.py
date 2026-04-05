"""Blog index + posts."""
from build import IMG, hero, cta_section, breadcrumb_html

POSTS = [
    {
        "slug": "texas-solar-2026-after-itc-expired",
        "title": "Texas Solar in 2026: What Changed After the Residential ITC Expired",
        "date": "2026-03-28",
        "author": "Brandon Hart",
        "category": "Policy",
        "excerpt": "The federal 30% residential solar tax credit expired July 4, 2025. Here's what Texas homeowners need to know about the new $0-down lease and PPA path — and why solar math still works in 2026.",
        "read_min": 8,
    },
    {
        "slug": "solar-lease-vs-ppa-texas-homeowners",
        "title": "Solar Lease vs. PPA: Which Is Right for Texas Homeowners?",
        "date": "2026-03-14",
        "author": "Hart Beat Energy Team",
        "category": "Financing",
        "excerpt": "With the residential ITC gone, $0-down lease and PPA contracts have become the dominant path to solar savings in Texas. We break down the real differences — escalator rates, buyout options, transferability, and the math behind each.",
        "read_min": 10,
    },
    {
        "slug": "ercot-storm-prep-solar-battery-homeowners",
        "title": "ERCOT Storm Prep: How Solar + Battery Protects Texas Homes",
        "date": "2026-02-21",
        "author": "Hart Beat Energy Team",
        "category": "Resilience",
        "excerpt": "After Uri, Beryl, and the 2024 derecho, Texas homeowners know grid reliability is no longer guaranteed. Here's how a properly-sized battery system keeps your lights, fridge, and A/C running through the next outage.",
        "read_min": 7,
    },
    {
        "slug": "houston-hoa-solar-approval-guide",
        "title": "Houston HOA Solar Approval: The Complete Homeowner Guide",
        "date": "2026-02-07",
        "author": "Hart Beat Energy Team",
        "category": "How-To",
        "excerpt": "Texas Property Code §202.010 limits what HOAs can restrict about solar. Here's exactly how to file for approval in a Houston-area HOA, what to expect, and how we handle the process for every homeowner we work with.",
        "read_min": 6,
    },
    {
        "slug": "commercial-solar-itc-macrs-2026",
        "title": "Commercial Solar in 2026: ITC + MACRS Still Delivers 5-Year Payback",
        "date": "2026-01-24",
        "author": "Brandon Hart",
        "category": "Commercial",
        "excerpt": "While residential incentives shifted, the commercial 30% Investment Tax Credit remains through 2032 — and when you stack it with 5-year MACRS accelerated depreciation, Texas businesses are still seeing 5-7 year paybacks.",
        "read_min": 9,
    },
    {
        "slug": "texas-solar-buyback-plans-retail-providers",
        "title": "Texas Solar Buyback Plans: Comparing Retail Electric Providers in 2026",
        "date": "2026-01-10",
        "author": "Hart Beat Energy Team",
        "category": "Financing",
        "excerpt": "In Oncor and CenterPoint territory, you pick your retail provider — and that choice directly affects how much you earn from solar exports. We compare Rhythm, TXU, Reliant, Green Mountain, and more.",
        "read_min": 8,
    },
]

def blog_index_page():
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Blog", None)]) + '</div>'
    body += hero(
        badge="📰 The Hart Beat Blog",
        headline_html='Texas solar insights, policy updates, and <span class="hl">homeowner guides</span>.',
        lede="Straight-talk articles on solar financing, ERCOT policy, battery storage, HOA approval, and everything in between. No fluff, no sales pitch — just the details Texas homeowners and businesses actually need.",
        cta_primary="Get a free quote", cta_primary_href="{BASE}contact.html",
        cta_secondary="Call (346) 330-2550", cta_secondary_href="tel:3463302550",        bg_image=IMG["hero_blog"],

    )
    cards = ""
    for p in POSTS:
        cards += f'''<article class="card post-card">
          <div class="post-card__meta"><span class="tag">{p["category"]}</span> · {p["date"]} · {p["read_min"]} min read</div>
          <h3 class="card__title"><a href="{{BASE}}blog/{p["slug"]}.html">{p["title"]}</a></h3>
          <p class="card__desc">{p["excerpt"]}</p>
          <div class="post-card__footer">By {p["author"]} · <a href="{{BASE}}blog/{p["slug"]}.html" class="card__link">Read article →</a></div>
        </article>'''
    body += f'''
<section class="section">
  <div class="container">
    <div class="grid grid-2">{cards}</div>
  </div>
</section>
'''
    body += cta_section(
        "Ready to talk solar for your home or business?",
        "Free consultation, custom modeling, and a clear path to energy savings.",
        "Get my free quote", "{BASE}contact.html",
        "Call (346) 330-2550", "tel:3463302550",
    )
    return body


POST_BODIES = {
    "texas-solar-2026-after-itc-expired": '''
<section class="section"><div class="container prose">
<p class="lede">On July 4, 2025, the federal 30% residential solar Investment Tax Credit expired. For the first time in almost two decades, new Texas homeowners installing solar cannot claim a federal tax credit. Here's what that actually means — and why the solar math still works in 2026.</p>

<h2>What exactly changed</h2>
<p>The One Big Beautiful Bill Act (signed July 2025) accelerated the sunset of Section 25D — the residential ITC. As of July 4, 2025, new residential solar purchases no longer qualify for the 30% federal tax credit. Commercial solar (Section 48) retains the 30% ITC through at least 2032.</p>

<h2>The $0-down lease and PPA path</h2>
<p>Because leases and PPAs are owned by a third-party financing entity, that entity — not the homeowner — claims the commercial ITC. That tax benefit is passed through to the homeowner in the form of lower monthly payments and locked-in rates. In practice, Texas homeowners today can get solar with:</p>
<ul class="check-list">
  <li>$0 down</li>
  <li>Monthly payment lower than their current electric bill</li>
  <li>2.9% annual escalator (or fixed-rate options)</li>
  <li>25-year production guarantee</li>
  <li>Full transferability at home sale</li>
</ul>

<h2>Why it still makes sense</h2>
<p>Texas retail electricity rates have risen 34% over the past five years, and ERCOT forecasts continued upward pressure. A lease or PPA locks you into a predictable rate that escalates slowly (or not at all), while your utility rate keeps climbing. Over 20 years, the typical Houston homeowner still saves $30,000-$50,000.</p>

<h2>Commercial customers: nothing changed</h2>
<p>If you're a Texas business, farm, nonprofit, or commercial property owner, the 30% ITC + MACRS depreciation stack remains fully intact through at least 2032. Typical payback: 5-7 years.</p>
</div></section>
''',
    "solar-lease-vs-ppa-texas-homeowners": '''
<section class="section"><div class="container prose">
<p class="lede">"Lease" and "PPA" get used interchangeably, but they're different contracts with different economics. Here's a plain-English breakdown of how each one works in Texas post-2025.</p>

<h2>Solar Lease</h2>
<p>You pay a fixed monthly payment to use the solar system on your roof. That payment does not change based on how much energy the panels produce. If the system overproduces, you keep the savings. If it underproduces, you still pay the same fixed rate.</p>

<h2>Power Purchase Agreement (PPA)</h2>
<p>You pay a per-kWh rate only for the energy the panels actually produce. There's no payment for a month the system is down. Your rate is lower than the utility's, locked in for 20-25 years with a modest annual escalator (typically 0-2.9%).</p>

<h2>Which wins in Texas?</h2>
<p>For most Texas homeowners, the answer comes down to risk preference. Leases give you pricing certainty. PPAs align your payment to actual production (slightly more favorable in shaded or complex-roof situations). Both are $0-down, both are transferable at home sale, and both are available with Hart Beat Energy.</p>
</div></section>
''',
    "ercot-storm-prep-solar-battery-homeowners": '''
<section class="section"><div class="container prose">
<p class="lede">Winter Storm Uri (2021), Hurricane Beryl (2024), and the May 2024 derecho made one thing clear: ERCOT grid reliability is no longer guaranteed. Here's how a properly-sized battery system keeps your household running through the next outage.</p>

<h2>What a battery actually backs up</h2>
<p>The size of your battery determines which loads stay online. A single Tesla Powerwall 3 (13.5 kWh usable) can typically support: refrigerator + freezer, internet + networking, lighting, phone charging, ceiling fans, and a small window A/C or mini-split — for roughly 12-24 hours depending on usage.</p>

<h2>Central A/C during outages</h2>
<p>Running central A/C during an outage requires 2-3 Powerwalls or equivalent. For Texas summer outages, most households step up to a 2-battery system so that at least one A/C zone stays online.</p>

<h2>Solar + battery beats generator</h2>
<p>Unlike a gas generator, a solar-charged battery recharges itself every sunny day. In multi-day outages (Beryl's aftermath lasted 10+ days for many Houston neighborhoods), battery + rooftop solar is the only residential backup source that keeps producing indefinitely.</p>
</div></section>
''',
    "houston-hoa-solar-approval-guide": '''
<section class="section"><div class="container prose">
<p class="lede">Texas Property Code §202.010 sharply limits what an HOA can restrict about residential solar. Here's the process for getting HOA approval in a Houston-area neighborhood — step by step.</p>

<h2>What HOAs can and can't do</h2>
<p>HOAs cannot prohibit solar entirely. They also cannot require placement that reduces production by more than 10%, or demand aesthetic modifications (paint, screens, etc.) that raise project cost by more than 10%.</p>

<h2>The approval timeline</h2>
<p>Most Houston-area HOAs approve solar within 30-45 days. Hart Beat Energy submits the architectural review package on your behalf — including roof layout, panel spec sheets, structural letter, and §202.010 compliance statement — and tracks the application through approval.</p>
</div></section>
''',
    "commercial-solar-itc-macrs-2026": '''
<section class="section"><div class="container prose">
<p class="lede">The commercial 30% Investment Tax Credit (Section 48) remains intact through at least 2032. Stack it with 5-year MACRS accelerated depreciation and Texas businesses are still seeing 5-7 year paybacks — sometimes shorter with bonus depreciation.</p>

<h2>The full incentive stack</h2>
<ul class="check-list">
  <li><strong>30% Federal ITC</strong> — direct reduction of federal tax liability</li>
  <li><strong>MACRS 5-year depreciation</strong> — recover ~85% of remaining cost basis over 5 years</li>
  <li><strong>60% Bonus depreciation (2026)</strong> — front-load depreciation in year 1</li>
  <li><strong>Texas no-income-tax advantage</strong> — federal deductions pass through cleanly</li>
</ul>

<h2>Typical commercial project economics</h2>
<p>For a $500,000 commercial solar project, after stacking ITC + bonus depreciation + year 1-5 MACRS, typical effective net cost drops to roughly $225,000-$275,000. Combined with $60,000-$90,000 in annual electric savings, payback is often under 6 years.</p>
</div></section>
''',
    "texas-solar-buyback-plans-retail-providers": '''
<section class="section"><div class="container prose">
<p class="lede">In Oncor (DFW) and CenterPoint (Houston) territories, you pick your retail electric provider. That choice directly affects how much you earn from exported solar. Here's how the major providers compare in 2026.</p>

<h2>Full 1:1 buyback (net metering equivalent)</h2>
<p>Providers like <strong>Rhythm Energy</strong>, <strong>Chariot Energy</strong>, and <strong>Green Mountain Energy</strong> offer plans that credit exports at or near your import rate. Best for systems sized close to your annual usage.</p>

<h2>Reduced-rate buyback</h2>
<p><strong>TXU</strong>, <strong>Reliant</strong>, and <strong>Direct Energy</strong> typically credit exports at 50-75% of import rate. Better for small/undersized systems where most production is consumed on-site.</p>

<h2>How we help</h2>
<p>We model your annual production against your bill and recommend the plan that maximizes your economics over a 20-year horizon. We'll also re-evaluate annually — retail plans change, and switching is free in Texas.</p>
</div></section>
''',
}


POST_HEROES = {
    "texas-solar-2026-after-itc-expired": IMG["feature_family"],
    "solar-lease-vs-ppa-texas-homeowners": IMG["feature_savings"],
    "ercot-storm-prep-solar-battery-homeowners": IMG["hero_storm"],
    "houston-hoa-solar-approval-guide": IMG["feature_home"],
    "commercial-solar-itc-macrs-2026": IMG["feature_warehouse"],
    "texas-solar-buyback-plans-retail-providers": IMG["feature_savings"],
}

def blog_post_page(slug):
    post = next(p for p in POSTS if p["slug"] == slug)
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Blog", "blog/index.html"), (post["title"], None)]) + '</div>'
    hero_img = POST_HEROES.get(slug, IMG["hero_blog"])
    body += f'''
<section class="hero hero--bg" style="background-image:url('{hero_img}')">
  <div class="container">
    <div class="post-meta" style="color:rgba(255,255,255,.85)"><span class="tag">{post["category"]}</span> · {post["date"]} · {post["read_min"]} min read · By {post["author"]}</div>
    <h1 class="post-title" style="color:#fff;max-width:900px">{post["title"]}</h1>
  </div>
</section>
'''
    body += POST_BODIES.get(slug, '<section class="section"><div class="container prose"><p>Article coming soon.</p></div></section>')
    body += cta_section(
        "Questions about solar for your home or business?",
        "Free consultation, custom modeling, no obligation.",
        "Get my free quote", "{BASE}contact.html",
        "Call (346) 330-2550", "tel:3463302550",
    )
    return body
