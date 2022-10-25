import numpy as np
import matplotlib.pylab as plt

def graf_euler(arrx, arry):
	plt.plot(arrx, arry, label = "MetEuler")
	plt.xlabel("x")
	plt.ylabel("F(x)")
	plt.legend()
	plt.savefig("Euler2.png")
	plt.close()

def graf_runge(arrx, arry):
	plt.plot(arrx, arry, label = "Met Runge-Kutta")
	plt.xlabel("x")
	plt.ylabel("f(x)")
	plt.legend()
	plt.savefig("Runge2.png")
	plt.close()


#Grafica Solucion analitica por euler:
graf_euler(np.genfromtxt("euler2d.dat", delimiter = ",", usecols=0) , np.genfromtxt("euler2.dat", delimiter = ",", usecols=1))
graf_runge(np.genfromtxt("rk42.dat", delimiter = ",", usecols=0) , np.genfromtxt("rk42.dat", delimiter = ",", usecols=1))