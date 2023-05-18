const puppeteer = require("puppeteer");
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
        /*item1 */
        const elem1 = await page.$("#item1");
        const val1 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elem1);
        /*console.log("item1:" + val1.transform);*/
        /*item5 */
        const elem5 = await page.$("#item5");
        const val5 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elem5);
        /*console.log("item5:" + val5.transform);*/
        /*item11 */
        const elem11 = await page.$("#item11");
        const val11 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elem11);
        /*console.log("item11:" + val11.transform);*/
        if (
            val1.transform == "none" &&
            val5.transform == "none" &&
            val11.transform == "none"
        ) {
            console.log("The Element have hover.");
        } else {
            console.error("Element without hover.");
            process.exit(1);
        }
        /* When the mouse hovers over an element */
        await page.hover("#box");
        await page.waitForTimeout(5000);
        /*item1 */
        const elemHandle1 = await page.$("#item1");
        const style1 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle1);
        /*console.log("item1:" + style1.transform);*/
        /*item2 */
        const elemHandle2 = await page.$("#item2");
        const style2 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle2);
        /*console.log("item2:" + style2.transform);*/
        /*item3 */
        const elemHandle3 = await page.$("#item3");
        const style3 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle3);
        /*console.log("item3:" + style3.transform);*/
        /*item4 */
        const elemHandle4 = await page.$("#item4");
        const style4 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle4);
        /*console.log("item4:" + style4.transform);*/
        /*item5 */
        const elemHandle5 = await page.$("#item5");
        const style5 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle5);
        /*console.log("item5:" + style5.transform);*/
        /*item6 */
        const elemHandle6 = await page.$("#item6");
        const style6 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle6);
        /*console.log("item6:" + style6.transform);*/
        /*item7 */
        const elemHandle7 = await page.$("#item7");
        const style7 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle7);
        /*console.log("item7:" + style7.transform);*/
        /*item8 */
        const elemHandle8 = await page.$("#item8");
        const style8 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle8);
        /*console.log("item8:" + style8.transform);*/
        /*item9 */
        const elemHandle9 = await page.$("#item9");
        const style9 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle9);
        /*console.log("item9:" + style9.transform);*/
        /*item10 */
        const elemHandle10 = await page.$("#item10");
        const style10 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle10);
        /*console.log("item10:" + style10.transform);*/
        /*item11 */
        const elemHandle11 = await page.$("#item11");
        const style11 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle11);
        /*console.log("item11:" + style11.transform);*/
        /*item12 */
        const elemHandle12 = await page.$("#item12");
        const style12 = await page.evaluate((x) => {
            return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
        }, elemHandle12);
        /*console.log("item12:" + style12.transform);*/

        if (
            style1.transform == "matrix(0.5, -0.866025, 0.866025, 0.5, 0, 0)" &&
            style2.transform ==
            "matrix(0.642788, -0.766044, 0.766044, 0.642788, 0, 0)" &&
            style3.transform ==
            "matrix(0.766044, -0.642788, 0.642788, 0.766044, 0, 0)" &&
            style4.transform == "matrix(0.866025, -0.5, 0.5, 0.866025, 0, 0)" &&
            style5.transform ==
            "matrix(0.939693, -0.34202, 0.34202, 0.939693, 0, 0)" &&
            style6.transform ==
            "matrix(0.984808, -0.173648, 0.173648, 0.984808, 0, 0)" &&
            style7.transform ==
            "matrix(0.984808, 0.173648, -0.173648, 0.984808, 0, 0)" &&
            style8.transform ==
            "matrix(0.939693, 0.34202, -0.34202, 0.939693, 0, 0)" &&
            style9.transform == "matrix(0.866025, 0.5, -0.5, 0.866025, 0, 0)" &&
            style10.transform ==
            "matrix(0.766044, 0.642788, -0.642788, 0.766044, 0, 0)" &&
            style11.transform ==
            "matrix(0.642788, 0.766044, -0.766044, 0.642788, 0, 0)" &&
            style12.transform == "matrix(0.5, 0.866025, -0.866025, 0.5, 0, 0)"
        ) {
            console.log("Congratulations! you are passed.");
        } else {
            console.error("Sorry! you didn't pass the challenge.");
            process.exit(1);
        }
        await browser.close();
    })();
} catch (err) {
    console.log(err);
}
