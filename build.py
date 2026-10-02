"""Generates the five pages from shared header/footer so they stay consistent."""
import os
OUT = os.path.join(os.path.dirname(__file__), 'site')

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://ii.miami/images/hero-poster.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="images/ig-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<header class="nav" id="nav">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="images/ig-mark.png" alt="ii Miami"><span>ii MIAMI</span></a>
    <button class="burger" id="burger" aria-label="Menu">Menu</button>
    <ul class="menu" id="menu">
      <li><a href="index.html"{on_home}>Home</a></li>
      <li><a href="properties.html"{on_prop}>Properties</a></li>
      <li><a href="development.html"{on_dev}>Development</a></li>
      <li><a href="jc-premier-builders.html"{on_jc}>J &amp; C Premier Builders</a></li>
      <li><a href="about.html"{on_about}>About</a></li>
    </ul>
  </div>
</header>
'''

FOOT = '''
<footer>
  <div class="wrap">
    <div>
      <div class="brandline">ii MIAMI</div>
      <p style="margin-top:12px;max-width:40ch">Florida development, construction and brokerage since 2001. We build what we sell.</p>
    </div>
    <div>
      <h5>Companies</h5>
      <ul>
        <li><a href="properties.html">Irving Group, Inc. — Brokerage</a></li>
        <li><a href="development.html">ii Miami — Development</a></li>
        <li><a href="jc-premier-builders.html">J &amp; C Premier Builders — CBC #1266533</a></li>
      </ul>
    </div>
    <div>
      <h5>Contact</h5>
      <ul>
        <li><a href="mailto:re@ii.miami">re@ii.miami</a></li>
        <li><a href="tel:+13059002100">+1 305-900-2100</a></li>
        <li>550 Biltmore Way, Mezzanine Ste. 200<br>Coral Gables, FL 33134</li>
        <li style="margin-top:12px"><a href="https://www.linkedin.com/company/iimiami" rel="noopener">LinkedIn</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@iimiami" rel="noopener">YouTube</a> &nbsp;·&nbsp; <a href="https://www.facebook.com/ii.miami" rel="noopener">Facebook</a></li>
      </ul>
    </div>
    <div class="fine">
      <span>© {year} ii Miami. All rights reserved.</span>
      <span>J &amp; C Premier Builders is a certified Florida building contractor, CBC #1266533.</span>
    </div>
  </div>
</footer>
<script>
  var nav=document.getElementById('nav');
  function onScroll(){nav.classList.toggle('solid',window.scrollY>40)} onScroll(); addEventListener('scroll',onScroll,{passive:true});
  document.getElementById('burger').addEventListener('click',function(){document.getElementById('menu').classList.toggle('open')});
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.1});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});
</script>
</body>
</html>
'''

def page(fname, title, desc, body, on):
    flags = {k: '' for k in ['on_home','on_prop','on_dev','on_jc','on_about']}
    flags['on_' + on] = ' class="on"'
    html = HEAD.format(title=title, desc=desc, **flags) + body + FOOT.replace('{year}', '2026')
    with open(os.path.join(OUT, fname), 'w') as f: f.write(html)
    print('wrote', fname, len(html))

# ------------------------------------------------------------------ HOME
home = '''
<section class="hero" style="padding:0">
  <video autoplay muted loop playsinline poster="images/hero-poster.jpg"><source src="video/hero.mp4" type="video/mp4"></video>
  <div class="wrap">
    <div class="eyebrow">Florida · Since 2001</div>
    <h1>We build<br>what we <em>sell.</em></h1>
    <p>Development, construction and brokerage under one roof. Twenty-five years of Florida projects, from single-family estates to 794-unit condominiums, built and sold by the same people.</p>
    <div class="btns"><a class="btn btn-fill" href="development.html">Our Work</a><a class="btn btn-line" href="about.html#contact">Contact</a></div>
  </div>
  <div class="scroll-hint">Scroll</div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow reveal">Three companies, one group</div>
    <h2 class="lede reveal">Every project starts with the land and ends with the <em>closing.</em></h2>
    <div class="pillars reveal">
      <a class="pillar" href="properties.html"><div class="num">01</div><h3>Brokerage</h3><p>Irving Group, Inc. — commercial real estate and business brokerage serving Florida since 2001.</p><span class="go">Properties →</span></a>
      <a class="pillar" href="development.html"><div class="num">02</div><h3>Development</h3><p>Residential and retail development across South Florida and the Gulf Coast, from entitlement to exit.</p><span class="go">Projects →</span></a>
      <a class="pillar" href="jc-premier-builders.html"><div class="num">03</div><h3>Construction</h3><p>J &amp; C Premier Builders — certified Florida building contractor building in Miami, Sarasota, Siesta Key and Longboat Key.</p><span class="go">J &amp; C →</span></a>
    </div>
  </div>
