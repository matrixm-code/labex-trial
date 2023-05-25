const puppeteer = require("puppeteer");

try {
  (async () => {
    const browser = await puppeteer.launch({
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });
    const page = await browser.newPage();
    await page.goto("http://127.0.0.1:8080/index.html", {
      waitUntil: "networkidle0",
    });

    await page.$eval("#color1", (el) => {
      el.value = "#fafa6e";
      el.dispatchEvent(new Event("change"));
    });
    await page.$eval("#color2", (el) => {
      el.value = "#089f8f";
      el.dispatchEvent(new Event("change"));
    });

    const style = await page.$eval(
      ".gradient",
      (el) => el && JSON.parse(JSON.stringify(window.getComputedStyle(el)))
    );

    if (
      !style.background.includes("rgb(8, 159, 143)") ||
      !style.background.includes("rgb(250, 250, 110)")
    ) {
      console.error("Sorry! you didn't pass the challenge.");
      process.exit(1);
    }

    await browser.close();
  })();
} catch (err) {
  console.log(err);
}
