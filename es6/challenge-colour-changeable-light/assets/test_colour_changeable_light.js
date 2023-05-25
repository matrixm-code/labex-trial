const puppeteer = require("puppeteer");

try {
  (async () => {
    const browser = await puppeteer.launch({
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 600, height: 400 });
    let url = `http://127.0.0.1:8080/index.html`;
    await page.goto(url, {
      waitUntil: "networkidle0",
    });

    let redlightDisplay, greenlightDisplay, defaultlightDisplay; //红绿灯像是否显示
    await page.waitForTimeout(4000);
    let defaultlightEle = await page.$("#defaultlight");
    if (!defaultlightEle) {
      console.log("no found #defaultlight.");
      process.exit(1);
    }
    defaultlightDisplay = await page.$eval(
      "#defaultlight",
      (e) => e.style.display
    );
    let redlight = await page.$("#redlight");
    if (!redlight) {
      console.log("no found #redlight.");
      process.exit(1);
    }
    redlightDisplay = await page.$eval("#redlight", (e) => e.style.display);

    if (
      defaultlightDisplay == "none" &&
      (redlightDisplay == "block" || redlightDisplay == "inline-block")
    ) {
      console.log("Red light test passed.");
    } else {
      console.log("Failed red light test.");
      process.exit(1);
    }
    await page.waitForTimeout(3000);
    redlight = await page.$("#redlight");
    if (!redlight) {
      console.log("no found #redlight.");
      process.exit(1);
    }
    redlightDisplay = await page.$eval("#redlight", (e) => e.style.display);
    let greenlight = await page.$("#greenlight");
    if (!greenlight) {
      console.log("no found #greenlight.");
      process.exit(1);
    }
    greenlightDisplay = await page.$eval("#greenlight", (e) => e.style.display);
    if (
      redlightDisplay == "none" &&
      (greenlightDisplay == "block" || greenlightDisplay == "inline-block")
    ) {
      console.log("Congratulations! you are passed.");
    } else {
      console.log("Sorry! you didn't pass the challenge.");

      process.exit(1);
    }
    await browser.close();
  })();
} catch (err) {
  console.log("An exception was caught with the following message:");
  console.log(err);

  process.exit(1);
}
