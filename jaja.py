import numpy as np
import simpleaudio as sa

# Frecuencias de notas musicales
NOTES = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
    'REST': 0
}

def play_note(note, duration=0.4, volume=0.3):
    fs = 44100  # samples per second
    t = np.linspace(0, duration, int(fs * duration), False)

    freq = NOTES.get(note, 0)
    if freq == 0:
        wave = np.zeros_like(t)
    else:
        wave = np.sin(freq * 2 * np.pi * t)

    audio = (wave * volume * 32767).astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

# Mini fragmento estilo chiptune de "Battle Against a True Hero"
melody = ['E4', 'E4', 'REST', 'E4', 'REST', 'C4', 'E4', 'REST', 'G4', 'REST']
durations = [0.2, 0.2, 0.1, 0.2, 0.1, 0.2, 0.2, 0.1, 0.4, 0.2]

for note, dur in zip(melody, durations):
    play_note(note, dur)
