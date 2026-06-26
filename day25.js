const progressBar = document.getElementById('progressBar');
const statusText = document.getElementById('status');
const advanceBtn = document.getElementById('advanceBtn');

let progress = 0;

advanceBtn.addEventListener('click', () => {
  progress = Math.min(progress + 25, 100);
  progressBar.style.width = `${progress}%`;
  statusText.textContent = `Progress: ${progress}%`;

  if (progress === 100) {
    advanceBtn.textContent = 'Completed';
    advanceBtn.disabled = true;
  }
});
