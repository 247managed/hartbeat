# Hart Beat Energy — hartbeat.solar

Production-ready static website for Hart Beat Energy, a Texas solar installation and maintenance company. 56 files, ~1MB, zero external dependencies at runtime beyond Google Fonts.

## Architecture

- **Static HTML site generator**, written in pure Python (no Node, no build chain)
- **Custom CSS design system** in `assets/css/styles.css` — CSS variables, responsive grid, nav with dropdowns, accessible mobile drawer, prefers-reduced-motion support
- **Vanilla JS** in `assets/js/main.js` — mobile nav toggle, savings calculator, form handler, FAQ accordion, smooth scroll, sticky nav
- **Full JSON-LD schema** — Organization, SolarPowerStation / LocalBusiness, WebSite, Service, FAQPage, BreadcrumbList, Article on every page
- **Complete SEO head** — meta description, canonical, Open Graph, Twitter Card, theme-color, favicons, apple-touch-icon, manifest

## Page inventory

| Section | Pages |
|---|---|
| Core | Homepage, Residential, Commercial, Battery Storage, Financing, Lease vs PPA, Contact |
| Maintenance | Hub, Cleaning, Repairs, Monitoring, Critter Guard, 50-Point Inspection, 40-Page Audit |
| Company | About, Reviews, FAQ, Case Studies, Warranty, Storm Claims, Referral, Careers, Membership |
| Locations | Houston, Austin, Dallas, San Antonio, Fort Worth, El Paso |
| Industries | Manufacturing, Logistics, Retail, Agriculture, Hospitality, Healthcare |
| Blog | Index + 6 posts (2026 ITC, Lease vs PPA, ERCOT Storm Prep, Houston HOA, Commercial MACRS, Retail Buyback) |
| Legal | Privacy, Terms, Sitemap (HTML) |
| Crawlers | `robots.txt`, `sitemap.xml`, `manifest.json` |

**Total: 48 HTML pages + assets + crawler files = 56 files**

## Build

```bash
cd website
python3 generate.py
```

Output is written to `website/dist/`. Deploy the contents of `dist/` to any static host (Netlify, Cloudflare Pages, S3+CloudFront, Vercel, GitHub Pages).

## Directory layout

```
website/
├── build.py               # template engine, brand config, schema helpers
├── generate.py            # main runner — imports all content, writes dist/
├── content_core.py        # home, residential, commercial, battery, financing, lease-vs-ppa
├── content_maintenance.py # maintenance hub + 6 detail pages
├── content_company.py     # about, contact, reviews, faq, case studies, etc.
├── content_locations.py   # 6 Texas city pages
├── content_industries.py  # 6 B2B industry pages
├── content_blog.py        # blog index + 6 posts
├── content_legal.py       # privacy, terms, sitemap
├── assets/
│   ├── css/styles.css
│   ├── js/main.js
│   └── images/            # logo.svg, favicon.*, apple-touch-icon.png, og-default.jpg
└── dist/                  # generated output — deploy this
```

## 2026 Solar Policy Compliance

The federal 30% residential Investment Tax Credit (Section 25D) **expired July 4, 2025** under the One Big Beautiful Bill Act. All residential copy on this site reflects the post-2025 reality:

- Residential pricing leads with **$0-down lease & PPA** contracts (third-party owner claims commercial ITC, passes savings through)
- Monthly payments: $89 / $135 / $198
- Commercial pages retain the 30% ITC + MACRS messaging — that incentive stack remains through 2032

When federal or state policy changes, update the relevant talking points in `content_core.py` and `content_blog.py`, then rerun `python3 generate.py`.

## Brand Config

All brand/contact info lives in `build.py` → `BRAND` dict:

- Phone: (346) 330-2550
- Email: info@hartbeat.solar
- Address: 1200 Smith St, Suite 1600, Houston, TX 77002
- Social: Facebook, Instagram, LinkedIn, YouTube, TikTok, X

Update once in `BRAND` and it propagates everywhere (nav, footer, schema, contact page).

## Deployment notes

- **Canonical URLs** assume the site is served at `https://www.hartbeat.solar`. Change `SITE_URL` in `build.py` if deploying to a different domain.
- **Trailing-slash handling**: `index.html` files are expected in subdirs (`/maintenance/`, `/blog/`). Configure your host to serve `index.html` on directory paths.
- **robots.txt + sitemap.xml** are pre-generated. Submit sitemap to Google Search Console and Bing Webmaster Tools on launch.
- **OG image** (`og-default.jpg`) is 1200×630. Replace with a photo-quality branded image before launch if desired (keep dimensions).

## Content updates

Each content file is standalone. To update:
1. Edit the relevant `content_*.py` file
2. Run `python3 generate.py`
3. Commit and redeploy `dist/`

To add a new city: add an entry to `CITIES` in `content_locations.py` and it will be generated automatically on next build.
To add a new blog post: add an entry to `POSTS` and body HTML to `POST_BODIES` in `content_blog.py`.
