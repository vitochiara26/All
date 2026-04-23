const toggleBtn = document.querySelector('.info-toggle');
const productPreview = document.querySelector('.product-preview');
const infoPanel = document.getElementById('product-info');

toggleBtn.addEventListener('click', () => {
  const isHidden = infoPanel.classList.toggle('hidden');

  toggleBtn.setAttribute('aria-expanded', !isHidden);
  toggleBtn.textContent = isHidden ? 'More Info' : 'Hide Info';
  productPreview.classList.toggle('expanded', !isHidden);

  if (!isHidden) {
    infoPanel.focus();
  }
});