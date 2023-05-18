const puppeteer = require("puppeteer"),
    BlinkDiff = require("blink-diff"),
    imgUrl = __dirname + "/";

try {
    (async () => {
        const browser = await puppeteer.launch({
            args: ["--no-sandbox", "--disable-setuid-sandbox"],
        });
        const page = await browser.newPage();
        await page.setViewport({ width: 600, height: 400 });
        await page.goto("http://127.0.0.1:8080/index.html", {
            waitUntil: "networkidle0",
        });
        // clear all alert
        page.evaluate(() => (alert = null));
        let box1 = await page.$("#box1");
        await box1.screenshot({
            path: `${imgUrl}box1.png`,
        });
        let box2 = await page.$("#box2");
        await box2.screenshot({
            path: `${imgUrl}box2.png`,
        });
        let box3 = await page.$("#box3");
        await box3.screenshot({
            path: `${imgUrl}box3.png`,
        });

        const imgDiff = (img, targetImg, diffImg) => {
            return new BlinkDiff({
                imageAPath: imgUrl + img,
                imageBPath: imgUrl + targetImg,
                threshold: 0.02, // 1% threshold
                imageOutputPath: imgUrl + diffImg,
            });
        };

        let diff1 = imgDiff("box1.png", "box1Target.png", "Diff1.png");
        let diff2 = imgDiff("box2.png", "box2Target.png", "Diff2.png");
        let diff3 = imgDiff("box3.png", "box3Target.png", "Diff3.png");

        let runcheckdiff = (difffn, index) => {
            return new Promise((reslove, reject) => {
                difffn.run(function (error, result) {
                    if (error) {
                        throw error;
                    } else {
                        let rel = Math.round((result.differences / result.dimension) * 100);
                        if (rel > 0) {
                            reject(`The ${index} picture does not pass the test.`);
                        } else {
                            reslove(index);
                        }
                    }
                });
            });
        };

        async function checkDiff() {
            await runcheckdiff(diff1, 1);
            await runcheckdiff(diff2, 2);
            await runcheckdiff(diff3, 3);
        }
        checkDiff().then(
            (_res) => {
            },
            (err) => {
                console.error(`The test failed because ${err}`);
                process.exit(1);
            }
        );

        await browser.close();
    })().catch((err) => {

        console.error(`The test failed because ${err}`);
        process.exit(1);
    });
} catch (err) {
    console.error(`The test failed because ${err}`);
    process.exit(1);
}
