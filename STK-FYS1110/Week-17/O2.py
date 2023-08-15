import numpy as np
import matplotlib.pyplot as plt

N   = 102             # antall terningkast
a   = [1,2,3,4,5,6]   # utfallsrom

# Simuler 'ekte' terningkast
p_ekte = len(a)*[(1/6)]
s_ekte = np.random.choice(a, N, p=p_ekte)

# Simuler 'falske' terningkast
p_falsk = [1/8, 1/8, 1/4, 1/4, 1/8, 1/8]
s_falsk = np.random.choice(a, N, p=p_falsk)

# Beregn frekvenser for hvert utfall
_, N_ekte  = np.unique(s_ekte, return_counts=True)
_, N_falsk = np.unique(s_falsk, return_counts=True)
print("Frekvenssum av ekte terningkast: " + str(np.sum(N_ekte)))
print("Frekvenssum av falske terningkast: " + str(np.sum(N_falsk)))

# Lag frekvensmatriser
f_mat_ekte  = np.array([a, N_ekte])
f_mat_falsk = np.array([a, N_falsk])
print("'Ekte' frekvensmatrise: \n" + str(f_mat_ekte))
print("'Falsk' frekvensmatrise: \n" + str(f_mat_falsk))

#
width = 1
plt.figure()
plt.bar(f_mat_ekte[0], f_mat_ekte[1], width, color = 'r', edgecolor = 'black')
plt.bar(f_mat_falsk[0], f_mat_falsk[1], width, color = 'b', edgecolor = 'black', alpha = 0.6)
plt.xlabel('Kategori $S_j$', fontsize = 14)
plt.ylabel('Frekvens $N_j$', fontsize = 14)
plt.legend(['Ekte', 'Falsk'], fontsize = 12)
plt.show()

