import numpy as np
import matplotlib.pyplot as plt

N = 8
omega = np.exp(-2j * np.pi / N)

# Crearea matricei Fourier
F = np.zeros((N, N), dtype=np.complex128)

for n in range(N):
    for k in range(N):
        F[n, k] = omega**(n * k)

# Afisarea partii reale si imaginare in subplot-uri separate
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Partea Reală a Matricei Fourier")
plt.imshow(np.real(F), cmap='viridis', origin='upper', interpolation='none')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title("Partea Imaginară a Matricei Fourier")
plt.imshow(np.imag(F), cmap='viridis', origin='upper', interpolation='none')
plt.colorbar()

plt.tight_layout()
plt.show()

# Calcularea produsului dintre F^H și F
F_H = np.conjugate(F).T  # Transpusa conjugată a lui F
product = np.dot(F_H, F)

# Verificarea unitarității
identity_matrix = np.eye(N, dtype=np.complex128)
is_unitary = np.allclose(product, identity_matrix)

if is_unitary:
    print("Matricea Fourier F este unitară.")
else:
    print("Matricea Fourier F nu este unitară.")