</section>

<section class="light">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">We ideally invest</div>
        <h2 class="lede">Experienced developers, brokers and investors with decades of work across <em>Florida.</em></h2>
      </div>
      <div class="prose reveal">
        <p>We maximize the exit value of each project, achieving an ideal investment for our capital partner groups. The sponsor controls the deal; partners share in the result.</p>
        <p>Related-party brokerage, construction and asset management are disclosed up front and paid at market. No hidden fees, ever.</p>
      </div>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>$525M</b><span>Investment transactions</span></div>
      <div class="stat"><b>5 yrs</b><span>Average hold time</span></div>
      <div class="stat"><b>17%</b><span>Average IRR realized at sale</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow reveal">Currently building</div>
    <h2 class="lede reveal">On the ground <em>now.</em></h2>
    <div class="grid reveal">
      <a class="card" href="development.html"><div class="ph"><img src="images/lincoln-blvd.jpg" alt="Lincoln Boulevard townhouses rendering" loading="lazy"></div><div class="tag">Miami</div><h4>Lincoln Boulevard</h4><p>New construction · 27 townhouses · 3/2.5</p></a>
      <a class="card" href="properties.html"><div class="ph"><img src="images/2420-novus.jpg" alt="2420 Novus Street, Sarasota" loading="lazy"></div><div class="tag">Sarasota</div><h4>Novus Street</h4><p>New construction · luxury single-family</p></a>
      <a class="card" href="properties.html"><div class="ph"><img src="images/831-siesta-rendering.jpg" alt="831 Siesta Drive rendering" loading="lazy"></div><div class="tag">Sarasota</div><h4>831 Siesta Drive</h4><p>Land or build-to-suit · luxury 5+ bedroom</p></a>
    </div>
  </div>
</section>

<section class="contact light" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">Contact</div>
    <h2 class="lede reveal">Tell us what you're looking to <em>build, buy or back.</em></h2>
    <p class="sub reveal" style="color:#3a3e45">Investors, buyers, brokers and landowners: we answer our own phone.</p>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-dark" href="mailto:re@ii.miami?subject=ii%20Miami%20inquiry">Email</a><a class="btn btn-dark" href="tel:+13059002100">Call +1 305-900-2100</a></div>
    <div class="addr reveal" style="color:#5f646c">550 Biltmore Way, Mezzanine Ste. 200 · Coral Gables, FL 33134</div>
  </div>
</section>
'''
page('index.html', 'ii Miami — We Build What We Sell', 'Florida development, construction and brokerage since 2001. ii Miami, Irving Group and J & C Premier Builders.', home, 'home')

# ------------------------------------------------------------------ PROPERTIES / BROKERAGE
prop = '''
<section class="hero short" style="padding:0">
  <img src="images/2420-novus.jpg" alt="">
  <div class="wrap">
    <div class="eyebrow">Irving Group, Inc.</div>
    <h1>Brokerage</h1>
    <p>Founded in 2001 as a commercial real estate and business brokerage serving the State of Florida. Today we broker our own developments and selected investment properties.</p>
  </div>
</section>

