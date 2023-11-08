import numpy as np
import matplotlib.pyplot as plt
import time

# Definirea dimensiunilor pentru care vom măsura timpii de execuție
N_values = [128, 256, 512, 1024, 2048, 4096, 8192]

execution_times_custom = []  # Lista pentru timpii de execuție ai implementării noastre
execution_times_numpy = []  # Lista pentru timpii de execuție ai numpy.fft.fft

for N in N_values:
    # Generarea unui semnal aleator
    x = np.random.rand(N)

    # Măsurarea timpului de execuție pentru implementarea noastră a DFT
    start_time = time.time()
    X_custom = np.zeros(N, dtype=complex)
    omega_values = np.linspace(0, 2 * np.pi, N)
    for k, omega in enumerate(omega_values):
        X_custom[k] = np.sum(x * np.exp(-2j * np.pi * np.arange(N) * omega / N))
    end_time = time.time()
    execution_times_custom.append(end_time - start_time)

    # Măsurarea timpului de execuție pentru numpy.fft.fft
    start_time = time.time()
    X_numpy = np.fft.fft(x)
    end_time = time.time()
    execution_times_numpy.append(end_time - start_time)

# Crearea graficului cu timpii de execuție
plt.figure(figsize=(10, 6))
plt.plot(N_values, execution_times_custom, marker='o', label='Implementare custom')
plt.plot(N_values, execution_times_numpy, marker='o', label='numpy.fft.fft')
plt.xlabel('Dimensiunea vectorului N')
plt.ylabel('Timp de execuție (secunde)')
plt.yscale('log')
plt.title('Compararea timpilor de execuție pentru DFT')
plt.legend()
plt.grid()
plt.show()
