// Historia de usuario 1: Selección de elementos principales
const regexPattern = document.getElementById("pattern");
const stringToTest = document.getElementById("test-string");
const testButton = document.getElementById("test-btn");
const testResult = document.getElementById("result");

// Historia de usuario 2: Selección de casillas de verificación de banderas
const caseInsensitiveFlag = document.getElementById("i");
const globalFlag = document.getElementById("g");

// Historia de usuario 3: Función para obtener las banderas seleccionadas
function getFlags() {
    let flags = "";
    if (caseInsensitiveFlag.checked) {
        flags += "i";
    }
    if (globalFlag.checked) {
        flags += "g";
    }
    return flags;
}

// Historias de usuario 4, 5 y 6: Escuchador de eventos al hacer clic en el botón
testButton.addEventListener("click", () => {
    const pattern = regexPattern.value;
    const flags = getFlags();
    const text = stringToTest.textContent;

    if (!pattern) {
        testResult.textContent = "no match";
        return;
    }

    try {
        const regex = new RegExp(pattern, flags);
        const matches = text.match(regex);

        if (matches) {
            // Historia de usuario 4: Resalta las coincidencias agregando la clase "highlight"
            stringToTest.innerHTML = text.replace(regex, '<span class="highlight">$&</span>');

            // Historia de usuario 5: Muestra las coincidencias separadas por coma y espacio
            testResult.textContent = matches.join(", ");
        } else {
            // Historia de usuario 6: Muestra "no match" cuando no hay coincidencias
            stringToTest.innerHTML = text;
            testResult.textContent = "no match";
        }
    } catch (error) {
        testResult.textContent = "no match";
    }
});