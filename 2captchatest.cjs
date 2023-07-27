const puppeteer = require('puppeteer-extra')

// add stealth plugin and use defaults (all evasion techniques)
const StealthPlugin = require('puppeteer-extra-plugin-stealth')
puppeteer.use(StealthPlugin())

const fakeUa = require('fake-useragent');
console.log(fakeUa());

const executablePath = '/snap/bin/chromium'; // Replace this with the path to your Chrome executable

puppeteer.launch({ executablePath: executablePath }).then(async browser => {

	// Create a new page 
	const page = await browser.newPage(); 
 
	// Setting page view 
	await page.setViewport({ width: 1280, height: 720 }); 

    // page set
    await page.setUserAgent(fakeUa())

	// Go to the website 
	await page.goto('https://www.immobilienscout24.de/expose/143404064#/'); 

    	// Wait for security check 
	await page.waitForTimeout(10000); 
 
	await page.screenshot({ path: 'image.png', fullPage: true }); 
 
	await browser.close(); 
});