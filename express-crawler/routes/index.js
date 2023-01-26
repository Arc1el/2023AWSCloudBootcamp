var express = require('express');
var router = express.Router();
const puppeteer = require('puppeteer');
const cheerio = require('cheerio');

async function crawl(){
  const browser = await puppeteer.launch({headless: true});
  const page = await browser.newPage();

  await page.goto('https://wanted.co.kr');

  const content = await page.content();
  const $ = cheerio.load(content);
  const lists = $("body");
  console.log(lists)

  await browser.close();     
};

/* GET home page. */
router.get('/', async function(req, res, next) {
  await crawl() 
  res.render('index', { title: 'Express' });
});

module.exports = router;
