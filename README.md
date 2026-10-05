# ii.miami — static site

Replaces the WordPress site at ii.miami (and jcpb.co, which redirects to the J & C page).

## Layout
- `index.html` · home (video hero)
- `properties.html` · all properties (519 Rountree, 733 Tiziano, 831 Siesta, 2420 Novus)
- `development.html` · in-development + completed projects
- `jc-premier-builders.html` · J & C Premier Builders (CBC #1266533)
- `about.html` · group overview, metrics, contact
- `css/site.css` · the only stylesheet
- `images/`, `video/hero.mp4` (5 MB, 1280p, muted loop; `images/hero-poster.jpg` shows until it loads)
- `CNAME` · `ii.miami` — GitHub Pages reads this for the custom domain
- The standby jcpb.co redirect site now lives in `../J&C Premier Builders/` (it was `jcpb-redirect/` here).
- `build.py` · regenerates the five pages from one shared header/footer (`python3 build.py`). Edit copy there, or edit the HTML directly for one-off tweaks.

## Publishing (GitHub Pages)
1. New repo `iimiami` under the IIMiami account; push everything here.
2. Settings → Pages → Deploy from branch `main` / root. Custom domain `ii.miami`; tick Enforce HTTPS once the certificate is issued.
3. GoDaddy DNS for ii.miami: delete the parked `@` A record; add A records `@` → 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153; CNAME `www` → `iimiami.github.io`. Leave MX and anything mail-related alone — email is not affected.
4. (Only if jcpb.co ever needs its own repo) Repo `jcpb` with the contents of `../J&C Premier Builders/`; same Pages setup; DNS for jcpb.co: same four A records, CNAME `www` → `iimiami.github.io`.
5. Once both resolve, cancel the GoDaddy Managed WordPress sites for ii.miami / jcpb.co (keep viafoundation.co).

## Content carried over from WordPress (verify before launch)
- Novus Street: **2420** (Properties page) is the finished house for sale; **2410** (J & C page) is the remaining lot from the original 2410 parcel, which was split in two; a future build-to-suit. Both are correct — two different properties.
- J & C phone is **+1 813-819-0000** (old site); group phone is **+1 305-900-2100**.
- Metrics ($525M / 5 yrs / 17% IRR) and the 360-unit BTR count are copied verbatim from the old site.
- Project photos are the 468×286 files from WordPress; they are fine at card size but will look soft if used larger. Replace with originals when convenient.
