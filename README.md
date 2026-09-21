# Pocket Browser

A small installable web app for collecting links instead of re-searching for them. Paste a URL, file it into a folder, and it's there next time you open the app.

The web app has no build step, no dependencies and no backend. The optional desktop wrapper (see below) packages the same files as a standalone app.

## Files

```
index.html       the whole app (markup, styles, and logic)
manifest.json    makes it installable (name, icons, colors)
sw.js            service worker — caches the app shell for offline use
icons/           app icons used by the manifest and browser tab
electron/main.js desktop app entry point (window, external-link handling)
package.json     desktop app metadata and installer build config
```

## Run it locally

Opening `index.html` directly (`file://...`) won't let the service worker register, so serve it over a local server instead:

```bash
python3 -m http.server 8000
# or
npx serve .
```

Then visit `http://localhost:8000`.

## Deploy on GitHub Pages

1. Create a repo and push these files to the root (or a `/docs` folder — either works, GitHub Pages serves plain static files with no build step).
2. In the repo: **Settings → Pages** → set the source to that branch/folder → save.
3. GitHub gives you a URL like `https://yourname.github.io/pocket-browser/`. Open it — since it's served over HTTPS with a manifest and service worker, your browser will offer to install it (an install icon in the address bar on desktop Chrome/Edge, or the in-app "Install app" button that appears once the browser's ready; on iOS Safari, use Share → Add to Home Screen).

## Desktop app (standalone)

The desktop build wraps the same `index.html` in Electron, so it runs as its own app with no localhost server and no browser.

```bash
npm install
npm start          # run the desktop app
npm run dist       # build installers into ./dist for your current OS
```

Saved links open in your default browser. Data lives in the app's own storage, separate from the browser/PWA version, so links saved there don't carry over.

### Releasing

Bump `version` in `package.json`, commit, then tag and push:

```bash
git tag v0.0.1
git push origin v0.0.1
```

The `Release desktop app` GitHub Action builds Windows, macOS and Linux installers and attaches them to a **draft** release. Review it on the Releases page and publish. Builds are unsigned, so Windows SmartScreen and macOS Gatekeeper will show a warning on first launch.

## How data is stored

Everything lives in the browser's `localStorage` — no login, no server, no sync between devices. That keeps the app dependency-free, but it does mean:
- Clearing your browser's site data clears your collection.
- It won't follow you to a different browser or device.

If you want real sync later, the natural next step is swapping the `LocalStore` object in `index.html` for calls to a backend of your choice (Firebase, Supabase, a small API of your own, etc.) — everything else in the app talks to storage through that one object, so it's a contained change.

## Customizing

- Colors, fonts, and layout are all in the `<style>` block at the top of `index.html` (CSS custom properties under `:root`, with a dark-mode override below).
- Regenerate the icons with `python3 make_icons.py` if you change the color palette (requires Pillow: `pip install pillow`).
