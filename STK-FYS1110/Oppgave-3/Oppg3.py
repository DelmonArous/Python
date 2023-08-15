import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

# Definer variabler
N   = 100                        # antall kast med to terninger
T1  = np.random.randint(1, 7, N) # antall øyne for terning 1
T2  = np.random.randint(1, 7, N) # antall øyne for terning 2

X = T1 + T2             # sum av antall øyne
Y = np.maximum(T1,T2)   # største antall øyne

#Etter n kast er gjennomsnittet lik summen av X- og Y-verdiene for de 
# n første kastene dividert med n
n       = np.arange(1, N+1)
gjsnX   = np.cumsum(X)/n
gjsnY   = np.cumsum(Y)/n

### Oppgave 3a) og 3b) ###

# Plot av gjennomsnittet etter n kast som en funksjon av n og sett skalaen 
# for aksene i 
plt.figure()
plt.plot(n, gjsnX, 'r-', n, gjsnY, 'b-')
plt.axis([0, N+1, 2, 12])
plt.xlabel('Antall kast n')
plt.ylabel('Gjennomsnitt av X og Y')
plt.legend(['X', 'Y'])
plt.show()

### Oppgave 3c) ###

# Definer stokastiske variabler
x = np.arange(2, 12+1)
y = np.arange(1, 6+1)

# Punktsannsynligheter
px = np.array([1,2,3,4,5,6,5,4,3,2,1])/36
py = np.array([1,3,5,7,9,11])/36

# Forventningsverdier
Ex = np.sum(x * px) 
Ey = np.sum(y * py)

print('Forventningsverdi for X/Y: ' + 
      str(np.round(Ex,2)) + '/' + str(np.round(Ey,2)))
