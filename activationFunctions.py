from re import X
import numpy as np
import matplotlib.pyplot as plt
from math import e

def relu(x):        #Se define una funcion relu con condicionales para que no admita valores menores a 0
    if(x>0):
        a=x
    else:
        a=0
    return a*a      #Se multiplica por si mismo segun la teoria

sigmoid = lambda x: 1/(1+e**(-x))
tanh = lambda x: ((e**x)-(e**(-x)))/((e**x)+(e**(-x)))
a= range(-5,6)      #La funcion range crea una lista que recorrar los valores intermedios, pero si pone de cota superior 5, llegaria hasta 4, entonces se pone 5+1 para que llegue hasta 5
b = []
reluc = []
sigmoidc = []
tanhc = []

for i in a:      #Los valores no se guardan enteramente en una lista sino en range, por ello recorriendo la lista y usando la funcion append creamos una lista que si tenga estos valores discretos
    b.append(i)

for i in b:       #Finalmente creamos un metodo similar para que imprima las salidas al meterlas dentro de la funcion relu
    reluc.append(relu(i))

for i in b:       #Finalmente creamos un metodo similar para que imprima las salidas al meterlas dentro de la funcion relu
    sigmoidc.append(sigmoid(i))

for i in b:       #Finalmente creamos un metodo similar para que imprima las salidas al meterlas dentro de la funcion relu
    tanhc.append(tanh(i))


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
fig.suptitle('Activation Functions', fontsize=16)
ax1.plot(b, reluc, '--')
ax1.set_title('ReLU Function')
ax2.plot(b, sigmoidc, '--')
ax2.set_title('Sigmoid Function')
ax3.plot(b,tanhc, '--')
ax3.set_title('TanH function')
plt.show()

    
