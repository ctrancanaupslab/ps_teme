import numpy as np
import matplotlib.pyplot as plt

# Definim intervalul de valori alpha
alpha = np.linspace(-np.pi/2, np.pi/2, 1000)

# Calculăm valorile reale ale sin(alpha)
sin_alpha = np.sin(alpha)

# Calculăm valorile aproximării sin(alpha) ~ alpha
alpha_approx = alpha

# Calculăm valorile aproximării Pade pentru sin(alpha)
pade_approx = (2*alpha) / (2 + alpha**2)

# Calculăm eroarea dintre aproximarea clasică și valoarea reală
error_approx = np.abs(sin_alpha - alpha_approx)

# Calculăm eroarea dintre aproximarea Pade și valoarea reală
error_pade = np.abs(sin_alpha - pade_approx)

# Creăm un grafic pentru valorile reale și cele aproximative
plt.figure(figsize=(12, 6))
plt.plot(alpha, sin_alpha, label='sin(alpha)', linewidth=2)
plt.plot(alpha, alpha_approx, label='alpha (Aproximare clasică)', linestyle='--')
plt.plot(alpha, pade_approx, label='Aproximare Pade', linestyle='--')
plt.xlabel('Alpha')
plt.ylabel('Valoare')
plt.legend()
plt.title('Aproximarea sin(alpha) ~ alpha și Aproximarea Pade')
plt.grid(True)

# Creăm un grafic pentru eroarea dintre aproximarea clasică și valoarea reală (logaritmic)
plt.figure(figsize=(12, 6))
plt.semilogy(alpha, error_approx, label='Eroare Aproximare Clasică')
plt.semilogy(alpha, error_pade, label='Eroare Aproximare Pade')
plt.xlabel('Alpha')
plt.ylabel('Eroare (logaritmic)')
plt.legend()
plt.title('Eroarea între Aproximări și Valoarea Reală (logaritmic)')
plt.grid(True)

plt.show()
