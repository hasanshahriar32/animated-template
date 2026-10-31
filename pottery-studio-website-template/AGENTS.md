# AGENTS.md: pottery studio website template

One-page website for a pottery studio that makes tableware to order, teaches classes and sells a few pieces. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/pottery-studio-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/pottery-studio-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/pottery-studio-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/pottery-studio-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:nav`: `.nav__bar` `.nav__menu` `.menu__close`
  - `section-script:opening`: `.op-screen`
  - `scene:opening`: `.op-screen` `.op-photo` `.op-title` `.op-band` `.op-hold` `.op-about` `.op-statement` `.page-grid` `.op-title--copy`
  - `section-script:contact`: `.ct-form` `.ct-status` `data-invalid` `data-sent`
  - `scene:commissions`: `.cm-stick` `.cm-room` `.cm-card` `.m-surface__photo`
  - `scene:process`: `.pr-pin` `.pr-track` `.pr-rule` `.pr-step` `.pr-step__photo`
  - `scene:glazes`: `.gl-row`
  - `scene:makers`: `.mk-list` `.mk-person` `.mk-photo` `.mk-text`
  - `scene:shop`: `.sh-bisque`
  - `scene:contact`: `.ct-title` `.ct-word` `.page-grid`
- `style="--len:N"` = characters in that display line, spaces included: `Cobalt` is 6, `Iron red` is 8, `Celadon` is 7, `Tenmoku` is 7, `fettle` is 6.
- The page-grid layer has five vertical lines that mark four columns, and two scenes read them by position: the opening cuts its photo into four strips at the three inner lines, and the contact heading's words scatter to the start of the first four lines, kept inside the fifth. Keep all five lines in this order if you change the layout.
- The opening scene clones the photo block and the h1 into four strips at run time, so keep the photo, the h1 and the band inside the first screen's wrappers as they are.
- Each glaze name and the footer wordmark are sized from an inline style="--len:N" (the number of characters of the word): Cobalt 6, Iron red 8, Celadon 7, Tenmoku 7, the wordmark 6. Set N to the length of each new word.
- The glaze colours live on each glaze row as --gl-ground and --gl-ink; the glazes scene reads them, so recolour a glaze there, and keep one row per colour state.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #f1f2f2 (page ground, nav bar, about screen, the glazes section before the first glaze), `--color-2` #0f0f10 (text, black buttons, hairlines, footer and phone menu ground, ink on the celadon glaze), `--color-3` #ffffff (venue cards and shop photo frames, button labels, footer text, ink on the cobalt, iron red and tenmoku glazes), `--color-4` #656869 (captions and small descriptions), `--color-5` #1d42cf (plus marks, button hover fill, form status line, the cobalt glaze ground), `--color-6` #b9361a (second plus mark colour, the iron red glaze ground), `--color-7` #a9c4b7 (the celadon glaze ground, used only there), `--color-8` #2a1c15 (the tenmoku glaze ground, the commissions section ground behind its photos, loading colour of photo frames); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, email, phone, form, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Book a class button in the first screen: now #classes; owner's target: your class booking page or calendar, or keep it on the classes list.
- Book links on the four class rows: now #contact; owner's target: a booking link for each class (a booking tool or a form with the class chosen), or keep them on the contact form.
- Start a commission button in the commissions section: now #contact; owner's target: your commission enquiry form or email.
- Join the waiting list button in the membership section: now #contact; owner's target: your waiting list form or email.
- Reserve links under the six shop pieces: now a mailto: link with the piece named in the subject; owner's target: your shop or payment link for each piece, or keep the email reservation.
- Send message button of the contact form: now a script checks the fields and shows a thank-you line; nothing is sent (the form has action="#contact"); owner's target: a form service (Formspree, Netlify Forms) or your own handler, or remove the form and keep the email and phone.
- Instagram and Newsletter links in the footer: now the Instagram homepage and a mailto: link; owner's target: your Instagram profile and your newsletter sign-up page.
- The form in `#contact` (fields `name`, `email`, `topic`, `message`) sends nothing; `section-script:contact` handles its submit in the page (read it before you connect a service). Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Fettle (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (30, Unsplash: opening 3, commissions 6, process 6, glazes 4, classes 1, makers 3, membership 1, shop 6): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Studio and place: a "former cutlery works in Sheffield", the placeholder address "1 Example Street, Sheffield S1 0ZZ" and the opening hours (opening, contact, footer).
- Class list, days, durations and prices: £48, £285, £165, £95, groups "of six", "a wheel each" (classes).
- Membership: £95 a month, no fixed term, 12.5 kg of clay, wheel time Tuesday to Sunday "booked online", a kiln that fires every Friday (membership).
- Commission terms: "samples in four weeks, a full order in twelve", "about 40 pieces of one shape", glaze recipe kept on file (commissions, FAQ).
- Client venues: Marrow, Lowfield Coffee and Hallam House with their districts (commissions): replace with real clients or remove.
- Firing details: bisque to 1000 C, glaze firing to 1240 C overnight, "about three weeks" (process).
- Glaze claims: four named glazes, "food safe, tested in the dishwasher", "tested in commercial dishwashers and microwaves", and the finish and use of each (glazes, FAQ).
- Team: Ruth Ainsley, Dev Mistry, Hana Kowalska, their roles and biographical lines such as "ten years making", "a chemist by training", "more than two thousand people" (makers).
- Shop pieces: six names, prices, sizes and glazes; shipping "anywhere in the UK" (shop).
- Collection and vouchers: pieces ready "three to four weeks after your class", gift vouchers "valid for a year" (FAQ).
- Reply time: "We reply within two working days" (form status line).

## Known limits
- Without JavaScript the menu button cannot open the menu; the nav links stay reachable in the bar on wide screens. The contact form has no sending code.
- The process section is pinned and moves sideways by the width of the six-step track minus one screen, about 1,200 px of scrolling at 1440 px and about 1,350 px on a 375 px phone (each step is 76vw there), which some visitors find tiring.
- The shop's pale bisque overlay and the glaze colour blend need JavaScript; without it (and with reduced motion) the shop photos show in colour from the start and each glaze row keeps its own colour band.
- The Make and Learn links in the about screen and the glaze names are set very large; keep them short. The glaze names and the footer wordmark shrink to fit by --len, Make and Learn do not.
- gsap, ScrollTrigger, SplitText and Lenis load from jsDelivr at the end of the body; if the CDN is blocked the page shows its still layout (steps in a grid, glaze rows as colour bands) while the menu and form scripts keep working.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Fettle left only in class names.
