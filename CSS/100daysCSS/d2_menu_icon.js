const menuIcon = document.querySelector('.menu-icon');

menuIcon.addEventListener('click', function() {
    this.classList.toggle('active');
    
    const lineas = this.querySelectorAll('div');
    lineas.forEach(div => {
        div.classList.remove('no-animation');
    });
});