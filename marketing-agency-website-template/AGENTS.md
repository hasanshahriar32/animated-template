# AGENTS.md: marketing agency website template

One-page website for a marketing or communications agency that publishes a yearly research report and runs a live series. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/marketing-agency-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/marketing-agency-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/marketing-agency-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/marketing-agency-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:nav`: `.nav__menu` `.nav__close`
  - `section-script:report`: `.report__form` `.report__status` `data-error` `data-ok`
  - `section-script:contact`: `.contact__form` `.contact__status` `data-error` `data-ok`
  - `scene:signals`: `.signals__arrow` `.signals__dial` `.signals__list` `.signals__item`
  - `scene:shifts`: `.shifts__row` `.shifts__tape` `.shifts__arrow` `.shifts__to`
  - `scene:field`: `.field__stage` `.field__shard` `.field__piece` `.field__lift`
  - `scene:sessions`: `.sessions__sheet` `.sessions__strip`
  - `scene:voices`: `.voices__pin` `.voices__track` `.voices__card` `.m-shard__tint`
  - `scene:report`: `.report__arrow` `.m-arrow__part` `.report__bit` `.report__cover`
  - `scene:contact`: `.contact__line` `.contact__arrow` `.m-arrow__part`
- `field` directly above `sessions`: the animation crosses that border and stops if they are split.
- `style="--len:N"` = characters in that display line, spaces included: `Halyard` is 7.
- The wordmark in the footer is sized from style="--len:7", the number of characters in the name: change it when you rename.
- Every signal item carries style="--signals-bearing:N" (degrees; positive points the big arrow up, negative down). The signals scene reads these values and adds one dial tick per item, so keep one value per item.
- The arrows, paper shards, dial and tape are CSS (clip-paths and grain masks), not images: recolour them through the --color variables in :root. The big arrows need three parts (shaft, upper, lower) in that markup.
- Photos in field notes and voices are paper-cut by the m-shard class; the red duotone is the m-shard__tint span, which the voices scene moves, so keep it in each portrait.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #f0f0f0 (cool grey page ground, the nav bar after the first scroll, the phone menu overlay), `--color-2` #141211 (text, outlines and rules, the filled button and the inactive dial ticks), `--color-3` #f83a1d (vermilion: the arrow, the sessions sheet, the tape over old measures, the button sweep on hover, the active dial tick, photo tints), `--color-4` #f5c3b2 (pink paper: loose bits and the grain over the sessions sheet and the arrow), `--color-5` #2a1f19 (dark brown paper bits and the ground behind photos), `--color-6` #8c7668 (taupe pieces inside the arrow and the dark bits), `--color-7` #c8343a (the Next live and Free pills and the red live link in the nav), `--color-8` #ffffff (text on the red pills and the live link), `--color-9` #5d5d62 (secondary text: facts line, the signals intro, notes, captions, roles, old measures, signal names away from the centre), `--color-10` #f7f7f6 (photo caption plates, session strips, the report cover and form fields); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, form, email, phone): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Live · 21 Oct button in the nav bar: now #sessions; owner's target: your broadcast or event registration page.
- Get the forecast button on the first screen: now #report; owner's target: keep #report, or link straight to your report landing page or PDF.
- Watch live button on the first screen: now #sessions; owner's target: your stream or event page.
- Save a seat buttons on the four session strips: now #contact; owner's target: your event booking or ticket page for each session.
- Send me the forecast button and the report form: now no request is sent: section-script:report checks the email and shows a thank-you line (the form action is #report); owner's target: your form handler, mailing-list service or a download link.
- Send button and the contact form: now no request is sent: section-script:contact checks the required fields and shows a thank-you line (the form action is #contact); owner's target: your form handler (Formspree, Netlify Forms or your own endpoint).
- The form in `#report` (fields `email`, `role`) sends nothing; `section-script:report` validates it and shows the thank-you text. Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The form in `#contact` (fields `name`, `email`, `message`) sends nothing; `section-script:contact` validates it and shows the thank-you text. Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Halyard (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (9, Unsplash: field 5, voices 4): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Research figures: "3,200 conversations · nine markets · 41,000 hours of viewing diaries" (first screen, field notes, voices, FAQ), "nine markets" and "8 of 9", "7 of 9", "6 of 9", "9 of 9" in the six signal statuses (signals).
- The six signals and six shifts with their claims: "thirty" people in a room, "a year after purchase", "ten years on one narrow thing", reply rate predicting purchase "twice as well as audience size" (signals, shifts).
- Report: "Sixty-four pages", seven chapters, the "Free" pill, the PDF "within a minute", "We write once more when the next edition is out" (report, FAQ, form status line).
- Sessions: four dates (Wed 21 Oct, 28 Oct, 4 Nov, 18 Nov 2026 at 18:00, with BST and GMT labels and machine-readable time tags), titles, the "Next live" pill and the nav's "Live · 21 Oct" (sessions, nav, overlay).
- Session logistics: "sixty seats" in the Bristol studio, seats "given out in the order requests arrive", the broadcast is free, recordings "within two days, with chapters" (sessions, FAQ).
- Guests named on the page: "three group-chat admins", Jonah Achebe's "repair channel that reviews products a year late", Inès Duarte on one-take answers (sessions strips).
- Team: Mara Ilves, Jonah Achebe, Inès Duarte and Callum Reyes with titles and lines such as "Read 140 group chats this year" and "three hundred creators a year"; the portraits are stock photos of real people and their alt texts name the people (voices).
- Respondent quote, "Respondent, 26, Leeds", and five city captions from Manchester, Leeds, Seoul, London and Lisbon, with the photo descriptions (field notes).
- Studio details: "independent influence and communications studio in Bristol", "Halyard Studio Ltd", the address 1 Example Street, Bristol BS1 0ZZ, the phone +44 117 000 0000 and hello@halyard.example are placeholders; studio hours "Monday to Friday, 9:30–18:00" (contact, footer, meta description).
- Service promises: a reply "within two working days"; a "ninety-minute working session for up to forty people, in person or online" (contact, FAQ).
- Method: "interviewed twice a year", "screen recordings people chose to share", "The method chapter lists every source" (FAQ).
- Role options in the report form: Brand or marketing, Agency, Creator, Research or teaching, Something else (report).

## Known limits
- Without JavaScript the Menu button cannot open the overlay and the nav links are hidden below 960 px; the footer repeats Signals, Live sessions, Report and Contact.
- Both forms only check the fields and print a thank-you line: nothing is sent or stored until you connect a form service.
- Session dates are written as 2026 dates and the nav says "Live · 21 Oct": they need updating by hand, including the time tags, once the dates pass.
- The Voices section pins the screen while the track runs sideways; on a short or very wide window the pinned stage is tight, and without motion it falls back to a plain grid.
- GSAP, ScrollTrigger, SplitText and Lenis load from jsDelivr at the end of the body: if that CDN is blocked the page still reads and the menu, forms and FAQ work, but nothing moves on scroll (only the CSS load-in and the arrow loop run).

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Halyard left only in class names.
