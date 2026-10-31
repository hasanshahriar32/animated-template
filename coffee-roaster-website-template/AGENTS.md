# AGENTS.md: coffee roaster website template

One-page website for a small coffee roastery with a counter that sells beans, drinks and refills. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/coffee-roaster-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/coffee-roaster-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/coffee-roaster-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/coffee-roaster-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:nav`: `.nav__menu-btn` `.nav__menu-label` `.nav__rail` `.nav__list`
  - `scene:beans`: `.beans__list` `.beans__turn` `.beans__row` `.beans__shot`
  - `scene:roast-days`: `.roast__step` `.roast__cell` `.m-stamp`
  - `scene:counter`: `.counter__list` `.counter__row` `.counter__in`
  - `scene:refills`: `.refills__track` `.refills__tin` `.refills__lid`
  - `scene:people`: `.people__photo`
  - `scene:visit`: `.visit__window`
- The bean photos and rows are matched by position, and the scene throws an error if the counts differ: keep one photo per coffee. The roast-day ticket likewise needs one cell per step, four of each.
- Each heading is a lockup of three spans (small line, big line, small line) that the lockup effect animates line by line; the effect animates whatever lines it finds, but the ruled look is built for three, so keep three.
- The round stamps are inline SVG with a word in a span; recolour them through the colour variables, and keep the word short so it stays inside the ring. The ring text is stretched to one full circle by textLength="490", so a much shorter or longer phrase looks spaced out or squeezed.
- The bag count in the top bar is plain text; it is not connected to any cart.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #fce9da (cream paper ground of the page, plus the text and rules on the indigo and rust sections and the fill of the light buttons on hover), `--color-2` #41339a (indigo ink: text and hairlines on cream, the ground of the three first-screen panels, the drinks board and the visit section, and the fill of the bag and Menu icons on hover), `--color-3` #a2481b (rust: small kicker labels, outlined buttons, refill figures, the ground of the roast-days and cupping sections, the current coffee name and the current rail link); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, phone, email, map, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- This week's beans button in the first screen: now #beans; owner's target: keep it, or link your online shop.
- Add to bag buttons on the five coffees: now #visit; the bag icon in the top bar shows 0 and links to #beans; owner's target: a checkout or shop link per coffee (Shopify, Stripe, Square); the bag count is plain text.
- Get a tin button in the refills section: now #visit; owner's target: your tin product page, or keep it on the visit section.
- Book a seat links on the four cupping dates: now mailto: counter address with a subject for each date; owner's target: a booking page per date, or keep the email links with your own address.
- Get directions button in the visit section: now a Google Maps search for Sheffield; owner's target: the map link of your shop.
- Wholesale enquiries link in the visit section: now mailto: counter address with the subject Wholesale; owner's target: your wholesale email or form.
- Phone link in the top bar and the visit section: now tel: the placeholder number; owner's target: your number.
- Instagram and Facebook links in the footer: now the home pages of instagram.com and facebook.com; owner's target: your own profiles.
- The name Little Drum Coffee Roasters (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (12, Unsplash: opening 1, beans 5, farms 1, counter 1, refills 1, cupping 1, people 1, visit 1): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Roast day and times: Thursday from 7 am, the Tuesday weighing, Friday bagging (opening, roast days, nav note)
- Batch numbers, weights, times and cup notes on the tickets (opening, roast days)
- Shelf life claims: three weeks on the shelf, best from a few days to five weeks (opening, FAQ)
- The five coffees: names, origins, processes, notes and prices from £8.00 to £10.50 (beans)
- Farm names, places, start years, cooperative size and altitude (farms)
- Drinks and prices on the board, oat milk at no extra cost, seats (counter)
- Refill terms: tin price £6, 10% off, bags saved last year 4,120 (refills)
- Cupping dates, themes and the Free offer (cupping)
- Owner names, roles, the founding year 2019 and the garage story (people)
- Postage and delivery terms: Wednesday cut-off, free postage over two bags, two or four week subscriptions (FAQ)
- Wholesale claims: a few cafes and offices in Sheffield, delivered by bike in returnable tins (FAQ)
- Address, opening hours, phone and email (visit, nav, footer)

## Known limits
- Without JavaScript the Menu button cannot open the link rail on screens narrower than 1024 px and the sections are not marked as current; the FAQ opens natively.
- Add to bag buttons and the bag count do not work as a shop: they link to the visit section until you connect a checkout.
- The beans and roast-days scenes sync photos and stamps to scroll position; on short laptop screens the sticky ticket and the round bean frame take most of the height.
- The slatted owners' photo is built at run time, so it is the plain photo until the script runs and in reduced motion.
- gsap, ScrollTrigger and Lenis load from a CDN near the end of the body, and the motion scripts after them wait for those files.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Little Drum Coffee Roasters left only in class names.
