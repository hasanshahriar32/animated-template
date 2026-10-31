# AGENTS.md: language school website template

One-page website for a language school or evening class provider, for adults who want to start or return to a language. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/language-school-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/language-school-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/language-school-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/language-school-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:navigation`: `.nav-menu` `.nav-close`
  - `scene:languages-track`: `.lg-stage` `.lg-viewport` `.lg-track` `.lg-panel` `.lg-shape`
  - `scene:levels-meter`: `.lv-meter` `.lv-level` `.lv-fill` `.lv-code`
  - `scene:trial-pile`: `.tr-pile` `.tr-piece` `.tr-panel`
  - `scene:overheard-thread`: `.oh-stage` `.oh-window` `.oh-thread` `.oh-line` `.oh-face` `.oh-bubble`
  - `scene:contact-bubble`: `.ct-bubble` `.ct-ground` `.ct-tail`
- `style="--len:N"` = characters in that display line, spaces included: `¡Hola!` is 6, `Bonjour!` is 8, `Ciao!` is 5, `Hallo!` is 6, `Olá!` is 4, `Konnichiwa!` is 11, `Annyeong!` is 9, `Marhaba!` is 8.
- Each greeting in the language panels has style="--len:N", the number of characters (for example 6 for "¡Hola!"): update it when a greeting changes.
- Each level bar has style="--lv-step:N" from 1 to 5, which sets how much of the bar is filled (a larger step fills more); the levels scene animates every .lv-fill it finds.
- The shapes (circles, scallops, rings, bars) are CSS and one SVG symbol, not images: recolour them through the colour variables in :root.
- The page has no copyright line; the credit link is added after the address line in the footer.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #ffffff (page background, the pill behind the nav bar once scrolled, level code tags, the circles holding the price shapes, text on dark panels), `--color-2` #4a231c (all main text, the menu overlay, the trial panel, the dark language panels, the Private lessons row, the C1 level bar, the button hover fill), `--color-3` #fcefe2 (the cream ground and tail of the closing speech bubble), `--color-4` #f4783a (orange panels, price row, level 3 bar, day pill and chat bubble), `--color-5` #f7c744 (the main button fill, the logo mark, the FAQ plus circle, yellow panels, pills and bubbles), `--color-6` #24804f (green panel, level 4 bar, day pill and chat bubble), `--color-7` #f49cb0 (pink panel, level 1 bar and chat bubble), `--color-8` #6fa8f2 (blue panel, price circle shape, day pill and chat bubble), `--color-9` #6e625c (small captions, level descriptions, the thread and FAQ leads, contact labels), `--color-10` #8c807a (the second half of the closing statement before it inks in), `--color-11` #e9ddd5 (hairlines between rows and questions, placeholder behind photos, the trial panel's paragraph); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, email, phone, social): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Book a free class buttons in the nav, the menu overlay and the first screen: now #trial; owner's target: your trial booking page, or keep #trial.
- Book a free class buttons in the trial and closing sections: now a mailto: link with the subject "Free class"; owner's target: your trial booking page or form.
- Book a place, Book a lesson and Get a pass buttons in the prices: now mailto: links with the subjects "Group course", "Private lessons" and "Club pass"; owner's target: your checkout, booking or enrolment pages, one per option.
- Phone and email links in the contact details: now a tel: link and a mailto: link with placeholder values; owner's target: your real phone number and email address.
- Instagram, Facebook and YouTube buttons in the footer: now the home pages of the three sites; owner's target: your own profiles, or remove the ones you do not use.
- The name Saylo (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (7, Unsplash: week 2, testimonials 5): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Location and contacts: 1 Example Street, Leeds LS1 0AA, "two minutes from the station", phone 0113 000 0000, hello@saylo.example (title and meta description, contact, footer).
- Languages and timetable: eight languages with days, times and level ranges, for example Spanish Mon and Wed at 18:30 and 20:00, A1 to C1, online too (languages).
- Courses and levels: five levels, about ten weeks each, ninety-minute classes twice a week at 18:30 and 20:00, groups of six at most (levels, week, prices, faq).
- Prices: Group course £260 a course, Private lessons £38 an hour, Club pass £45 a term, "Prices include materials" (prices).
- Clubs and walks: Friday conversation clubs from six at a named café on Call Lane, a Saturday market walk from ten till twelve at Kirkgate Market (week).
- Hours: front desk Mon to Thu 10:00 to 21:30, Fri 10:00 to 18:00, Sat 10:00 to 13:00 (contact).
- Promises and policy: a free class before paying, every class streams online, missed classes can be made up in another group, "nobody corrects you unless you ask" (trial, week, faq).
- Teachers: people who grew up speaking the language, trained by the school, most have lived in Leeds for years (faq). No teacher is named.
- Students and quotes: Hannah, Tom, Priya, Daniel and Sam with their sayings, languages and stages; the portraits are stock photos of real people (testimonials).
- Company courses: courses for teams in the client's office or the school's (faq).
- School and city: "Saylo Language School" and Leeds (title, meta description, footer).

## Known limits
- Without JavaScript the menu button does nothing on phones, so the section links are not reachable there except through the footer, which repeats the same four.
- Without JavaScript the language track stays one clipped row (the data-track attribute is in the markup and only a script removes it), so the panels past the screen edge cannot be seen or scrolled to; with reduced motion they show as a grid.
- The pinned language track and the pinned chat thread are long on a phone: the track is the full width of eight panels and the thread holds for 2.5 screens.
- The five student portraits are stock photos of real people with first names as alt texts: replace them with your own students' photos, with their consent.
- GSAP, ScrollTrigger, SplitText and Lenis load from a CDN at the end of the body.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Saylo left only in class names.
