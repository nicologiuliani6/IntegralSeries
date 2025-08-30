import numpy as np
from math import factorial
# Funzione da integrare
def f(x):
    return x**3 * np.exp(x**2)
# Derivata n-esima approssimata con differenze finite centrali
def nth_derivative(f, x, n, h=1e-5):
    if n == 0:
        return f(x)
    elif n == 1:
        return (f(x+h) - f(x-h)) / (2*h)
    elif n == 2:
        return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)
    else:
        # Ricorsivo per n>2 (meno preciso, ma funziona)
        return (nth_derivative(f, x+h, n-1, h) - nth_derivative(f, x-h, n-1, h)) / (2*h)
# Intervallo
a, b = 0, 1
print("Risultato atteso: 0.5")
# Micro-intervalli
N_values = [1, 2, 5, 10, 50, 100, 500, 1000]
# Massimo ordine dei termini pari della serie di Taylor
n_max = 4
for N in N_values:
    delta = (b - a) / N
    integral = 0.0
    for k in range(N):
        xk = a + k*delta
        ck = xk + delta/2  # punto centrale
        micro_sum = 0.0
        for n in range(0, n_max+1, 2):  # termini pari
            f_der = nth_derivative(f, ck, n)
            term = f_der * ((delta/2)**(n+1) * 2) / factorial(n+1)
            micro_sum += term
        integral += micro_sum
    print(f"Integrale approssimato con N={N} micro-intervalli e termini fino a n={n_max}: {integral}")
