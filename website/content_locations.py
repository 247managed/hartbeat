"""City landing pages for local SEO."""
from build import IMG, hero, cta_section, breadcrumb_html

CITIES = {
    "houston": {
        "name": "Houston",
        "region": "Harris County, Texas",
        "utility": "CenterPoint Energy",
        "avg_bill": "$210/month",
        "avg_production": "1,400 kWh/kW/year",
        "avg_savings": "$1,800/year",
        "weather": "Hot, humid summers with frequent hurricane threats from the Gulf. High solar irradiance March–October.",
        "neighborhoods": ["The Heights", "Montrose", "River Oaks", "West University", "Bellaire", "Memorial", "Cypress", "Katy", "Sugar Land", "The Woodlands", "Clear Lake", "Pearland", "Spring"],
        "specific": "CenterPoint offers distributed generation interconnection for residential and commercial. We navigate the interconnection queue, HOA approvals common to Houston-area communities, and hurricane-resilient mounting for Gulf Coast properties.",
    },
    "austin": {
        "name": "Austin",
        "region": "Travis County, Texas",
        "utility": "Austin Energy",
        "avg_bill": "$175/month",
        "avg_production": "1,450 kWh/kW/year",
        "avg_savings": "$1,650/year",
        "weather": "Hot, dry summers with occasional hail. Consistent sun year-round.",
        "neighborhoods": ["Downtown", "East Austin", "South Congress", "Hyde Park", "Tarrytown", "Zilker", "Barton Hills", "Circle C", "Cedar Park", "Round Rock", "Pflugerville", "Lakeway", "Westlake"],
        "specific": "Austin Energy runs a Value of Solar Tariff that credits exported kWh. Their Solar PV rebate program has historically provided additional incentives. We handle all Austin Energy interconnection paperwork and rebate applications.",
    },
    "dallas": {
        "name": "Dallas",
        "region": "Dallas County, Texas",
        "utility": "Oncor",
        "avg_bill": "$195/month",
        "avg_production": "1,420 kWh/kW/year",
        "avg_savings": "$1,720/year",
        "weather": "Hot summers, occasional severe hail in spring. Strong solar irradiance.",
        "neighborhoods": ["Uptown", "Highland Park", "University Park", "Lake Highlands", "Oak Cliff", "Bishop Arts", "Preston Hollow", "Lakewood", "Plano", "Frisco", "McKinney", "Richardson", "Irving"],
        "specific": "Oncor is the delivery utility — you choose your retail provider. Many Dallas retail providers offer solar buyback plans (Rhythm, TXU, Green Mountain, etc.). We help you evaluate buyback rates alongside your system design to maximize export value.",
    },
    "san-antonio": {
        "name": "San Antonio",
        "region": "Bexar County, Texas",
        "utility": "CPS Energy",
        "avg_bill": "$165/month",
        "avg_production": "1,440 kWh/kW/year",
        "avg_savings": "$1,590/year",
        "weather": "Hot, dry summers. Some of the highest solar irradiance in Texas.",
        "neighborhoods": ["Alamo Heights", "Terrell Hills", "Stone Oak", "Shavano Park", "Hollywood Park", "Dominion", "Northwest Side", "Helotes", "Boerne"],
        "specific": "CPS Energy offers one of the strongest solar rebate programs in Texas plus generous net-metering. We are an approved CPS Energy solar installer and handle rebate paperwork end-to-end. Commercial MACRS depreciation stacks with CPS incentives.",
    },
    "fort-worth": {
        "name": "Fort Worth",
        "region": "Tarrant County, Texas",
        "utility": "Oncor",
        "avg_bill": "$185/month",
        "avg_production": "1,410 kWh/kW/year",
        "avg_savings": "$1,680/year",
        "weather": "Similar to Dallas — hot summers, hail risk in spring.",
        "neighborhoods": ["TCU Area", "Westover Hills", "Rivercrest", "Tanglewood", "Westcliff", "Arlington Heights", "Arlington", "Keller", "Southlake", "Grapevine", "North Richland Hills"],
        "specific": "Oncor delivery territory with retail choice. We work with homeowners choosing retail providers like TXU, Rhythm, Reliant, and Green Mountain to optimize their solar buyback structure alongside system design.",
    },
    "el-paso": {
        "name": "El Paso",
        "region": "El Paso County, Texas",
        "utility": "El Paso Electric",
        "avg_bill": "$155/month",
        "avg_production": "1,600 kWh/kW/year",
        "avg_savings": "$1,540/year",
        "weather": "Desert climate — highest solar irradiance in Texas. Hot, dry year-round with minimal cloud cover.",
        "neighborhoods": ["Westside", "Upper Valley", "Eastside", "Mission Valley", "Northeast El Paso", "Horizon City", "Socorro"],
        "specific": "El Paso Electric operates differently from ERCOT utilities — they offer their own net-metering structure and rebate programs. Desert climate delivers 12–18% higher annual production than Houston. We size systems accordingly.",
    },
}


