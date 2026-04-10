# Models and Simulation

#### Tomas Marmay ~ FAMAF 2025

---

### Overview

This repository contains the practical work for the **Models and Simulation** course at FAMAF. The course covers the mathematical and computational foundations of simulation: pseudo-random number generation, statistical sampling methods, Monte Carlo integration, discrete-event simulation, and Markov chains. All implementations are in Python.

---

### Shared Modules

These modules are reused across the practical guides:

- **`generador_numeros_pseudoaleatorios.py`** — Pseudo-random number generators: Von Neumann middle-square method, mixed congruential generator, multiplicative congruential generator, and auxiliary utilities.
- **`monte_carlo.py`** — Monte Carlo integration in one and two dimensions.
- **`graficador.py`** — Plotting utilities for visualizing distributions and simulation results.

---

### Practical Guides

Each folder contains the assignment PDF and the Python scripts solving the exercises.

| Folder | Topics |
|--------|--------|
| `guia3/` | Pseudo-random number generation, congruential generators, uniformity tests |
| `guia4/` | Discrete random variable generation, inverse transform method |
| `guia5/` | Continuous random variable generation: inverse transform, acceptance-rejection |
| `guia6/` | Normal distribution generation (Box-Muller, Kinderman-Ramage), other continuous distributions |
| `guia7/` | Markov chains: transition matrices, steady-state distributions, eigenvalue analysis |

---

### Final Project — Repair Problem Simulation

**[`proyecto/CuevasMarmay.ipynb`](proyecto/CuevasMarmay.ipynb)** · **[PDF](proyecto/CuevasMarmay.pdf)**

Discrete-event simulation of a supermarket checkout system subject to machine failures and repairs. Two scenarios are modeled and compared:

- **Exercise 1:** `N` registers in service, `S` spares, **1 repair technician**. Failure times follow an exponential distribution `F ~ E(λ = 1/TF)` and repair times `R ~ E(λ = 1/TR)`. The simulation estimates total system downtime over a fixed horizon.
- **Exercise 2:** Same system but with **2 repair technicians** vs. adding an extra spare machine. Compares both strategies statistically over 10,000 simulation runs to determine which option maximises system uptime.

The notebook includes simulation code, result analysis, confidence intervals, and plots comparing both configurations.

> Assignment guide: [`guia_problema_de_reparacion.pdf`](proyecto/guia_problema_de_reparacion.pdf)

---

### Exams

- `parcial1/` — First midterm
- `parcial2/` — Second midterm
- `parcial3/` — Third midterm / final

Each folder includes the exam script and, where available, past-year versions for reference.

---

### Theory Materials

PDF lecture notes are in the [`teorico/`](teorico/) folder (chapters 1–5, 7–8).

Personal annotated notes with highlights: [OneNote notebook](https://onedrive.live.com/redir?resid=9058A3FC122E9092%21125&authkey=%21AJL8n7n0jj1Xx7E&page=View&wd=target%28Modelos%20y%20simulaci%C3%B3n.one%7Cc2fcaa61-86bb-7445-afb8-6812a61ea75e%2FRepaso%20y%20cap%C3%ADtulo%202%7Cc9b34b93-24f5-1946-9f83-35f4fa5039a5%2F%29&wdorigin=NavigationUrl)

Main reference: [Simulation — Sheldon M. Ross](https://acrobat.adobe.com/id/urn:aaid:sc:US:6c224e8b-f5e8-4e26-9fa6-3366a93e660c)
