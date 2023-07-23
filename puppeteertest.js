#!/usr/bin/node

import puppeteer from 'puppeteer-extra';
import pluginStealth from 'puppeteer-extra-plugin-stealth';
import path from 'node:path'; 
import { fileURLToPath } from 'url';
import fs from 'fs';
import yaml from 'js-yaml'; 

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const getConfig = () => {
    try {
      const fullPath = path.resolve(__dirname, 'config.yaml');
      console.log('fullPath: ', fullPath);
      const filePath = fs.existsSync(fullPath) ? fullPath : defaultFullPath;
      console.log('Reading config from ', filePath);
      const config =  yaml.load(fs.readFileSync(filePath, 'utf8'));
      console.log('Schedule: ', config.cronSchedule);
      return config;
    } catch (e) {
      console.log(e);
      return { storage: {} }
    }
  };
 
(async () => {
  puppeteer.use(pluginStealth()) ;

  const config = getConfig()
  console.log(config.crawler)

  // Launch pupputeer-stealth 
  const browser = await puppeteer.launch({
    headless: false,
    slowMo: 250, // slow down by 250ms
    args: ['--no-sandbox', '--disable-setuid-sandbox']});

  const context = await browser.createIncognitoBrowserContext();
  
  const page = await context.newPage();
  await page.setCacheEnabled(false);
  await page.setUserAgent(config.crawler.userAgent);

  console.log("going to page");
  // Navigate the page to a URL
  await page.goto("https://www.immobilienscout24.de/expose/143404064", { waitUntil: ['domcontentloaded'] });

  // Set screen size
  await page.setViewport({ width: 1080, height: 1024 });

  // Wait for security check
  await page.waitForTimeout(30000);

  await page.screenshot({ path: 'image.png', fullPage: true }); 

  // Type into search box
  console.log("typing in page");

  await browser.close();
})();