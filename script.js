const themeBtn = document.getElementById('theme-toggle');
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') { document.body.classList.add('dark'); themeBtn.textContent = 'Дневной'; }
themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    const isDark = document.body.classList.contains('dark');
    themeBtn.textContent = isDark ? 'Дневной' : 'Ночной';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});
const audio = document.getElementById('audio');
if (audio) {
    const playBtn = document.getElementById('play-btn');
    const progressBar = document.getElementById('progress-bar');
    const progressFill = document.getElementById('progress-fill');
    const currentTimeEl = document.getElementById('current-time');
    const durationEl = document.getElementById('duration');
    function formatTime(sec) {
        if (isNaN(sec)) return '0:00';
        const m = Math.floor(sec / 60);
        const s = Math.floor(sec % 60).toString().padStart(2, '0');
        return m + ':' + s;
    }
    audio.addEventListener('loadedmetadata', () => { durationEl.textContent = formatTime(audio.duration); });
    playBtn.addEventListener('click', () => {
        if (audio.paused) { audio.play(); playBtn.textContent = 'Пауза'; }
        else { audio.pause(); playBtn.textContent = 'Старт'; }
    });
    audio.addEventListener('timeupdate', () => {
        const percent = (audio.currentTime / audio.duration) * 100;
        progressFill.style.width = percent + '%';
        currentTimeEl.textContent = formatTime(audio.currentTime);
    });
    progressBar.addEventListener('click', (e) => {
        const rect = progressBar.getBoundingClientRect();
        const percent = (e.clientX - rect.left) / rect.width;
        audio.currentTime = percent * audio.duration;
    });
    audio.addEventListener('ended', () => { playBtn.textContent = 'Play'; progressFill.style.width = '0%'; });
}
