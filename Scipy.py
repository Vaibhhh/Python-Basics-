#Exponential Function
from scipy import special
a=special.exp10(2)
print(a)

b=special.exp2(3)
print(b)

#Trignometry
c=special.cosdg(90)
print(c)

#Integeration
from scipy import integrate
help(integrate.quad)
i=scipy.integrate.quad(lambda x:special.exp10(x),0,1)
print(i)
