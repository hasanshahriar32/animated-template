# AGENTS.md: group fitness website template

One-page website for a group fitness studio with a class timetable and passes. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/group-fitness-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/group-fitness-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/group-fitness-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/group-fitness-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:nav`: `.nav__menu` `.menu__close`
  - `section-script:opening`: `.op__s1`
  - `scene:opening`: `.op__s2` `.op__sky` `.op__frame` `.op__half--a` `.op__half--b` `.op__copy` `.op__actions` `.op__dusk` `.op__st` `.op__sun` `.op__gap` `.op__line` `.op__snap--a` `.op__snap--b`
  - `scene:classes`: `.cl__list` `.cl__row` `.cl__band` `.cl__label` `.cl__pic` `.cl__meta`
  - `scene:arc`: `.arc__stage` `.arc__line` `.arc__sun` `.arc__phase`
  - `scene:room`: `.rm__pile` `.rm__shot`
  - `scene:coaches`: `.co__stage` `.co__track` `.co__card` `.co__sun` `.co__photo`
  - `scene:rewind`: `.rw__word` `.rw__pics` `.rw__pic--1` `.rw__pic--2`
  - `scene:regulars`: `.rg__board` `.rg__quote`
  - `section-script:contact`: `.ct__form` `.ct__done`
- `style="--len:N"` = characters in that display line, spaces included: `Rewind` is 6, `Highkick` is 8.
- The wordmark in the footer and the word "Rewind" are sized from an inline --len on the element (8 and 6, the number of characters); set it to the length of your own word so it keeps filling the width.
- The stickers, the striped suns, the curve and the sun in the arc section are inline SVG and CSS shapes, not images: recolour them through the colour variables. The arc curve is one SVG path that the sun follows, so a new curve must be a single path.
- The opening scene reads the offsets of the second screen, the sky and the photo frame, and the coaches scene pins for the width of the row; keep the structure of those blocks when you change their content.
- The timetable lists the days in separate columns; add or remove slots inside a day freely, the stamp effect presses whatever is in each list.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #f3f3f2 (page background, upper half of the opening, the gridded timetable ground and the contact section), `--color-2` #111014 (text, every border and offset shadow, and the near-black ground of the arc and Rewind sections), `--color-3` #e7d9ea (lilac ground of the classes, coaches and passes sections, the quote board and the second opening screen's dusk), `--color-4` #eda2cf (pink ground of the room, quotes and footer, the opening floor, the phone menu and the button hover stripes), `--color-5` #f2913e (orange in the striped suns, the dot that rides the arc, three disc and arc stickers, the triangle sticker's gradient and a ghost behind the Rewind word), `--color-6` #d8df3d (lime: default button fill, class band, badges, highlighted cards, the curve and the headings on near-black grounds), `--color-7` #84ade0 (blue cards, two arc stickers, the footer wordmark's second shadow and a ghost behind the Rewind word), `--color-8` #0b8f6c (green, the fill of the zigzag sticker in the passes section), `--color-9` #ffffff (nav pill, photo frames, form fields, white cards and text on the near-black sections); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, form, phone, email, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Free class button in the top bar, Book a free class (opening), Book a class (timetable and drop-in), Get the ten-pack, Go unlimited and Get on the list buttons: now #contact, the free-class form near the end of the page; owner's target: your booking or membership page (Mindbody, Glofox, Momence) if you use one, or keep #contact once the form is connected.
- See the timetable button in the opening, See the passes link in the timetable: now #week and #passes; owner's target: keep them.
- Phone and email links in the contact section and footer: now a tel: link and a mailto: link to the demo values; owner's target: your studio's phone as tel:+44... and your email.
- Instagram and TikTok links in the footer: now the instagram.com and tiktok.com home pages; owner's target: your profile addresses.
- Book my free class button in the contact form: now validates the form, shows a thank-you line and resets it; nothing is sent; owner's target: a form service (Formspree, Netlify Forms) or your booking system.
- The form in `#contact` (fields `name`, `phone`, `email`, `class`, `day`, `note`) sends nothing; `section-script:contact` handles its submit in the page (read it before you connect a service). Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Highkick (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (21, Unsplash: opening 3, classes 7, room 5, coaches 4, rewind 2): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Studio identity: "Since 1986" and "Sweat like it's 1986" (opening, coaches, footer); Bev "has taught step since 1986" (coaches).
- Place and contact: First floor, Calder Mill, 1 Example Street, Leeds, the phone 0113 000 0000 and hello@highkick.example (contact, footer) are placeholders; put in the real ones.
- Desk hours: Mon to Fri 6:30 to 21:00, Sat 8:30 to 13:00, Sun 9:30 to 12:30 (contact).
- Classes: seven classes with durations, levels and descriptions, "32 spots a class" (opening, classes, room); the classes line says every class runs fifty minutes or less while Skate Fit is listed at 60 minutes, so make them agree.
- Timetable: 22 slots over seven days with times, classes and coach names (timetable); the page says "Twenty-four classes" in the timetable line, so make the line match your real count.
- Booking rules: bookable seven days ahead, cancel up to two hours before, 32 spots (room, timetable).
- Passes and prices: Drop-in £12, Ten-pack £95 valid four months, Unlimited £59 a month with Rewind Fridays at half price, no joining fee, 20% off for students and over-65s (passes).
- Free first class: "Your first class is on us" and "First class free" (contact, passes, nav).
- Rewind Fridays: the last Friday of the month, next date "Friday 30 October", 7 pm to 10 pm, over-18s, £8 with skates, £4 for Unlimited members (rewind); the date is fixed text and will go out of date.
- Room claims: sprung maple floor, mirrors on two walls, a speaker stack, ceiling fans, showers and lockers free with every class, an old wool mill (room).
- Coaches: Dani Reyes ("Boxed for Yorkshire at nineteen"), Marco Bell, Bev Okafor, Theo Lund with their classes and one-line biographies (coaches); the portraits are stock photos.
- Member quotes: Priya ("in 2019"), Joe, Hannah, Carol ("sixty-one"), Sam, invented for the demo (regulars).
- Footer: "© 2026 Highkick Studio Ltd" and "Made loud in Leeds" — put in your legal name and city.

## Known limits
- GSAP, ScrollTrigger, MotionPath and Lenis load as four separate jsDelivr scripts at the end of body, without defer; the motion scripts after them need them, and if the CDN fails the page stays static.
- Without JavaScript the menu button cannot open its overlay (an attribute hides it), so at 960 px and below there is no navigation, and the form posts to #contact instead of showing its thank-you line; the content stays visible and the nav links stay reachable on wide screens.
- The free-class form sends nothing: the button only shows the thank-you line, so connect a form service or your booking system before publishing.
- The coaches row is pinned while it slides sideways on every screen size, and on a phone the cards are 74% of the screen width, so the pinned scroll is long; the arc screen is pinned for a screen and a half.
- The timetable line says twenty-four classes while the columns hold 22, and the Rewind date is fixed text; both need your own numbers.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Highkick left only in class names.
