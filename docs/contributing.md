# How to contribute

Anyone at TeleCMI can suggest changes. Nothing goes live until a reviewer approves it, just like suggesting mode in Google Docs.

## How a change goes live

1. **Suggest.** Open the page and click the pencil icon (**Edit this page**). GitHub opens the page for editing. Make your change and click **Commit changes…**, then **Propose changes**.
2. **Discuss.** GitHub opens a *pull request*, which is your suggestion. Reviewers comment on it, and you can reply or make more edits.
3. **Approve.** A reviewer approves and merges it. The site updates by itself within about two minutes.

Every past version is kept in GitHub's history, so nothing is ever lost.

## Adding a new screen

1. On GitHub, go to the right folder, for example `docs/connle/users/`.
2. Choose **Add file › Create new file** and name it after the screen, like `add-user.md`.
3. Copy the [screen template](authoring/screen-template.md) into it and fill it in.
4. Upload your screenshot into the folder's `img/` subfolder with **Add file › Upload files**.
5. Add a link to the new page in the area's list (for example `docs/connle/index.md`).
6. Propose the change as above.

## Screenshots

- **Demo account only.** No real customer names, phone numbers, recordings or billing details. Hide them before you capture.
- Capture the full browser window at 100% zoom, in light mode. Crop out browser tabs and your desktop.
- **Numbered markers:** put a numbered circle on every control, matching the rows in the Controls table. Any tool works (Windows Snipping Tool, Paint, Excalidraw). Or save the clean screenshot plus a small `.markers.json` file and run `python tools/annotate.py <file>.markers.json`.

## Writing rules

- Use the **exact label** shown in the product, so search finds it.
- **Describe the effect, not the click.** "Sends missed calls to voicemail after 30 seconds" beats "Click to enable voicemail."
- Write for a new colleague in their first week. Explain product terms the first time you use them.
- If you're not sure how something works, say so in your pull request instead of guessing.

## Reviewers

- Check the screenshot against the live product, then set `status: verified`, `last_checked` and `checked_by` at the top of the page.
- After each release, re-check the screens that changed.
