# AGENTS.md: toy store website template

One-page website for an independent toy shop and its workshops, repairs and gift lists. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/toy-store-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/toy-store-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/toy-store-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/toy-store-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:navigation`: `.nav__menu` `.nav__close` `.nav__links`
  - `section-script:tinker`: `.tk-run` `.tk-ribbon` `.tk-session` `.tk-card`
  - `section-script:swap`: `.sw-frame` `.sw-notes` `data-x` `data-y`
  - `scene:opening`: `.op-board` `.op-tile` `.op-stage`
  - `scene:shelves`: `.sh-view` `.sh-track` `.sh-list` `.sh-photo`
  - `scene:squad`: `.sq-deck` `.sq-card`
  - `scene:tinker`: `.tk-run` `.tk-ribbon` `.tk-ball` `.tk-session` `data-stops`
  - `scene:swap`: `.sw-frame` `.sw-lens` `.sw-notes` `data-x` `data-y`
  - `scene:gifts`: `.gf-card` `.gf-burst` `.gf-sticker`
  - `scene:shop`: `.sp-front` `.sp-shutter`
  - `scene:contact`: `.ct-list` `.ct-item`
- `style="--len:N"` = characters in that display line, spaces included: `squiggle` is 8.
- The 3 by 3 puzzle is nine .op-tile elements, each showing one ninth of the same photo through its --c and --r custom properties; the scene reads the grid's column count and the position of the tiles, and the ninth tile (class op-tile--last) is the one that drops in last. To change the photo, change the src on all nine images; keep nine tiles in a 3 by 3 grid.
- The wordmark "squiggle" in the footer is sized by style="--len:8", the number of characters of the word; update it when you rename the shop.
- The ribbon in the tinker section is built by section-script:tinker from the position of the cards, and the ball and the lit sessions follow its stops. Keep the order of sessions and one ribbon path in .tk-run; it redraws itself when you change the number of cards, but the zigzag rows are set by nth-child rules for four cards only, so a fifth card needs its own grid-row rule.
- The notched corners (.u-notch) are drawn with a clip-path: shape() outline; browsers without shape() show a whole rounded card with the tab set inside. The swap lens reads each note's data-x and data-y (percent of the photo) as its spots.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #ffffff (page background, form fields, the number discs in the gift steps, text on cobalt), `--color-2` #24201c (text on every light ground, field borders and the outline of the Menu button), `--color-3` #fde77d (hours card, contact card, one ground of the tester and workshop cards, the plus discs in the questions, first shutter), `--color-4` #f7aacb (default pill button, gifts card and address card, some badges and card grounds, open question border, second shutter, lens ring), `--color-5` #a9c34c (opening text card, some badges and card grounds, third shutter, tabs of workshops the ball has not reached), `--color-6` #2d47c6 (cobalt buttons (Start a list, Get directions, Send it), the cobalt badges (Puzzles, Wind-up repairs, Open), the ribbons, fourth shutter, focus ring), `--color-7` #f48a3a (orange badges, the age and date tabs, the ball that rolls down the workshop ribbon), `--color-8` #fbdde9 (repair card, one ground of the tester and workshop cards, photo placeholders, outlines of the logo pill, the link bar and closed questions, footer rule, open question fill); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, map, phone, email, form): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Plan a visit button in the opening: now #contact; owner's target: keep it on the contact section, or point it to your booking or visit page.
- Meet the Test Squad link in the opening: now #squad; owner's target: keep it, or change it if you rename or remove the testers section.
- Start a list button in the birthday lists section: now #contact; owner's target: your gift-list or wishlist page, or keep it on the contact form.
- Get directions button in the shop section: now a Google Maps search for Brighton; owner's target: the Google Maps link of your shop.
- Phone link in the contact section: now a tel: link to a placeholder number; owner's target: your shop phone in tel: form (+44...).
- Email link in the contact section: now a mailto: link to a placeholder address; owner's target: your shop email.
- Send it button of the contact form: now a form with action="#" that sends nothing; owner's target: your form endpoint (Formspree, Netlify Forms) or remove the form and keep the phone and email.
- The form in `#contact` (fields `name`, `email`, `message`) sends nothing. Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it.
- The name Squiggle (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (23, Unsplash: opening 1, shelves 6, squad 5, hospital 2, tinker 4, swap 1, gifts 2, shop 2): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Shop identity: independent toy shop, two floors in the North Laine, Brighton; Squiggle Toys Ltd (opening, shop, footer, meta description).
- The promise and the process: "No toy gets a shelf until a kid has tried to break it", a squad that takes new toys home "every month", toys dropped if they bore, snap or vanish "within a week" (opening, squad).
- Test Squad: Rosa 6, Theo 3, Amara 9, Lily 5, Jonah 10 with roles and quotes; the photos are stock pictures of children (squad). Never use real children's names or photos without permission.
- Shelf categories and example ranges, such as jigsaws from 12 to 1,000 pieces (shelves).
- Repair prices and timing: Re-stuffing £8, New eyes or buttons £5, Torn seams from £6, Wind-up repairs from £10, Wheels and axles £6; Saturday mornings; "most patients go home within a week" (hospital).
- Tinker table: every Saturday at ten, free, no booking, ages five and up, twelve seats, children under eight need a grown-up; four sessions with dates 12 Oct, 19 Oct, 26 Oct and 2 Nov (tinker, FAQ). The dates carry no year and need updating.
- Swap box rules: clean, working, all or most pieces, credit never expires, no soft toys for swapping (swap, FAQ); the three toy stories, including a rubber-headed boy, a tin airliner from Hove and twins with a pink coach (swap).
- Birthday list service: friends buy from the list in the shop or by phone; every present wrapped and tagged; the sticker "Wrapped free in our own paper" (gifts).
- Opening hours: Monday to Friday 9:30 to 18:00, Saturday 9:00 to 18:00, Sunday 10:30 to 16:30, and "Every day of the week" (shop, contact).
- Postage and vouchers: posts anywhere in the UK, payment link sent by phone or email; gift vouchers from £10 that never expire; the toilet is upstairs, past the puzzles; the play table upstairs; "try me" tags (FAQ).
- Place and contact: address, postcode, phone and email are placeholders (1 Example Street, 01632 000 000, hello@squiggle.example); the North Laine and Hove are real places in Brighton and Hove (shop, swap).
- Footer: "© 2026 Squiggle Toys Ltd · 1 Example Street, Brighton BN1 0ZZ": put in your legal name and address.

## Known limits
- Without JavaScript the Menu button on phones cannot open the overlay (wide screens show the links); the tinker ribbon does not appear because its path is drawn by a script, and the orange ball sits alone below the last card; the form still needs an endpoint.
- The contact form has no handler: it posts to "#" and shows no thank-you line, so connect Formspree or Netlify Forms, or remove it.
- The workshop dates carry no year and their weekdays fit 2024, not 2026; update them before publishing.
- The opening and the shelves hold the screen while you scroll (about 170svh of scroll for the puzzle, the width of the row for the shelves); on very short screens the held card and board can feel tight.
- GSAP, ScrollTrigger, MotionPathPlugin and Lenis load as four synchronous scripts from jsDelivr at the end of the body; the swap section shows one 1390 px photo twice (page and lens, one download).

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Squiggle left only in class names.
