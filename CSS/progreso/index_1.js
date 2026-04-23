const form = document.getElementById('progressForm');
const steps = form.querySelectorAll('.form-step');
const progressBar = form.querySelector('.progress-bar');
const currentStepSpan = document.getElementById('currentStep');
const totalStepsSpan = document.getElementById('totalSteps');
const percentageSpan = document.getElementById('percentage');

const totalSteps = steps.length;
let currentStep = 0;

totalStepsSpan.textContent = totalSteps;

function updateProgress() {
  const percent = Math.round(((currentStep + 1) / totalSteps) * 100);
  progressBar.style.width = percent + '%';
  currentStepSpan.textContent = currentStep + 1;
  percentageSpan.textContent = percent + '%';

  // Update ARIA attribute
  form.querySelector('.progress-container').setAttribute('aria-valuenow', percent);
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

form.addEventListener('submit', e => {
  e.preventDefault();
  alert('Form submitted! Thanks!');
});

showStep(currentStep);