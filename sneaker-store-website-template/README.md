# Free HTML sneaker store website template with GSAP scroll animations

Sneaker store website template: one free HTML file for an independent streetwear shop with a single product drop, a priced lookbook, a repair service, two store cards and a Saturday run club. The look is pale green ground, near-black type, one lime accent and heavy uppercase headings. AGENTS.md is included, so Claude Code, Cursor or Codex can adapt it.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) ![one HTML file: no build](https://img.shields.io/badge/one%20HTML%20file-no%20build-orange) ![GSAP: ScrollTrigger](https://img.shields.io/badge/GSAP-ScrollTrigger-88ce02)

**[Live demo](https://8bsite.github.io/sneaker-store-website-template/)** · **[Use this template](https://github.com/new?template_name=sneaker-store-website-template&template_owner=8bsite)** · **[Download ZIP](https://github.com/8bsite/sneaker-store-website-template/archive/refs/heads/main.zip)** · **[Template page on 8b.com](https://8b.com/templates/strade/)**

<a href="https://8bsite.github.io/sneaker-store-website-template/"><img src="previews/desktop.png" alt="Sneaker store website template: first screen on a desktop" width="76.1%"></a> <a href="https://8bsite.github.io/sneaker-store-website-template/"><img src="previews/phone.png" alt="Sneaker store website template: first screen on a phone" width="21.9%"></a>

<p align="center"><a href="https://8bsite.github.io/sneaker-store-website-template/"><img src="previews/scroll.gif" alt="Sneaker store website template: scrolling through the first sections" width="40%"></a><br><sub>Scroll animation</sub></p>

## Use it with Claude Code, Cursor or Codex

Download the four files into your project folder (`curl.exe` in Windows PowerShell):

```bash
curl -LO https://raw.githubusercontent.com/8bsite/sneaker-store-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/sneaker-store-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/sneaker-store-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/sneaker-store-website-template/main/CREDITS.md
```

Then fill in the angle brackets and give your agent this prompt:

```text
Read AGENTS.md, then edit index.html. Make this the site for <my shop: name, city, the current drop with name, price, pair count, sizes and release date, look prices, repair terms, two store addresses and hours, run club time, shipping and returns, email and phone>. Replace first the shop name, euro prices, Porto and Rotterdam details, VAT line. Keep the ids, data-8b-section, data-8b-motion and data-8b-part, the selectors AGENTS.md lists and the two word spans of the contact wordmark. Ask me for missing facts; never invent prices, hours, addresses or contacts.
```

Give the agent the drop facts first: name, price, pair count, sizes, materials, release date and shop link, then both store addresses, hours and repair terms. It replaces the demo euro prices, Porto workshop, Rotterdam stores and VAT line, and points the reminder, bag, repair and run buttons at real pages. Vibe coding in Claude Code or Cursor works when the agent asks for missing prices and hours instead of inventing them.

No agent? Click **[Use this template](https://github.com/new?template_name=sneaker-store-website-template&template_owner=8bsite)**, edit `index.html` on GitHub and turn on **Settings > Pages**.

## Sections and motion

- **Navigation**: fixed top bar: wordmark, three links (Shop, Repairs, Stores) and three icon links. The navigation bar slides up out of view when you scroll down and returns when you scroll up; this keeps working with reduced motion.
- **Drop 07: Concrete Low**: first screen: headline of the product drop, a paragraph, a photo, a spec list and a reminder button. On load the photo is cut into tiles that start scattered and turned and lock together into the picture, while the headline slides in by line and the badge pops.
- **Five ways to wear October**: five outfits with photo, name and three priced pieces, shown as a sideways rail. The section pins and the row of looks travels sideways as you scroll, for as long as the row is wider than the screen, while each photo drifts slightly inside its frame.
- **Worn on the city before it is sold**: heading, paragraph, a tall photo and a wear-test table of five pieces. The heading slides in by line and the tall photo opens from a centre column as it arrives.
- **Repairs for life**: heading, paragraph and button, then three step cards with photos. Scrubbed with the scroll, the three step cards start piled on the middle card (the first on phones), each turned a little, and spread into their row.
- **Two stores, one repair bench**: two store cards with photo, address, opening hours table and a directions link. The heading slides in, each store photo opens from a centre column and each badge pops in.
- **Saturday run club**: run club panel: heading, paragraph, button, a night photo and three pace lanes. Scrubbed with the scroll, each pace line enters from the right and settles at the left, the fast group travelling furthest.
- **Before you ask**: five questions and answers in native &lt;details&gt; elements. The heading slides in by line; each question is a native details element, so it opens without scripts.
- **Say hello**: large "Say hello" wordmark, a paragraph with email and phone, and a message form. Scrubbed with the scroll, the letters of the Say hello wordmark start spread across the width and turned, then close into the two words.
- **Footer**: logo, six links, the two store addresses and a small print line.

## Design

![#f4f7ec](https://img.shields.io/badge/-%23f4f7ec-f4f7ec?style=flat-square) page background and the top bar  
![#121411](https://img.shields.io/badge/-%23121411-121411?style=flat-square) text, button hover fill, the run club panel and the footer background  
![#c6ef4e](https://img.shields.io/badge/-%23c6ef4e-c6ef4e?style=flat-square) the accent: button fill, badges, run club paces, open FAQ plus  
![#e5eadb](https://img.shields.io/badge/-%23e5eadb-e5eadb?style=flat-square) icon circles, image frame backing, the closed FAQ plus  
![#cfd6c3](https://img.shields.io/badge/-%23cfd6c3-cfd6c3?style=flat-square) dashed rules and form field borders  
![#ffffff](https://img.shields.io/badge/-%23ffffff-ffffff?style=flat-square) repair cards, form fields, text on the dark panels  
![#737869](https://img.shields.io/badge/-%23737869-737869?style=flat-square) declared in :root but not used by any rule in the shipped page  
![#a9ae9f](https://img.shields.io/badge/-%23a9ae9f-a9ae9f?style=flat-square) run club paragraph and group labels, footer address and small print  
![#1f231d](https://img.shields.io/badge/-%231f231d-1f231d?style=flat-square) dashed rules inside the run club panel and the footer  
![#5d6254](https://img.shields.io/badge/-%235d6254-5d6254?style=flat-square) spec labels, wear-test column heads, hours labels, contact labels

**Schibsted Grotesk**: uppercase display type: headings, look and store names, repair step titles, FAQ questions, the price, the large contact wordmark and the logo, in semibold and bold. **Host Grotesk**: body text in regular weight, buttons and table text in medium to semibold, and small uppercase labels (Google Fonts). A 12-column grid on desktop. Most sections set a big uppercase heading against a block of text on the far side, and dashed rules separate spec cells, look prices, store rows and FAQ items. The lookbook is a row of 3:4 portrait cards with a priced list under each. The run club and the footer are rounded near-black panels on the pale ground. Photos sit in rounded frames. Below 900 px most sections stack to one column.

## Questions

**Can this sneaker website template take orders online?**  
No, not by itself. The bag, saved looks and members icons only scroll to a section, and the file has no cart, wishlist or login. Point them at your cart or checkout page and a member or wishlist page, or remove the icons. The template presents the drop and does not take payment.

**Where does the contact form send its messages?**  
Nowhere yet. The form needs a name, an email and a message, then shows a thank-you line and clears the fields without sending anything. Connect Formspree or Netlify Forms before publishing, or delete the form and its script. Without JavaScript it posts to the page itself, which also sends nothing.

**Can I get a site like this without editing code?**  
Yes, by another route. [8B's AI website builder](https://8b.com/templates/8b/) designs a new site from a sentence you write, with its own design rather than this template. Designing and restyling are free. Publishing with hosting and SSL, full HTML export and AI edits in chat are on Pro at $9 a month billed yearly. It also runs in Claude and ChatGPT.

## Is it the right base?

As a streetwear brand website template it suits a shop with one hero release, a workshop story and a community event. A label that sells many drops from a calendar and credits its artists is closer to the [limited-drop label](https://8b.com/templates/scrawl/) template. This one has no cart, wishlist or login, and the navigation bar has no phone menu. Owners who do not code can use 8B's builder instead.

## Before you publish

- Replace what is marked `data-8b-placeholder` (social preview image, favicon, map, email, phone, form) and the invented demo facts; [AGENTS.md](AGENTS.md) lists them.
- The form sends nothing yet: connect it to Formspree or Netlify Forms, or remove it.

## Tech

GSAP 3.13.0, ScrollTrigger, Lenis 1.3.27 from jsDelivr, 64 KB, no build step. Chrome and Edge 108+, Safari 15.4+, Firefox 121+ (it uses :has(), cascade layers, small/dynamic viewport units). With "reduce motion" on, the page is complete and still.

## License

MIT, see [LICENSE](LICENSE). Photos, fonts and libraries keep their own licences: [CREDITS.md](CREDITS.md). More free templates: [8b.com/templates](https://8b.com/templates/) · [github.com/8bsite](https://github.com/8bsite).
