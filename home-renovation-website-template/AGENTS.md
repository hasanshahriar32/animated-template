# AGENTS.md: home renovation website template

One-page website for a design-and-build renovation company, for owners of older houses who want a kitchen, extension, loft or bathroom. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/home-renovation-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/home-renovation-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/home-renovation-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/home-renovation-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:nav`: `.nv-menu` `.nv-close`
  - `section-script:opening`: `.op-stage`
  - `section-script:contact`: `.ct-form` `.ct-status`
  - `scene:method`: `.mt-sheet` `.mt-step` `.mt-steps`
  - `scene:rooms`: `.rm-plan` `.rm-room` `data-dx` `data-dy`
  - `scene:projects`: `.pj-track` `.pj-card` `.m-duo__tone` `.pj-cap`
  - `scene:letter`: `.lt-env` `.lt-paper` `.lt-tile` `.lt-front` `data-dx` `data-dy`
  - `scene:snags`: `.sn-sheet` `.sn-item` `.sn-stamp` `.sn-ink` `.sn-tick`
  - `scene:faq`: `.fq-folder`
  - `scene:footer`: `.ft-tile` `data-dx` `data-dy` `data-r`
- `style="--len:N"` = characters in that display line, spaces included: `squarefoot` is 10.
- The footer wordmark has style="--len:10", the number of characters in "squarefoot"; change it with the name. The nav wordmark is plain text.
- The method contact sheet is a 2×2 grid of exactly four photos and the scene zooms to a quarter per photo, so keep four photos and four steps. The rooms plan has six rooms and the footer and letter each have four tiles.
- Each plan room and tile starts its movement from its own data-dx and data-dy (the footer tiles also data-r): keep these attributes when changing the text, and keep the rooms' modifier classes (rm-room--front, --kitchen and so on), which place them on the plan.
- The paper, the plan lines, the four logo tiles, the envelope, the stamp and the door arcs are CSS and inline SVG, not images: recolour them through the --color-1 to --color-8 variables in :root. The photos get their cobalt duotone from a CSS tone layer and filter (in the projects the scene adds it and fades it out, so with reduced motion or no JavaScript those five show in full colour), so any photo works.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #e9dfcb (the paper ground under the graph grid, including the opening stage), `--color-2` #2a2926 (body text, the faint graph lines and the borders of the method steps and diary pages), `--color-3` #2446d0 (cobalt: the opening plan lines, room borders and titles, step numbers, the Extend sheet, the footer ground, button fill on hover and the duotone photos), `--color-4` #1b2457 (deep navy: button bases, the letter section ground, the footer panel and the dim over the opening photo), `--color-5` #c23d27 (vermilion: the Rebuild sheet, the icon tile in every button, diary margin lines and notes, snag ticks and strike lines, the Signed off stamp and the stamp box on the envelope), `--color-6` #cfb98f (manila: the Refresh sheet, the questions folder and its tab, the envelope, the tape on diary photos and the footer column titles), `--color-7` #fbf8f1 (warm white: the paper sheets and cards (nav strip, diary, letter, snag list, review slips, form), photo frames and captions, text on cobalt, vermilion and navy, and the stamp), `--color-8` #48443d (the grey-brown of pencil notes and small captions); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, phone, form, email, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Book a site visit buttons in the nav, the phone menu and the footer, and the Book a free site visit, Start with a site visit and Price my room, rebuild and extension buttons: now #contact; owner's target: your booking or enquiry page, or keep #contact once the form is connected.
- See finished rooms link in the opening sheet: now #projects; owner's target: keep it, or point it to a project gallery or portfolio page.
- Request a visit button in the contact form: now submits the form and shows the thank-you line, nothing is sent; owner's target: your form service (Formspree, Netlify Forms) in the form's action, or an email or CRM handler.
- phone button in the questions folder, the phone note in the nav and menu, and the contact and footer phone links: now tel: link to the placeholder 0161 000 0000; owner's target: your real phone number in the tel: href and the visible text.
- Email links in the contact list and the footer: now mailto: link to the placeholder hello@squarefoot.example; owner's target: your real address.
- Privacy and Terms links in the footer: now #footer; owner's target: your privacy policy and terms pages.
- The form in `#contact` (fields `name`, `phone`, `email`, `postcode`, `room`, `message`) sends nothing; `section-script:contact` validates it and shows the thank-you text. Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Squarefoot (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (13, Unsplash: opening 1, method 4, projects 5, diary 2, contact 1): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Founding and name: "since 2011" (nav corner note), the company name "Squarefoot Renovations Ltd" and the area "Manchester" (title, meta description, footer).
- Prices: Refresh £65, Rebuild £140, Extend £210 per sq ft, "from"; "Prices include labour, materials, waste removal and VAT"; "Every quote is fixed for 60 days" (pricing).
- Guarantee and terms: a ten-year workmanship guarantee in writing, the snag list fixed before the final invoice, five per cent held until the snag list is empty, a small deposit to book a start date (method, snags, faq).
- Timings: a site visit of about 90 minutes, drawings within two weeks with three layouts, programmes of four to six weeks for bathrooms, six to nine for kitchens, ten to twelve for lofts and twelve to sixteen for extensions (method, faq).
- Working hours and conduct: 8 am to 5 pm on weekdays, never on Sundays, deliveries before 9:30, a callback within one working day (letter, contact).
- Projects: five jobs with districts, job types and durations, such as a 1905 terrace in Chorlton in 9 weeks and a 260 sq ft rear extension in Burnage in 16 weeks (projects).
- The diary: the clients "the Okafors", house no. 40, six weekly entries with events and weekdays, and the names Amara and Tunde (diary, reviews).
- The letter: numbers 38 and 40 and 42, "From Monday 3 March", the weeks 2 and 4 as the noisiest, the site lead "Dan" and his phone (letter, faq, contact).
- Insurance and certification: public liability and contract works insurance, certified electrics and gas work, a handover folder with drawings and certificates (faq, method).
- Reviews: three quotes with names and districts (Amara and Tunde, Helen, Rob and Mei) are invented placeholders; use real, permitted reviews (reviews).
- Areas and address: Chorlton, Didsbury, Withington, Levenshulme, Burnage, Whalley Range; the yard "Example Yard, Manchester"; the phone 0161 000 0000 and hello@squarefoot.example are placeholders (contact, footer).
- The snag list: six items for a house at "40 Example Road", a street name that must change to a real or generic one (snags).
- Planning claim: that many single-storey rear extensions fall under permitted development and that the firm handles applications and lawful development certificates (faq).
- Services: the six services and the three package descriptions must match what the firm really offers (rooms, pricing).

## Known limits
- Without JavaScript the phone menu button cannot open the overlay and the header links are hidden on phones; the footer repeats Method, Rooms, Pricing, Projects and FAQ and the Book a site visit link.
- The contact form sends nothing: with JavaScript it shows the thank-you line, without it the form posts to #contact. Connect a form service before publishing.
- On wide screens the projects section pins and a horizontal track runs through it; on every screen wider than 860 px the intro and the cards share one pinned screen and the track starts off to the right, so the first moments show mostly the heading until the first card arrives.
- The pencil notes are in a handwriting font at small sizes in grey; check them at 375 px when you change the copy, since they sit above or beside headings.
- The footer wordmark and the nav corner notes are decorative or hidden on narrow screens: the corner notes with the phone and "since 2011" show only above 1180 px.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Squarefoot left only in class names.
