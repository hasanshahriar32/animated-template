# AGENTS.md: pharmacy website template

One-page website for an independent pharmacy with weekly medicine packs, a walk-in clinic, vaccinations, a small shop and bike delivery. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/pharmacy-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/pharmacy-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/pharmacy-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/pharmacy-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:site-nav`: `.nav__tabs` `data-tab`
  - `section-script:shop`: `.shop__row` `.shop__drawer`
  - `section-script:contact`: `.contact__status`
  - `scene:packs`: `.packs__week` `.packs__seal` `.packs__dose`
  - `scene:clinic`: `.clinic__col` `.clinic__cell` `.clinic__marker` `.clinic__photos` `data-step`
  - `scene:shop`: `.shop__rows` `.shop__row` `.shop__panel` `.shop__photo`
  - `scene:delivery`: `.delivery__runway` `.delivery__stage` `.delivery__track` `.delivery__fill`
  - `scene:people`: `.people__frame` `.people__slat` `.people__cell`
  - `scene:faq`: `.faq__list` `.faq__tab`
- `style="--len:N"` = characters in that display line, spaces included: `HALE` is 4.
- Each section carries data-tab with the position of its header tab (1 to 5; tab 0, Hale, is the fallback before any section reaches the header); a new part needs its tab in the strip and that number.
- The clinic scene pairs each condition cell with the photo whose data-step equals the cell's position (0 to 3), and the CSS grid and marker are sized for four cells; the people scene is written for exactly three portraits and three cards; each shop button opens the panel named in its aria-controls.
- The wordmark in the footer takes its size from style="--len:4", the number of characters in "HALE"; update it with the name.
- The folder tabs, bars and the example week grid are CSS, not images: recolour them through the colour variables in :root. The shop panels are shown or hidden with the hidden attribute by section-script:shop.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #c9c9c7 (grey page ground and header bar, empty photo frames, the Visit tab of the questions), `--color-2` #ffffff (white sheets, the first header tab, question cards, text on the dark folders), `--color-3` #131313 (text, black bars and rules, table lines, the seal bar and the route fill), `--color-4` #d4e3f3 (pale blue: weekly packs folder, bedtime row, form fields, default button fill, Repeats tab), `--color-5` #f6d4dc (pink: clinic and vaccination folders, midday row, Clinic tab), `--color-6` #d1e8d9 (green: shop and delivery folders, evening row, the thank-you line, Shop tab), `--color-7` #fbefc4 (yellow: people and story folders, morning row, the form button, People tab), `--color-8` #575757 (dark grey: questions and contact folders, the Visit tab in the header); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, phone, email, form): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Find us link in the header: now #contact; owner's target: keep, or a map link.
- Order a repeat link in the header, the Order a repeat button and the Ask about weekly packs link in the first part, and the four Book links in the vaccination table: now #order (the repeat form in the contact section); owner's target: your online repeat-prescription or booking page, or keep #order once the form is connected.
- The tab strip in the header (Hale, Repeats, Clinic, Shop, People, Visit): now #packs, #packs, #clinic, #shop, #people and #contact (the first two tabs both go to #packs); owner's target: keep as anchors.
- Ask us to order something links under each of the four shop shelves: now #contact; owner's target: your shop enquiry page or email.
- Send to the counter button of the repeat form: now the form has action="#order" and method="post"; section-script:contact checks the fields, shows the thank-you line and clears the form, nothing is sent; owner's target: your form handler or prescription system, over HTTPS, with a privacy notice (the form asks for name, date of birth, phone and medicines).
- The form in `#contact` (fields `name`, `birthdate`, `phone`, `medicines`, `handover`) sends nothing; `section-script:contact` handles its submit in the page (read it before you connect a service). Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Hale (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (20, Unsplash: weekly-packs 1, walk-in-clinic 4, vaccinations 1, shop 4, bike-delivery 5, pharmacists 3, independent-since-1987 1, contact 1): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Name and ownership: Hale, "Hale Pharmacy Ltd", owner and superintendent pharmacist "Nadia Okafor", Sami and June, Margaret Hale who opened in 1987, the dog Biscuit "on the counter since 2015", "Registered pharmacy" (people, story, footer).
- Location: Leeds, the address, "two doors up from the bakery, opposite the stop for the 56 bus", two short-stay bays behind the shop reached from Hollis Avenue (title, meta description, contact, FAQ); the phone 0113 000 0000 and the email counter@hale.example are placeholders.
- Opening hours: Monday to Friday 8:30 to 19:00, Saturday 9:00 to 17:00 with the clinic room open, Sunday 10:00 to 13:00 dispensary only (contact, clinic).
- Clinic claims: "seven common conditions under the NHS Pharmacy First service", ten minutes in private, ages and conditions on the four cells, blood pressure free from 40, seen "usually within twenty minutes" (clinic, FAQ).
- Vaccinations: flu free at 65 and over, in pregnancy or with a long-term condition and £16 for others, Covid free at 75 and over, travel jabs six weeks before flying, chickenpox two doses, seasons and eligibility (jabs table, FAQ).
- Weekly packs: for people on four or more medicines, free, checked by a second pharmacist, and the numbers of tablets in the example week (packs).
- Repeats service: requests made seven days before running out, a text when packed, repacked the same day a dose changes (FAQ, packs, form thank-you line).
- Delivery: Tuesdays and Fridays, free within a mile and a half, tracked post for £3 further out, leaves 9:30, back by eleven, the five stops with times (delivery).
- Shop: the four shelves and their products, "malaria tablets with a consultation", special orders "usually by the next afternoon" with the price told first (shop, FAQ).
- Staff details: years at the counter ("twenty-two years"), roles, "nobody here works for a head office", "three chains offered to buy the shop" (people, story).
- Promises and access: a reply within one working day, a private conversation "always", a level door, "nobody at the counter will ask you why" (form, FAQ, contact).
- Place names on the delivery round (Example Street, a placeholder, Brudenell Row, Hollis Avenue, Cardigan Grove, Kirk Lane) and the postcode district in the meta description: replace with the real round (delivery, meta description).

## Known limits
- Without JavaScript the shop buttons do nothing and three of the four shelves stay hidden (only Sleep & Calm shows), so the Skin & Sun, Baby & Bath and Travel Kit texts cannot be read. The tab raised in the header does not follow the scroll. The page has no menu to open, so navigation still works.
- The repeat form asks for a name, a date of birth, a phone number and medicines, but sends nothing: the script only checks it and shows the thank-you line. Connect it to a secure endpoint and add a privacy notice before launch, because the data is health related.
- On phones (760 px and below) the header tab labels shrink to 10.5 px to fit six tabs in one row, and the Find us link is hidden.
- The bike delivery stage is held under the header for the full height of the screen minus the header, and has a minimum height of 520 px, so on windows shorter than about 630 px the held stage is taller than the screen.
- Photos are lazy-loaded from Unsplash, including the one on the first screen; self-host them before launch.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Hale left only in class names.
