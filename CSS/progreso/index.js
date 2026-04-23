const form = document.getElementById('multiStepForm');
const steps = form.querySelectorAll('.form-step');
const progressBar = form.querySelector('.progress-bar');
const progressText = form.querySelector('.progress-text');
const totalSteps = steps.length;

let currentStep = 0;

function updateProgress() {
  const percent = ((currentStep + 1) / totalSteps) * 100;
  progressBar.style.width = percent + '%';
  progressText.textContent = `Step ${currentStep + 1} of ${totalSteps}`;
}

function showStep(index) {
  steps.forEach((step, i) => {
    step.classList.toggle('active', i === index);
  });
  updateProgress();
}

form.querySelectorAll('.next-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    if (currentStep < totalSteps - 1) {
      currentStep++;
      showStep(currentStep);
    }
  });
});

form.querySelectorAll('.prev-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    if (currentStep > 0) {
      currentStep--;
      showStep(currentStep);
    }
  });
});

showStep(currentStep);

form.addEventListener('submit', e => {
  e.preventDefault();
  alert('Form submitted!');
});