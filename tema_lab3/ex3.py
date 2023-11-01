import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului
N = 512  # Numărul de eșantioane
n = np.arange(N)  # n = 0, 1, 2, ..., N-1
fs = 1000  # Frecvența de eșantionare (Hz)
T = 1 / fs  # Perioada de eșantionare
t = n * T  # Timpul

# Definirea semnalului compus din trei componente de frecvență
frequencies = [50, 100, 200]  # Frecvențele caracteristice ale componentelor (Hz)
amplitudes = [1.0, 0.5, 0.3]  # Amplitudinile componentelor
x = np.sum([amp * np.sin(2 * np.pi * freq * t) for amp, freq in zip(amplitudes, frequencies)], axis=0)

# Calculul transformatei Fourier folosind relația dată
X = np.zeros(N, dtype=complex)
omega_values = np.linspace(0, 2 * np.pi, N)  # Valorile posibile ale lui omega

for k, omega in enumerate(omega_values):
    X[k] = np.sum(x * np.exp(-2j * np.pi * n * omega / N))

# Calculul modulului transformatei Fourier
X_modulus = np.abs(X)

# Afișarea semnalului și modulului transformatei Fourier
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Semnal compus din trei componente sinusoidale")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()

plt.subplot(2, 1, 2)
freq_axis = np.fft.fftfreq(N, T)
plt.plot(freq_axis, X_modulus)
plt.title("Modulul Transformatei Fourier")
plt.xlabel("Frecvență (Hz)")
plt.ylabel("Amplitudine")
plt.grid()

plt.tight_layout()
plt.show()
