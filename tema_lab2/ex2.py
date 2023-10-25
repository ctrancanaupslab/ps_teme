import numpy as np
import matplotlib.pyplot as plt

# parametrii semnalului
amplitudine = 1.0
frecventa = 5  # Hz 
faze = [0, np.pi/4, np.pi/2, 3*np.pi/4] 

# eșantionare
Fs = 1000  # frecvența de eșantionare
t = np.linspace(0, 1, Fs, endpoint=False)  # vectorul timp

# gGenerare semnale sinusoidale cu diferite faze
semnale_sinusoidale = []
for fase in faze:
    semnal = amplitudine * np.sin(2 * np.pi * frecventa * t + fase)
    semnale_sinusoidale.append(semnal)

# afișare semnale sinusoidale
plt.figure(figsize=(10, 6))
for i, fase in enumerate(faze):
    plt.plot(t, semnale_sinusoidale[i], label=f'Faza = {fase:.2f}')

# adăugare zgomot și calcul SNR pentru unul dintre semnale
semnal_curent = semnale_sinusoidale[2]  # Alegem un semnal pentru adăugarea de zgomot
SNR_dorit = 10  # Valoarea dorită pentru SNR

# generare zgomot aleatoriu
zgomot = np.random.normal(0, 1, len(semnal_curent))

# calcularea lui gamma
gama = np.sqrt(np.linalg.norm(semnal_curent) ** 2 / (SNR_dorit * np.linalg.norm(zgomot) ** 2))

# adăugarea zgomotului la semnal
semnal_cu_zgomot = semnal_curent + gama * zgomot

# afișare semnal cu zgomot
plt.plot(t, semnal_cu_zgomot, label=f'Semnal cu Zgomot (SNR = {SNR_dorit})', linestyle='--')

# configurare grafic
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.legend()
plt.title('Semnale Sinusoidale cu Zgomot Adăugat')
plt.grid(True)

# afișare grafic
plt.show()
Acest cod generează ma
