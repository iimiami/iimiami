"""Generates the five pages from shared header/footer so they stay consistent."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

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
    <a class="brand" href="index.html"><img src="images/logo-white.png" alt="ii.miami"></a>
    <button class="burger" id="burger" aria-label="Menu">Menu</button>
    <ul class="menu" id="menu">
      <li><a href="index.html"{on_home}>Home</a></li>
      <li><a href="properties.html"{on_prop}>Properties</a></li>
      <li><a href="development.html"{on_dev}>Development</a></li>
      <li><a href="jc-premier-builders.html"{on_jc}>J &amp; C Premier Builders</a></li>
      <li><a href="limited-partners.html"{on_invest}>Invest</a></li>
      <li><a href="about.html"{on_about}>About</a></li>
    </ul>
  </div>
</header>
'''

FOOT = '''
<footer>
  <div class="wrap">
    <div>
      <img class="footlogo" src="images/logo-white.png" alt="ii.miami">
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
        <li><a href="mailto:properties@ii.miami">properties@ii.miami</a></li>
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
    flags = {k: '' for k in ['on_home','on_prop','on_dev','on_jc','on_invest','on_about']}
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
    <p>Development, construction and brokerage under one roof. Twenty-five years of Florida projects, from single-family estates to 300-unit communities, built and sold by the same people.</p>
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
        <div class="eyebrow">Limited partners</div>
        <h2 class="lede">We build it, we own it, and we invite a few partners to own it <em>with us.</em></h2>
      </div>
      <div class="prose reveal">
        <p>Since 2001 the ii Miami group has developed, built and brokered its own projects across Florida &mdash; more than 250 homes since 2005, and 300-plus units now in development. We are opening select long-term, income-producing holds to limited partners.</p>
        <p>One sponsor controls each deal and invests alongside you. Related-party brokerage, construction and asset management are disclosed up front and paid at market. No hidden fees, ever.</p>
        <div class="btns"><a class="btn btn-dark" href="limited-partners.html">Invest with us &rarr;</a></div>
      </div>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>250+</b><span>Homes developed since 2005</span></div>
      <div class="stat"><b>300+</b><span>Units in development</span></div>
      <div class="stat"><b>2001</b><span>Developing across Florida since</span></div>
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
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-dark" href="mailto:properties@ii.miami?subject=ii%20Miami%20inquiry">Email</a><a class="btn btn-dark" href="tel:+13059002100">Call +1 305-900-2100</a></div>
    <div class="addr reveal" style="color:#5f646c">550 Biltmore Way, Mezzanine Ste. 200 · Coral Gables, FL 33134</div>
  </div>
</section>
'''
page('index.html', 'ii Miami — We Build What We Sell', 'Florida development, construction and brokerage since 2001. ii Miami, Irving Group and J & C Premier Builders.', home, 'home')

# ------------------------------------------------------------------ PROPERTIES / BROKERAGE
prop = '''
<section class="hero short" style="padding:0">
  <img src="images/519-rountree-hero.jpg" alt="">
  <div class="wrap">
    <div class="eyebrow">ii Miami</div>
    <h1>Properties</h1>
    <p>Homes and homesites we have built, own or are developing — for sale now or coming to market. Each is offered through its listing brokerage, noted on the property.</p>
  </div>
</section>

<section class="light">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">For sale &amp; coming soon</div>
        <h2 class="lede">Real estate currently <em>offered.</em></h2>
      </div>
      <div class="prose reveal"><p>Every property here is owned or developed by the ii Miami group. Some are listed with our own Irving Group, Inc., a licensed Florida broker; others with outside brokerages, as noted. Related-party interests are disclosed on every deal.</p></div>
    </div>
    <div class="grid two-up reveal">
      <a class="card" href="https://519rountree.com/" rel="noopener"><div class="ph"><img src="images/519-rountree-dusk.jpg" alt="519 Rountree Drive, Longboat Key, at dusk" loading="lazy"></div><div class="tag">Longboat Key, FL</div><h4>519 Rountree Drive</h4><p>New construction · waterfront · dock &amp; lift · listed by Compass</p><span class="link">View property</span></a>
      <a class="card" href="https://733tiziano.com/" rel="noopener"><div class="ph"><img src="images/733-tiziano.jpg" alt="733 Tiziano Avenue, Coral Gables — oak canopy street" loading="lazy"></div><div class="tag">Coral Gables, FL</div><h4>733 Tiziano Avenue</h4><p>±10,200 sf homesite · Platinum Triangle · coming soon</p><span class="link">View property</span></a>
      <a class="card" href="831-siesta.html"><div class="ph"><img src="images/831-siesta-rendering.jpg" alt="831 Siesta Drive concept rendering" loading="lazy"></div><div class="tag">Sarasota, FL</div><h4>831 Siesta Drive</h4><p>Vacant residential lot or luxury 5+ bedroom build-to-suit</p><span class="link">View property</span></a>
      <a class="card" href="https://www.realtor.com/realestateandhomes-detail/M9251180814" rel="noopener"><div class="ph"><img src="images/2420-novus.jpg" alt="2420 Novus Street, Sarasota" loading="lazy"></div><div class="tag">Sarasota, FL</div><h4>2420 Novus Street</h4><p>New construction · luxury single-family home</p><span class="link">View listing</span></a>
    </div>
  </div>
</section>

<section class="contact" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">Property inquiries</div>
    <h2 class="lede reveal">Direct to the <em>owner.</em></h2>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-fill" href="mailto:properties@ii.miami?subject=Properties&body=Please%20send%20me%20more%20info%20on%20your%20available%20properties.">Email properties@ii.miami</a><a class="btn btn-line" href="tel:+13059002100">+1 305-900-2100</a></div>
  </div>
</section>
'''
page('properties.html', 'Properties — ii Miami', 'Homes and homesites built, owned or developed by the ii Miami group — for sale or coming to market in Longboat Key, Coral Gables and Sarasota.', prop, 'prop')


# ------------------------------------------------------------------ 831 SIESTA
siesta = '''
<section class="hero short" style="padding:0">
  <img src="images/831-aerial-1.jpg" alt="831 Siesta Drive, Sarasota — aerial with Sarasota Bay beyond">
  <div class="wrap">
    <div class="eyebrow">Sarasota, FL · Bay Island</div>
    <h1>831 Siesta Drive</h1>
    <p>A rare 0.386-acre triangular homesite with exceptional privacy and the opportunity to create a distinctive elevated residence capturing light and breezes off Sarasota Bay.</p>
    <div class="btns"><a class="btn btn-fill" href="https://www.realtor.com/realestateandhomes-detail/M5618264187" rel="noopener">Lot listing</a><a class="btn btn-line" href="mailto:properties@ii.miami?subject=831%20Siesta%20Drive">Build-to-suit inquiry</a></div>
  </div>
</section>

<section class="light">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">The property</div>
        <h2 class="lede">Vacant lot, or a luxury 5+ bedroom <em>build-to-suit.</em></h2>
      </div>
      <div class="prose reveal">
        <p><strong>Property features.</strong> With over 276 ft of frontage on Siesta Drive and an unusually wide rear building area, the site supports striking architectural design, generous indoor-outdoor living, elevated terraces, and a resort-style pool concept surrounded by tropical landscaping.</p>
        <p><strong>Location.</strong> The mainland is just over the bridge, while the powder-soft sands of Siesta Beach are minutes away, surrounded by luxury estates that elevate the neighborhood.</p>
        <p><strong>The opportunity.</strong> A custom home can make a bold statement here, and a build-to-suit option is available through J &amp; C Premier Builders, our licensed contractor (CBC #1266533).</p>
        <p><strong>Your next chapter.</strong> For the buyer waiting for the right property, this exceptional Bay Island homesite delivers rare convenience, privacy, and potential.</p>
      </div>
    </div>
    <div class="gallery reveal">
      <img src="images/831-rendering-large.jpg" alt="Concept rendering of a custom home at 831 Siesta Drive" loading="lazy">
      <img src="images/831-aerial-2.jpg" alt="Aerial view toward downtown Sarasota" loading="lazy">
      <img src="images/831-aerial-4.jpg" alt="Aerial of the parcel outline" loading="lazy">
      <img src="images/831-aerial-5.jpg" alt="Aerial toward Siesta Key" loading="lazy">
      <img src="images/831-south-view.jpg" alt="Parcel from above, south view" loading="lazy">
      <img src="images/831-front.jpg" alt="Street view from Siesta Drive" loading="lazy">
    </div>
    <p class="caps" style="margin-top:18px;opacity:.7">Concept rendering shown for illustration; design subject to buyer selection and permitting.</p>
  </div>
</section>

<section class="contact" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">Irving Group, Inc. · Licensed Florida broker</div>
    <h2 class="lede reveal">Direct to the <em>broker.</em></h2>
    <p class="reveal" style="max-width:52ch;margin:0 auto 26px">Related-party interests disclosed: Irving Group is the listing broker and J &amp; C Premier Builders is the affiliated contractor.</p>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-fill" href="mailto:properties@ii.miami?subject=831%20Siesta%20Drive">Email properties@ii.miami</a><a class="btn btn-line" href="tel:+13059002100">+1 305-900-2100</a></div>
  </div>
</section>
'''
page('831-siesta.html', '831 Siesta Drive, Sarasota — Lot or Build-to-Suit', 'Rare 0.386-acre Bay Island homesite in Sarasota: vacant lot or luxury 5+ bedroom build-to-suit by J & C Premier Builders. Offered by Irving Group, Inc.', siesta, 'prop')

# ------------------------------------------------------------------ DEVELOPMENT
completed = [
 ('519-rountree.jpg','519 Rountree','Luxury SFR · Longboat Key, FL','https://519rountree.com/'),
 ('cedar-woods.jpg','Cedar Woods','165 units · Homestead, FL',None),
 ('chateau-de-ville.jpg','Chateau de Ville','72 units · Dania Beach, FL',None),
 ('cedar-west.jpg','Cedar West','135 units · Homestead, FL',None),
 ('universal-plaza.jpg','Universal Plaza','Retail center · Doral, FL',None),
 ('shoppes-at-41st.jpg','Shoppes and Doral at 41st','Retail center · Doral, FL',None),
 ('starbucks-doral.jpg','Starbucks','QSR · Doral, FL',None),
 ('checkers-tampa.jpg','Checkers','QSR · Tampa, FL',None),
]
def card(img, name, sub, u):
    href = u or '#'
    rel = ' rel="noopener"' if u else ''
    return f'<a class="card" href="{href}"{rel}><div class="ph"><img src="images/{img}" alt="{name}" loading="lazy"></div><h4>{name}</h4><p>{sub}</p></a>\n'
cards = ''.join(card(*c) for c in completed)
dev = f'''
<section class="hero short plain" style="padding:0">
  <img src="images/dev-hero.jpg" alt="Build-to-rent townhomes rendering">
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
    <div class="eyebrow reveal" style="display:inline-block">Limited partners</div>
    <h2 class="lede reveal">Deal-by-deal structures, sponsor <em>control.</em></h2>
    <p class="sub reveal">Each project is its own entity with its own capital. Partners receive a preferred return and share in the result; the sponsor manages. Everything related-party is disclosed up front.</p>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-fill" href="limited-partners.html">How we partner</a><a class="btn btn-line" href="mailto:invest@ii.miami?subject=Limited%20partner%20interest">Email invest@ii.miami</a><a class="btn btn-line" href="tel:+13059002100">+1 305-900-2100</a></div>
  </div>
</section>
'''
page('development.html', 'Development — ii Miami', 'Residential and retail development across Florida. 360-unit build-to-rent townhouse community in development; Cedar Woods, Cedar West, Chateau de Ville and retail centers in Doral completed.', dev, 'dev')

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
      <a class="card" href="831-siesta.html"><div class="ph"><img src="images/831-siesta-aerial.jpg" alt="831 Siesta Drive aerial" loading="lazy"></div><div class="tag">Sarasota, FL</div><h4>Siesta Drive</h4><p>Land or build to suit · luxury home · 831 Siesta Dr</p></a>
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

# ------------------------------------------------------------------ LIMITED PARTNERS
REG = "mailto:invest@ii.miami?subject=Limited%20partner%20interest&body=Name%3A%0AEntity%20(if%20any)%3A%0AAccredited%20investor%20(yes%2Fno)%3A%0AInvestment%20range%3A%0AInterest%3A%20income%20hold%20%2F%20development%20%2F%20both%0APhone%3A%0A"
lp = '''
<section class="hero short" style="padding:0">
  <img src="images/dev-hero.jpg" alt="">
  <div class="wrap">
    <div class="eyebrow">Limited partners</div>
    <h1>Own the building,<br>not the <em>flip.</em></h1>
    <p>Long-term, income-producing Florida real estate, developed and operated by people who put their own money in first.</p>
    <div class="btns"><a class="btn btn-fill" href="''' + REG + '''">Register interest</a><a class="btn btn-line" href="#how">How it works</a></div>
  </div>
</section>

<section class="light">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">Why partner with us</div>
        <h2 class="lede">Twenty-five years of building for <em>ourselves.</em></h2>
      </div>
      <div class="prose reveal">
        <p>Since 2001 the ii Miami group has developed, built and brokered its own projects across Florida: single-family estates, townhouse communities, condominium towers and retail centers. More than 250 homes since 2005. More than 300 units in development today.</p>
        <p>We have always invested our own capital. We are now opening select long-term holds to a small number of limited partners who want durable income from real assets and a sponsor they can call.</p>
      </div>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>250+</b><span>Homes developed since 2005</span></div>
      <div class="stat"><b>300+</b><span>Units in development</span></div>
      <div class="stat"><b>2001</b><span>Developing across Florida since</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow reveal">Three things we will not change</div>
    <h2 class="lede reveal">Simple structures, run by <em>owners.</em></h2>
    <div class="pillars reveal">
      <div class="pillar"><div class="num">01</div><h3>We develop what we own</h3><p>The principals have developed more than 250 homes since 2005 and build today through our own licensed contractor, J &amp; C Premier Builders. Partners come in beside the people who entitle, build and operate the asset.</p></div>
      <div class="pillar"><div class="num">02</div><h3>Control stays with the sponsor</h3><p>One decision-maker, one deal at a time. No blind pool, no committee. You know exactly what you own and who is running it.</p></div>
      <div class="pillar"><div class="num">03</div><h3>You see every fee first</h3><p>Brokerage, construction and asset management are related parties. They are named, disclosed and priced at market in the offering documents &mdash; before a dollar moves.</p></div>
    </div>
  </div>
</section>

<section class="light" id="how">
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">How it works</div>
        <h2 class="lede">What a partnership <em>looks like.</em></h2>
      </div>
      <div class="prose reveal">
        <p><strong>One entity per investment.</strong> Each project is its own company with its own capital, its own lender and its own books. Nothing is cross-collateralized with anything else.</p>
        <p><strong>Partners are paid first.</strong> Limited partners receive a preferred return before the sponsor participates in profits. Distributions from operations are paid as the property generates them.</p>
        <p><strong>Holds are measured in years, not quarters.</strong> We buy and build to own. Partners receive a K-1 each year and a plain-language report on the asset.</p>
        <p><strong>Accredited investors only.</strong> Terms, minimums and the full fee schedule are set out in each offering's documents.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="two">
      <div class="reveal">
        <div class="eyebrow">Current focus</div>
        <h2 class="lede">Build-to-rent, held for <em>income.</em></h2>
      </div>
      <div class="prose reveal">
        <p>A 300-plus-unit build-to-rent townhouse community in Central Florida, developed in phases and held for the long term. Designed, built and managed by the group, for rental income from the first certificate of occupancy.</p>
        <p>This is for investors who want durable income from real assets, a sponsor they can call, and a structure they can read in an afternoon. It is not for anyone looking for a quick flip or a liquid product.</p>
      </div>
    </div>
  </div>
</section>

<section class="contact" id="contact">
  <div class="wrap">
    <div class="eyebrow reveal" style="display:inline-block">Register interest</div>
    <h2 class="lede reveal">Tell us what you are <em>looking for.</em></h2>
    <p class="sub reveal">A short email is enough. We will come back to you directly, and you will hear about an opportunity only when there is one.</p>
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-fill" href="''' + REG + '''">Email invest@ii.miami</a><a class="btn btn-line" href="tel:+13059002100">+1 305-900-2100</a></div>
    <p class="sub reveal" style="font-size:12px;opacity:.7;margin-top:28px">This page describes the sponsor and its approach. It is not an offer to sell, or a solicitation of an offer to buy, any security. Offers are made only to qualified investors through the offering documents for a specific investment.</p>
  </div>
</section>
'''
page('limited-partners.html', 'Limited Partners — Invest with ii Miami', 'Long-term, income-producing Florida real estate for limited partners. Sponsor-controlled, deal-by-deal structures; every related-party fee disclosed up front. Accredited investors.', lp, 'invest')

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
        <p>Each deal is its own structure, sponsor-managed, with the sponsor's own capital alongside partners'. We are now opening select long-term, income-producing holds to <a href="limited-partners.html">limited partners</a>.</p>
        <p>Since 2001 the group has developed, built and brokered single-family estates, townhouse communities of up to 300 units, condominiums, and retail centers for national tenants across South Florida and the Gulf Coast.</p>
      </div>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>250+</b><span>Homes developed since 2005</span></div>
      <div class="stat"><b>300+</b><span>Units in development</span></div>
      <div class="stat"><b>2001</b><span>Developing across Florida since</span></div>
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
    <div class="btns reveal" style="justify-content:center"><a class="btn btn-dark" href="mailto:properties@ii.miami">properties@ii.miami</a><a class="btn btn-dark" href="tel:+13059002100">+1 305-900-2100</a></div>
    <div class="addr reveal" style="color:#5f646c">550 Biltmore Way, Mezzanine Ste. 200 · Coral Gables, FL 33134</div>
    <div class="addr reveal" style="color:#5f646c;margin-top:10px"><a href="https://www.linkedin.com/company/iimiami" rel="noopener" style="text-decoration:none">LinkedIn</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@iimiami" rel="noopener" style="text-decoration:none">YouTube</a> &nbsp;·&nbsp; <a href="https://www.facebook.com/ii.miami" rel="noopener" style="text-decoration:none">Facebook</a></div>
  </div>
</section>
'''
page('about.html', 'About — ii Miami', 'The ii group of companies: Florida real estate developers, brokers and investors since 2001. More than 250 homes developed since 2005; 300-plus units in development.', about, 'about')
