# TeleCMI Product Repo

The source for TeleCMI's product documentation site: every screen of Admin Console and Connle, with annotated screenshots. Pages live in `docs/`, and the site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Contributors: read [docs/contributing.md](docs/contributing.md).

## One-time setup (about 15 minutes)

1. **Create the repository.** On GitHub, create a new repository named `telecmi-product-repo` under your organisation, then upload these files. Public repositories get free hosting on GitHub Pages; see "Keeping it private" below.
2. **Point the edit button at it.** In `mkdocs.yml`, replace `YOUR-ORG` in `repo_url` with your GitHub organisation name.
3. **Turn on the site.** Settings › Pages › Source: **GitHub Actions**. The next push publishes the site at `https://YOUR-ORG.github.io/telecmi-product-repo/`.
4. **Name the reviewers.** In `.github/CODEOWNERS`, replace the placeholders with your reviewers' GitHub usernames.
5. **Require review before anything goes live.** Settings › Branches › Add rule for `main`:
    - Require a pull request before merging
    - Require approvals: 1
    - Require review from Code Owners
6. **Add contributors.** Settings › Collaborators and teams: product experts get **Write** access (they can propose changes, but can't merge to `main` without approval). Anyone else can still suggest changes by forking.

## Keeping it private

GitHub Pages on the free plan only publishes **public** repositories. If the docs must stay internal and free:

- Keep the repository private, and host the built site on **Cloudflare Pages** (free: connect the repo, build command `pip install -r requirements.txt && mkdocs build`, output folder `site`).
- Protect it with **Cloudflare Access** (free for up to 50 users), allowing only `@telecmi.com` email addresses.

Check GitHub's and Cloudflare's current free-plan limits before choosing.

## Preview locally (optional)

```
pip install -r requirements.txt
mkdocs serve
```
