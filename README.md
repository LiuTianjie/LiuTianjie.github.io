# Liu Tao — personal website

A concise, bilingual resume-style homepage. The layout deliberately follows the original site: one readable column, system typography, brief experience, project lists, and contact links.

## Edit and preview

English and Chinese content and the shared HTML template live in `scripts/build-site.py`:

```sh
python3 scripts/build-site.py
python3 -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173/` or `/zh.html`. Commit both generated pages after editing. There is no JavaScript or external font dependency. The shared CSS includes system dark mode, mobile layout, and a print stylesheet.

## Publish

GitHub Pages serves the repository root from `master`. Push reviewed changes, then verify the Pages build and both language URLs.

Keep experience factual, project descriptions brief, and product claims aligned with their repositories. Preserve the resume style; avoid promotional hero sections, oversized slogans, decorative cards, or invented achievements.
