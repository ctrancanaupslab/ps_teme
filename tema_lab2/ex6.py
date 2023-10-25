import numpy as np
import matplotlib.pyplot as plt

# Alegerea frecvenței de eșantionare
fs = 1000  # Hz (de exemplu, o frecvență de eșantionare de 1000 Hz)

# a) Semnal cu f = fs / 2
f_a = fs / 2
t = np.arange(0, 1, 1/fs)
signal_a = np.sin(2 * np.pi * f_a * t)

# b) Semnal cu f = fs / 4
f_b = fs / 4
signal_b = np.sin(2 * np.pi * f_b * t)

# c) Semnal cu f = 0 Hz (constant)
signal_c = np.zeros_like(t)  # Semnal constant

# Vizualizarea semnalelor
plt.figure(figsize=(10, 6))

plt.subplot(311)
plt.plot(t, signal_a)
plt.title('Semnal a) f = fs / 2')

plt.subplot(312)
plt.plot(t, signal_b)
plt.title('Semnal b) f = fs / 4')

plt.subplot(313)
plt.plot(t, signal_c)
plt.title('Semnal c) f = 0 Hz (constant)')

plt.tight_layout()
plt.show()
