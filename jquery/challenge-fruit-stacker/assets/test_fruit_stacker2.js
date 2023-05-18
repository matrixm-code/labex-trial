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
    // 点2个苹果
    await page.click("#fruit-four"); // 点击一个苹果
    await sleep(300);
    await page.click("#fruit-three"); // 点击一个苹果
    // 在点击2个菠萝
    await page.click("#fruit-six"); // 点击一个菠萝
    await page.click("#fruit-one"); //  点击一个菠萝
    // 点击一个牛油果
    await page.click("#fruit-eight"); //  点击一个牛油果
    // 再点击2个葡萄
    await page.click("#fruit-ten"); //  点击一个葡萄
    await page.click("#fruit-twelve"); //  点击一个葡萄
    await sleep(300);
    let boxLen5 = await page.$$eval("#box li", (el) => el.length);
    if (boxLen5 !== 7) {
      console.log("没有可消除项时，box 中的 li 长度不正确");
      process.exit(1)
    }
    await page.click("#fruit-nine"); //  点击一个牛油果
    await sleep(300);
    let boxLen6 = await page.$$eval("#box li", (el) => el.length);
    if (boxLen5 !== 7) {
      console.log("超过7个无可消除选项时，再次点击水果 box 中的 li 长度不正确");
      process.exit(1)
    }
    console.log('全部检测通过')
    await browser.close();
  })().catch((err) => {
    console.log(err);
    process.exit(1);
  });
} catch (err) {
  console.log(err);
  process.exit(1);
}
