
document.addEventListener("DOMContentLoaded", function () {
    let form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        let inputs = form.querySelectorAll("input");
        for (let input of inputs) {
            if (input.value.trim() === "") {
                event.preventDefault();
                alert("Por favor, preencha todos os campos.");
                break;
            }
        }
    });
});
