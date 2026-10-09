// 1. Evento para cuando se hace clic con el ratón
const drumPads = document.querySelectorAll('.drum-pad');

drumPads.forEach(pad => {
    pad.addEventListener('click', () => {
        const audio = pad.querySelector('.clip');

        if (audio) {
            // Reproducir audio directamente
            audio.currentTime = 0;
            audio.play();

            // Actualizar el display
            const display = document.getElementById('display');
            display.innerText = pad.id.replace(/-/g, ' ');

            // Efecto visual
            pad.classList.add('active');
            setTimeout(() => pad.classList.remove('active'), 100);
        }
    });
});

// 2. Evento para cuando se presiona una tecla (Testeado para FreeCodeCamp)
document.addEventListener('keydown', function (event) {
    // Asegurarnos de capturar la tecla y ponerla en mayúscula
    const key = event.key ?
        event.key.toUpperCase() :
        String.fromCharCode(event.keyCode).toUpperCase();
    
    const audio = document.getElementById(key);

    if (audio) {
        // Reproducir audio directamente
        audio.currentTime = 0;
        audio.play();

        // Obtener el botón padre y actualizar el display
        const pad = audio.parentElement;
        const display = document.getElementById('display');
        display.innerText = pad.id.replace(/-/g, ' ');

        // Efecto visual
        pad.classList.add('active');
        setTimeout(() => pad.classList.remove('active'), 100);
    }
});