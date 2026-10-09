const textInput = document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn");
const resultDiv = document.getElementById("result");

checkBtn.addEventListener("click", () => {
    const inputValue = textInput.value;

    // Si el campo está vacío, se muestra la alerta requerida
    if (inputValue === "") {
        alert("Please input a value");
        return;
    }

    // Elimina caracteres no alfanuméricos (incluye guiones bajos) y convierte a minúsculas
    const cleanedText = inputValue.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();

    // Invierte la cadena limpia
    const reversedText = cleanedText.split("").reverse().join("");

    // Compara el texto limpio con su reverso y muestra el resultado respetando el texto original
    if (cleanedText === reversedText) {
        resultDiv.textContent = `${inputValue} is a palindrome`;
    } else {
        resultDiv.textContent = `${inputValue} is not a palindrome`;
    }
});