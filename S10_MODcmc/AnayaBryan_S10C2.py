#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt


# 1) lea los datos de resorte.dat y almacenelos.
dataR = np.genfromtxt("resorte.dat", delimiter = " ")
t = dataR[:,0]
y = dataR[:,1]

# Graficar datos
plt.figure()
plt.plot(t,y)
#plt.savefig("t_vs_A")
plt.close()

#xp = np.linspace(0,5,100)
#yp = np.exp(-xp)*np.cos(100*xp)
#plt.figure()
#plt.plot(xp,yp)
#plt.savefig("modelo.png")




# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por  
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros que se busca determinar.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne los datos modelados  
# 2b.) Definir una funcion que retorne la funcion de verosimilitud

# Función modelo ------------------------------------
def modelo(t,a,gama,omega):
    xt = a*np.exp(-gama*t)*np.cos(omega*t)
    return xt

# Función "likelihood" ------------------------------
def likelihood(t,a,gama,omega):
    chi2 = np.sum( ((y - modelo(t,a,gama,omega))**2) )
    exp = np.exp(-.5*chi2)
    return exp



# 2c.) Caminata

# Función para estimar parámetros -------------------
def caminata(n,aini,gamaini,omegaini,sigma1,sigma2,sigma3):
    # x1 -> valores para la amplitud
    # x2 -> valores para gamma
    # x3 -> valores para omega
    x1,x2,x3 = np.zeros(n), np.zeros(n), np.zeros(n)
    x1[0],x2[0],x3[0] = 0,0,0
    aold = aini
    gamaold = gamaini
    omegaold = omegaini
    for i in range(0,n-1):
        x1_new = x1[i] + np.random.uniform(-sigma1,sigma1)
        x2_new = x2[i] + np.random.uniform(-sigma2,sigma2)
        x3_new = x3[i] + np.random.uniform(-sigma3,sigma3)
        
        l_new = likelihood(t,x1_new,x2_new,x3_new)
        l_old = likelihood(t,aold,gamaold,omegaold)
        alpha = l_new / l_old
        
        if ( alpha > 1 ):
            x1[i+1] = x1_new
            x2[i+1] = x2_new
            x3[i+1] = x3_new
            aold, gamaold, omegaold = x1_new, x2_new, x3_new
        else:
            b = np.random.uniform()
            if (b < alpha):
                x1[i+1] = x1_new
                x2[i+1] = x2_new
                x3[i+1] = x3_new
                aold, gamaold, omegaold = x1_new, x2_new, x3_new
            else:
                x1[i+1] = aold
                x2[i+1] = gamaold
                x3[i+1] = omegaold
            
    return x1,x2,x3

#condiciones iniciales: tomen por ejemplo:
aini=7.5
gamaini=0.6
omegaini=18.2

#numero de pasos: empiecen con 10000 y aumenten el número si ven que el algoritmo necesita mas pasos para converger.
n=10000

sigma1 = 0.8
sigma2 = 0.5
sigma3 = 0.1
x1,x2,x3 = caminata(n,aini,gamaini,omegaini,sigma1,sigma2,sigma3)

# Prueba de graficar arreglos para los parámetros
plt.figure()
plt.plot(x1)
#plt.savefig("x1.png")
plt.close()

plt.figure()
plt.plot(x2)
#plt.savefig("x2.png")
plt.close()

plt.figure()
plt.plot(x3)
#plt.savefig("x3.png")
plt.close()


# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."

a_best = np.mean(x1[2000:])
gamma_best = np.mean(x2[2000:])
omega_best = np.mean(x3[2000:])
print("LOS MEJORES PARAMETROS SON a =",a_best,"; gamma =",gamma_best,"; omega = ",omega_best)



# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.png
plt.figure()
plt.plot(t,y,label='Datos originales')
t_mod = np.linspace(0,5,1000)
plt.plot(t_mod,modelo(t_mod,a_best,gamma_best,omega_best),label="Modelo")
plt.legend()
plt.savefig("Resorte.png")
plt.close()



# 3) SABIENDO QUE omega=np.sqrt(k/m), imprima un mensaje dónde diga si puede o NO determinar k Y m de manera individual usando el método anterior. Justifique su respuesta (puede hacer pruebas con el código para responder).
print("Dado que el algoritmo utilizado funciona para encontrar el conjunto de mejores parámetros, sería posible encontrar, por aparte, la masa y la constante del resorte. El modelo tendría que cambiarse a: A*exp(-gamma*t)*cos(sqrt(k)t/sqrt(m)). Tomando sqrt(k)=k', sqrt(m)=m', el modelo se convierte a:A*exp(-gamma*t)*cos(k't/m'). Se podrían encontrar los parámetros por separado que mejor ajusten la función coseno utilizando el método anterior.")



