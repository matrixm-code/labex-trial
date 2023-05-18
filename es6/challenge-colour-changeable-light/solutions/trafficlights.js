let trafficlightsTimer = 3000;
// red light
function red() {
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      defaultlight.style.display = "none";
      redlight.style.display = "inline-block";
      resolve();
    }, trafficlightsTimer);
  });
}
// green light
function green() {
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      redlight.style.display = "none";
      greenlight.style.display = "inline-block";
      resolve();
    }, trafficlightsTimer);
  });
}

async function trafficlights() {
  await red();
  await green();
}

trafficlights();
module.exports = { trafficlights };
