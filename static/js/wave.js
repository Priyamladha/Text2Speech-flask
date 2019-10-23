var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    waveColor: 'black',
    progressColor: 'blue',
    
});

wavesurfer.load('static/welcome.mp3');

wavesurfer.on('ready', function () {
    wavesurfer.play();
    
});
