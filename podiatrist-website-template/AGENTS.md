# AGENTS.md: podiatrist website template

One-page website for a podiatry clinic or small health practice that takes bookings and home visits. One file, `index.html`, with inline CSS and scripts (GSAP, ScrollTrigger, Lenis from jsDelivr); no build step, and none is needed for copy, colour or photo edits.

## Files
Edit these files, not a page fetched by URL (that arrives as a summary).
```bash
curl -LO https://raw.githubusercontent.com/8bsite/podiatrist-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/podiatrist-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/podiatrist-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/podiatrist-website-template/main/CREDITS.md
```
Upload `index.html`, LICENSE and CREDITS.md; not this file, README.md or `previews/`.

## Keep
- Every `id`, `data-8b-section`, `data-8b-motion` and `data-8b-part` (`section:<id>` styles, `scene:<id>` animation).
- Selectors the scripts use:
  - `section-script:nav`: `.nav__menu` `.nav__sheet` `.nav__close`
  - `section-script:faq`: `.fq-item`
  - `section-script:contact`: `.ct-status` `data-sent` `data-missing`
  - `scene:visit`: `.vi-step` `.vi-grid` `.m-text-6` `.vi-circle`
  - `scene:conditions`: `.co-photo` `.co-row`
  - `scene:gait`: `.ga-stage` `.ga-track`
  - `scene:stories`: `.st-quote` `.st-word`
  - `scene:home`: `.ho-ring` `.ho-photo` `.ho-visual`
  - `scene:faq`: `.fq-list` `.fq-item`
- The first-visit cards sit in a zig-zag CSS grid by their own classes (vi-step--1 to vi-step--4), the gait observations in a four-column grid and the insole stages in a two-column grid, so keep four of each or adjust those grid rules when you change the count.
- The scene:visit script adds a fill element inside each card, and scene:gait copies the stage image into strips and scene:stories rewraps the words of each quote; keep the card, image and quote markup as it is and the scripts will restore the page on cleanup.
- The round photos and the light green fill that shrinks off them on load, the rings in the home visit section and the masks of the team portraits are CSS shapes: recolour them through the colour variables.
- The conditions photos stack in source order and pair with the rows by position, so keep one photo per row and the same order.
- Colours and fonts are variables in `:root` (`data-8b-part="tokens"`): `--color-1` #eef68e (lime tiles (trust notes, first visit, condition rows, insole intro, price note, contact details, footer), the phone menu sheet and the focus colour inside form fields, and the text of the home visit section), `--color-2` #0e3a1e (text everywhere outside the home visit section, the frame and 4px gaps between tiles, button rims, borders, price row rules and the FAQ plus marks), `--color-3` #b8ec80 (light green tiles (conditions stage, team and FAQ headings), hover fill on buttons, the wash across each first-visit card, photo-disc fills, the top of the page background and the rings on the home visit section), `--color-4` #f2f8e8 (pale tiles (opening, price list, stories, team cards, FAQ rows, form), the navigation bar, form fields and the lower page background), `--color-5` #23c45f (the fill of the label pill in the main buttons and the arrow on their dark caps), `--color-6` #157a3d (step numerals, the Day labels in the insole stages and the background of the home visit section); body text needs 4.5:1 contrast.
- With reduced motion the page must read in full.
- Keep the header comment and `<meta name="generator">`. Keep the "Design: 8B" footer link unless the site owner asks to remove it.

