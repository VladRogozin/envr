document.getElementById('playlist-select').addEventListener('change', function() {
    var playlistId = this.value;
    if (playlistId) {
        window.location.href = playlistId;
    }
});