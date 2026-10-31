# AGENTS.md: electrician website template

One-page website for a home electrician with fixed prices, landlord reports and an emergency line. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/electrician-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/electrician-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/electrician-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/electrician-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:navigation`: `.nav__menu` `.menu__close` `.nav__links`
  - `section-script:contact`: `.contact__form` `.contact__status`
  - `scene:rooms`: `.rooms__row` `.rooms__photo` `.rooms__name`
  - `scene:charge`: `.charge__panel` `.charge__sheet` `.charge__tab` `.charge__view`
  - `scene:landlords`: `.ll__row` `.ll__fill` `.ll__item`
  - `scene:team`: `.team__grid` `.team__member`
  - `scene:night`: `.night__grid` `.night__phone` `data-tone`
  - `scene:reviews`: `.reviews__track` `.reviews__list`
- `style="--len:N"` = characters in that display line, spaces included: `Ohmstead` is 8.
- The wordmark "Ohmstead" in the footer is sized by style="--len:8", the number of characters of the word; update it when you rename the business.
- The rooms scene pairs the list rows with the photos in the frame by position (the smaller of the two counts); keep one photo per room, in the same order.
- The step numbers in the opening come from a CSS counter, and the Due and Passed badges in the landlord rows are both in the HTML (CSS and the scene decide which shows); keep both badges in every row.
- The cells of the night grid are created by the script from the stage size; do not add cells by hand. Headings with the lines effect are cut into lines by SplitText and put back when they land, so keep them as plain text.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #f8f6f1 (cream: reading sheets, photo tabs, form fields and text on the dark green bands), `--color-2` #212320 (near-black ink: text on cream and aqua, button hover fill, landlord rule lines), `--color-3` #575953 (grey for secondary text on cream, the Due badge and landlord rows before they are checked), `--color-4` #e0dcd3 (stone: hairline rules between rows, review card borders and the photo placeholder ground), `--color-5` #a4e6f4 (aqua accent: opening sheet, primary buttons, Passed badges, charger price tab and lit night cells), `--color-6` #10231a (dark green: page ground, tidy promise, prices, night stage panel, footer and the tab notch on dark photos), `--color-7` #a6b8ac (sage: secondary text on the dark green bands), `--color-8` #1c3428 (deep green: charger and contact photo panels, dark photo ground, the rule above the footer credit line); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, phone, form, email): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Book a visit buttons (navigation bar, menu overlay, opening, footer link): now #contact; owner's target: keep them on the visit form, or point them to your booking calendar.
- See fixed prices link in the opening: now #prices; owner's target: keep it, or change it if you rename or remove the price list.
- Get a charger quote button in the charger section: now #contact; owner's target: keep it on the form, or point it to a charger quote page.
- Book a landlord check button in the landlord section: now #contact; owner's target: keep it on the form, or point it to a landlord booking page.
- Phone links (navigation, menu, FAQ, contact, footer) and the out-of-hours number link in the night section: now tel: links to two placeholder numbers; owner's target: your office phone and your out-of-hours phone in tel: form (+44...).
- Email links in the contact details and the footer: now mailto: links to a placeholder address; owner's target: your office email.
- Request a visit button of the form: now a script that checks name and phone, shows a thank-you line and clears the form; nothing is sent; owner's target: your form endpoint (Formspree, Netlify Forms) or your CRM form, and drop the thank-you script.
- The form in `#contact` (fields `name`, `phone`, `postcode`, `job`, `message`) sends nothing; `section-script:contact` handles its submit in the page (read it before you connect a service). Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Ohmstead (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (14, Unsplash: rooms 6, tidy 2, charge 1, team 4, contact 1): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Company and place: Ohmstead Electrical Ltd, Sheffield and the villages around it out to Hathersage, Stocksbridge and Dronfield; the address, postcode, phones and email are placeholders (contact, footer, FAQ).
- Process promises: free visit of about forty minutes, itemised quote within two working days, no day rates, certificate emailed before leaving (opening, FAQ).
- Prices: all eight rows of the price list (sockets from £95, lights from £45, outdoor socket from £140, smoke alarms from £240, fuse board from £585, charger from £895, landlord report £160 for up to three bedrooms, full rewire from £5,400 in about seven working days) and "include parts, testing, the certificate and VAT" (prices, charge).
- Charger claims: a 7 kW charger, up to ten metres of cable, load balancing, off-peak set-up, solar and battery readiness (charge, prices).
- Landlord claims: a report every five years, same-day report to landlord and agent, booking around tenants (landlords).
- Compliance claims: building control notification, certificates with every job, public liability cover of five million pounds (FAQ). Never invent registrations or insurance.
- Team: nine electricians, all employed, none subcontracted; Jess Okafor, Dan Whitlow, Ray Brennan and Tom Lau with specialities; the portraits are stock photos (team).
- Emergency service: out-of-hours line answered by an electrician, most callouts reached within the hour, emergency callout £95 with the first hour included (night).
- Reviews: eight named reviews with districts of Sheffield and jobs, "kept short and unedited" (reviews). Replace with real, permitted reviews.
- Response times and hours: reply "within two working hours", call back "within two working hours", hours Monday to Friday 7:30 to 18:00 and Saturday 8:00 to 13:00 (contact).
- Gallery captions: "A rewire, day seven", "Most asked: ..." photo tabs (rooms, tidy).
- Footer: "© 2026 Ohmstead Electrical Ltd. Registered in England.": put in your legal name and company number.

## Known limits
- Without JavaScript the Menu button on narrow screens cannot open the overlay (wide screens show the links), and the night grid stays empty because its cells are made by script.
- The visit form sends nothing: its handler is a script that shows the thank-you line and clears the fields, and without JavaScript the form posts to the page itself (action "#"), so connect a form service or CRM.
- The night section is 230vh tall and the rooms frame is sticky; check both on short laptop screens, where the rooms frame can crowd the list.
- The reviews turn into two clipped sliding rows only when the script runs; with reduced motion they stay a wrapped grid, as do the other scenes.
- GSAP, ScrollTrigger and SplitText load from the jsDelivr CDN at the end of the body, so the effects depend on that request succeeding.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Ohmstead left only in class names.