<section class="light">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">Available</div>
        <h2 class="lede">Real estate currently <em>offered.</em></h2>
      </div>
      <div class="prose reveal"><p>Contact us for more information on whether our current investment opportunities can add value to your portfolio. Licensed Florida broker; related-party interests disclosed on every deal.</p></div>
    </div>
    <div class="grid two-up reveal">
      <a class="card" href="http://www.831siesta.com" rel="noopener"><div class="ph"><img src="images/831-siesta-rendering.jpg" alt="831 Siesta Drive concept rendering" loading="lazy"></div><div class="tag">Sarasota, FL</div><h4>831 Siesta Drive</h4><p>Vacant residential lot or luxury 5+ bedroom build-to-suit</p><span class="link">831siesta.com</span></a>
      <a class="card" href="https://www.realtor.com/realestateandhomes-detail/M9251180814" rel="noopener"><div class="ph"><img src="images/2420-novus.jpg" alt="2420 Novus Street, Sarasota" loading="lazy"></div><div class="tag">Sarasota, FL</div><h4>2420 Novus Street</h4><p>New construction · luxury single-family home</p><span class="link">View listing</span></a>
    </div>
  </div>
</section>

<section class="contact" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">Brokerage inquiries</div>
    <h2 class="lede reveal">Direct to the <em>broker.</em></h2>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-fill" href="mailto:re@ii.miami?subject=RE%20Brokerage&body=Please%20send%20me%20more%20info%20on%20available%20investment%20properties.">Email re@ii.miami</a><a class="btn btn-line" href="tel:+13059002100">+1 305-900-2100</a></div>
  </div>
</section>
'''
page('properties.html', 'Properties — ii Miami Brokerage', 'Available real estate from Irving Group, Inc., a Florida commercial real estate and business brokerage founded in 2001.', prop, 'prop')

# ------------------------------------------------------------------ DEVELOPMENT
completed = [
 ('519-rountree.jpg','519 Rountree','Luxury SFR · Longboat Key, FL','https://519rountree.com/'),
 ('oceanview-condos.jpg','Oceanview Condos (A &amp; B)','794 units · Sunny Isles, FL',None),
 ('cedar-woods.jpg','Cedar Woods','165 units · Homestead, FL',None),
 ('gables-waterway-towers.jpg','Gables Waterway Towers','87 units · Coral Gables, FL',None),
 ('chateau-de-ville.jpg','Chateau de Ville','72 units · Dania Beach, FL',None),
 ('cedar-west.jpg','Cedar West','135 units · Homestead, FL',None),
 ('universal-plaza.jpg','Universal Plaza','Retail center · Doral, FL',None),
 ('micc.jpg','MICC','Flex retail · Doral, FL',None),
 ('shoppes-at-41st.jpg','Shoppes at 41st','Retail center · Doral, FL',None),
 ('starbucks-doral.jpg','Starbucks','QSR · Doral, FL',None),
 ('doral-at-41st.jpg','Doral at 41st','Retail center · Doral, FL',None),
 ('checkers-tampa.jpg','Checkers','QSR · Tampa, FL',None),
]
def card(img, name, sub, u):
    href = u or '#'
    rel = ' rel="noopener"' if u else ''
    return f'<a class="card" href="{href}"{rel}><div class="ph"><img src="images/{img}" alt="{name}" loading="lazy"></div><h4>{name}</h4><p>{sub}</p></a>\n'
cards = ''.join(card(*c) for c in completed)
dev = f'''
<section class="hero short" style="padding:0">
  <img src="images/oceanview-condos.jpg" alt="">
  <div class="wrap">
    <div class="eyebrow">ii Miami</div>
    <h1>Development</h1>
    <p>Residential and retail development across Florida: entitlement, design, construction and sale, run by the sponsor from start to finish.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="feature">
      <div class="ph reveal"><img src="images/lincoln-blvd.jpg" alt="Build-to-rent townhouse rendering" loading="lazy"></div>
      <div class="reveal">
        <div class="eyebrow">In development</div>
        <h2 class="lede">Three-phase build-to-rent <em>townhouse</em> community.</h2>
        <ul>
          <li>360 two-story build-to-rent townhouses</li>
          <li>2–4 bedroom floorplans</li>
          <li>Three phases · Florida</li>
        </ul>
        <a class="btn btn-fill" href="mailto:info@ii.miami?subject=Please%20sign%20me%20up%20for%20the%20investment%20newsletter&body=My%20primary%20real%20estate%20investment%20interest%20is%20in%20the%20________%20%5Bmulti-family%2FSFR%2Fretail%2Fland%5D%20asset%20class.">Request information</a>
      </div>
    </div>
  </div>
