from math import *

def f(x):
	return cos(x)
	
def trapes(f,a,b,n):
	h = (b-a)/n
	sum = 0.0
	for i in range(1,n):
		x = a + i*h
		sum = sum + f(x)
		
	I = 0.5*h*(f(a)+f(b)+2*sum)
	return(I)
	
	
a = 0.0; b = 1.0
M = 24
eps = 1.0e-12

n = 1; 

I = trapes(f,a,b,n)

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
