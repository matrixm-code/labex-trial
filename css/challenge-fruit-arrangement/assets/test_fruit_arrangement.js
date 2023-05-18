const puppeteer = require("puppeteer"),
  BlinkDiff = require("blink-diff"),
  imgUrl = __dirname + "/";

try {
  (async () => {
    const browser = await puppeteer.launch({
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 750 });
    await page.goto("http://127.0.0.1:8080/index.html", {
      waitUntil: "networkidle0",
    });
    await page.screenshot({ path: imgUrl + "Screenshots.png", fullPage: true });

    const diff = new BlinkDiff({
      imageAPath: imgUrl + "314482target.png",
      imageBPath: imgUrl + "Screenshots.png",
      threshold: 0.02, // 1% threshold
      imageOutputPath: imgUrl + "Diff.png", //Diff path
    });

    diff.run(function (error, result) {
      if (error) {
        throw error;
      } else {
        let rel = Math.round((result.differences / result.dimension) * 100);
        console.log("Congratulations! you are passed.");
        if (rel > 0) {
          console.error("Sorry! you didn't pass the challenge.");
          process.exit(1);
        }
      }
    });
    await browser.close();
  })();
} catch (err) {
  console.log(err);
}
