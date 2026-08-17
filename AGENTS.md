# Repository guide

- Use the checked-in `./arbor`; do not add Node.js, CSS frameworks, or another build step.
- Prefer semantic HTML and existing Ivy/Lattice styles; check `STYLEREF.md` before adding custom CSS or JavaScript.
- Do not edit generated site data or commit `public/`. Validate the production build with `docker build --platform linux/amd64 --file container/Dockerfile .`; it runs data sync and Arbor checks without modifying the checkout.
