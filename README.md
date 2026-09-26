# Liu Tao — personal website

A static, bilingual portfolio for the tools behind [github.com/LiuTianjie](https://github.com/LiuTianjie).

## Edit and preview

The English and Chinese copy and shared HTML template live in `scripts/build-site.py`. After editing:

```sh
python3 scripts/build-site.py
python3 -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173/` or `/zh.html`. Commit both generated HTML files. The website itself has no build-time dependency on GitHub Pages and remains readable without JavaScript; JavaScript only handles the install-command copy button.

- `css/main.css`: shared responsive styles, system dark mode, and reduced-motion support.
- `img/projects/`: existing project logos and real product screenshots.
- `img/fonts/`: self-hosted Manrope and Instrument Serif with their OFL licenses.
- `404.html`: a direct path back to the portfolio for missing pages.

## Publish

GitHub Pages serves the repository root from `master`. Push reviewed source and generated pages to that branch, then verify the Pages build and both public language URLs.

Keep product claims aligned with the linked repositories. Screenshots illustrate the captured UI; the Luma manifest is explicitly an example. Do not add placeholder usage counts, testimonials, release dates, or unverified platform support.
