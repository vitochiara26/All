const searchIcon = document.querySelector('.search-icon');
const searchInput = document.querySelector('.search-input');
const menuIcon = document.querySelector('.menu-icon');
const panel = document.querySelector('.panel');
const menu = document.querySelector('.menu');

searchIcon.addEventListener('click' , () => {
    searchInput.classList.toggle('active');
});

menuIcon.addEventListener('click', () => {
    panel.classList.toggle('show-menu');
    menu.classList.toggle('active');
});
