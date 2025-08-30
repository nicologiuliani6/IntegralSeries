# Integrale di Taylor

**Autore:** Nicolò Giuliani
**Data:** 30/08/2025

---

## Problema

Calcolare l'area sotto una curva, cioè il valore dell'integrale definito di una funzione tra due punti, può diventare molto complicato quando la funzione è molto complessa, non ha primitive note o varia rapidamente. In questi casi, metodi classici come l'integrazione simbolica o la somma di Riemann possono essere inefficienti o richiedere un numero molto elevato di intervalli per ottenere una buona precisione.

L'idea è sviluppare un metodo numerico basato su **micro-intervalli** e sulla **serie di Taylor**, così da ottenere un'approssimazione rapida e accurata anche per funzioni complesse.

---

## Idea principale

Invece di calcolare l'integrale sull'intervallo completo `[a, b]`, si divide l'intervallo in **sottointervalli** `[x_k, x_k + delta]`. Per ciascun sottointervallo, si approssima la funzione tramite la **serie di Taylor** centrata in `x_k` e si integra questa approssimazione.

In altre parole, l'area totale sotto la curva si calcola sommando le aree dei micro-intervalli.

---

## Serie di Taylor

La serie di Taylor permette di approssimare una funzione in un punto `a` come:

```
f(x) ≈ f(a) + f'(a)*(x-a) + f''(a)/2!*(x-a)^2 + f'''(a)/3!*(x-a)^3 + ...
```

Più termini si usano, più l'approssimazione diventa precisa.

---

## Micro-integrali

L'integrale sull'intervallo `[a, b]` può essere suddiviso come somma di **micro-integrali**:

```
Area ≈ sum_{k=0}^{N-1} integral of f(x) from x_k to x_k + delta
x_k = a + k * delta
delta = (b - a) / N
```

In questo modo, calcolare l'integrale di funzioni complesse diventa più semplice ed efficiente, perché ogni micro-intervallo può essere trattato come un piccolo problema in cui la funzione è ben approssimabile con Taylor.
