# Integrale di Taylor

**Autore:** Nicolò Giuliani  
**Data:** 30/08/2025

---

## Problema

Calcolare l'area sotto una curva, ovvero il valore dell'integrale definito:

$
\int_a^b f(x) \, dx
$

può diventare molto complicato quando la funzione $f(x)$ è estremamente complessa, non ha primitive note o varia rapidamente.  
In questi casi, metodi classici come l'integrazione simbolica o la somma di Riemann possono essere inefficienti o richiedere un numero elevato di intervalli per ottenere una buona precisione.

L'idea è quindi di sviluppare un metodo numerico basato su micro-intervalli e sulla **serie di Taylor**, in modo da ottenere un'approssimazione rapida e accurata anche per funzioni complesse.

---

## Idea principale

Invece di calcolare un integrale definito su \([$a,b$]\), si divide l'intervallo in sottointervalli \([$x_k$, $x_k$ $+\Delta$]\) e per ciascun intervallo si integra la funzione approssimata tramite la **serie di Taylor** centrata in \($x_k$\).

Definiamo il nostro obiettivo:

$
\text{Area} = \int_{a}^{b} f(x) \, dx
$

La serie di Taylor ci dice che possiamo approssimare una funzione in un punto \(a\) come:

$
f(x) \approx \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n
$

---

## Micro-integrali

L'integrale può essere suddiviso in micro-intervalli:


$
\int_a^b f(x) \, dx \approx \sum_{k=0}^{N-1} \int_{x_k}^{x_k + \Delta} f(x) \, dx, \quad
x_k = a + k \Delta, \quad \Delta = \frac{b-a}{N}
$

---


