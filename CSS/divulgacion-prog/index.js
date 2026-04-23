const btn = document.getElementById('show-details-btn');
const content = document.getElementById('extra-content');

btn.addEventListener('click', () => {
  const isHidden = content.classList.toggle('hidden');
  btn.setAttribute('aria-expanded', !isHidden);
  if (!isHidden) {
    content.focus();
  }
});
