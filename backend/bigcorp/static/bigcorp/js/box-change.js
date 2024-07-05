const boxes = document.querySelectorAll(".box");

boxes.forEach((box) => {
  box.addEventListener("mouseover", () => {
    const boxColor = getComputedStyle(box).getPropertyValue("background-color");
    document.body.style.backgroundColor = boxColor;
    const welcome = document.getElementById("welcome");
    welcome.innerText = `Welcome to ${box.innerHTML}`;
  });

  box.addEventListener("mouseout", () => {
    document.body.style.backgroundColor = "#000000";
    const welcome = document.getElementById("welcome");
    welcome.innerText = "Welcome to BigCorp";
  });
});
