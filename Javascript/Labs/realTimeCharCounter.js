const textInput = document.getElementById("text-input");
const charCount = document.getElementById("char-count");

const MAX_CHARS = 50;

textInput.addEventListener("input", () => {
    if (textInput.value.length > MAX_CHARS) {
        textInput.value = textInput.value.slice(0, MAX_CHARS);
    }
    
    const currentLength = textInput.value.length;

    charCount.textContent = `Character Count: ${currentLength}/${MAX_CHARS}`;

    if (currentLength === MAX_CHARS) {
        charCount.classList.add("limit-reached");
    } else {
        charCount.classList.remove("limit-reached");
    }
})