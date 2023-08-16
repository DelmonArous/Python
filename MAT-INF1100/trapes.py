from math import * 

def f(x):
	return cos(x)
	
def trapes(f,a,b,n): 
	h = (b-a)/float(n)
	s = 0.0
	i = 1

	while i <= (n/2.):           # regner omtrent bare halvparten av funksjonsverdiene  
		x = a + (2*i - 1)*h  
		s = s + f(x)         # beregner funksjonsverdiene til de gitte x-verdiene
		i += 1
		
	I = Ip/2. + h*s  # I er tilnearming av arealet, Ip er en gitt
	return(I)        # variabel i den nederste lokken som betegner en tilnearmingen
	                 # av det tidligere arealet
a = 0.0; b = 1.0
M = 24
eps = 1E-12   # feilen vi onsker
n = 1 
h = (b-a)/float(n) 

I = h*(f(a)+f(b))/2.   # dette skal bli Ip, I[0]

j = 1
abserr = abs(I)
print "%2i. iterasjon: I=%1.14f, feil= %e" %(j, I, abserr/abs(I))

while j<M and abserr>eps*abs(I):
	j = j + 1
        Ip = I
	n = 2*n; 
	
	I = trapes(f,a,b,n)
	
	abserrold = abserr
	
	abserr = abs(I-Ip)
	
	print "%2i. iterasjon: I=%1.14f, feil= %e" %(j, I, abserr/abs(I))
	print abserrold/abserr
	
print "\n%i iterasjoner: I=%1.14f feil=%e " %(j, I, abserr/abs(I))
print "\nEksakt verdi=%1.14f, eksakt feil=%e" %(sin(b),abs(sin(b)-I)/abs(sin(b)))

'''
real	0m0.484s
user	0m0.480s   # Ved implementering av formel (2)
sys	0m0.000s
------------------
real	0m0.625s
user	0m0.590s   # Ved implementering av formel (1) 
sys	0m0.030s
'''
