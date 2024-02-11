// Подключаем аудио-плеер
var audioPlayer = document.getElementById('audio-player');
var playPauseButton = document.getElementById('play-pause-button');
var seekBar = document.getElementById('seek-bar');
var isPlaying = false;

// Функция для воспроизведения и паузы
function togglePlayPause() {
    if (!isPlaying) {
        audioPlayer.play();
        isPlaying = true;
        playPauseButton.innerHTML = '<img src="/static/img_svg/paus.svg" alt="Pause Image">';
    } else {
        audioPlayer.pause();
        isPlaying = false;
        playPauseButton.innerHTML = '<img src="/static/img_svg/play.svg" alt="Pause Image">';
    }
}

// Функция для изменения скорости воспроизведения
function changeSpeed(speed) {
    audioPlayer.playbackRate = speed;
}

// Функция для перемотки аудио
function rewindAudio(seconds) {
    var currentTime = audioPlayer.currentTime;
    var newTime = Math.max(0, currentTime - seconds);
    audioPlayer.currentTime = newTime;
}



// Слушатель для завершения воспроизведения
audioPlayer.addEventListener('ended', function() {
    isPlaying = false;
    playPauseButton.innerHTML = '<img src="/static/img_svg/play.svg" alt="Pause Image">';
});

// Устанавливаем начальную скорость воспроизведения
changeSpeed(0.9);


//// Слушатель для обновления ползунка прогресса воспроизведения
//audioPlayer.addEventListener('timeupdate', function() {
//    var currentTime = audioPlayer.currentTime;
//    var duration = audioPlayer.duration;
//    seekBar.value = (currentTime / duration) * 100;
//});

//// Слушатель для изменения положения воспроизведения при перемещении ползунка
//seekBar.addEventListener('input', function() {
//    var seekTo = audioPlayer.duration * (seekBar.value / 100);
//    audioPlayer.currentTime = seekTo;
//});