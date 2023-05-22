const puppeteer = require("puppeteer"),
  BlinkDiff = require("blink-diff"),
  imgUrl = __dirname + "/";

try {
  (async () => {
    const browser = await puppeteer.launch({
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1024, height: 120 });
    await page.goto("http://127.0.0.1:8080/index.html");
    await page.screenshot({ path: imgUrl + "Screenshots.png", fullPage: true });

    const diff = new BlinkDiff({
      imageAPath: imgUrl + "157483target.png",
      imageBPath: imgUrl + "Screenshots.png",
      imageOutputPath: imgUrl + "Diff.png",
    });

    diff.run(function (error, result) {
      if (error) {
        throw error;
      } else {
        let rel = Math.round((result.differences / result.dimension) * 100);
        if (rel > 15) {
          console.log("Sorry! you didn't pass the challenge.");
          process.exit(1);
        }
      }
    });
    await browser.close();
  })();
} catch (err) {
  console.log(err);
}
