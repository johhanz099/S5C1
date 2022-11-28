import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt("data.dat", delimiter = ",")
time = data[:,0]

# Filtrar datos para imprimir cada dos
def filtrar(data):
    for j in range(data.shape[1]):
        for i in range(0,data.shape[0],5):
            data = np.delete(data,i,j)



# Dado el orden de los cuerpos, hacer las gráficas
def graficarDat(data,cuerpos):
    plt.figure()
    for i in range(1,len(cuerpos)*2+1,2):
        plt.plot(data[:,i],data[:,i+1],label=cuerpos[i-int((i/2+1))])
    plt.legend()
    plt.savefig("Simulacion.png")
    plt.close()
    
graficarDat(data,['Sonda','Tierra','Jupiter','Sol'])
        
    
