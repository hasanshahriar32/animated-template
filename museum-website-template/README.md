# Free HTML museum website template with GSAP scroll animations

Museum website template: one free HTML page for a natural history museum or any collection, with six halls, a main exhibition, drawer tours, learning sessions, monthly late openings and membership. Hand-coloured plates sit on teal, amber and ice grounds with yellow accents. It is one file with an AGENTS.md that Claude Code, Cursor or Codex can adapt.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) ![one HTML file: no build](https://img.shields.io/badge/one%20HTML%20file-no%20build-orange) ![GSAP: ScrollTrigger](https://img.shields.io/badge/GSAP-ScrollTrigger-88ce02)

**[Live demo](https://8bsite.github.io/museum-website-template/)** · **[Use this template](https://github.com/new?template_name=museum-website-template&template_owner=8bsite)** · **[Download ZIP](https://github.com/8bsite/museum-website-template/archive/refs/heads/main.zip)** · **[Template page on 8b.com](https://8b.com/templates/wrenfield/)**

<a href="https://8bsite.github.io/museum-website-template/"><img src="previews/desktop.png" alt="Museum website template: first screen on a desktop" width="76.1%"></a> <a href="https://8bsite.github.io/museum-website-template/"><img src="previews/phone.png" alt="Museum website template: first screen on a phone" width="21.9%"></a>

<p align="center"><a href="https://8bsite.github.io/museum-website-template/"><img src="previews/scroll.gif" alt="Museum website template: scrolling through the first sections" width="40%"></a><br><sub>Scroll animation</sub></p>

## Use it with Claude Code, Cursor or Codex

Download the four files into your project folder (`curl.exe` in Windows PowerShell):

```bash
curl -LO https://raw.githubusercontent.com/8bsite/museum-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/museum-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/museum-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/museum-website-template/main/CREDITS.md
```

Then fill in the angle brackets and give your agent this prompt:

```text
Read AGENTS.md, then edit index.html. Make this the site for <my museum: name, founding year, collection size, halls or galleries, current exhibition with dates and price, tour and late-opening prices, learning sessions, membership levels, opening hours, access details, charity number, ticketing link>. Replace first the museum name, hall names, exhibition, prices, plates and contacts. Keep the section ids, the data-8b attributes the scripts read and the classes AGENTS.md lists. Ask me for missing facts and never invent dates, prices, visitor numbers, charity numbers or contacts.
```

Give Claude Code, Cursor or Codex the facts only the museum has: founding year, specimen counts, hall names and floors, exhibition dates, ticket and tour prices, opening hours and charity number. The demo invents all of them, and its plates and photos are stock images to swap for your own collection. Vibe coding goes fastest when the agent also updates each style="--len:N" number after renaming a hall, and asks instead of guessing a price.

No agent? Click **[Use this template](https://github.com/new?template_name=museum-website-template&template_owner=8bsite)**, edit `index.html` on GitHub and turn on **Settings > Pages**.

## Sections and motion

- **Navigation**: top bar with the brand, five links, social icons, member and ticket icons and a menu button; full-screen menu. The bar turns solid after 40 px and slides away on scroll down and back on scroll up, which still happens with reduced motion; the menu opens a full-screen overlay.
- **Every specimen is a moment someone kept still.**: a hand-coloured bird plate tinted amber across the screen, beside a text panel with the h1, a button and a specimen label. On load the amber plate settles from a slight zoom, the panel lines slide in from the right and the bar over the heading and the label rules grow.
- **Six halls, one family tree.**: six halls sliding past sideways, each with its name, a plate, floor and a line. The section pins and the six halls slide sideways, each plate drifting slower than its hall and each name faster; with reduced motion they become a plain grid.
- **The Colour of Flight**: the main exhibition: a plate printed in three colour layers that slide into register, with title lines and facts. Three colour layers of one plate slide together into register as it crosses the screen, and the two title lines close in from opposite sides.
- **Ninety-seven in every hundred specimens never go on show.**: a cabinet of four drawers whose trays slide out as you scroll, with a drawer-tour button. Each tray slides out of its drawer front as the drawer rises, alternately from left and right on desktop.
- **A third of the year, our curators are out there.**: fieldwork: a photo under a lens, text and three research projects. A yellow lens travels up the photo, a bar grows by the heading and two small glyphs rise at their own rate.
- **Learn**: four session cards arriving scattered and tilted, then lining up. The four session cards start scattered and tilted and turn into one straight row on scroll.
- **After hours, the halls are yours.**: evening openings: a gallery photo that lights up from grey, a large word and four dated events. The photo comes up from dark grey to full colour on arrival and each date rule lights yellow when its row reaches the reading line.
- **Keep a drawer open.**: membership: a heading, a plate under a lens and four label cards (three levels and a one-off adoption).
- **Free, Tuesday to Sunday.**: visiting information in a two-by-two table beside a gallery photo that narrows into its column. On desktop the photo starts across the whole section and narrows to its column while the information slides in from the right.
- **Before you come**: six questions in native &lt;details&gt;.
- **Write to the curators.**: four ways to reach the museum: a message form, phone, address with email and a newsletter form. The four columns start as a staircase and rise into one level row as the section arrives.
- **Footer**: large wordmark, four link columns and a charity line.

## Design

![#5995a8](https://img.shields.io/badge/-%235995a8-5995a8?style=flat-square) teal page ground of the halls, sessions and contact sections, the solid nav bar and the frame under the two lens photos  
![#ffffff](https://img.shields.io/badge/-%23ffffff-ffffff?style=flat-square) the large uppercase words and text on the deep teal blocks, the exhibition print sheet  
![#0d1f2b](https://img.shields.io/badge/-%230d1f2b-0d1f2b?style=flat-square) body text, the nav, the menu overlay and the ground of the exhibition, Lates, FAQ and footer  
![#eab12f](https://img.shields.io/badge/-%23eab12f-eab12f?style=flat-square) yellow accent: filled buttons, grown underlines, nav hover bar, Lates glow, FAQ plus marks  
![#f6d97c](https://img.shields.io/badge/-%23f6d97c-f6d97c?style=flat-square) pale yellow ground of the field section and the lens discs, and the fill that floods outlined buttons on hover  
![#c97f1c](https://img.shields.io/badge/-%23c97f1c-c97f1c?style=flat-square) amber ground of the membership section and of the whole opening, where it tints the plate, and the opening panel on phones  
![#e9f2f4](https://img.shields.io/badge/-%23e9f2f4-e9f2f4?style=flat-square) pale ice ground of the drawers and visit sections, session cards, membership labels and specimen label

**Gabarito**: headings, hall names, uppercase labels and buttons, in weights 600 to 800. **Google Sans**: body text and form fields at regular weight, larger lead lines at medium weight (Google Fonts). Content hangs on one left line at a tenth of the width, which three hairlines mark in the opening. The opening is a full-screen plate tinted amber beside a text panel with a three-row specimen label (Specimen, Plate, Shown in). Six halls follow as big names over plates, then an exhibition with a facts list, four drawers, three research projects, four session cards, four dated events, four membership cards, a two-by-two visit table, a FAQ and four contact columns.

## Questions

**Is this free web design for museums and heritage charities?**  
Yes. It is one index.html under the MIT license, so a museum, a charity or a freelancer building for one can use it at no cost. GSAP, ScrollTrigger and Lenis load from jsDelivr, there is no build step, and the Unsplash photos are listed in CREDITS.md.

**Can this museum template work for an art gallery or another collection?**  
Yes, after a text pass. The six halls become galleries, the drawer tours become tours of the archive or store, and the plates become your own images. It then works as a free gallery website template for a library, archive or botanic garden, and suits gallery websites that lean on a collection.

**Do the booking buttons and forms send anything?**  
No. Both forms only validate and show a thank-you line, and the Book, Join and Tickets buttons jump to #visit or #contact. Connect Formspree or Netlify Forms for the forms and point each button at a ticketing, membership or donation page.

## Is it the right base?

This museum website design suits a place with a real collection and a calendar of events. A gallery that mostly runs night programmes and screenings fits the [kunsthalle](https://8b.com/templates/nocturna/) template better. Booking is the weak spot: every Book button jumps to a section of the page until you point it at a ticketing tool, and both forms send nothing yet. An owner who does not code can try 8B instead.

## Before you publish

- Replace what is marked `data-8b-placeholder` (social preview image, favicon, social, map, form, phone, email) and the invented demo facts; [AGENTS.md](AGENTS.md) lists them.
- The form sends nothing yet: connect it to Formspree or Netlify Forms, or remove it.

## Tech

GSAP 3.13.0, ScrollTrigger, Lenis 1.3.4 from jsDelivr, 111 KB, no build step. Chrome and Edge 111+, Safari 16.2+, Firefox 113+ (it uses color-mix(), cascade layers). With "reduce motion" on, the page is complete and still.

## License

MIT, see [LICENSE](LICENSE). Photos, fonts and libraries keep their own licences: [CREDITS.md](CREDITS.md). More free templates: [8b.com/templates](https://8b.com/templates/) · [github.com/8bsite](https://github.com/8bsite).
