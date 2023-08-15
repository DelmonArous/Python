import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# os.system('cls')
plt.close('all')

# Open and read txt. file
path = "https://www.uio.no/studier/emner/matnat/math/STK1100/data/doedelighet.txt"
# path = 'https://www.uio.no/studier/emner/matnat/math/STK1100/data/doedssannsynlighet-felles.txt'
df   = pd.read_csv(path, sep = '\t')

# Store column data
alder   = df['alder'].values
menn    = df['menn'].values
kvinner = df['kvinner'].values

# Dødelighetstabellen inneholder ettårige dødssannsynligheter pr. 1000 
# individer; P(X >= x). Vi deler på 1000 slik at vi får sannsynligheter
qz = np.array(menn)/1000
rz = np.array(kvinner)/1000

### Oppgave 1a) ### 

# Plot dødssannsynligheter
# plt.figure()
# plt.plot(alder, qz, 'r-', alder, rz, 'b-')
# plt.xlabel('Alder (år)')
# plt.ylabel('$q_z$ og $r_z$')
# plt.title('Ettårige dødssannsynligheter')
# plt.legend(['Menn', 'Kvinner'])
# plt.show()

plt.figure()
plt.semilogy(alder, qz, 'r-', alder, rz, 'b-')
plt.xlabel('Alder (år)', fontsize = 14)
plt.ylabel('$q_z$ og $r_z$', fontsize = 14)
plt.title('Ettårige dødssannsynligheter', fontsize = 18)
plt.legend(['Menn', 'Kvinner'], fontsize = 12)
plt.show()

### Oppgave 1b) ###

# Overlevelsessannsynligheter er gitt fra produktsetningen; 
# S(x) = P(X>x) 
# = P(X>0) * P(X>1|X>0) * ... * P(X>x) * P(X>x|X>x-1)
# = P(X>0) * P(X>1|X>=1) * ... * P(X>x) * P(X>x|X>=x)
# = (1-q0) * (1-q1) * ... *(1-qx) 
Sx = np.cumprod(1 - qz)
Sy = np.cumprod(1 - rz)

# Kumulativ sannsynlighetsfordeling for levealder X; F(x)
# F(x) = P(X <= x) = 1 - P(X > x) = 1 - S(x) 
Fx = 1 - Sx
Fy = 1 - Sy

# Plot kumulativ fordeling
plt.figure()
plt.plot(alder, Fx, 'r-', alder, Fy, 'b-')
plt.xlabel('Alder (år)', fontsize = 14)
plt.ylabel('$F_X(x)$ og $F_Y(y)$', fontsize = 14)
plt.title('Kumulative fordelingsfunksjoner for levealder', fontsize = 18)
plt.legend(['Menn', 'Kvinner'], fontsize = 12)
plt.show()

### Oppgave 1c) ###

ind_60 = np.where(alder == 60)
ind_70 = np.where(alder == 70)
ind_80 = np.where(alder == 80)
ind_90 = np.where(alder == 90)

print('Sannsynligheten for at en mann/kvinne blir minst 60 år: ' + 
      str(np.round(Sx[ind_60],3))[1:-1] + '/' + 
      str(np.round(Sy[ind_60],3))[1:-1])
print('Sannsynligheten for at en mann/kvinne blir minst 70 år: ' + 
      str(np.round(Sx[ind_70],3))[1:-1] + '/' + 
      str(np.round(Sy[ind_70],3))[1:-1])
print('Sannsynligheten for at en mann/kvinne blir minst 80 år: ' + 
      str(np.round(Sx[ind_80],3))[1:-1] + '/' + 
      str(np.round(Sy[ind_80],3))[1:-1])
print('Sannsynligheten for at en mann/kvinne blir minst 90 år: ' + 
      str(np.round(Sx[ind_90],3))[1:-1] + '/' + 
      str(np.round(Sy[ind_90],3))[1:-1])

### Oppgave 2a) ###

# Medianaldrene for menn og kvinner
median_xalder = np.interp(0.5, Fx, alder)
median_yalder = np.interp(0.5, Fy, alder)

print('Median alder for mann/kvinne: ' + 
      str(np.round(median_xalder,1)) + '/' + 
      str(np.round(median_yalder,1)) + ' år')

### Oppgave 2b) ###

# Bestemmer punktsannsynligheten p(x) = P(X=x) = F(x) - F(x-1)
# For x = 0, har vi at p(0) = P(X=0) = P(X<=0) = F(0)
tmp_Fx           = np.zeros(107)
tmp_Fy           = np.zeros(107)
tmp_Fx[1:107]    = Fx[0:106]
tmp_Fy[1:107]    = Fy[0:106]
px               = Fx - tmp_Fx
py               = Fy - tmp_Fy

# Plot sannsynlighetsfordelingen for p(x)
width = 1
plt.figure()
plt.bar(alder, px, width, color = 'r', edgecolor = 'black')
plt.bar(alder, py, width, color = 'b', edgecolor = 'black', alpha = 0.6)
plt.xlabel('Alder (år)', fontsize = 14)
plt.ylabel('$p_X(x)$ og $p_Y(y)$', fontsize = 14)
plt.title('Punktsannsynligheter for levealder', fontsize = 18)
plt.legend(['Menn', 'Kvinner'], fontsize = 12)
plt.show()

### Oppgave 2c) ###

# Forventet levealder for for menn E(X) og kvinner E(Y) er gitt ved
Ex = np.sum(alder * px) 
Ey = np.sum(alder * py)

print('Forventet levealder for mann/kvinne: ' + 
      str(np.round(Ex,1)) + '/' + str(np.round(Ey,1)) + ' år')

# Forventet gjenstsående levealder E(X|X>=a) ved a = 0, 30, 50 og 80 år
for a in np.array([0, 30, 50, 80]):
    h_alder = (alder - a)*(alder >= a)
    EhX = sum(h_alder * px)
    EhY = sum(h_alder * py)
    
    print('Forventet gjenstsående levealder for mann/kvinne ved ' + str(a) + 
          ' år: ' + str(np.round(EhX,1)) + '/' + str(np.round(EhY,1)) + ' år')
    
EhX = np.zeros(107)
EhY = np.zeros(107)

for a in np.arange(107):
    h_alder = (alder - a)*(alder >= a)
    EhX[a] = sum(h_alder * px)
    EhY[a] = sum(h_alder * py)

# Plot forventet gjenstårende levealder
plt.figure()
plt.plot(alder, EhX, 'r-', alder, EhY, 'b-')
plt.xlabel('Alder (år)', fontsize = 14)
plt.ylabel('$E_{h_X}(x)$ og $E_{h_Y}(y)$ (år)', fontsize = 14)
plt.title('Forventet gjenstående levealder', fontsize = 18)
plt.legend(['Menn', 'Kvinner'], fontsize = 12)
plt.show()
