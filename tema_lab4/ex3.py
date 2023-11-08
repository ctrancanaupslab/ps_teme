import numpy as np
import matplotlib.pyplot as plt

# Frecvența semnalului original
f0 = 5  # Hz

# Durata semnalului original
T = 1  # secunde

# Perioada semnalului original
T0 = 1 / f0

# Frecvența de eșantionare sub Nyquist
fs1 = 8  # Hz

# Frecvența de eșantionare deasupra Nyquist
fs2 = 15  # Hz

# Timpul semnalului original
t_original = np.linspace(0, T, int(T * fs2), endpoint=False)

# Semnalul original
x_original = np.sin(2 * np.pi * f0 * t_original)

# Semnalul eșantionat sub Nyquist
t1 = np.linspace(0, T, int(T * fs1), endpoint=False)
x1 = np.sin(2 * np.pi * f0 * t1)

# Semnalul eșantionat deasupra Nyquist
t2 = np.linspace(0, T, int(T * fs2), endpoint=False)
x2 = np.sin(2 * np.pi * f0 * t2)

# Plotează semnalul original și cele două semnale eșantionate
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t_original, x_original)
plt.title('Semnal original')
plt.subplot(3, 1, 2)
plt.stem(t1, x1, use_line_collection=True)
plt.title('Semnal eșantionat sub Nyquist (fs < 10 Hz)')
plt.subplot(3, 1, 3)
plt.stem(t2, x2, use_line_collection=True)
plt.title('Semnal eșantionat deasupra Nyquist (fs > 10 Hz)')

plt.tight_layout()
plt.show()
