"""Industry vertical pages for commercial solar."""
from build import IMG, hero, cta_section, breadcrumb_html

INDUSTRIES = {
    "manufacturing": {
        "name": "Manufacturing",
        "headline": "Cut manufacturing energy costs with commercial solar.",
        "lede": "Manufacturing plants run 16–24 hours a day and carry some of the highest electricity bills in Texas. Solar + storage flattens demand charges, hedges against ERCOT price spikes, and stacks with 30% ITC + MACRS depreciation.",
        "stat_1": ("35-55%", "Typical energy bill reduction"),
        "stat_2": ("5-7 yr", "Payback with ITC + MACRS"),
        "stat_3": ("25 yr", "Production warranty"),
        "pain_points": [
            ("Demand charges eating margin", "Peak demand charges can represent 30-50% of a manufacturing electric bill. Battery storage discharges during peak windows to shave demand."),
            ("ERCOT price volatility", "Wholesale exposure means summer price spikes hit the P&L. On-site generation caps your exposure."),
            ("Roof real estate going unused", "Most manufacturing facilities have 50,000+ sq ft of flat roof. That's 500 kW+ of solar capacity sitting idle."),
            ("Sustainability reporting pressure", "Customers and lenders increasingly require Scope 2 emissions reduction. On-site solar counts directly toward corporate ESG targets."),
        ],
        "use_cases": [
            "Food & beverage processing plants",
            "Metal fabrication & machining shops",
            "Plastics & injection molding",
            "Aerospace component manufacturing",
            "Chemical & petrochemical facilities",
            "Textile and apparel manufacturing",
        ],
    },
    "logistics": {
        "name": "Logistics & Warehousing",
        "headline": "Power distribution centers with rooftop solar.",
        "lede": "Distribution centers and cold-storage warehouses combine massive rooftops with high electric loads — a near-perfect match for commercial solar. Add battery storage for backup on critical refrigeration and you've hedged climate risk too.",
        "stat_1": ("40-65%", "Typical energy bill reduction"),
        "stat_2": ("4-6 yr", "Payback with ITC + MACRS"),
        "stat_3": ("1 MW+", "Typical system size"),
        "pain_points": [
            ("Cold storage refrigeration loads", "Refrigerated warehouses run compressors 24/7. Solar + battery backs up refrigeration during outages, protecting perishable inventory."),
            ("Growing EV fleet charging demand", "Fleet electrification is accelerating. On-site solar + chargers lowers fuel costs and avoids utility demand charges from fast-charging."),
            ("Underutilized roof space", "A 200,000 sq ft distribution center can host 1.5–2 MW of solar — enough to offset most daytime consumption."),
            ("Long-term lease uncertainty", "PPAs and solar leases offer zero-capex options that work inside lease terms."),
        ],
        "use_cases": [
            "3PL distribution centers",
            "E-commerce fulfillment warehouses",
            "Cold storage & food distribution",
            "Truck terminals & cross-docks",
            "Fleet maintenance depots",
            "Last-mile delivery hubs",
        ],
    },
    "retail": {
        "name": "Retail & Multi-Site",
        "headline": "Solar across your retail portfolio.",
        "lede": "Retail chains have predictable daytime load profiles that match solar production almost hour-for-hour. We design and deploy across multiple sites, manage ITC claim timing, and handle landlord approvals for leased locations.",
        "stat_1": ("30-50%", "Typical energy bill reduction"),
        "stat_2": ("6-8 yr", "Payback with ITC + MACRS"),
        "stat_3": ("Portfolio", "Multi-site program management"),
        "pain_points": [
            ("HVAC drives summer peak bills", "Retail HVAC load peaks at the same hours as solar production — direct offset opportunity."),
            ("Landlord approval friction", "We handle landlord negotiation, structural letters, and lease amendments to get your PPA approved."),
            ("Multi-state tax complexity", "30% ITC applies to every state, but depreciation benefits vary. We model the full stack per location."),
            ("Brand sustainability messaging", "Visible rooftop solar and EV chargers differentiate your brand at the point-of-sale."),
        ],
        "use_cases": [
            "Big-box retail & grocery chains",
            "Restaurant & QSR franchises",
            "Auto dealerships & service centers",
            "Pharmacy & convenience stores",
            "Bank branches & credit unions",
            "Hospitality, hotels, and motels",
        ],
    },
    "agriculture": {
        "name": "Agriculture & Ranching",
        "headline": "Solar for Texas farms and ranches.",
        "lede": "Irrigation pumps, grain drying, poultry houses, and dairy operations all benefit from on-site solar. USDA REAP grants stack with the 30% ITC to cover 50-60% of project costs for qualifying rural producers.",
        "stat_1": ("50%+", "Project cost covered by REAP + ITC"),
        "stat_2": ("3-5 yr", "Payback with grants stacked"),
        "stat_3": ("USDA REAP", "Grant assistance included"),
        "pain_points": [
            ("Irrigation pumping costs", "Center-pivot irrigation is one of the biggest farm electric expenses. Solar directly offsets daytime pumping."),
            ("Poultry & dairy ventilation", "24/7 ventilation and cooling loads make poultry houses and dairies ideal for solar + storage."),
            ("Grain drying seasonal spikes", "Harvest-time drying creates short, high-cost demand windows. Battery storage shaves these."),
            ("Remote site infrastructure", "Off-grid or weak-grid sites benefit from standalone solar + battery microgrids."),
        ],
        "use_cases": [
            "Row crop & cotton irrigation",
            "Poultry houses & egg layer operations",
            "Dairy & livestock ranches",
            "Grain elevators & drying facilities",
            "Greenhouse & hydroponic operations",
            "Wineries & agritourism venues",
        ],
    },
    "hospitality": {
        "name": "Hospitality & Hotels",
        "headline": "Lower energy costs without disrupting guests.",
        "lede": "Hotels run energy-intensive HVAC, laundry, and pool/spa operations 24/7. Solar + storage cuts operating expense, supports sustainability certifications, and — done right — never interrupts guest experience.",
        "stat_1": ("25-40%", "Energy cost reduction"),
        "stat_2": ("6-9 yr", "Payback with ITC + MACRS"),
        "stat_3": ("Zero disruption", "Guest-first install protocols"),
        "pain_points": [
            ("HVAC + laundry = high OPEX", "Hotels spend 4-8% of revenue on energy. Solar shifts that to fixed, predictable costs."),
            ("Sustainability certifications", "LEED, Green Key, and corporate brand standards increasingly require on-site renewable generation."),
            ("Guest-facing install concerns", "We schedule installs in low-occupancy windows, use quiet equipment, and stage materials off-site."),
            ("Pool/spa heating loads", "Solar thermal + PV combined can eliminate pool-heating gas costs."),
        ],
        "use_cases": [
            "Full-service hotels & resorts",
            "Limited-service & extended-stay",
            "Boutique & independent hotels",
            "Conference centers & event venues",
            "Restaurants & banquet halls",
            "Spas & wellness facilities",
        ],
    },
    "healthcare": {
        "name": "Healthcare Facilities",
        "headline": "Resilient power for clinics and medical offices.",
        "lede": "Medical facilities need reliable power for patient safety, equipment, and medication storage. Solar + battery backup protects critical loads, reduces operating costs, and supports hospital sustainability goals.",
        "stat_1": ("30-45%", "Energy cost reduction"),
        "stat_2": ("Critical load", "Battery backup for patient safety"),
        "stat_3": ("5-7 yr", "Payback with ITC + MACRS"),
        "pain_points": [
            ("Patient safety during outages", "Battery backup keeps medical devices, vaccine refrigeration, and life-safety systems running through grid failures."),
            ("24/7 HVAC + sterilization loads", "Operating rooms, imaging suites, and labs run continuously — ideal fit for battery load-shifting."),
            ("Sustainability + mission alignment", "Many health systems have net-zero commitments. On-site solar directly supports Scope 2 reduction."),
            ("Quiet install requirements", "We coordinate with facility managers to avoid disrupting patient care zones."),
        ],
        "use_cases": [
            "Outpatient clinics & urgent care",
            "Medical & dental office buildings",
            "Ambulatory surgery centers",
            "Specialty & imaging centers",
            "Veterinary hospitals",
            "Senior living & assisted care",
        ],
    },
}


