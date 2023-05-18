// 接口列表页 增加接口，删除接口，获取接口
const puppeteer = require("puppeteer");
const pageURL = "http://127.0.0.1:8080";

let sleep = (time) =>
  new Promise((r) => {
    setTimeout(r, time);
  });
try {
  (async () => {
    const browser = await puppeteer.launch({
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });
    const page = await browser.newPage();
    await page.goto(pageURL, {
      waitUntil: ["load", "domcontentloaded", "networkidle0", "networkidle2"],
    });
    await page.setViewport({
      width: 1600,
      height: 768 * 2,
    });
    console.log("打开页面");
    await page.click("#fruit-four"); // 点击一个苹果
    await sleep(300);
    await page.click("#fruit-three"); // 点击一个苹果
    await sleep(300);
    let boxLen = await page.$$eval("#box li", (el) => el.length);
    if (boxLen !== 2) {
      console.log("点击2个苹果时 box 中的 li 长度错误");
      process.exit(1);
    }
    //关闭puppeteer
    await page.click("#fruit-six"); // 点击一个菠萝
    await sleep(300);
    let boxLen2 = await page.$$eval("#box li", (el) => el.length);
    if (boxLen2 !== 3) {
      console.log("点击2个苹果一个菠萝 box 中的 li 长度错误");
      process.exit(1);
    }
    await page.click("#fruit-five"); // 再点击一个苹果
    await sleep(300);
    let boxLen3 = await page.$$eval("#box li", (el) => el.length);
    if (boxLen3 !== 1) {
      console.log("点击3个苹果，1个菠萝 box 中的 li 长度错误");
      process.exit(1);
    }
    await page.click("#fruit-two"); //  点击一个菠萝
    await sleep(300);
    await page.click("#fruit-one"); //  点击一个菠萝
    await sleep(300);
    let boxLen4 = await page.$$eval("#box li", (el) => el.length);
    if (boxLen4 !== 0) {
      console.log("点击三个苹果，三个菠萝 box 中的 li 长度错误");
      process.exit(1);
    }

      await page.click('#fruit-eight');// 点击一个牛油果
      await page.click('#fruit-ten') // 点击一个葡萄
      let boxLen5 = await page.$$eval("#box li", (el) => el.length);
      if(boxLen5!==2){
       console.log("点击三个苹果，三个菠萝，一个牛油果，一个葡萄 box 中的 li 长度错误");
        process.exit(1);
      }

    console.log("通过全部检测");
    await browser.close();
  })().catch((err) => {
    console.log(err);
    process.exit(1);
  });
} catch (err) {
  console.log(err);
  process.exit(1);
}
