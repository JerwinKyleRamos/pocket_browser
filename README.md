# Pocket Browser

A small installable web app for collecting links instead of re-searching for them. Paste a URL, file it into a folder, and it's there next time you open the app.

No build step, no dependencies, no backend — it's three files plus a folder of icons.

## Files

```
index.html       the whole app (markup, styles, and logic)
manifest.json    makes it installable (name, icons, colors)
sw.js            service worker — caches the app shell for offline use
icons/           app icons used by the manifest and browser tab
```

## Run it locally

Opening `index.html` directly (`file://...`) won't let the service worker register, so serve it over a local server instead:

```bash
python3 -m http.server 8000
# or
npx serve .
```

Then visit `http://localhost:8000`.

## How data is stored

Everything lives in the browser's `localStorage` — no login, no server, no sync between devices. That keeps the app dependency-free, but it does mean:
- Clearing your browser's site data clears your collection.
- It won't follow you to a different browser or device.

If you want real sync later, the natural next step is swapping the `LocalStore` object in `index.html` for calls to a backend of your choice (Firebase, Supabase, a small API of your own, etc.) — everything else in the app talks to storage through that one object, so it's a contained change.
