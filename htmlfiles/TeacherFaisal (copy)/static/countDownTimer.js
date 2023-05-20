const startingMinutes = 0.2;
let time = startingMinutes * 60;
let isPaused = false;

const countdownEl = document.getElementById('countdown');
const pauseButton = document.getElementById('pause-button');
const statusDiv = document.querySelector('.center');


setInterval(updateCountdown, 1000);

function updateCountdown() {
  if (isPaused) {
    return;
  }
  const minutes = Math.floor(time / 60);
  let seconds = time % 60;

  seconds = seconds < 10 ? '0' + seconds : seconds;

  countdownEl.innerHTML = `${minutes}:${seconds}`;
  time--;

  if (time === 0){
    pause();
    statusDiv.style.display = 'block';
    pauseButton.disabled = "disabled";
  }
}

function pause() {
  isPaused = !isPaused;
}
