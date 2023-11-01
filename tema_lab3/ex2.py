import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului sinusoidal
N = 64  # Numărul de eșantioane
n_values = np.arange(N)  # n = 0, 1, 2, ..., N-1
x = np.sin(2 * np.pi * 0.2 * n_values)  # Semnal sinusoidal de frecvență 0.2 Hz

# Graficul 1: Infasurarea semnalului pe cercul unitate
y = x * np.exp(-2j * np.pi * n_values / N)  # Calculul y[n]

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.title("Infasurarea semnalului pe cercul unitate")
plt.plot(np.real(y), np.imag(y), marker='o', markersize=4, linestyle='-', color='blue')
plt.xlabel('Partea Reală')
plt.ylabel('Partea Imaginară')
plt.grid()

# Graficul 2: Infasurarea pentru diferite valori ale lui omega
omegas = [0.2 * 2 * np.pi, 0.4 * 2 * np.pi, 0.6 * 2 * np.pi, 1.0 * 2 * np.pi]  # Valori ale lui omega
colors = ['red', 'green', 'blue', 'purple']

plt.subplot(1, 2, 2)
plt.title("Infasurarea pentru diferite valori ale lui omega")
for omega, color in zip(omegas, colors):
    z = x * np.exp(-2j * np.pi * omega * n_values / N)  # Calculul z[omega]
    distance = np.abs(z)  # Calculul distanței de la origine
    plt.plot(np.real(z), np.imag(z), marker='o', markersize=4, linestyle='-', color=color, label=f'ω={omega / (2 * np.pi):.2f} Hz')

plt.xlabel('Partea Reală')
plt.ylabel('Partea Imaginară')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
