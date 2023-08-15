import numpy as np
import matplotlib.pyplot as plt

N_tot   = 10000             # antall terningkast
a       = [1,2,3,4,5,6]     # utfallsrom
p_j     = len(a)*[(1/6)]    # sannsynligheter
vec     = np.arange(17,N_tot,len(a)*10)
f_j     = np.empty(len(vec))
p       = len(vec)*[(1/6)]

for idx, n in enumerate(vec):

    # Simuler n terningkast
    S_j = np.random.choice(a, n, p=p_j)

    # Beregn relativ frekvens for hver kategori
    _, N_j  = np.unique(S_j, return_counts=True)
    f_j_temp = N_j/n
    f_j[idx] = f_j_temp[-1] # relativ frekvens for terninkast 6

# Plot forventet gjenstårende levealder
plt.figure()
plt.plot(vec, f_j, 'r-', vec, p, 'b-')
plt.xlabel('Antall terningkast', fontsize = 14)
plt.ylabel('Relativ frekvens for terningkast 6', fontsize = 14)
plt.legend(['Simulert', 'Teoretisk'], fontsize = 12)
plt.show()