CITY_HEROES = {
    "houston": IMG["city_houston"],
    "austin": IMG["city_austin"],
    "dallas": IMG["city_dallas"],
    "san-antonio": IMG["city_sanantonio"],
    "fort-worth": IMG["city_fortworth"],
    "el-paso": IMG["city_elpaso"],
}

def city_page(slug):
    city = CITIES[slug]
    name = city["name"]
    body = '<div class="container" style="padding-top:28px">' + breadcrumb_html([("Texas Coverage", "locations/houston.html"), (name, None)]) + '</div>'
    body += hero(
        badge=f"📍 {name}, Texas",
        headline_html=f'Solar installation, financing, and maintenance in <span class="hl">{name}</span>.',
        lede=f"Hart Beat Energy has installed and maintained solar systems across {name} for over a decade. We understand the {city['utility']} interconnection process, local HOA dynamics, and {city['region']} building codes.",
        cta_primary=f"Get your {name} quote", cta_primary_href="{BASE}contact.html",
        cta_secondary="Call (346) 330-2550", cta_secondary_href="tel:3463302550",
        bg_image=CITY_HEROES.get(slug, IMG["hero_home"]),
        stats=[(city["avg_savings"], f"Avg {name} annual savings"), (city["avg_production"], "Production per kW"), (city["avg_bill"], f"Avg {name} bill")],
    )
    neighborhoods_html = ", ".join(city["neighborhoods"])
    body += f'''
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Local Intel</span>
      <h2>Solar in {name} — what you need to know</h2>
      <p><strong>Your utility:</strong> {city['utility']}. {city['specific']}</p>
      <p><strong>Your weather:</strong> {city['weather']}</p>
      <p><strong>Neighborhoods we serve:</strong> {neighborhoods_html} — plus surrounding areas.</p>
    </div>
    <div>
      <div class="card card--feature">
        <h3>{name} solar quick-math</h3>
        <div class="grid grid-2 mt-3">
          <div><div class="stat__n">{city['avg_bill']}</div><div class="stat__l">Avg monthly bill</div></div>
          <div><div class="stat__n">{city['avg_savings']}</div><div class="stat__l">Typical annual savings</div></div>
          <div><div class="stat__n">{city['avg_production']}</div><div class="stat__l">kWh per kW installed</div></div>
          <div><div class="stat__n">{city['utility']}</div><div class="stat__l">Local utility</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="text-center mb-4"><span class="eyebrow">Services in {name}</span><h2>Everything you need from one team.</h2></div>
    <div class="grid grid-4">
      <div class="card"><div class="card__icon">🏠</div><h3 class="card__title">Residential Solar</h3><p class="card__desc">$0-down lease &amp; PPA available for {name} homeowners.</p><a href="{{BASE}}residential.html" class="card__link">Learn more →</a></div>
      <div class="card"><div class="card__icon">🏢</div><h3 class="card__title">Commercial Solar</h3><p class="card__desc">{name} businesses still qualify for 30% ITC + MACRS.</p><a href="{{BASE}}commercial.html" class="card__link">Learn more →</a></div>
      <div class="card"><div class="card__icon">🔋</div><h3 class="card__title">Battery Storage</h3><p class="card__desc">Tesla Powerwall installs throughout {name} metro.</p><a href="{{BASE}}battery-storage.html" class="card__link">Learn more →</a></div>
      <div class="card"><div class="card__icon">🛠</div><h3 class="card__title">Maintenance</h3><p class="card__desc">Local {name} crews, 24hr dispatch, all brands serviced.</p><a href="{{BASE}}maintenance/index.html" class="card__link">Learn more →</a></div>
    </div>
  </div>
</section>
'''
    body += cta_section(
        f"Ready to go solar in {name}?",
        f"Free in-home consultation, custom roof modeling, and side-by-side financing comparison — no obligation.",
        f"Get my {name} quote", "{BASE}contact.html",
        "Call (346) 330-2550", "tel:3463302550",
    )
    return body
