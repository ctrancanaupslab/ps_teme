import numpy as np
import matplotlib.pyplot as plt

# Creează un semnal sinusoidal cu frecvența de eșantionare de 1000 Hz și o perioadă de 1 secundă
fs = 1000  # Frecvența de eșantionare
t = np.arange(0, 1, 1/fs)  # Un vector de timp de la 0 la 1 secundă
signal = np.sin(2 * np.pi * 100 * t)  # Semnal sinusoidal cu frecvența de 100 Hz

# Decimarea la 1/4 din frecvența inițială (pastrăm doar al 4-lea element)
decimated_signal = signal[::4]

# Afisarea semnalelor
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Semnal initial cu frecventa de esantionare de 1000 Hz')

plt.subplot(2, 1, 2)
t_decimated = np.arange(0, 1, 1/fs/4)  # Vectorul de timp pentru semnalul decimat
plt.plot(t_decimated, decimated_signal)
plt.title('Semnal decimat la 1/4 din frecventa initiala (de la inceput)')

plt.tight_layout()
plt.show()

# Repetarea decimarii de la al doilea element din vector
decimated_signal_starting_from_2nd_element = signal[1::4]

# Afisarea semnalelor decimate pornind de la al doilea element
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Semnal initial cu frecventa de esantionare de 1000 Hz')

plt.subplot(2, 1, 2)
t_decimated = np.arange(1/fs/4, 1, 1/fs/4)  # Vectorul de timp pentru semnalul decimat
plt.plot(t_decimated, decimated_signal_starting_from_2nd_element)
plt.title('Semnal decimat la 1/4 din frecventa initiala (incepand de la al doilea element)')

plt.tight_layout()
plt.show()
