# Free HTML outdoor gear rental website template with GSAP scroll animations

Outdoor gear rental website template: one free HTML file for a shop that hires out tents, packs and boots by the night. It has six priced shelves of kit, four ready packs with a nights switch, a fitting section and a route table, on pale blue. AGENTS.md is included, so Claude Code, Cursor or Codex can adapt it.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) ![one HTML file: no build](https://img.shields.io/badge/one%20HTML%20file-no%20build-orange) ![GSAP: ScrollTrigger](https://img.shields.io/badge/GSAP-ScrollTrigger-88ce02)

**[Live demo](https://8bsite.github.io/outdoor-gear-rental-website-template/)** · **[Use this template](https://github.com/new?template_name=outdoor-gear-rental-website-template&template_owner=8bsite)** · **[Download ZIP](https://github.com/8bsite/outdoor-gear-rental-website-template/archive/refs/heads/main.zip)** · **[Template page on 8b.com](https://8b.com/templates/kitfell/)**

<a href="https://8bsite.github.io/outdoor-gear-rental-website-template/"><img src="previews/desktop.png" alt="Outdoor gear rental website template: first screen on a desktop" width="76.1%"></a> <a href="https://8bsite.github.io/outdoor-gear-rental-website-template/"><img src="previews/phone.png" alt="Outdoor gear rental website template: first screen on a phone" width="21.9%"></a>

<p align="center"><a href="https://8bsite.github.io/outdoor-gear-rental-website-template/"><img src="previews/scroll.gif" alt="Outdoor gear rental website template: scrolling through the first sections" width="40%"></a><br><sub>Scroll animation</sub></p>

## Use it with Claude Code, Cursor or Codex

Download the four files into your project folder (`curl.exe` in Windows PowerShell):

```bash
curl -LO https://raw.githubusercontent.com/8bsite/outdoor-gear-rental-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/outdoor-gear-rental-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/outdoor-gear-rental-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/outdoor-gear-rental-website-template/main/CREDITS.md
```

Then fill in the angle brackets and give your agent this prompt:

```text
Read AGENTS.md, then edit index.html. Make this the site for <my hire shop: name, town, shelves of kit with nightly prices, ready packs with prices for 2 nights, 3 nights and a week, hire terms, deposit and damage rules, delivery area, hours, phone, email, company number>. Replace first the shop name, the Lake District routes, prices and quotes. Keep the section ids, the classes AGENTS.md lists and the three data-price values on each pack. Ask me for missing facts and never invent prices, terms, routes, reviews or contacts.
```

Vibe coding with Claude Code, Cursor or Codex starts with the facts only the shop has: shelf prices, pack contents, hire terms, delivery area and hours. The demo invents them all, with the Lake District routes, quotes and company number. Change each pack price in the visible text, its value attribute and its three data-price attributes, and keep the id on every kit card, because the shelf index is built from the card titles and ids.

No agent? Click **[Use this template](https://github.com/new?template_name=outdoor-gear-rental-website-template&template_owner=8bsite)**, edit `index.html` on GitHub and turn on **Settings > Pages**.

## Sections and motion

- **Navigation**: top bar with wordmark, five links and a Book kit button; on small screens a menu button opens a full-screen overlay. The bar slides up out of view when you scroll down and returns on scrolling up; this keeps working with reduced motion.
- **We own the tent you would use twice a year, so you don’t have to.**: a statement as the h1, a paragraph and a How hire works button on a pale ground beside a framed mountain photo. On load the photo frame opens from a pill shaped slit to its rounded shape while the heading, text and button lift in, and the photo then drifts sideways in a slow CSS loop.
- **Everything in the kit room, by the night.**: heading with a Reserve kit button beside six kit cards (tents, sleep, packs, cook, boots, shells) with an index of shelves. A sticky index of the six shelf names follows the card in the middle of the screen, and each card grows from tilted and dimmed to full size as it arrives.
- **Ready packs, so you only choose the weekend.**: ready packs with a nights switch: four cards with photo, five items, and a price that follows the choice of 2 nights, 3 nights or a week. The four pack cards travel from one tilted pile to their places as the grid rises, and the prices change when you pick 2 nights, 3 nights or a week.
- **How hire works**: four numbered hire steps: Book, Get fitted, Go, Bring it back muddy. The intro line fills word by word from grey to ink as you scroll, and each step title rises into view.
- **Fitted, not handed over.**: a held photo frame that swaps between three photos while three fitting stories scroll past. Three photos stack in one sticky frame and each wipes up over the last as its fitting story reaches the middle of the screen.
- **Between every hire, the same six checks.**: six care checks as a horizontal track of panels, each with a tick, a sentence and a photo. The section pins and the six check panels slide sideways, each tick swelling from a pale dot as its panel arrives.
- **A route card with every hire.**: a photo and a table of four walking routes with distance, ascent, time and grade. The photo opens from a pill shaped slit to its full rounded frame.
- **Where the kit went last month.**: a 3 by 3 grid of six customer photos and three quotes that zooms out from the centre photo. On wide screens the section pins and the grid shrinks from the centre photo until all nine cells show.
- **Questions people ask at the counter**: a heading with a photo beside six questions and answers in native &lt;details&gt; elements.
- **Come and get fitted.**: a village photo that widens to full width beside a card with shop address, hours, phone, email and buttons. Scrubbed with scroll, the village photo widens from a rounded window to full width while the details card stays still.
- **Footer**: route notes sign-up form, four links, a large wordmark and legal lines.

## Design

![#ecf1f5](https://img.shields.io/badge/-%23ecf1f5-ecf1f5?style=flat-square) page ground and the opening screen  
![#06132e](https://img.shields.io/badge/-%2306132e-06132e?style=flat-square) text, the packs band, the footer and the full-screen menu  
![#2b3bff](https://img.shields.io/badge/-%232b3bff-2b3bff?style=flat-square) the only accent: button fills on hover, kit prices, the shelf index marker, focus outlines  
![#b4ddf8](https://img.shields.io/badge/-%23b4ddf8-b4ddf8?style=flat-square) background of the care section  
![#ffffff](https://img.shields.io/badge/-%23ffffff-ffffff?style=flat-square) kit cards and other surfaces, text on navy  
![#4c5a70](https://img.shields.io/badge/-%234c5a70-4c5a70?style=flat-square) descriptions under headings, table headings, detail labels and unselected shelf links  
![#a7b4ca](https://img.shields.io/badge/-%23a7b4ca-a7b4ca?style=flat-square) small text on navy: the packs intro and legend, field placeholders, the form message and the legal lines  
![#ddebf6](https://img.shields.io/badge/-%23ddebf6-ddebf6?style=flat-square) round buttons, small badges, photo backing and link underlines

**National Park**: headings and the h1 at regular weight, card titles and pack prices at medium, the logo and the footer wordmark at 800. **Golos Text**: body text, labels, kit prices and form fields at regular and medium weights, buttons at semibold 600 (Google Fonts). Rounded cards and pill buttons carry the page: white kit cards with wide photos, round arrow buttons, a table of four routes and a three by three grid of trip photos and quotes. Headings are large and light, set in lines that rise into view. The ground alternates pale blue, a navy packs band, a light blue care band and a navy footer, so each stage of a hire has its own screen.

## Questions

**Does the Book kit button take bookings?**  
No. Every Book kit and Reserve kit button, and the arrow on each card, jumps to the visit card, and the Book by email button opens a mail draft. There is no calendar or payment. Point the buttons at your own booking page, or keep them as enquiry links.

**Does the route notes sign-up form send anything?**  
No. The form in the footer checks the email, shows a thank-you line and sends nothing. Connect Formspree or Netlify Forms with the steps in AGENTS.md, or delete the form and its script before publishing.

**Can I get a site like this without editing code?**  
Yes, in a different way. [8B's AI website builder](https://8b.com/templates/8b/) designs a new site from a sentence, not this template. Designing and restyling are free. Publishing with hosting and SSL, full HTML export and AI edits in chat are on Pro at $9 a month billed yearly. It also runs inside Claude and ChatGPT through the 8B connector.

## Is it the right base?

It suits a shop with a fixed price list, bundles and a hands-on fitting. A venue that sells timed sessions, lessons and parties, such as a [skating venue](https://8b.com/templates/spinway/), needs a different base. The weak spot is booking: every Book kit button jumps to the visit card, and no calendar shows free dates. Without code, 8B can design a new site instead.

## Before you publish

- Replace what is marked `data-8b-placeholder` (social preview image, favicon, phone, email, map, form, social) and the invented demo facts; [AGENTS.md](AGENTS.md) lists them.
- The form sends nothing yet: connect it to Formspree or Netlify Forms, or remove it.

## Tech

GSAP 3.13.0, ScrollTrigger, SplitText, Lenis 1.3.4 from jsDelivr, 99 KB, no build step. Chrome and Edge 111+, Safari 16.2+, Firefox 121+ (it uses color-mix(), :has(), cascade layers, small/dynamic viewport units). With "reduce motion" on, the page is complete and still.

## License

MIT, see [LICENSE](LICENSE). Photos, fonts and libraries keep their own licences: [CREDITS.md](CREDITS.md). More free templates: [8b.com/templates](https://8b.com/templates/) · [github.com/8bsite](https://github.com/8bsite).
