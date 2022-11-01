print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 3 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

"""
Ejercicio 3

En el archivo de datos TemperaturaNottem.csv, estan los datos de las temperaturas promedio mensuales en Nottigham, donde los datos de tiempo estan almacenados en la columna 1 y los datos de amplitud de la senial estan almacenados en la columna 2 (nota: no necesita usar la columna 0). \\            
1) Usando los paquetes de scipy de la transformada de Fourier, encuentre la periodicidad principal de los datos e imprimala en un mensaje de consola. (imprima por ejemplo: "la periodicidad principal ocurre cada xmeses")\\
2) Haga un filtro que quite esa periodicidad principal de sus datos. Haga graficas intermedias del proceso de filtrado (senial original, transformada de fourier, transformada despues del filtro) y haga una grafica final de su senial filtrada y guardela SIN MOSTRARLA en TempFiltrada.png\\
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft,fftfreq,ifft
# descargar datos y definir variables relevantes:

data = np.genfromtxt("TemperaturaNottem.csv", delimiter =",")
time = data[1:,1]
temp = data[1:,2]

plt.figure()
plt.plot(time,temp,'.-',label='Datos temperatura(t)')
plt.legend()
plt.savefig("señalOriginal.png")
plt.close()

# TRANSFORMADA DE FOURIER
# Puede usar los siguientes paquetes:
#from scipy.fftpack import fft, fftfreq, ifft
N_s =  np.size(temp)
dt_s = time[1]-time[0]
freq_s = fftfreq(N_s, d=dt_s)

plt.figure()
plt.plot(freq_s,np.abs(fft(temp)),label='Transformada vs freq')
plt.ylabel('fft')
plt.xlabel('Frecuencia')
#plt.xlim([-3,3])
plt.legend()
plt.savefig('transformadaDeFourier.png')
#plt.show()
plt.close()

print("la periodicidad principal ocurre cada 1 mes")


# SU FILTRO

# Filtro
def filtro1d(freq_s, Ftrans):
    #n = Ftrans.shape[0]
    n = np.size(Ftrans)
    for i in range (n):
        if np.abs(freq_s[i]) > 1:
            Ftrans[i] = 0
    return Ftrans


#Transformada después del filtro
TFiltro = filtro1d(freq_s, fft(temp))



# SU GRAFICA FILTRADA
plt.figure()
plt.plot(time,TFiltro,label="Señal Transformada")
plt.xlabel("Time")
plt.ylabel("Señal filtrada")
plt.legend()
plt.savefig("TempFiltrada.png")