## Replace
- `data-8b-placeholder` (og-image, favicon, phone, form, email): real value in, attribute out; no value, remove the row (no image: drop `og:image`, set `twitter:card` to `summary`).
- Book a visit button in the top bar, Book an assessment buttons (opening, first visit), Arrange a home visit button: now #contact, the call-back form; owner's target: your online booking page (Cliniko, Jane, Calendly) if you book there, or keep #contact once the form is connected.
- Phone links in the questions, contact and footer sections: now a tel: link to the demo number; owner's target: your front desk number as tel:+44....
- Email link in the contact section: now a mailto: link to the demo address; owner's target: your clinic email.
- Request a call back button in the contact form: now submits the form to nothing; a script shows a thank-you line and resets the fields; owner's target: a form service (Formspree, Netlify Forms) or your booking system.
- Insole prices, See the prices and Can I claim on insurance? links: now #prices and #faq; owner's target: keep them.
- The form in `#contact` (fields `name`, `phone`, `email`, `topic`, `time`, `message`) sends nothing; `section-script:contact` handles its submit in the page (read it before you connect a service). Formspree: `action="https://formspree.io/f/<id>"` and `fetch` POST `new FormData(form)` first. Netlify: `data-netlify="true"` and a hidden `form-name`. Or delete it and the script.
- The name Footnote Podiatry (any letter case); the favicon letter and colours in `<link rel="icon">`.
- Photos (23, Unsplash: opening 2, process 3, conditions 6, gait-lab 1, orthotics 4, stories 3, team 3, home-visits 1): `src`, no `srcset`/`sizes`, `width`/`height` to the ratio, `alt`, CREDITS.md.
- `<title>`, meta description, og tags.

## Ask the owner for
All demo text, never to be invented:
- Clinic identity: "Since 2011", "three podiatrists", "more than 11,000 pairs of feet" (opening, team).
- Place and contact: placeholders only, "1 Example Street, Lace Market, Nottingham NG1 0ZZ", a step-free entrance, the phone 0115 000 0000 and hello@footnote.example (FAQ, contact, footer); put in the clinic's real address, phone and email.
- Hours: Mon to Fri 8:00 to 19:00, Sat 9:00 to 14:00, Sun closed (opening, contact).
- Registration and insurers: "HCPC registered and members of the Royal College of Podiatry", "most health insurers accepted" (opening, FAQ, footer); state only what your clinic holds.
- Prices and times: seven services from £15 to £395 with durations from 20 to 75 minutes (prices); the £15 home visit charge and six mile radius (home visits).
- Clinical claims: 45 minute nail surgery under local anaesthetic, shockwave therapy for heels lasting over six months, 240 frames a second video, nine working days for insoles, a review at six weeks (conditions, gait, orthotics, process).
- Insole policy: two to four years of life and a yearly check and re-cover included for two years (FAQ).
- Staff: Imogen Hale, Tom Achebe and Mei Lin Park with roles, specialities and "ask about" lines (team).
- Patient stories: Priya, Derek and Hannah with ages and conditions, invented for the demo; real patient quotes need written consent (stories).
- Policies: no GP referral needed, children seen with a parent in the room, what to bring to a first visit (FAQ).
- Process claims: a fifteen minute history, a walk on the gait track, same-day treatment, a plan emailed the same evening (process).
- Footer: "© 2026 Footnote Podiatry Ltd. All podiatrists registered with the HCPC."; put in your legal name and registration.

## Known limits
- GSAP, ScrollTrigger and Lenis load from jsDelivr at the end of the body; if the CDN is blocked the page stays static, with the nav, menu, FAQ and form scripts still working.
- Without JavaScript the menu button cannot open its sheet (an attribute hides it) and the call-back form cannot show its thank-you line; the FAQ answers still open and the nav links stay reachable on wide screens.
- The call-back form sends nothing: the button only shows the thank-you line, so connect a form service or your booking system before publishing.
- With reduced motion or without JavaScript the six conditions photos stay stacked, so the stage shows only the last one (the Skin row) beside every row, and the gait stage is still held for a little over one screen with a plain photo; that hold is short on screens under about 700 px tall.
- The stylesheet still carries rules for a removed opening (op-screen, op-intro, op-photo) that no markup uses; they can be deleted.

## Check
375 and 1440 px, reduced motion on, console clean; `data-8b-placeholder` and Footnote Podiatry left only in class names.
