# AGENTS.md: interior design website template

One-page website for an interior colour studio or interior designer, with a method, projects, paints, fixed prices and a contact form. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/interior-design-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/interior-design-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/interior-design-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/interior-design-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `scene:method`: `.method__tile` `.method__tile--petals` `.method__petal` `.method__tile--arrow` `.method__arrow` `.method__tile--socket` `.method__ring` `.method__tile--rings` `.method__rings` `.method__tile--photo` `.method__tile--plus` `.method__plus` `.method__tile--halves` `.method__half` `.method__tile--stars` `.m-spark` `.method__tile--text` `.method__fill`
  - `scene:alphabet`: `.alphabet__g` `.alphabet__entry` `.alphabet__letter`
  - `scene:rooms`: `.rooms__sheet` `.rooms__stage` `.rooms__photo`
  - `scene:voices`: `.voices__badge` `.voices__rings` `.voices__shape` `.voices__w1` `.voices__w2`
  - `scene:prices`: `.prices__row` `.m-rule` `.prices__pill` `.prices__head`
  - `scene:paints`: `.paints__track` `.paints__deck` `.paints__card` `.paints__mark`
  - `scene:light`: `.light__wall` `.light__sun` `.light__lamp` `.light__hour`
  - `scene:sittings`: `.sittings__chain` `.sittings__slide` `.sittings__line` `.sittings__pip`
  - `scene:contact`: `.contact__title` `.contact__l` `.contact__g` `.contact__l--j` `.contact__dot`
  - `section-script:contact`: `.contact__form` `.contact__status`
  - `section-script:nav`: `.nav__menu` `.nav__close`
- `voices` directly above `prices`: the animation crosses that border and stops if they are split.
- `style="--len:N"` = characters in that display line, spaces included: `Colour first` is 12.
- The contact word "Bonjour" is split into one span per letter with style="--len:7" (the character count); change both together if the word changes. The Colour first pair has style="--len:12".
- The Sittings section is drawn for four: the SVG chain places four rings at fixed cx positions (150, 383, 617, 850) with per-ring colours set by nth-child in the CSS, and the steps grid has four columns; to change the number, edit the rings, their colours and the steps together.
- The tiles, rings, petals, sparkles, the sunlit wall and the lamp are CSS and SVG, not images: recolour them through the five colour variables in :root (near-white, periwinkle, pink, lime, ink blue).
- The six paint cards each take their colour from a class (paints__card--pervenche, --bonbon and so on); rename the class and its colour rule together.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #f6f6f9 (page ground, navigation bar, and text on the periwinkle bands and the menu overlay), `--color-2` #5767c2 (body text and headings, hairline rules, the quote, price and sittings bands, the menu overlay and the daylight wall), `--color-3` #fbb3c9 (glossary letter discs, the plus and ring tiles, the hover dot on buttons, one paint card, the open question icon), `--color-4` #dde833 (the Commissions and form buttons, price pills, the opening text tile's fill, one paint card and the daylight lamp), `--color-5` #242b68 (text on lime and pink surfaces, form text, the opening button, focus outlines and the darkest paint card); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, form, email, phone, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Book a colour walk buttons in the first section and in the Commissions heading: now #contact; owner's target: your online booking page, or keep #contact once the form is connected.
- See the rooms tile in the first section: now #rooms; owner's target: keep, or a page with your full portfolio.
- Contact form (Send a note): now action="#": it checks the required fields and shows a thank-you line, nothing is sent; owner's target: your form service (Formspree, Netlify Forms) or your own endpoint.
- Instagram and Pinterest links in the footer: now the home pages https://www.instagram.com/ and https://www.pinterest.com/; owner's target: your own profile addresses.
- The form in `#contact` (fields `name`, `email`, `room`, `message`) sends nothing; `section-script:contact` validates it and shows the thank-you text. Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Pervenche (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (7, Unsplash: method 1, rooms 6): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Prices: Colour walk €280, One-room drawing €1,900, Light score €850, Whole-home specimen from €7,400, "Fixed prices, written down before we start" and "bought at cost and never marked up" (prices).
- Location and address: Lyon (title, meta description, nav, footer), "1 Example Street, 69000 Lyon, France" (contact, footer), phone +33 4 00 00 00 00 and bonjour@pervenche.example are placeholders.
- Hours and replies: "Tuesday to Saturday, 10 to 6" (contact), "Replies within two days" (contact strip and thank-you line), "Studio visits by appointment" (menu, contact strip).
- Projects: Salon Grenadine, Lilac attic, Pâtisserie Mauve, Teal guest room, Café Lilas, Velvet duplex, with towns (Lyon, Annecy, Grenoble, Valence, Geneva) and years 2023 to 2025 (rooms).
- Client quotes and names: Inès and Paul, Clara Morel, Salomé Roux, with their projects (voices).
- Process promises: four meetings "never more", three weeks from the first sitting to the specimen sheet and two more for the painters, swatches a metre square on your walls, a tin of every shade left behind (sittings, faq, paints).
- Service area: colour walks "within two hours of Lyon by train", drawings and light scores made remotely from photos, plans and a video call (faq).
- The paints: six house paints mixed in Lyon from three pigments, each with a pairing; sold only within a commission (paints, faq).
- Colour walk contents: two hours in your rooms and a written palette (prices, sittings); the Light score covers lamps, colour temperatures, dimmers and switch positions (prices).
- Studio claims: "Created with patience in Lyon" and "Our blue, and our name" in the glossary entry for Pervenche (footer, alphabet).
- Project names such as Salon Grenadine, Pâtisserie Mauve and Café Lilas read like real businesses: replace them with the studio's own projects (rooms, voices).

## Known limits
- Without JavaScript the Menu button cannot open the overlay and the form posts back to the page instead of showing the thank-you line; on phones the top links are hidden, but the footer repeats Method, Rooms, Paints, Prices and Questions.
- The A to Z wall and the sunlit wall are decorative and hidden from screen readers; the glossary and the hour list carry the content.
- On phones the daylight wall sits above its text, so it has scrolled away by the time the Night line is read, and the ring chain is small (about 90 px rings).
- The alphabet wave stretches letters only to 85% width, because only that part of the font's width axis is loaded.
- Fonts and GSAP load from Google Fonts and jsDelivr, so a first visit needs a network connection.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Pervenche left only in class names.
