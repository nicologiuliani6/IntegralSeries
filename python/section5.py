import numpy as np
# Funzione da integrare
def f(x):
    return x**3 * np.exp(x**2)
# Intervallo
a, b = 0, 1
# Risultato atteso (approssimativo)
print("Risultato atteso: 0.5")
# Numero di micro-intervalli
N_values = [1, 2, 5, 10, 50, 100, 500, 1000, 100000]
for N in N_values:
    delta = (b - a) / N
    integral = 0.0
    for k in range(N):
        xk = a + k*delta
        ck = xk + delta/2  # punto centrale
        # Solo il termine n=0: f(c_k) * delta
        integral += f(ck) * delta
    print(f"Integrale approssimato con N={N} micro-intervalli: {integral}")