</section>

<section class="light">
  <div class="wrap">
    <div class="eyebrow reveal">Track record</div>
    <h2 class="lede reveal">Notable completed <em>developments.</em></h2>
    <div class="grid four-up reveal">
{cards}    </div>
  </div>
</section>

<section class="contact" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">Capital partners</div>
    <h2 class="lede reveal">Deal-by-deal structures, sponsor <em>control.</em></h2>
    <p class="sub reveal">Each project is its own entity with its own capital. Partners receive promote economics; the sponsor manages. Everything related-party is disclosed up front.</p>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-fill" href="mailto:info@ii.miami?subject=Development%20inquiry">Email info@ii.miami</a><a class="btn btn-line" href="tel:+13059002100">+1 305-900-2100</a></div>
  </div>
</section>
'''
page('development.html', 'Development — ii Miami', 'Residential and retail development across Florida. 360-unit build-to-rent townhouse community in development; 794-unit Oceanview Condos, Cedar Woods, Gables Waterway Towers and more completed.', dev, 'dev')

# ------------------------------------------------------------------ J & C PREMIER BUILDERS
jc = '''
<section class="hero short" style="padding:0">
  <img src="images/519-rountree.jpg" alt="">
  <div class="wrap">
    <div class="eyebrow">Certified Florida Building Contractor · CBC #1266533</div>
    <h1>J &amp; C Premier <em>Builders</em></h1>
    <p>A partnership of experienced residential and commercial developers, serving Florida for over 30 years. Currently building in Miami, Sarasota, Siesta Key and Longboat Key.</p>
    <div class="btns"><a class="btn btn-fill" href="mailto:info@jcpremierbuilders.com?subject=JC%20Premier&body=Please%20send%20me%20more%20info%20on%20JC%20Premier%20Builders.">Email</a><a class="btn btn-line" href="tel:+18138190000">Call +1 813-819-0000</a></div>
  </div>
</section>

<div class="license">Residential &amp; retail · <b>Certified Building Contractor CBC #1266533</b> · State of Florida</div>

<section class="light">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">Builder-developer</div>
        <h2 class="lede">We build for ourselves first, so we build like <em>owners.</em></h2>
      </div>
      <div class="prose reveal">
        <p>J &amp; C Premier Builders is the construction arm of the ii Miami group. Most of what we build, we also developed and will sell, which means the budget, the schedule and the finish are our problem, not a change order.</p>
        <p>We specialize in residential and retail construction: single-family estates, townhouse communities, and retail centers for national tenants.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow reveal">Projects under development</div>
    <h2 class="lede reveal">On the <em>boards.</em></h2>
    <div class="grid four-up reveal">
      <a class="card" href="https://www.google.com/maps/place/14654+Lincoln+Blvd,+Miami,+FL" rel="noopener"><div class="ph"><img src="images/lincoln-blvd.jpg" alt="Lincoln Boulevard townhouses" loading="lazy"></div><div class="tag">Miami, FL</div><h4>Lincoln Boulevard</h4><p>New construction · 27 townhouses · 3/2.5 units · 14654 Lincoln Blvd</p></a>
      <a class="card" href="https://www.google.com/maps/place/2410+Novus+St,+Sarasota,+FL+34237" rel="noopener"><div class="ph"><img src="images/novus-street.jpg" alt="Novus Street homes" loading="lazy"></div><div class="tag">Sarasota, FL</div><h4>Novus Street</h4><p>New construction · 2 modern single-family homes · 2410 Novus St</p></a>
      <a class="card" href="https://519rountree.com/" rel="noopener"><div class="ph"><img src="images/519-rountree-b.jpg" alt="519 Rountree Drive, Longboat Key" loading="lazy"></div><div class="tag">Longboat Key, FL</div><h4>Rountree Drive</h4><p>New construction · luxury waterfront home · 519 Rountree Dr</p></a>
      <a class="card" href="http://www.831siesta.com" rel="noopener"><div class="ph"><img src="images/831-siesta-aerial.jpg" alt="831 Siesta Drive aerial" loading="lazy"></div><div class="tag">Sarasota, FL</div><h4>Siesta Drive</h4><p>Land or build to suit · luxury home · 831 Siesta Dr</p></a>
    </div>
  </div>
