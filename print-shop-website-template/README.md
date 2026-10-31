# Free HTML print shop website template with GSAP scroll animations

Print shop website template: one free HTML file for a copy and print shop that takes walk-in and file-based jobs, with a counter queue, a paper table, a poster-size demo, a file checklist and a quote form. The look is a layout app in paper white, ink and five bright accents. AGENTS.md is included for Claude Code, Cursor or Codex.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) ![one HTML file: no build](https://img.shields.io/badge/one%20HTML%20file-no%20build-orange) ![GSAP: ScrollTrigger](https://img.shields.io/badge/GSAP-ScrollTrigger-88ce02)

**[Live demo](https://8bsite.github.io/print-shop-website-template/)** · **[Use this template](https://github.com/new?template_name=print-shop-website-template&template_owner=8bsite)** · **[Download ZIP](https://github.com/8bsite/print-shop-website-template/archive/refs/heads/main.zip)** · **[Template page on 8b.com](https://8b.com/templates/shortrun/)**

<a href="https://8bsite.github.io/print-shop-website-template/"><img src="previews/desktop.png" alt="Print shop website template: first screen on a desktop" width="76.1%"></a> <a href="https://8bsite.github.io/print-shop-website-template/"><img src="previews/phone.png" alt="Print shop website template: first screen on a phone" width="21.9%"></a>

<p align="center"><a href="https://8bsite.github.io/print-shop-website-template/"><img src="previews/scroll.gif" alt="Print shop website template: scrolling through the first sections" width="40%"></a><br><sub>Scroll animation</sub></p>

## Use it with Claude Code, Cursor or Codex

Download the four files into your project folder (`curl.exe` in Windows PowerShell):

```bash
curl -LO https://raw.githubusercontent.com/8bsite/print-shop-website-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/print-shop-website-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/print-shop-website-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/print-shop-website-template/main/CREDITS.md
```

Then fill in the angle brackets and give your agent this prompt:

```text
Read AGENTS.md, then edit index.html. Make this the site for <my shop: name, town, address, what I print, job types with sizes, paper and turnaround, prices, hours, same-day cutoff, delivery terms>. Replace first the shop name, the Leicester address, the pound prices, the counter rows, the paper table, the recent jobs and the contacts. Keep the section ids, the tab, photo and panel names and the seven size items. Point the quote form at my form service. Ask for any missing fact; never invent prices, hours or contacts.
```

Vibe coding goes fastest when the agent starts from the shop's real facts: what you print, the price per job, paper stocks, opening hours, the same-day cutoff, delivery terms and file rules. Claude Code, Cursor or Codex should replace those first, then the six counter rows, the paper table and the six recent jobs. It must keep the section ids, the data-8b-section, data-8b-motion and data-8b-part attributes and the selectors AGENTS.md lists. The demo's prices, hours and jobs are invented.

No agent? Click **[Use this template](https://github.com/new?template_name=print-shop-website-template&template_owner=8bsite)**, edit `index.html` on GitHub and turn on **Settings > Pages**.

## Sections and motion

- **Navigation**: a vertical Same-day print! label, a strip with address and status, the wordmark, five square button links and a send-files icon. The header slides away on scroll down past 140px and returns on scroll up; on narrow screens a Menu button opens a full-screen link overlay.
- **Proof first.**: first screen: the h1 Proof first. with a lead and button, and four job tabs that swap a photo and a spec list. On load the heading block rises in and a paper layer and three ink layers wipe off the proof photo in turn; the four tabs swap the photo and spec list on click or arrow keys.
- **Walk in. Walk out with it.**: a print queue of six jobs whose bars fill in turn and whose Ready badges stamp down. Scrubbed as the queue crosses the screen: each row's bar fills in turn and its Ready badge stamps in.
- **Pick your paper.**: photo of coloured card edges beside a table of six paper stocks with weight badges. On arrival the photo opens from a crop, the heading gets a highlight sweep and the six weight badges stamp in.
- **Big is our small size.**: a held stage where a poster wall is dragged out by selection handles from A6 to A0 while a marker steps along the size row. Pinned for about two screens of scrolling: the poster wall grows from a small sheet to full size through seven sizes, selection handles follow its corners and a yellow marker steps from A6 to A0.
- **Off the press this week.**: six recent jobs listed like dockets, each with a thumbnail, spec, time and a status stamp. The heading gets a highlight sweep, the thumbnails open from a crop and the status badges stamp in.
- **Fold it, stitch it, bind it, trim it.**: four finishing panels that unfold from a tight zig-zag into one flat strip. On wide screens the section is pinned for about one and a half screens while four panels unfold sideways from a zig-zag into a flat strip, alternate ones starting darker; on narrow screens they unfold vertically without pinning.
- **Paper with a past.**: a pledge about recycled paper with three fact tiles and a photo. The heading gets a highlight sweep, the three tiles stamp in and the photo opens from a crop.
- **Send it right, get it right.**: a four-point file checklist beside a sample sheet that gets its bleed, trim marks, safe area and colour bar as the checks tick. On wide screens the section is pinned for about a screen and a third: the four ticks draw one by one, each followed by the next mark on the sample sheet: bleed line, trim marks, safe area, colour bar; on narrow screens the list and the sheet scrub separately.
- **Asked at the counter.**: six questions and answers (native details). The heading gets a highlight sweep; each question's plus box turns on opening.
- **Come in, or send it over.**: a shop-front photo that is re-cropped by drag handles, address, hours, phone, email and a quote form. The shop-front photo starts cropped tight and zoomed, and its selection handles drag the crop out to the whole photo as the section scrolls in.
- **Footer**: wordmark with a line about the shop, visit and talk columns, page links and a base line.

## Design

![#f7efe5](https://img.shields.io/badge/-%23f7efe5-f7efe5?style=flat-square) page ground, the header bar, card and table surfaces, form fields, text on the ink sections  
![#171513](https://img.shields.io/badge/-%23171513-171513?style=flat-square) text, every 1.5px border, the strip above the header, the finishing section and the footer  
![#ffc21f](https://img.shields.io/badge/-%23ffc21f-ffc21f?style=flat-square) yellow: buttons, icon buttons, the margin stripe, selection handles, the active tab, the size marker, the FAQ plus box, two heading highlights, the column heads in the footer  
![#ff6a3d](https://img.shields.io/badge/-%23ff6a3d-ff6a3d?style=flat-square) coral: the wordmark blocks in the header and footer, the jobs heading highlight, the bleed line on the sample sheet, link hover fill, one badge  
![#8682f7](https://img.shields.io/badge/-%238682f7-8682f7?style=flat-square) violet: the paper section ground, the safe-area line on the sample sheet, two counter icons, one weight badge  
![#a9dcf6](https://img.shields.io/badge/-%23a9dcf6-a9dcf6?style=flat-square) pale blue: the file checklist section ground, the FAQ heading highlight, one counter icon, photo placeholders  
![#bdf35f](https://img.shields.io/badge/-%23bdf35f-bdf35f?style=flat-square) lime: the recycled section ground, the Ready and Collected badges, tab and FAQ row hover, one counter icon  
![#57514a](https://img.shields.io/badge/-%2357514a-57514a?style=flat-square) muted text: column heads, small notes, spec labels, FAQ answers

**Reddit Sans**: the only typeface, one variable file for weights 400 to 900: headings at 900 with tight tracking, titles and the main buttons at 700, labels and the small buttons at 600, body at 400 (Google Fonts). A 44px left margin carries a yellow stripe and an ink hairline, with a vertical Same-day print! label hanging in it under the header. Every block is a box with a 1.5px ink border and square corners: the queue, the paper table, the quote form, the FAQ list. Most sections are two-column splits, a heading and lead against a table, photo or form. Tables and rows restack on phones.

## Questions

**Does it work outside the UK?**  
Yes, after a text pass. The layout suits any shop, but the demo is a Leicester shop: prices in pounds, VAT, A-series paper sizes, a postcode and a UK phone number. Replace them, and relabel the size row if you print other formats, keeping seven items.

**Does the quote form send anything?**  
No. It usually opens the visitor's email program with the entered text, addressed to the demo address, so it fails for visitors with no mail app. There is no file upload field. Point the form at Formspree or Netlify Forms, or at your own endpoint.

**Can I get a site like this without editing code?**  
Yes. Describe the shop to [8B's AI website builder](https://8b.com/templates/8b/) and its engine designs a new site, its own design and not this template. Designing and restyling are free; publishing with hosting and SSL, full HTML export and AI edits in chat are on Pro at $9 a month billed yearly. It also runs inside Claude and ChatGPT.

## Is it the right base?

Pick this as the base when the shop sells by quote and over the counter and wants a playful, colourful page. Among print shop website templates, a small press that sells prints online and wants a price calculator fits [a template built around one](https://8b.com/templates/dotdrum/) better. The weak spots: the quote form only opens the visitor's mail app, and the pinned sections make the page long. Owners who do not code can use 8B's builder instead.

## Before you publish

- Replace what is marked `data-8b-placeholder` (social preview image, favicon, email, phone, form) and the invented demo facts; [AGENTS.md](AGENTS.md) lists them.
- The form sends nothing yet: connect it to Formspree or Netlify Forms, or remove it.

## Tech

GSAP 3.13.0, ScrollTrigger, Lenis 1.3.11 from jsDelivr, 100 KB, no build step. Chrome and Edge 108+, Safari 15.4+, Firefox 101+ (it uses cascade layers, small/dynamic viewport units). With "reduce motion" on, the page is complete and still.

## License

MIT, see [LICENSE](LICENSE). Photos, fonts and libraries keep their own licences: [CREDITS.md](CREDITS.md). More free templates: [8b.com/templates](https://8b.com/templates/) · [github.com/8bsite](https://github.com/8bsite).