IND_HEROES = {
    "manufacturing": IMG["feature_factory"],
    "logistics": IMG["feature_warehouse"],
    "retail": IMG["feature_retail"],
    "agriculture": IMG["feature_farm"],
    "hospitality": IMG["feature_hotel"],
    "healthcare": IMG["feature_hospital"],
}

def industry_page(slug):
    ind = INDUSTRIES[slug]
    name = ind["name"]
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Commercial", "commercial.html"), (name, None)]) + '</div>'
    body += hero(
        badge=f"🏭 {name} Solar",
        headline_html=ind["headline"],
        lede=ind["lede"],
        cta_primary="Request commercial quote", cta_primary_href="{BASE}contact.html",
        cta_secondary="Call (346) 330-2550", cta_secondary_href="tel:3463302550",
        bg_image=IND_HEROES.get(slug, IMG["hero_commercial"]),
        stats=[ind["stat_1"], ind["stat_2"], ind["stat_3"]],
    )
    pain_cards = "".join(
        f'<div class="card"><h3 class="card__title">{p[0]}</h3><p class="card__desc">{p[1]}</p></div>'
        for p in ind["pain_points"]
    )
    uc_items = "".join(f'<li>{u}</li>' for u in ind["use_cases"])
    body += f'''
<section class="section">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Why Solar for {name}</span><h2>The challenges we solve.</h2></div>
    <div class="grid grid-2">{pain_cards}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container split">
    <div>
      <span class="eyebrow">Facilities We Serve</span>
      <h2>{name} facility types</h2>
      <ul class="check-list">{uc_items}</ul>
    </div>
    <div>
      <div class="card card--feature">
        <h3>What's included in every commercial project</h3>
        <ul class="check-list">
          <li>Energy-use analysis & load profile modeling</li>
          <li>Roof structural evaluation & design</li>
          <li>Full ITC + MACRS financial modeling</li>
          <li>Utility interconnection & permitting</li>
          <li>Turn-key install with dedicated PM</li>
          <li>25-year production warranty</li>
          <li>Ongoing monitoring & maintenance contract</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''
    body += cta_section(
        f"See the numbers for your {name.lower()} facility.",
        "We'll model your utility bills, roof capacity, and financial return — no obligation.",
        "Request commercial quote", "{BASE}contact.html",
        "Call (346) 330-2550", "tel:3463302550",
    )
    return body
