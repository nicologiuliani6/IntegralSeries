# Integrale di Taylor

**Autore:** Nicolò Giuliani  
**Data:** 30/08/2025

---

## 📋 Panoramica

Questo progetto presenta un metodo numerico innovativo per il calcolo di integrali definiti basato sulla combinazione di **micro-intervalli** e **serie di Taylor**. Il metodo è particolarmente efficace per funzioni complesse che non hanno primitive note o che variano rapidamente.

## 🎯 Problema

Il calcolo dell'area sotto una curva tramite l'integrale definito `∫[a,b] f(x)dx` può diventare molto complesso quando:

- La funzione è estremamente complessa
- Non esistono primitive note in forma chiusa
- La funzione varia rapidamente nell'intervallo di integrazione

I metodi tradizionali come l'integrazione simbolica o la somma di Riemann possono risultare inefficienti o richiedere un numero molto elevato di suddivisioni per ottenere precisione accettabile.

## 💡 Soluzione Proposta

### Concetto Chiave

Invece di calcolare l'integrale sull'intervallo completo `[a, b]`, il metodo:

1. **Divide** l'intervallo in N sottointervalli (micro-intervalli) `[x_k, x_k + Δ]`
2. **Approssima** la funzione in ogni micro-intervallo usando la serie di Taylor
3. **Integra** analiticamente l'approssimazione di Taylor
4. **Somma** tutti i contributi per ottenere il risultato finale

### Formula Matematica

```
Area ≈ Σ[k=0 to N-1] ∫[x_k to x_k+Δ] f_Taylor(x) dx

dove:
- x_k = a + k·Δ
- Δ = (b-a)/N
- f_Taylor(x) = serie di Taylor centrata nel punto medio c_k = x_k + Δ/2
```

### Vantaggio del Punto Centrale

Centrando la serie di Taylor nel punto medio di ogni micro-intervallo:

- ✅ **Solo i termini pari contribuiscono** (i termini dispari si annullano)
- ✅ **Errore locale minimizzato** (|x - c_k| ≤ Δ/2)
- ✅ **Convergenza rapida** anche con pochi termini
- ✅ **Efficienza computazionale** migliorata

## 📊 Risultati

### Caso Test: ∫[0,1] x³e^(x²) dx ≈ 0.5

| N | Rettangoli | Errore % | Taylor (n≤4) | Errore % | Miglioramento |
|---|------------|----------|--------------|----------|---------------|
| 1 | 0.0000 | 100.0% | 1.1441 | 128.82% | -28.82% |
| 2 | 0.3858 | 22.85% | 0.4001 | 19.98% | +12.38% |
| 5 | 0.4378 | 12.43% | 0.5047 | 0.93% | **+92.52%** |
| 10 | 0.4573 | 8.53% | 0.4998 | 0.04% | **+99.53%** |
| 50+ | 0.4675+ | 6.50%+ | 0.5000 | 0.00% | **+100.0%** |

Il metodo raggiunge precisione quasi perfetta già con N=10 micro-intervalli!

## 📁 Struttura del Progetto

```
├── README.md                    # Questo file
├── integrale_di_taylor.tex      # Documentazione completa LaTeX
├── integrale_di_taylor.pdf      # Documentazione PDF (generata da .tex)
└── python/
    ├── section2.py              # Implementazione base (regola dei rettangoli)
    ├── section5.py              # Micro-intervalli con punto centrale
    └── section5_with_taylor.py  # Implementazione completa con Taylor
```

## 📖 Documentazione Completa

Per la trattazione matematica dettagliata, le dimostrazioni formali e i grafici comparativi, consulta la documentazione completa:

**📄 [Documentazione PDF](./integrale_di_taylor.pdf)** ← *Documento principale con teoria e analisi*

Il file PDF include:
- Derivazione matematica completa del metodo
- Analisi teorica della convergenza
- Grafici logaritmici degli errori
- Confronti quantitativi dettagliati
- Discussione sui limiti di stabilità numerica

## 🚀 Come Utilizzare

### Requisiti
```bash
pip install numpy
```

### Esempio Base
```python
import numpy as np
from math import factorial

def integrale_taylor(f, a, b, N=10, n_max=4):
    """
    Calcola l'integrale definito usando micro-intervalli e serie di Taylor
    
    Args:
        f: funzione da integrare
        a, b: estremi di integrazione
        N: numero di micro-intervalli
        n_max: massimo ordine pari della serie di Taylor
    """
    delta = (b - a) / N
    integral = 0.0
    
    for k in range(N):
        xk = a + k * delta
        ck = xk + delta/2  # punto centrale
        
        # Somma solo termini pari della serie di Taylor
        for n in range(0, n_max+1, 2):
            f_der = nth_derivative(f, ck, n)
            term = f_der * ((delta/2)**(n+1) * 2) / factorial(n+1)
            integral += term
    
    return integral

# Esempio d'uso
def f(x):
    return x**3 * np.exp(x**2)

risultato = integrale_taylor(f, 0, 1, N=10, n_max=4)
print(f"Risultato: {risultato:.10f}")  # ≈ 0.5000000000
```

### Esecuzione degli Script

```bash
# Metodo tradizionale (rettangoli)
python3 python/section2.py

# Micro-intervalli con punto centrale
python3 python/section5.py

# Metodo completo con Taylor
python3 python/section5_with_taylor.py
```

## ⚠️ Note Importanti

- **Stabilità numerica**: Il metodo diventa instabile per ordini elevati (n > 6-8)
- **Derivate numeriche**: L'implementazione usa differenze finite che introducono errori di round-off
- **Funzioni analitiche**: Il metodo funziona meglio con funzioni infinitamente derivabili

## 🔬 Applicazioni

Questo metodo è particolarmente utile per:

- **Funzioni oscillanti ad alta frequenza**
- **Integrali in fisica matematica** (meccanica quantistica, elettromagnetismo)
- **Simulazioni numeriche** dove serve alta precisione con pochi calcoli
- **Funzioni definite implicitamente** o tramite serie

## 📚 Riferimenti Teorici

Il metodo si basa su:
- **Serie di Taylor** per l'approssimazione locale
- **Teorema fondamentale del calcolo integrale**
- **Metodi di quadratura numerica avanzati**

## 🤝 Contributi

Per miglioramenti o estensioni del metodo, aprire una issue o una pull request. Aree di sviluppo futuro:

- Implementazione con derivate simboliche (SymPy)
- Controllo adattivo dell'errore
- Estensione a integrali multipli
- Ottimizzazione per funzioni specifiche

---

*Per domande o chiarimenti, contattare l'autore.*
