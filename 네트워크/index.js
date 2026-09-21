let n = 0;

    const num = document.getElementById("num");
    const numInput = document.getElementById("b2");
    const increase = document.getElementById("b1");

    increase.addEventListener("click", function () {
        n = n + 1;
        num.innerHTML = n;
        numInput.value = n;
    });