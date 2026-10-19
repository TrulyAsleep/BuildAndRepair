// Re-render the Workshop images from images.html.
//   npm install playwright && npx playwright install chromium
//   node render.cjs <output-dir>
// Set CHROME_PATH to use an existing Chromium instead of Playwright's download.
const path = require('path');
const { chromium } = require('playwright');

const pages = [
  { name: 'thumb', w: 1024, h: 1024 },
  { name: 'updated', w: 1920, h: 1080 },
  { name: 'features', w: 1920, h: 1080 },
  { name: 'dropin', w: 1920, h: 1080 },
];

(async () => {
  const outDir = process.argv[2] || __dirname;
  const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  for (const p of pages) {
    const page = await browser.newPage({ viewport: { width: p.w, height: p.h } });
    await page.goto('file://' + path.join(__dirname, 'images.html') + '?page=' + p.name);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(outDir, p.name + '.png') });
    console.log('rendered', p.name);
    await page.close();
  }
  await browser.close();
})();
