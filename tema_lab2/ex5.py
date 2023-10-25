import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Parametri pentru semnalele sinusoidale
durata = 1.0  # Durata semnalului în secunde
frecventa_1 = 440  # Frecvența primului semnal (A4)
frecventa_2 = 880  # Frecvența celui de-al doilea semnal (A5)
amplitudine = 0.5  # Amplitudinea semnalelor

# Generăm timpul pentru un eșantion de frecvență de 44.1 kHz
timp = np.linspace(0, durata, int(44100 * durata), False)

# Generăm cele două semnale sinusoidale
semnal_1 = amplitudine * np.sin(2 * np.pi * frecventa_1 * timp)
semnal_2 = amplitudine * np.sin(2 * np.pi * frecventa_2 * timp)

# Concatenăm cele două semnale într-un singur vector
semnal_combinat = np.concatenate((semnal_1, semnal_2))

# Redăm audio semnalul combinat
sd.play(semnal_combinat, 44100)
sd.wait()

# Afișăm semnalele într-un grafic
plt.figure(figsize=(10, 4))
plt.subplot(3, 1, 1)
plt.plot(timp, semnal_1)
plt.title(f"Semnal {frecventa_1} Hz")

plt.subplot(3, 1, 2)
plt.plot(timp, semnal_2)
plt.title(f"Semnal {frecventa_2} Hz")

plt.subplot(3, 1, 3)
plt.plot(timp, semnal_combinat)
plt.title("Semnal Combinat")
plt.tight_layout()
plt.show()


# observatii:
# 1) sunetul a fost redat audio si se poate auzi o nota muzicala data de frecventa 1 (A4) urmata de alta data de frecvenaa 2 (A5)
# 2) graficul afisat prezinta cele doua semnale sinusoidale cu aceeasi forma de unda, dar de frecvente diferite. Prima jumatate a graficului reprezinta semnalul cu frecventa 1, iar a doua jumatate reprezinta semnalul cu frecventa 2. Semnalul combinat arata o tranzitie clara între cele două frecvențe.
