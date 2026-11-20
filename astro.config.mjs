import { defineConfig } from 'astro/config';

// Every page is built as a flat .html file at the site root, with styles inlined
// and links written relative (see src/lib/site.ts). The same build then works
// as a private preview artifact, on GitHub Pages under any path, or on a domain.
export default defineConfig({
  build: {
    format: 'file',
    inlineStylesheets: 'always',
  },
  devToolbar: { enabled: false },
});