</section>

<section class="contact light" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">J &amp; C Premier Builders</div>
    <h2 class="lede reveal">Have a lot, a plan, or <em>both?</em></h2>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-dark" href="mailto:info@jcpremierbuilders.com?subject=JC%20Premier">info@jcpremierbuilders.com</a><a class="btn btn-dark" href="tel:+18138190000">+1 813-819-0000</a></div>
    <div class="addr reveal" style="color:#5f646c">Certified Florida Building Contractor · CBC #1266533</div>
  </div>
</section>
'''
page('jc-premier-builders.html', 'J & C Premier Builders — Certified Florida Building Contractor', 'J & C Premier Builders, CBC #1266533. Residential and retail construction in Miami, Sarasota, Siesta Key and Longboat Key.', jc, 'jc')

# ------------------------------------------------------------------ ABOUT
about = '''
<section class="hero short" style="padding:0">
  <img src="images/gables-waterway-towers.jpg" alt="">
  <div class="wrap">
    <div class="eyebrow">About</div>
    <h1>We ideally <em>invest.</em></h1>
    <p>The ii group of companies are experienced real estate developers, brokers and investors with decades of experience throughout Florida.</p>
  </div>
</section>

<section class="light">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">How we work</div>
        <h2 class="lede">Maximize the exit value of every <em>project.</em></h2>
      </div>
      <div class="prose reveal">
        <p>We maximize the exit value of each project, achieving an ideal investment for our capital partner groups. Each deal is its own structure, sponsor-managed, with the sponsor's own capital alongside partners'.</p>
        <p>Since 2001 the group has developed, built and brokered single-family estates, townhouse communities, condominium towers of up to 794 units, and retail centers for national tenants across South Florida and the Gulf Coast.</p>
      </div>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>$525M</b><span>Investment transactions</span></div>
      <div class="stat"><b>5 yrs</b><span>Average hold time</span></div>
      <div class="stat"><b>17%</b><span>Average IRR realized at sale</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow reveal">The group</div>
    <h2 class="lede reveal">Three companies, one <em>sponsor.</em></h2>
    <div class="pillars reveal">
      <a class="pillar" href="properties.html"><div class="num">Est. 2001</div><h3>Irving Group, Inc.</h3><p>Commercial real estate and business brokerage. Licensed Florida broker.</p><span class="go">Brokerage →</span></a>
      <a class="pillar" href="development.html"><div class="num">Development</div><h3>ii Miami</h3><p>Sponsor and developer of residential and retail projects across Florida.</p><span class="go">Projects →</span></a>
      <a class="pillar" href="jc-premier-builders.html"><div class="num">CBC #1266533</div><h3>J &amp; C Premier Builders</h3><p>Certified Florida building contractor. Residential and retail construction.</p><span class="go">Construction →</span></a>
    </div>
  </div>
</section>

<section class="contact light" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">Contact</div>
    <h2 class="lede reveal">Coral <em>Gables.</em></h2>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-dark" href="mailto:re@ii.miami">re@ii.miami</a><a class="btn btn-dark" href="tel:+13059002100">+1 305-900-2100</a></div>
    <div class="addr reveal" style="color:#5f646c">550 Biltmore Way, Mezzanine Ste. 200 · Coral Gables, FL 33134</div>
    <div class="addr reveal" style="color:#5f646c;margin-top:10px"><a href="https://www.linkedin.com/company/iimiami" rel="noopener" style="text-decoration:none">LinkedIn</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@iimiami" rel="noopener" style="text-decoration:none">YouTube</a> &nbsp;·&nbsp; <a href="https://www.facebook.com/ii.miami" rel="noopener" style="text-decoration:none">Facebook</a></div>
  </div>
</section>
'''
page('about.html', 'About — ii Miami', 'The ii group of companies: experienced Florida real estate developers, brokers and investors. $525M in transactions, 17% average realized IRR.', about, 'about')
