# Chloe + Sam — Wedding Website

**Live:** <https://wedding-website-phi-sandy.vercel.app> (Vercel project
`wedding-website`, account samharris26-4273). Deploys are made from an
optimized bundle (downscaled images, subset font — built by the deploy step,
not committed here); the full-resolution originals stay in `assets/`.

Public-facing landing page for the Summer 2027 wedding, styled to match the
hand-drawn "scribble" illustration pack bought on Canva (Pipi Scribble
Collection + Signature Drinks).

## Structure

- `index.html` — the landing page (single page, no build step). Contains two
  custom inline SVGs drawn in the pack's style: the hero **tipi scene**
  (tipis, festoon lights along the lane, mini helter skelter) and the
  **helter skelter** card illustration.
- `styles.css` — cream paper / black ink / yellow-highlighter theme.
  Fonts: Permanent Marker (headings), Architects Daughter (body), Caveat (script).
- `assets/illustrations/` — 67 curated transparent PNGs, individually cut out
  of the Canva pack pages with friendly names (e.g. `champagne-clink.png`,
  `heart-marry-me.png`, `just-married-car.png`). Reuse these anywhere.
- `assets/sprites/` — every auto-extracted sprite from all pack pages
  (`<page>--NN.png` + `<page>.json` bounding boxes), in case something else
  is needed later.
- `assets/source/` — full-page PNG exports of the five Canva designs.

## Previewing

From this folder: `python3 -m http.server 8642` then open
<http://localhost:8642>. (The `.claude/launch.json` preview serves a mirror
from the session scratchpad because macOS doesn't let the preview panel's
processes read ~/Documents.)

## Framing

The ceremony happens privately with family a few days before; the site sells
**the party** (12th June 2027 is a sample date until the real one is chosen).

## Sample content (swap for real details as decisions land)

Sections marked with a dashed "sample" stamp on the page contain placeholder
content: the date (12th June 2027), the running-order times, the venue
("the tipi field" + sketch map), travel/stay, the bar's signature drinks,
dress code, the RSVP form (not wired to a backend yet), and the FAQs.
