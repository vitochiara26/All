const toggleBtn = document.getElementById('toggle-advanced-btn');
const advancedDetails = document.getElementById('advanced-details');

toggleBtn.addEventListener('click', () => {
  const isHidden = advancedDetails.classList.toggle('hidden');
  toggleBtn.setAttribute('aria-expanded', !isHidden);
  if (!isHidden) {
    advancedDetails.focus();
  }
});