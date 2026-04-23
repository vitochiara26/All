document.querySelectorAll('.details-btn').forEach(button => {
  button.addEventListener('click', () => {
    const product = button.closest('.product');
    const details = product.querySelector('.product-details');
    const isHidden = details.classList.toggle('hidden');
    product.setAttribute('aria-expanded', !isHidden);
    if (!isHidden) {
      details.focus();
      button.textContent = 'Hide details';
    } else {
      button.textContent = 'More details';
    }
  });
});
