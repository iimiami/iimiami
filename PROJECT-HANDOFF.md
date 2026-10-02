# ii Miami websites — project handoff

Written Oct 2, 2026, to carry this work into its own project. Everything below is the state of play; the folder this file sits in is the site itself.

## What this is

Rebuild of the ii Miami group's web presence as plain static sites, replacing GoDaddy Managed WordPress. Three domains are involved:

| Domain | Status | Where it lives |
|---|---|---|
| **733tiziano.com** | Live on GitHub Pages, HTTPS enforced | repo `iimiami/733tiziano`; master copy in OneDrive `733 Tiziano Ave/Cost Intelligence/Web/` |
| **ii.miami** | Rebuilt, not yet live (still on WordPress) | this folder; no repo yet |
| **jcpb.co** | Rebuilt as a redirect to the J & C page, not yet live | `jcpb-redirect/` in this folder; no repo yet |

Also on the same GoDaddy Managed WordPress plan (Pro 5): **519rountree.com** (not touched yet) and **viafoundation.co** (stays on WordPress; the charity updates it from South America). Once ii.miami and jcpb.co move, the WordPress plan gets downgraded to a smaller tier, not cancelled.

## Accounts and access

- **GitHub account:** `IIMiami` (github.com/iimiami). Owns the site repositories. Future sites go under the same account; it can be converted to an organization later if more people need access.
- **Hosting:** GitHub Pages, free. One repo per domain. Custom domain via a `CNAME` file in the repo plus DNS at GoDaddy.
- **Domains and DNS:** GoDaddy. Domains are a separate product from hosting; cancelling WordPress hosting does not affect them. Email (Microsoft 365 / Workspace) is also separate; never touch MX or mail-related DNS records.
- **Access for Claude:** a fine-grained personal access token, generated at github.com/settings/personal-access-tokens/new, scoped to specific repositories, with Contents, Pages and Administration set to Read and write. The token for `733tiziano` was issued Oct 2, 2026 (90-day expiry). A new token scoped to the new repos is needed for ii.miami and jcpb.co. Tokens are pasted into the chat when needed and are not stored anywhere.
- **Where pushes run from:** Claude's cloud environment cannot reach GitHub; pushes run on James's Mac through the Claude desktop app (a clone kept in the session's home folder, outside OneDrive). Don't initialise git inside a OneDrive folder; OneDrive blocks deletion of git's lock files.

## Publishing workflow (per site)

1. Create the repo under IIMiami (public, empty, no README).
2. Push the folder contents; GitHub Pages serves from branch `main`, root.
3. Settings → Pages: custom domain set from the `CNAME` file; tick **Enforce HTTPS** once the certificate issues (usually under an hour; if it stalls, remove and re-add the custom domain).
4. GoDaddy DNS for the domain: delete the parked `@` A record; add four A records on `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; CNAME `www` → `iimiami.github.io`. Leave everything else.
5. Any later change: edit the files, commit, push; live in about a minute. James approves every push ("say go").

## This folder (ii.miami site)

- `index.html` home with muted looping video hero (`video/hero.mp4`, 5 MB; poster `images/hero-poster.jpg`)
- `properties.html` Irving Group brokerage page (two listings: 831 Siesta Dr, 2420 Novus St)
- `development.html` 360-unit three-phase BTR townhouse feature plus twelve completed projects
- `jc-premier-builders.html` J & C Premier Builders, CBC #1266533, four projects under development
- `about.html` group overview, metrics ($525M transactions / 5-yr avg hold / 17% avg realized IRR), Coral Gables address, socials
- `css/site.css` the only stylesheet (same visual language as 733tiziano.com: Cormorant Garamond + Inter, dark ink, cream, gold accent)
- `images/` the 468×286 photos pulled from the WordPress site; fine at card size, soft when used as page headers. Replace with originals when available.
- `build.py` regenerates the five pages from one shared header and footer (`python3 build.py`). Edit copy there, or edit the HTML directly.
- `CNAME` (`ii.miami`), `.nojekyll`
- `jcpb-redirect/` a one-page site with its own `CNAME` (`jcpb.co`) that forwards to `https://ii.miami/jc-premier-builders.html`. Goes in its own repo.
- `_to_delete/` leftovers from an aborted git init; safe to delete.

All copy was carried over from the WordPress site, tightened but not invented. Contact details on the site: re@ii.miami, info@ii.miami, info@jcpremierbuilders.com, +1 305-900-2100 (group), +1 813-819-0000 (J & C), 550 Biltmore Way, Mezzanine Ste. 200, Coral Gables, FL 33134.

## Decisions still open

1. **Novus Street address:** the old site said 2410 on the J & C page and 2420 on Properties. The new site copies that. Pick one.
2. **J & C phone:** keep the Tampa number (813-819-0000) or switch to 305-900-2100.
3. **Page-header photos:** four sub-pages use upscaled card images as headers. Real photos of 519 Rountree, Oceanview, Gables Waterway Towers and 2420 Novus would fix it.
4. **519rountree.com:** still on WordPress; not yet decided whether it gets rebuilt, redirected, or retired.
5. **Timing of the WordPress downgrade:** after ii.miami and jcpb.co resolve to GitHub and have been checked.

## 733tiziano.com, for reference

Live and separate, but same account and workflow. Price upon request; contact 733@ii.miami (alias to be created on the ii.miami mail domain) and 305-900-2100 (RingCentral, takes SMS); "For Brokers" section with compensation offered and confirmed in writing (no number published), buyer registration by email, licensee-owner disclosure in the footer. Photos: James's own retouched sidewalk-canopy shot as hero, a labeled Platinum Triangle aerial (gold triangle and labels), house-front aerial, lot pair. Retouched full-size files in `733 Tiziano Ave/Cost Intelligence/Sale/Photos-WIP/Retouched/`. Pending: James's manual cleanup of the two street-canopy drone shots (#7, #10); optional broker flyer PDF, inquiry form, analytics.
