import numpy as np
import matplotlib.pyplot as plt

# parametrii semnalului sinusoidal
amplitudine = 1.5  # Amplitudinea semnalului
frecventa = 2.0   # Frecvența semnalului (în hertzi)
faza = np.pi / 4  # Faza semnalului (în radiani)

# crearea unui vector de timp de la 0 la 2 secunde cu o rezoluție de 0.01 secunde
t = np.arange(0, 2, 0.01)

# generarea semnalului sinusoidal
semnal_sinus = amplitudine * np.sin(2 * np.pi * frecventa * t + faza)

# generarea semnalului cosinusoidal identic cu semnalul sinusoidal
semnal_cosinus = amplitudine * np.cos(2 * np.pi * frecventa * t + faza)

# afișarea celor două semnale pe subplot-uri separate
plt.figure(figsize=(10, 6))

# subplot pentru semnalul sinusoidal
plt.subplot(2, 1, 1)
plt.plot(t, semnal_sinus)
plt.title('Semnal Sinusoidal')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)

# subplot pentru semnalul cosinusoidal
plt.subplot(2, 1, 2)
plt.plot(t, semnal_cosinus)
plt.title('Semnal Cosinusoidal')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()  # Pentru a asigura o dispunere corectă a subplot-urilor
plt.show()
