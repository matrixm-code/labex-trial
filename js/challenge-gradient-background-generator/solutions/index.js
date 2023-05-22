const inputs = document.querySelectorAll(".controls input");
var root = document.querySelector(":root");

for (let index = 0; index < inputs.length; index++) {
  const input = inputs[index];
  input.onchange = function (e) {
    root.style.setProperty(`--${e.target.id}`, this.value);
  };
}
