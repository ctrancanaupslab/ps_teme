import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului initial
frecventa = 10  # Hz
amplitudine = 1
faza = 0

# Perioada semnalului
perioada = 1 / frecventa

# Timpul de la 0 la 2 perioade
timp = np.linspace(0, 2 * perioada, 1000)

# Construirea semnalului sinusoidal initial
semnal_initial = amplitudine * np.sin(2 * np.pi * frecventa * timp + faza)

# Afisare semnal
plt.figure(figsize=(10, 4))
plt.plot(timp, semnal_initial)
plt.title('Semnal sinusoidal initial')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)

# Eșantionarea cu o frecvență sub-Nyquist
frecventa_esantionare = 15  # sub-Nyquist
pas_esantionare = 1 / frecventa_esantionare

# Eșantionarea semnalului initial
esantioane = semnal_initial[::int(1 / pas_esantionare)]

# Afisare semnal eșantionat
plt.figure(figsize=(10, 4))
plt.stem(timp[::int(1 / pas_esantionare)], esantioane, basefmt='C0', linefmt='C1', markerfmt='C2o')
plt.title('Eșantionarea semnalului sub-Nyquist')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)

# Parametrii semnalelor secundare
frecventa_1 = 5  # Hz
frecventa_2 = 15  # Hz

# Construirea semnalelor secundare
semnal_secundar_1 = amplitudine * np.sin(2 * np.pi * frecventa_1 * timp + faza)
semnal_secundar_2 = amplitudine * np.sin(2 * np.pi * frecventa_2 * timp + faza)

# Eșantionarea semnalelor secundare cu aceeași frecvență de eșantionare
esantioane_1 = semnal_secundar_1[::int(1 / pas_esantionare)]
esantioane_2 = semnal_secundar_2[::int(1 / pas_esantionare)]

# Afisare semnale eșantionate
plt.figure(figsize=(10, 4))
plt.stem(timp[::int(1 / pas_esantionare)], esantioane_1, basefmt='C0', linefmt='C1', markerfmt='C2o', label='5 Hz')
plt.stem(timp[::int(1 / pas_esantionare)], esantioane_2, basefmt='C0', linefmt='C3', markerfmt='C4s', label='15 Hz')
plt.title('Eșantionarea semnalelor secundare cu aceeași frecvență de eșantionare')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.legend()
plt.grid(True)

plt.show()
