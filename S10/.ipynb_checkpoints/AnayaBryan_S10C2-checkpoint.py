#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt

dataR = np.genfromtxt("resorte.dat", delimiter = " ")
t = dataR[:,0]
y = dataR[:,1]

# Graficar datos
plt.figure()
plt.plot(t,y)
plt.savefig("t_vs_A")
plt.close()

#xp = np.linspace(0,5,100)
#yp = np.exp(-xp)*np.cos(100*xp)
#plt.figure()
#plt.plot(xp,yp)
#plt.savefig("modelo.png")

# Función modelo ------------------------------------
def modelo(t,a,gama,omega):
    xt = a*np.exp(-gama*t)*np.cos(omega*t)
    return xt

# Función "likelihood" ------------------------------
def likelihood(t,a,gama,omega):
    chi2 = np.sum( ((y - modelo(t,a,gama,omega))**2) )
    exp = np.exp(-.5*chi2)
    return exp

# Función para estimar parámetros -------------------
def caminata(n,aini,gamaini,omegaini,sigma1,sigma2,sigma3):
    x1,x2,x3 = np.zeros(n), np.zeros(n), np.zeros(n)
    x1[0],x2[0],x3[0] = 0,0,0
    for i in range(0,n-1):
        x1_new = x1[i] + np.random.uniform(-sigma1,sigma1)
        x2_new = x2[i] + np.random.uniform(-sigma2,sigma2)
        x3_new = x3[i] + np.random.uniform(-sigma3,sigma3)
        
        l_new = likelihood(t,x1_new,x2_new,x3_new)
        l_old = likelihood(t,aini,gamaini,omegaini)
        alpha = l_new / l_old
        
        if ( np.random.rand() < min(1,alpha) ):
            x1[i+1] = x1_new
            x2[i+1] = x2_new
            x3[i+1] = x3_new
        else:
            x1[i+1] = x1[i]
            x2[i+1] = x2[i]
            x3[i+1] = x3[i]
            
    #r = np.array([])
    return x1,x2,x3

aini = 7.5
gamaini = 0.6
omegaini = 18.2
n = 10000
sigma1 = 0.2
sigma2 = 0.2
sigma3 = 0.2
x1,x2,x3 = caminata(n,aini,gamaini,omegaini,sigma1,sigma2,sigma3)
plt.figure()
plt.plot(x1)
plt.savefig("x1.png")
plt.close()













# Función para graficar
def crearGraf(n,sigma1,sigma2,sigma3,aini,gamaini,omegaini):
    plt.figure()
    plt.hist(caminata(n,aini,gamaini,omegaini,sigma1,sigma2,sigma2),density=True,bins=30)
    plt.plot(x_f,mifun(x_f))
    plt.savefig("histograma_"+str(sigma)+"_"+str(n)+".pdf")
    plt.close()

# 1) lea los datos de resorte.dat y almacenelos.

# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por  
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros que se busca determinar.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne los datos modelados  


# 2b.) Definir una funcion que retorne la funcion de verosimilitud


# 2c.) Caminata

#condiciones iniciales: tomen por ejemplo:
aini=7.5
gammaini=0.6
omegaini=18.2

#numero de pasos: empiecen con 10000 y aumenten el número si ven que el algoritmo necesita mas pasos para converger.
iteraciones=10000


# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."

# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.png

# 3) SABIENDO QUE omega=np.sqrt(k/m), imprima un mensaje dónde diga si puede o NO determinar k Y m de manera individual usando el método anterior. Justifique su respuesta (puede hacer pruebas con el código para responder).



