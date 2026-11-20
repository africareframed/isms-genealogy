#!/usr/bin/env bash
# Build the site and publish dist/ to the gh-pages branch (GitHub Pages serves it).
set -euo pipefail
cd "$(dirname "$0")/.."
npx astro build
rm -rf /tmp/isms-pages && cp -r dist /tmp/isms-pages && cd /tmp/isms-pages
git init -q -b gh-pages
git add -A
git -c user.name="Claude" -c user.email="noreply@anthropic.com" commit -q -m "Deploy site $(date -u +%Y-%m-%dT%H:%MZ)"
git push -q --force https://github.com/africareframed/isms-genealogy gh-pages
echo "Deployed to https://africareframed.github.io/isms-genealogy/"
