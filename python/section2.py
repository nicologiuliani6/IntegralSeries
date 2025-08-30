import numpy as np

# Funzione da integrare
def f(x):
    return x**3 * np.exp(x**2)

# Intervallo
a, b = 0, 1

print("Risulatato atteso: 0.5")

# Valori di N in incrementi di 1000
for N in range(1, 1001, 10):  # N = 1000, 2000, ..., 5000
    delta = (b - a) / N
    integral = 0.0
    for k in range(N):
        xk = a + k*delta
        integral += f(xk) * delta  # micro-integrale con regola dei rettangoli
    print(f"Integrale approssimato (N={N}): {integral}")
