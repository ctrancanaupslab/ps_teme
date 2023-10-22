import numpy as np
import matplotlib.pyplot as plt

# a) crearea axei reale de timp
t = np.arange(0, 0.03, 0.0005)

# b) construirea semnalelor x(t), y(t) și z(t)
x_t = np.cos(520 * np.pi * t + np.pi / 3)
y_t = np.cos(280 * np.pi * t - np.pi / 3)
z_t = np.cos(120 * np.pi * t + np.pi / 3)

# b) afisarea grafica a semnalelor continue
plt.figure(figsize=(12, 6))

plt.subplot(311)
plt.plot(t, x_t)
plt.title('Semnalul x(t)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.subplot(312)
plt.plot(t, y_t)
plt.title('Semnalul y(t)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.subplot(313)
plt.plot(t, z_t)
plt.title('Semnalul z(t)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.tight_layout()

# c) esantionarea semnalelor cu o frecventa de 200 Hz
fs = 200  # Frecventa de esantionare
n = np.arange(0, 0.03, 1/fs)

x_n = np.cos(520 * np.pi * n + np.pi / 3)
y_n = np.cos(280 * np.pi * n - np.pi / 3)
z_n = np.cos(120 * np.pi * n + np.pi / 3)

# c) afisarea grafica a semnalelor esantionate
plt.figure(figsize=(12, 6))

plt.subplot(311)
plt.stem(n, x_n, markerfmt='ro', linefmt='r-')
plt.title('Semnalul esantionat x[n]')
plt.xlabel('n (eșantioane)')
plt.ylabel('Amplitudine')

plt.subplot(312)
plt.stem(n, y_n, markerfmt='ro', linefmt='r-')
plt.title('Semnalul esantionat y[n]')
plt.xlabel('n (eșantioane)')
plt.ylabel('Amplitudine')

plt.subplot(313)
plt.stem(n, z_n, markerfmt='ro', linefmt='r-')
plt.title('Semnalul esantionat z[n]')
plt.xlabel('n (eșantioane)')
plt.ylabel('Amplitudine')

plt.tight_layout()
plt.show()
