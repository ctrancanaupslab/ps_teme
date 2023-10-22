import numpy as np
import matplotlib.pyplot as plt

# a) semnal sinusoidal de frecventa 400 Hz cu 1600 esantioane
frecventa_a = 400  # Hz
esantioane_a = 1600
t_a = np.linspace(0, 1, esantioane_a, endpoint=False)
semnal_a = np.sin(2 * np.pi * frecventa_a * t_a)

plt.figure(figsize=(8, 4))
plt.subplot(3, 2, 1)
plt.plot(t_a, semnal_a)
plt.title("Semnal Sinusoidal 400 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()

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

# d) semnal tip square de frecventa 300 Hz
frecventa_d = 300  # Hz
semnal_d = np.sign(np.sin(2 * np.pi * frecventa_d * t_a))

plt.subplot(3, 2, 4)
plt.plot(t_a, semnal_d)
plt.title("Semnal Square 300 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()

# e) Semnal 2D aleator
semnal_2d_aleator = np.random.rand(128, 128)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(semnal_2d_aleator, cmap='viridis')
plt.title("Semnal 2D Aleator")
plt.colorbar()

# f) Semnal 2D
# Vom crea un semnal 2D cu o regiune neagra si o regiune alba
semnal_2d_alegere = np.zeros((128, 128))  # Creăm un array de 0-uri

# definim coordonatele pentru regiunea alba (de exemplu, un patrat in centru)
dimensiune_regiune_alba = 40
x_start = 44
y_start = 44
x_end = x_start + dimensiune_regiune_alba
y_end = y_start + dimensiune_regiune_alba
semnal_2d_alegere[y_start:y_end, x_start:x_end] = 1  # umplem regiunea cu 1-uri

plt.subplot(1, 2, 2)
plt.imshow(semnal_2d_alegere, cmap='plasma')
plt.title("Semnal 2D")
plt.colorbar()

plt.tight_layout()
plt.show()
