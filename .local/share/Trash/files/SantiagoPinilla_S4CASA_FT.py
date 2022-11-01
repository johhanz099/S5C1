import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq

N = 128 # number of point in the whole interval
f = 200.0 # frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )

#Implementación númerica Trans. de Fourier
def fourierT(ft):
	N = ft.shape[0]
	n = np.arange(N)
	X = np.array(0)
	for k in range (N):
		X = np.append(X, np.sum(ft*np.exp(-1j*2*np.pi*k*n/N)))
	return X[1:]

Y = fourierT(y) #Implementacion numerica
Y_real = fft(y)/N #Libreria fft
freq = np.fft.fftfreq(N, d=dt) #Arreglo de las frecuencias

plt.plot(np.abs(Y), label = "Transformada numerica")
plt.plot(np.abs(Y_real),label = "Transformada libreria")
plt.legend()
plt.close()


#Ejercicio 2
datos1d = np.genfromtxt("signal.dat")


plt.plot(datos1d[:,0], datos1d[:,2], label = "Señal 1d")
plt.legend()
plt.savefig("signal.png")
plt.close()

N1 = datos1d[:,2].shape[0]
dt1 = datos1d[0,0] - datos1d[1,0]
datos1d_transfor = fourierT(datos1d[:,2])
frecuencia = np.fft.fftfreq(N1, d=dt1)
plt.plot(frecuencia, np.abs(datos1d_transfor), label = "Transformada numerica")
plt.legend()
plt.savefig("Fourier_trans.png")
plt.close()

# Funcion filtro de bajos
def filtro_bajos(freq, FX):
    n = FX.shape[0]
    for i in range (freq.shape[0]):
        if np.abs(freq[i]) > 500: # filtro para freecuencias mayores a 500
            FX[i] = 0
    return FX
#Transformada filtrada
trans_filt = filtro_bajos(frecuencia, datos1d_transfor)

#Ejercicio 3

img = plt.imread("moon.jpg")
Fimg = np.fft.fft2(img)
Fimg_shift = np.fft.fftshift(Fimg)

def filtro2d(Fxy):
    for i in range (Fxy.shape[0]):
        for j in range (Fxy.shape[1]):
            if np.abs(Fxy[i,j]) > 10000000:
                Fxy[i,j] = 0
    return Fxy

img_filt = np.fft.ifft2(np.fft.fftshift(filtro2d(Fimg_shift)))
plt.imshow(np.abs(img_filt))
plt.savefig("Lunafiltrada.png")
plt.close()
