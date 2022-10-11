import numpy as np
import matplotlib.pylab as plt

datFinicial = np.genfromtxt("Finicial.dat", delimiter = ",")
xf = datFinicial[:,0]
yf = datFinicial[:,1]

plt.figure()
plt.plot(xf,yf,label='Condición inicial')
plt.xlabel("x")
plt.ylabel("h")
plt.ylim(-.5*np.max(yf),2*np.max(yf))
plt.legend()
plt.savefig("Finicial.png")
plt.close()


dataOnda = np.genfromtxt("dataOnda.dat", delimiter = ",")
t = dataOnda[:,0]
fils, cols = dataOnda.shape[0], dataOnda[1]
plt.figure()
for i in range(10):
	plt.plot(t,dataOnda[i,1:])
plt.savefig("GrafOnda")
