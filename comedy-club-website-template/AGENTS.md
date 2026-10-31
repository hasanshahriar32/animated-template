# AGENTS.md: comedy club website template

One-page website for a comedy club, theatre or small venue with a weekly programme, a bar and private hire. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/comedy-club-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/comedy-club-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/comedy-club-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/comedy-club-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:nav`: `.nav__menu` `.menu` `.menu__close`
  - `section-script:openmic`: `.om__form` `.om__status` `data-invalid` `data-sent`
  - `scene:week`: `.wk__row`
  - `scene:rules`: `.rl__item` `.rl__old` `.rl__strike` `.rl__new`
  - `scene:alumni`: `.al__stage` `.al__track` `.al__line` `.al__comic` `.al__pic`
  - `scene:bar`: `.br__pin` `.br__row` `.br__card` `.br__lean` `.br__pic`
  - `scene:reviews`: `.rv__grid` `.rv__item` `.rv__face` `.rv__brush`
  - `scene:visit`: `.vs__blob` `.vs__word`
- `style="--len:N"` = characters in that display line, spaces included: `Snort` is 5.
- The wordmark in the visit section is sized from style="--len:5", the number of characters in the name: update it if you rename the venue.
- The week rows and the bar cards are laid out by CSS grids and read by their scenes, so they take any number of items; the alumni line-up is a row of five portraits that the spotlight walks along, so check the layout if you change the count.
- The struck-through rules, the arrows beside headings and the brush underlines are inline SVG and CSS, not images: recolour them through the colour variables in :root.
- Photos are hotlinked Unsplash images with a placeholder background colour set inline on each; replace the src, alt text and the background colour together.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #ffd20a (page ground behind the week, open mic, hire and visit sections, the nav bar, the yellow buttons and the hover fill of the dark ones, and headings and names on dark sections), `--color-2` #141414 (text and borders on light grounds, the first-screen panel, house rules, alumni, reviews, footer and menu overlay grounds, and the dark buttons), `--color-3` #ffffff (grounds of the room, bar and FAQ sections, text on dark grounds, the menu link hover colour and the hover fill of the yellow buttons); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, phone, email, form, map, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Book tickets button in the phone menu overlay: now #week (the programme); owner's target: your ticketing page.
- Book tonight button on the first screen: now #visit (the address and box office phone); owner's target: the ticket page for tonight's show.
- Book buttons on the seven night rows in the week section: now #visit for Tuesday, Wednesday, Friday, Saturday and Sunday, #openmic for Monday, #tonight for Thursday; owner's target: one ticket page per night, or one booking page for all seven.
- Ask about a date button in the hire section: now a mailto link to hire@snort.example; owner's target: your private hire enquiry address or form.
- Call the box office button in the visit section: now tel:+441130000000; owner's target: your box office phone number.
- Directions link in the visit section: now a Google Maps search for Leeds; owner's target: a Google Maps link to your venue.
- Instagram, TikTok and YouTube links in the footer: now the home pages of the three networks; owner's target: your profile addresses.
- Newsletter link in the footer: now a mailto link to hello@snort.example with the subject Newsletter; owner's target: your newsletter sign-up page.
- The form in `#openmic` (fields `name`, `email`, `line`) sends nothing; `section-script:openmic` handles its submit in the page (read it before you connect a service). Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Snort (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (29, Unsplash: opening 1, week 7, room 2, openmic 1, alumni 5, bar 6, hire 1, reviews 6): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Club facts: 164 seats, a railway arch in Leeds, shows seven nights a week, 18+ with ID at the door, a bar open till two (title, meta description, room, footer, faq).
- Tonight's show: Thu 16 Oct, doors 19:30, The Late Show at 20:00, £14, "23 seats left", four acts with start times and descriptions (opening).
- Programme: seven shows with days, times and prices from £3 to £20, including two Saturday shows at 19:00 and 22:00 (week).
- Room details: nine metres to the mic, a train over the arch at 21:12 every night, a low brick vault (room); step-free entrance, four wheelchair spaces, an accessible toilet and a hearing loop (faq).
- Policies: phones locked in a pouch at the door, unallocated seats with doors half an hour before the show, tickets swapped up to 24 hours before, refunds the same day if the show is cancelled, no crunchy food during a set (rules, faq).
- Open mic: twelve spots every Monday, five minutes each, a date within three weeks, a light at four and a half minutes (openmic).
- Alumni: five named comics with first-gig years from 2014 to 2018 and their later careers (alumni); the portraits are stock photos of real people.
- Bar: six items with names, descriptions and prices (£5.40 to £10), a house pale ale brewed two streets away, food served until 21:00 and after the show, table service that stops when the MC walks on (bar, faq).
- Private hire: from £600 for the room Sunday to Wednesday, from £1,400 for a private show, £45 a head for a team workshop, what each includes (hire).
- Reviews: six quotes with first names and the show attended; replace with real reviews (reviews).
- Address: "Arch 1, Example Wharf, Leeds LS1 0AA", box office 0113 000 0000 (Tuesday to Sunday from 17:00), three email addresses and the walking route from the station are placeholders (visit, footer, openmic).
- Company name "Snort Comedy Club Ltd" and "An independent comedy club in a railway arch in Leeds" (footer).

## Known limits
- Without JavaScript the Menu button cannot open the overlay. On phones the five bar links are hidden, so the footer links (five sections) are the only fallback navigation.
- The open-mic form only checks the fields and shows a message; it sends nothing until you connect a form service or remove it.
- The bar pins the screen for its sideways track at every width, and the alumni section holds for about 1.8 screens on screens wider than 900 px, which can feel long on short laptop screens.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Snort left only in class names.
