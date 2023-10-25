import numpy as np
import matplotlib.pyplot as plt

# Creează un eșantion de puncte temporale
t = np.linspace(0, 1, 1000, endpoint=False)

# Generează un semnal sinusoidal
signal_sinusoidal = np.sin(2 * np.pi * 5 * t)  # Frecvența de 5 Hz

# Generează un semnal sawtooth
signal_sawtooth = 2 * (t - np.floor(t + 0.5))

# Calculează suma semnalelor
signal_sum = signal_sinusoidal + signal_sawtooth

# Creează un subplot cu 3 grafice
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, signal_sinusoidal)
plt.title('Semnal Sinusoidal')

plt.subplot(3, 1, 2)
plt.plot(t, signal_sawtooth)
plt.title('Semnal Sawtooth')

plt.subplot(3, 1, 3)
plt.plot(t, signal_sum)
plt.title('Suma Semnalelor')

# Afișează graficele
plt.tight_layout()
plt.show()
