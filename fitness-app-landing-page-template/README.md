# Free HTML fitness app landing page template with GSAP scroll animations

Fitness app landing page template: one free HTML file for a training app with adaptive plans and coaching. Rounded panels in a charcoal frame hold a seven-day chart, four coaches, a drawn phone whose screen changes as you scroll, a distance challenge, weekly group runs and three plans. AGENTS.md tells Claude Code or Cursor what to replace and keep.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) ![one HTML file: no build](https://img.shields.io/badge/one%20HTML%20file-no%20build-orange) ![GSAP: ScrollTrigger](https://img.shields.io/badge/GSAP-ScrollTrigger-88ce02)

**[Live demo](https://8bsite.github.io/fitness-app-landing-page-template/)** · **[Use this template](https://github.com/new?template_name=fitness-app-landing-page-template&template_owner=8bsite)** · **[Download ZIP](https://github.com/8bsite/fitness-app-landing-page-template/archive/refs/heads/main.zip)** · **[Template page on 8b.com](https://8b.com/templates/kurvo/)**

<a href="https://8bsite.github.io/fitness-app-landing-page-template/"><img src="previews/desktop.png" alt="Fitness app website template: first screen on a desktop" width="76.1%"></a> <a href="https://8bsite.github.io/fitness-app-landing-page-template/"><img src="previews/phone.png" alt="Fitness app website template: first screen on a phone" width="21.9%"></a>

<p align="center"><a href="https://8bsite.github.io/fitness-app-landing-page-template/"><img src="previews/scroll.gif" alt="Fitness app website template: scrolling through the first sections" width="40%"></a><br><sub>Scroll animation</sub></p>

## Use it with Claude Code, Cursor or Codex

Download the four files into your project folder (`curl.exe` in Windows PowerShell):

```bash
curl -LO https://raw.githubusercontent.com/8bsite/fitness-app-landing-page-template/main/index.html
curl -LO https://raw.githubusercontent.com/8bsite/fitness-app-landing-page-template/main/AGENTS.md
curl -LO https://raw.githubusercontent.com/8bsite/fitness-app-landing-page-template/main/LICENSE
curl -LO https://raw.githubusercontent.com/8bsite/fitness-app-landing-page-template/main/CREDITS.md
```

Then fill in the angle brackets and give your agent this prompt:

```text
Read AGENTS.md, then edit index.html. Make it the landing page for <my fitness app: name, how it adapts training, disciplines, coaches, publishable member results, challenge, clubs, plans and prices, store and sign-up links, contacts, company name>. Replace first the name, week chart, coaches, member stories, prices and every #get-app button. Keep the classes AGENTS.md lists, three phone screens with three notes and five route checkpoints; make every --len match its line's character count. Ask me for anything missing; never invent prices, member numbers, results, coach credentials or store links.
```

For vibe coding with Claude Code or Cursor, give the agent your app's facts first: the demo invents every one, down to 200 coaches and 18,000 members. The week chart lives in two places: each day's --cv-h height and the line's seven points. The script pairs three phone screens with three notes, so keep both. Five checkpoints sit on the route; a new count means changing the path, their positions and the script's point list together. Replace the third story's avatar, cropped from a crowd photo.

No agent? Click **[Use this template](https://github.com/new?template_name=fitness-app-landing-page-template&template_owner=8bsite)**, edit `index.html` on GitHub and turn on **Settings > Pages**.

## Sections and motion

- **Navigation**: fixed top bar: logo in a dark corner tab, four section links, Get the app button; hides on scroll down; full-screen menu on phones. The bar slides away while you scroll down and returns when you scroll back up; after 400 px its link pill turns charcoal and its Get the app button turns lime.
- **Plans that bend**: first screen: the h1, a lead, three cues as pills with a line each, a button, and a seven-day bar chart with a line over the bar tops. On load the headline opens from condensed to extended letters and the seven bars, starting nearly level and grey, grow or shrink to their minutes and take their colours one after another; on screens 768 px and wider the line over them draws itself.
- **Coaches who know you**: four coaches as large overlapping round portraits with name, discipline pill and one line; lime Find my coach button. The heading stretches open as the panel arrives, and each discipline pill drops in tilted, then settles level with a bounce.
- **Train anything**: four disciplines as full-width pill rows: big name, weekly class count, one line and a photo. Scrubbed with the scroll, the four rows come in lower, tilted, shifted sideways and clipped short, then level out, line up and open to show the class count, text and photo.
- **One screen, whole week**: a phone drawn in CSS with three app views (today's session, recovery score, coach chat) beside three notes on a timeline. The phone stays in view while you scroll past three notes, the second and third screens wiping up over the one before as a lime dot marks the matching note; on phones it is held for about a screen of scrolling, then the notes follow.
- **Real people, real curves**: three member stories: a small result curve with a lime result tag, a quote, an avatar, a name and how long they have been members. As each card arrives its sparkline draws itself from left to right and its lime result tag drops in and settles.
- **The October hundred**: a monthly 100 km challenge: a route with five checkpoints and rewards, a photo with an arched top and a lime join button. Scrubbed: the route draws itself while a lime dot rides along it, each checkpoint lighting up as the dot passes; on phones the route runs down beside the list.
- **Sunday clubs**: weekly free group runs: a photo and a list of six cities, each with a meeting point and a start time. The heading stretches open, and the six start time pills drop in with a bounce as they reach the screen.
- **Pick your plan**: three plans side by side with the same five rows: a free one, the recommended one in lime, and one for two people. Scrubbed: on wide screens the three plans start stacked and fanned over the middle card and spread into a row; up to 900 px they start pulled up onto the first card and slide apart downward.
- **Questions, answered**: questions and answers (native &lt;details&gt;) beside a short intro with a link to contact. The heading stretches open on arrival; the round plus beside each question turns into a cross when the answer opens and fills lime on hover.
- **Let's move**: lime contact panel: lead, Get the app button, email, phone, address, three social links and a Write to us corner tab (contacts are placeholders). Scrubbed as the panel rises into view, a graphite shade covering most of it shrinks into the upper left corner and leaves the panel lime.
- **Footer**: the wordmark across the full width, copyright with the Design: 8B credit, six links and a tagline. The full-width wordmark opens from condensed to extended letters as it reaches the screen.

## Design

![#232323](https://img.shields.io/badge/-%23232323-232323?style=flat-square) charcoal frame and footer, corner tabs, dark buttons, the drawn phone, text on light panels, the line over the chart bars  
![#c5d8d8](https://img.shields.io/badge/-%23c5d8d8-c5d8d8?style=flat-square) mint: the app and run club panels, the HIIT row, member story cards, the free plan card, the rows, ring track and coach's bubbles inside the phone  
![#f2f4f5](https://img.shields.io/badge/-%23f2f4f5-f2f4f5?style=flat-square) off-white: the first screen, member stories and pricing panels, the Cycling row, the phone's screen, text on graphite and charcoal  
![#8d91e6](https://img.shields.io/badge/-%238d91e6-8d91e6?style=flat-square) lilac: the disciplines panel, the regular chart bars, the session card, recovery ring and your own chat bubbles in the phone, sparklines, the challenge route  
![#d8f45f](https://img.shields.io/badge/-%23d8f45f-d8f45f?style=flat-square) lime: today's bar, the recommended plan, the contact panel, the small filled tags (class counts, member results, Today and Ready in the phone) and the buttons on dark panels, the challenge dot and checkpoints, the active note marker  
![#444444](https://img.shields.io/badge/-%23444444-444444?style=flat-square) graphite: the coaches, challenge and questions panels, the Strength and Yoga rows, the two-person plan, coach portrait rings, the contact shade  
![#a4c3bd](https://img.shields.io/badge/-%23a4c3bd-a4c3bd?style=flat-square) sage: the bars of the easy days in the week chart  
![#c2c2c2](https://img.shields.io/badge/-%23c2c2c2-c2c2c2?style=flat-square) light grey: secondary text on graphite panels, the dashed ghost route, unlit checkpoints, rules between questions, footer text, and the grey the chart bars start from  
![#4f5552](https://img.shields.io/badge/-%234f5552-4f5552?style=flat-square) dark grey-green: day labels and caption under the chart, the rest day's dashed outline, membership lengths, meeting points, the price note

**TikTok Sans**: display face at weights 500 and 600 with a width axis: the very wide uppercase headings and footer wordmark, discipline names, subheads, button labels, pills and tags, prices, the recovery number, the contact lines. **Geist**: text face at weights 400 and 500: body copy and leads, small uppercase labels such as the nav links and day names, text links, member quotes (Google Fonts). A charcoal frame shows in 12 px gaps around rounded panels, each in one flat colour. From the second section on, each panel's heading sits in a charcoal corner tab cut into its upper left with a slanted edge; the logo uses the same tab, and the contact panel ends with a mirrored one at the lower right. Pills repeat: chart bars, discipline rows, badges, buttons. Most sections pair two columns, for example the route beside an arched photo.

## Questions

**Where do the Get the app and plan buttons lead?**  
To the plans list. With no store badges, QR code or sign-up form, Get the app, Start free, Try Pro free, Try Duo free, Find my coach and Join the hundred all point to #get-app. As a download app landing page, it needs your store and sign-up links; a waitlist needs a form wired to Formspree or Netlify Forms.

**How does it behave on phones, with reduced motion or with JavaScript off?**  
Up to 900 px the nav links fold into a menu button; on phones chart days become rows with sideways bars. Reduced motion stops smooth scrolling, entrance and scroll animations and lists the three phone screens one under another; hover effects and the hiding nav bar stay. Without JavaScript the menu cannot open; the six footer links and questions work.

**Can I build a fitness website without editing code?**  
Yes: describe the site in a sentence and [8B's AI website builder](https://8b.com/templates/8b/) designs a new one, not this template. Designing and restyling are free; publishing with hosting and SSL, full HTML export and AI edits in chat are on Pro at $9 a month billed yearly. It also runs inside Claude and ChatGPT through the 8B connector.

## Is it the right base?

Choose this as your fitness landing page when you sell a training app with free and paid plans, coaches, challenges and group runs. An app outside fitness, shown feature by feature, sits better on the [captioning app](https://8b.com/templates/linea/) template. Two weak spots: with no store badges or QR code, every Get the app, plan, Find my coach and Join the hundred button stops at the plans list, and the copy promises five disciplines beside four rows. Set real links and match the count before launch.

## Before you publish

- Replace what is marked `data-8b-placeholder` (social preview image, favicon, email, phone, social) and the invented demo facts; [AGENTS.md](AGENTS.md) lists them.

## Tech

GSAP 3.13.0, ScrollTrigger, Lenis 1.3.27 from jsDelivr, 85 KB, no build step. Chrome and Edge 108+, Safari 15.4+, Firefox 121+ (it uses :has(), cascade layers, small/dynamic viewport units). With "reduce motion" on, the page is complete and still.

## License

MIT, see [LICENSE](LICENSE). Photos, fonts and libraries keep their own licences: [CREDITS.md](CREDITS.md). More free templates: [8b.com/templates](https://8b.com/templates/) · [github.com/8bsite](https://github.com/8bsite).
