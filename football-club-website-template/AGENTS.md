# AGENTS.md: football club website template

One-page website for a volunteer-run youth football club, for parents looking for a team. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/football-club-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/football-club-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/football-club-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/football-club-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `scene:squads`: `.squads__deck` `.squads__card`
  - `scene:week`: `.week__stage` `.week__rail` `.week__big` `.week__day`
  - `scene:promises`: `.promises__item` `.promises__band`
  - `scene:coaches`: `.coaches__row` `.coaches__name` `.coaches__first` `.coaches__last` `.coaches__photo`
  - `scene:join`: `.join__steps` `.join__step` `.join__num` `.join__title` `.join__text`
  - `scene:fees`: `.fees__stage` `.fees__field--2` `.fees__col--1` `.fees__col--3`
  - `scene:contact`: `.contact__rows` `.contact__row` `.contact__text` `aria-hidden`
  - `section-script:nav`: `.nav__menu` `.menu__close`
  - `section-script:contact`: `.contact__form` `.contact__status`
- `style="--len:N"` = characters in that display line, spaces included: `Everybody plays.` is 16, `No trials under 13.` is 19, `First kit is free.` is 18, `Coaches who stay.` is 17, `Come and play.` is 14, `First session free.` is 19, `See you Saturday.` is 17, `Kilnfield` is 9.
- The promise lines, the three contact rows and the footer wordmark each have style="--len:N" equal to their character count; CSS sizes the type from it, so update N when you change the words.
- Each week day holds its own huge day name (.week__big, aria-hidden) and each join step its own .join__num inside the item, so copy a whole item to add a day or step. scene:week measures the rail, so more days lengthen the pin; the join steps sit in a 4-column grid (2 columns up to 1080 px), so a fifth step starts a new row.
- The fees section is three coloured columns: scene:fees scales the black middle field (.fees__field--2) and slides the text of the outer columns; the orange and cream fields stay put, and all three colours come from the CSS variables.
- Each fixture's time element has a datetime attribute; update it together with the visible text.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #141414 (text on the light pages and on orange, the black sections (opening, week, coaches, fees, contact, footer), the dark squad and quote cards, the button marks), `--color-2` #ff4d1f (signal orange: the nav mark, the main button, the promises and join sections, one squad card, two quote cards, the first fee column, the first contact row, week day labels, the form status line), `--color-3` #ece6d8 (cream: text on the black sections, the questions section, the third squad card, the third fee column, button hover text), `--color-4` #f6f3ec (page background, the nav bar, and the fill that sweeps across the dark button on hover), `--color-5` #5c5a55 (intro paragraphs and table heads on light grounds, and the tone behind photos before they load), `--color-6` #a7a194 (quieter text on the black sections (club line, intros, roles, labels) and the underline of form fields); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, email, form, phone, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- "Free session" button in the nav: now #contact; owner's target: your session booking page, or keep #contact once the form is connected.
- "Find your squad" button and "Read our four promises" link in the opening: now #squads and #promises; owner's target: keep as they are.
- "Ask about a bursary" button in the fees section: now mailto: with a placeholder address; owner's target: your own email, or a page with a bursary form.
- Instagram, Facebook and YouTube links in the footer: now the home pages of the networks; owner's target: your club's profile pages, or remove what you do not have.
- "Volunteer with us", "Safeguarding" and "Privacy" links in the footer: now #contact, #faq and #contact; owner's target: your volunteer page, safeguarding policy and privacy policy.
- Phone and email links in the contact section: now tel: and mailto: with placeholders; owner's target: your real number and address.
- Booking form in the contact section: now action="#": nothing is sent, the script only shows a thank-you line; owner's target: a form service address (Formspree, Netlify Forms).
- The form in `#contact` (fields `child`, `squad`, `email`, `phone`) sends nothing; `section-script:contact` validates it and shows the thank-you text. Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Kilnfield Colts FC (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (16, Unsplash: opening 1, squads 4, week 7, coaches 4): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Club identity: name, Armley in Leeds, founded 1987, 480 boys and girls aged five to eighteen, "nobody is cut", "run by volunteers since 1987" (opening, promises, footer, meta description).
- Squads: names, age ranges, training days and times, formats (4 v 4, 7 v 7 to 9 v 9, 11 v 11), six girls-only teams, two levels in the youth section (squads, week, FAQ).
- Weekly programme: floodlights six nights a week, Girls' night until nine, Keeper school for under 9s up, forty minis on four pitches, Thursday boot swap, Friday futsal for under 13s and up, fourteen home games on Saturdays from nine till two (week).
- Promises: equal minutes up to under 12 and at least half a match after, no trials under 13, free first kit of shirt, shorts and socks, coaches staying at least two seasons (promises, squads, FAQ).
- Fixtures: the dates 11 and 12 October, eight teams, opponents, kick-off times, pitches and the ground (fixtures); update the datetime attributes with the visible text.
- Coaches: names, roles, licences (UEFA C, UEFA B, FA Introduction to Coaching, FA Level 2 goalkeeping), years coaching, the quotes, thirty-two volunteers, FA badges, safeguarding certificates, DBS checks, two adults at every session (coaches, FAQ). The portraits are stock photos of real people and their alt texts name them.
- Joining: first session free, no forms or fee, about two weeks to the first match, loaned boots, bibs and shin pads (squads, join, FAQ).
- Fees: £12, £18 and £22 a month, what each includes, "nothing is added on top", one in five on a bursary (fees).
- Parent and volunteer quotes with names and roles, and the claim of a daughter captaining the under 11 girls in two seasons (voices).
- Ground and hours: Kilnfield Recreation Ground, Example Lane, Armley, Leeds LS0 0AA (street and postcode are placeholders), clubhouse hours on weekdays, Saturday and Sunday, tea hatch opening at nine, a covered stand (contact, FAQ).
- Opponents named in the fixtures (Stanningley Wasps, Gotts Park Rangers, Wyther Vale and others) and the league app mention (fixtures).
- Contact: reply within a day with a time and the coach's name; phone, email and bursary email are placeholders (contact, fees).

## Known limits
- Without JavaScript the menu button cannot open the overlay on narrow screens, the quote row does not loop and the form sends nothing; the FAQ still opens.
- The booking form has action="#" and nothing is sent; connect a form service before publishing.
- The week track pins the section and the deck and the join steps pin from 1081 px; each pin adds scroll length, so the page is long on desktop.
- The huge day names in the week track are decorative and hidden from assistive technology; the day label in each card carries the information.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Kilnfield Colts FC left only in class names.
