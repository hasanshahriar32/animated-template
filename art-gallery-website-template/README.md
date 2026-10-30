# Free HTML art gallery website template with GSAP scroll animations

This art gallery website template is one free HTML file for a gallery, kunsthalle or museum that opens late: an opening screen, a six-night programme, four rooms, five resident artists, a midnight screening, passes and a visit form. White ruled cells meet dark night screens and a coral glow. AGENTS.md is included, so an AI agent can adapt it.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) ![one HTML file: no build](https://img.shields.io/badge/one%20HTML%20file-no%20build-orange) ![GSAP: ScrollTrigger](https://img.shields.io/badge/GSAP-ScrollTrigger-88ce02)

**[Live demo](https://8bsite.github.io/art-gallery-website-template/)** · **[Use this template](https://github.com/new?template_name=art-gallery-website-template&template_owner=8bsite)** · **[Download ZIP](https://github.com/8bsite/art-gallery-website-template/archive/refs/heads/main.zip)** · **[Template page on 8b.com](https://8b.com/templates/nocturna/)**

<a href="https://8bsite.github.io/art-gallery-website-template/"><img src="previews/desktop.png" alt="Art gallery website template: first screen on a desktop" width="76.1%"></a> <a href="https://8bsite.github.io/art-gallery-website-template/"><img src="previews/phone.png" alt="Art gallery website template: first screen on a phone" width="21.9%"></a>

<p align="center"><a href="https://8bsite.github.io/art-gallery-website-template/"><img src="previews/scroll.gif" alt="Art gallery website template: scrolling through the first sections" width="40%"></a><br><sub>Scroll animation</sub></p>

## Use it with Claude Code, Cursor or Codex

Download the four files into your project folder (`curl.exe` in Windows PowerShell):

```bash
curl -LO https://raw.githubusercontent.com/8bsite/art-gallery-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/art-gallery-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/art-gallery-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/art-gallery-website-template/main/CREDITS.md
```

Then fill in the angle brackets and give your agent this prompt:

```text
Read AGENTS.md, then edit index.html. Make this the site for <my venue: name, address, opening hours, rooms, season events with dates, resident artists, any screening, ticket and pass prices>. Replace first the name, hours, six programme rows, five artists, prices and the Rotterdam address. Keep the section ids and the classes AGENTS.md lists, set each --len to its text length, and keep four rooms, eight relay cities and three pass cards. Ask me for missing facts and never invent dates, prices, artists or contacts.
```

Claude Code, Cursor or Codex can adapt this by vibe coding in a few passes. Start with the name, hours, address and the six programme rows, then the four rooms, five artists and the screening. Ask the owner for every date, price, artist name, film title and house rule; the demo invents all of them. Leave the ids, the script classes and the data-8b attributes AGENTS.md lists alone, and reset the --len number on the wordmark, the rails and the artist names when their text changes.

No agent? Click **[Use this template](https://github.com/new?template_name=art-gallery-website-template&template_owner=8bsite)**, edit `index.html` on GitHub and turn on **Settings > Pages**.

## Sections and motion

- **Navigation**: white top bar over the right two thirds: arch logo, coral dot, four links, Menu button; Menu opens a dark overlay with seven links; the bar hides on scroll down. The bar hides when you scroll down past half a screen and returns on scroll up; Menu opens a dark overlay of seven links.
- **Lights down at nine. Eyes open till two.**: dark screen with the heading "Lights down at nine. Eyes open till two.", intro, Get a pass button, See the season link, three fact cells and five stars. On load the heading lines, text and three fact cells rise in one after another. The glow breathes and the five stars turn slowly, and both pause while the section is off screen.
- **Six nights to stay up for**: ledger of six nights with dates, titles, formats and rooms, beside a sticky arch window that shows a photo per night. As each row reaches the reading line its photo rises into the arch over the previous one, and on desktop a coral dot slides down the rule to that row.
- **Four rooms, one long night**: dark stage with the heading "Four rooms, one long night", a Plan a visit button and a plan of four rooms that a coral lamp walks through. Pinned: each room starts under a dark veil, a coral lamp travels from room to room, and each veil lifts as the lamp arrives.
- **Five artists who work at night**: five resident artists as huge two-weight names with a role line and an arch portrait each. As each row crosses the screen the light first name thickens while the heavy surname thins, they trade back, and the portrait slides along the row.
- **Head lights**: 3x3 ruled credits grid with a film still in the middle that opens to the full screen. Pinned: the still opens from the middle cell to the full screen, the other cells slide off the edges and the title travels down onto the picture.
- **One film, eight midnights**: one row of eight city cells in midnight order that a coral line sweeps across, each turning dark. A coral line sweeps across the row of cities, and each cell fills with night as the line passes.
- **Close your eyes**: light-blue section: one featured note in a big arch, two short notes with round photos, a row of five stars. The heading rises, the arch photo opens upward, the two notes draw their hairlines and the five stars turn with scroll.
- **One evening, or every one**: three passes with price, three included items and a button each: One Night, Night Pass, Patron. The three cards start stacked and slightly turned, then fan out into a row as you scroll.
- **Questions for the night**: vertical rail "Before you come", an intro with three stars and five questions that open and close. A hairline draws in below each question and the three stars turn with scroll.
- **Come late. Stay later.**: four info cells, the heading "Come late. Stay later." and a form with name, email and question, over a light-blue dawn disc. A large light-blue disc rises from below and grows behind the heading and form as you scroll.
- **Footer**: dark footer with the wordmark filling the width and four ruled columns.

## Design

![#ffffff](https://img.shields.io/badge/-%23ffffff-ffffff?style=flat-square) page ground of the light sections, text on the dark screens and footer, the Buy a ticket card  
![#101014](https://img.shields.io/badge/-%23101014-101014?style=flat-square) text and hairlines on light sections, the dark night screens, the footer and filled buttons  
![#c6ddf7](https://img.shields.io/badge/-%23c6ddf7-c6ddf7?style=flat-square) the light-blue journal section, the dawn disc behind the contact form, the round Get a pass button and the Patron card  
![#f0654a](https://img.shields.io/badge/-%23f0654a-f0654a?style=flat-square) coral accent: the glow, the dot, the room lamp, the relay line, button hover fills and the Night Pass card  
![#5a5b64](https://img.shields.io/badge/-%235a5b64-5a5b64?style=flat-square) secondary body text and captions on light sections  
![#a9abb6](https://img.shields.io/badge/-%23a9abb6-a9abb6?style=flat-square) small secondary text on the dark screens, the menu overlay and the footer: room captions, the screening synopsis, the footer columns

**Pliant**: headings and the vertical rails, a variable font from weight 200 to 900 that pairs a light line with a heavy one; card and cell titles at weight 600. **Host Grotesk**: body text, labels, form fields and buttons, in weights 400 to 600; labels and buttons are small uppercase with wide spacing (Google Fonts). A hairline grid divides each section. On a desktop a left column about a third wide holds the label, with the content to its right; the opening and FAQ add a narrow rail of rotated type. Sections mostly alternate white and near black, with one light-blue journal. The programme, artists and passes read as ruled rows or cards, the screening is a three by three credits grid around the still, and the relay is a row of eight cells.

## Questions

**Can a museum or a daytime gallery use it?**  
Yes, after a text pass. A museum website design can keep the rooms, programme and passes, but the demo copy is built around night hours: nine to two, free entry before 22:00 and a Friday midnight screening. Replace those, or remove the screening and relay sections with their animation scripts and repoint the links to #screening.

**Where does the visit form send its messages?**  
Nowhere yet. The form needs a name, an email and a question, then shows a thank-you line and clears itself without sending anything. Connect Formspree or Netlify Forms with the steps in AGENTS.md, or replace the form with a link, and rewrite the thank-you line.

**Can I get a site like this without editing code?**  
Yes, in a different way. [8B's AI website builder](https://8b.com/templates/8b/) designs a new site from a sentence, with its own design, not this template. Designing and restyling are free; publishing with hosting and SSL, HTML export and AI edits in chat are on Pro at $9 a month billed yearly. It also runs inside Claude and ChatGPT through the 8B connector.

## Is it the right base?

This is the right base when a venue keeps late hours, runs dated events and sells passes. A venue built around one dated event fits [a template made for events](https://8b.com/templates/ondo/) better, and a gallery with hundreds of works or a shop needs more than one page. One weak spot: without JavaScript the Menu button cannot open its overlay, and on phones that overlay holds the only Residents and Midnight screening links. Owners who do not want to edit code can use a no-code builder instead.

## Before you publish

- Replace what is marked `data-8b-placeholder` (social preview image, favicon, email, phone, form, social) and the invented demo facts; [AGENTS.md](AGENTS.md) lists them.
- The form sends nothing yet: connect it to Formspree or Netlify Forms, or remove it.

## Tech

GSAP 3.13.0, ScrollTrigger, Lenis 1.3.27 from jsDelivr, 105 KB, no build step. Chrome and Edge 111+, Safari 16.2+, Firefox 113+ (it uses color-mix(), cascade layers, small/dynamic viewport units). With "reduce motion" on, the page is complete and still.

## License

MIT, see [LICENSE](LICENSE). Photos, fonts and libraries keep their own licences: [CREDITS.md](CREDITS.md). More free templates: [8b.com/templates](https://8b.com/templates/) · [github.com/8bsite](https://github.com/8bsite).
