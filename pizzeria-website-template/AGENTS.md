# AGENTS.md: pizzeria website template

One-page website for a neighbourhood pizzeria with a slice window, regular nights and table bookings. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/pizzeria-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/pizzeria-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/pizzeria-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/pizzeria-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:navigation`: `.nav__menu` `.nav__overlay` `.nav__close` `data-ground`
  - `section-script:opening`: `.opening__first`
  - `scene:opening`: `.opening__first` `.opening__window` `.opening__say` `.m-text-5` `.opening__ring` `.opening__line--1` `.opening__line--2` `.opening__pill` `.opening__wave`
  - `section-script:contact`: `.contact__form` `.contact__status` `data-error` `data-sent`
  - `scene:dough`: `.dough__track` `.dough__shot` `.dough__name` `.dough__frame-wrap`
  - `scene:rule`: `.rule__track` `.rule__line` `.rule__word` `.rule__pill` `.rule__ring`
  - `scene:pies`: `.pies__list` `.pie`
  - `scene:people`: `.people__list` `.person` `.person__ring`
  - `scene:corner`: `.corner__mark` `.corner__ring` `.corner__photo`
  - `scene:contact`: `.contact__send` `.contact__ring`
  - `scene:footer`: `.footer__mark` `.footer__bar` `.footer__ring`
- `style="--len:N"` = characters in that display line, spaces included: `Pizza for the` is 13, `Whole block` is 11, `One more slice` is 14, `Monella` is 7.
- The opening heading lines, the house rule line and the footer wordmark are sized from an inline style="--len:N" (the number of characters): "Pizza for the" 13, "Whole block" 11, "One more slice" 14, "Monella" 7. Set N to the length of each new text.
- The street number 14 in Find me is a big drawn element circled by an SVG ellipse that the corner scene shrinks onto it; change the number inside the same wrapper, and keep the ellipse proportions in mind for long numbers.
- Words wrapped in the m-lift class (underlined words that pop up) carry the personality of the copy; wrap one to three words per sentence the same way.
- The dough scene counts the photos and the step names, takes the smaller of the two and sets the held height from that count (about 58 percent of a screen per step); keep one photo for each step. The pie fan uses a list of six tilts, reused in turn.
- The ellipse stroke in Find me is drawn with a stroke-dashoffset tween with autoRound off; keep that flag, or the line pops instead of drawing.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #ff3b21 (page background and the grounds of the first screen, dough, house rule, slice window, nights, questions and footer; heading colour on cream bands; one pie card, the send button and the street number), `--color-2` #f6f2e8 (cream grounds of the second opening screen, pies, people, find me, contact and the menu overlay; large heading text on red bands; the light button fill and the footer wordmark), `--color-3` #b81f0c (body text, logo and raised words on cream bands, the ellipse drawn round 14 and the text of the light button), `--color-4` #1c0b07 (body text, rules, button ink and raised-word underlines on red bands, and the backing of the capsule photos), `--color-5` #86a6d6 (background of the first pie card), `--color-6` #f1c232 (background of the second pie card), `--color-7` #0e6b46 (background of the third pie card, with cream text); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, social, phone, email, map, form): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- See my pies button in the first screen: now #pies; owner's target: keep it, or point it to your online menu.
- Book a table buttons in the first screen and the menu: now #contact; owner's target: your booking page (OpenTable, Resy, SevenRooms) or keep it on the request form.
- Meet my people button in the second screen: now #people; owner's target: keep it.
- Call to order button under the pies: now a tel: link; owner's target: your phone, or your delivery or ordering page.
- Or grab a slice at the window link under the pies: now #slices; owner's target: keep it.
- Get directions button in the Find me section: now a Google Maps search for the street; owner's target: the Google Maps link of your shop.
- Round send button of the request form: now a script checks the name and a phone or email and shows a line; nothing is sent (the form has action="#"); owner's target: a form service (Formspree, Netlify Forms) or your booking system, or remove the form and keep the phone.
- Instagram links in the header and the footer: now the Instagram homepage; owner's target: your Instagram profile.
- The form in `#contact` (fields `reason`, `name`, `reach`, `date`, `guests`, `note`) sends nothing; `section-script:contact` handles its submit in the page (read it before you connect a service). Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Monella (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (21, Unsplash: opening 2, dough 5, rule 1, pies 4, slices 1, people 4, nights 3, corner 1): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Founding and history: "Since 1994 on the same corner", "thirty years", "my first night on Example Street" (opening, dough, footer).
- Pie names, tags and prices: £11, £13, £12 and £12 (pies).
- Slice window prices and hours: five slices at £3.50 to £4, "opens at eleven", "From 11 am until the trays run out" (slices, corner).
- Opening hours: Monday closed, Tuesday to Thursday noon to 10 pm, Friday and Saturday noon to 11.30 pm, Sunday noon to 9 pm (corner, footer).
- Dough process claims: "Forty-eight hours in the cold", "seven in the morning", "Ninety seconds in the wood oven", "Plum tomatoes" (dough).
- House rule: "After ten at night the last slice on the table is on the house." (rule): a promise the owner must be willing to keep.
- Regulars: Sal, Nina, Theo and Kofi with their quotes and details (people): replace or remove, never present as real customers.
- Weekly nights: Dough school (kids six to twelve, Tuesday 4.30 pm), The long table (Thursday 7 pm), Quiz and a pie (Sunday 6 pm) (nights).
- Group and food policies: groups "up to twenty-four ... any night but Thursday", a gluten-free base, dogs welcome, delivery "within a mile" "from five o'clock", dough balls £2 each (FAQ).
- Address and neighbouring street: the street name and number 14 (also drawn big in Find me) and Lime Row (menu, corner, footer).
- Reply promise: "We answer the same day" (contact).

## Known limits
- Without JavaScript the menu button cannot open the menu, the request form has no sending code, and the logo and Instagram button stay cream over the cream bands; the pies and footer links stay reachable.
- The dough and the house rule sections are held for a long scroll, which feels slow on a short screen; with reduced motion or without JavaScript the dough frame shows only the last of its five photos.
- The rule line is set very large; long replacement text needs a matching --len or it will overflow on phones.
- The photo in the house rule section and the many decorative rings carry no information; the rings have no alt text and are hidden from screen readers.
- gsap, ScrollTrigger and Lenis load from jsDelivr at the end of the body; if the CDN is blocked the page shows without motion and smooth scrolling.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Monella left only in class names.
