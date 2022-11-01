#!/usr/bin/env python
# coding: utf-8

# In[117]:


import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft,ifft,fftfreq,ifftshift,ifft2,fft2


# In[2]:


# Ejercicio 1
N = 128 # number of point in the whole interval
f = 200.0 # frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )

plt.figure()
plt.plot(t,y,label='Señal')
plt.show()


# In[139]:


def fourier(x):
    N = x.shape[0]
    n = np.arange(N)
    x_n = np.array(0)
    for k in range(N):
        x_n = np.append(x_n,np.sum(x*np.exp(-1j*2*np.pi*k*n/N)))
    return x_n[1:]


# In[140]:


y_f = fourier(y)
y_l = fft(y)/N
freq = fftfreq(N,d=dt)

fig1 = plt.figure(figsize=(15,8))
ax1 = fig1.add_subplot(121)
ax2 = fig1.add_subplot(122)

ax1.plot(freq,np.abs(y_f),label='Fourier Funct')
ax1.plot(freq,np.abs(y_l),label='Fourier Lib')
ax1.set_title('Fourier(freq)')
ax1.set_xlabel("freq")
ax1.legend()

ax2.plot(np.abs(y_f),label='Fourier Funct')
ax2.plot(np.abs(y_l),label='Fourier Lib')
ax2.set_title('Fourier')
ax2.set_xlabel('t')
ax2.legend()

plt.legend()
plt.show()
plt.close()


# In[141]:


# Ejercicio 2
signal = np.genfromtxt('signal.dat', delimiter = ',')
#data = np.genfromtxt('room-temperature.csv', skip_header = 1, delimiter = ',', usecols = (1,2,3,4))


# In[143]:


t_s, sig = signal[:,0], signal[:,1]

plt.figure()
plt.plot(t_s,sig,label='Señal en función del tiempo')
plt.title('Señal')
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('signal.png')
plt.legend()
plt.grid()
#plt.show()
plt.close()


# In[144]:


#
N_s =  np.size(sig)
dt_s = t_s[1]-t_s[0]
freq_s = fftfreq(N_s,d=dt_s)

plt.figure()
plt.plot(freq_s,np.abs(fourier(sig)),label='Función')
plt.ylabel('fft')
plt.xlabel('Frecuencia')
plt.legend()
plt.savefig('Fourier_trans.png')
plt.xlim(-2000,2000)
#plt.show()
plt.close()


# In[109]:


# Definir filtro 1d
def filtro1d(fft,freq,filtroFreq):
    for i in range(np.size(fft)):
        if np.abs(freq[i]) > filtroFreq:
            fft[i] = 0
    return fft

# Aplicar filtro
sig_filtr = filtro1d(np.abs(fourier(sig)),freq_s,1000)

plt.plot(freq_s,sig_filtr,500)
plt.xlim(-2000,2000) # para encontrar frecuencias a filtrar


# In[110]:


sig_i = ifft(sig_filtr)

plt.plot(t_s,np.real(sig),label='señal')
plt.plot(t_s,np.real(sig_i),label='señal filtrada')
plt.legend()
# Para revisar el resultado


# In[138]:


# Parte 3 Filtro 2d
moon = plt.imread('moon.jpg')
FTmoon = fft2(moon)
Fshift = ifftshift(FTmoon)


plt.plot(Fshift)
#plt.plot(FTmoon)
#plt.xlim(0,1e7)
plt.ylim(0,0.2e7)
plt.show()


# In[118]:





# In[119]:





# In[ ]:




