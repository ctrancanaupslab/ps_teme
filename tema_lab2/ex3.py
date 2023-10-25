import numpy as np
import sounddevice as sd
from scipy.io import wavfile
import matplotlib.pyplot as plt

# a) semnal sinusoidal de frecventa 400 Hz cu 1600 esantioane
frecventa_a = 400  # Hz
esantioane_a = 1600
t_a = np.linspace(0, 1, esantioane_a, endpoint=False)
semnal_a = np.sin(2 * np.pi * frecventa_a * t_a)

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(t_a, semnal_a)
plt.title("Semnal Sinusoidal 400 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()

# Redare semnal a
sd.play(semnal_a, frecventa_a)
sd.wait()

# Salvare semnal a ca fișier .wav
wavfile.write("semnal_a.wav", frecventa_a, semnal_a)

# Citire semnal a din fișier .wav și verificare
frecventa_a_read, semnal_a_read = wavfile.read("semnal_a.wav")
assert np.array_equal(semnal_a, semnal_a_read)

# b) semnal sinusoidal de frecventa 800 Hz care dureaza 8 secunde
frecventa_b = 800  # Hz
durata_b = 8  # secunde
esantioane_b = int(durata_b * frecventa_b)
t_b = np.linspace(0, durata_b, esantioane_b, endpoint=False)
semnal_b = np.sin(2 * np.pi * frecventa_b * t_b)

plt.subplot(3, 2, 2)
plt.plot(t_b, semnal_b)
plt.title("Semnal Sinusoidal 800 Hz (8 secunde)")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()

# Redare semnal b
sd.play(semnal_b, frecventa_b)
sd.wait()

# c) semnal tip sawtooth de frecventa 240 Hz
frecventa_c = 240  # Hz
t_c = np.linspace(0, 1, esantioane_a, endpoint=False)
semnal_c = 2 * (t_c * frecventa_c - np.floor(0.5 + t_c * frecventa_c))

plt.subplot(3, 2, 3)
plt.plot(t_c, semnal_c)
plt.title("Semnal Sawtooth 240 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()

# Redare semnal c
sd.play(semnal_c, frecventa_c)
sd.wait()

# d) semnal tip square de frecventa 300 Hz
frecventa_d = 300  # Hz
semnal_d = np.sign(np.sin(2 * np.pi * frecventa_d * t_a))

plt.subplot(3, 2, 4)
plt.plot(t_a, semnal_d)
plt.title("Semnal Square 300 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()

# Redare semnal d
sd.play(semnal_d, frecventa_d)
sd.wait()

plt.show()
