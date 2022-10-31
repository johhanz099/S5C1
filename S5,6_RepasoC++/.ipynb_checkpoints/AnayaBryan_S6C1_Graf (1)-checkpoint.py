import numpy as np
import matplotlib.pylab as plt

def grafArr(arr,title,nameGraf):
	plt.plot(arr,'r.')
	plt.title(title)
	plt.xlabel('x')
	plt.ylabel('y')
	#plt.legend()
	plt.savefig(nameGraf)
	#plt.show()
	plt.close()

## grafArr([1,2,1,2,1,2,1,2,1])

data1_rand = np.genfromtxt('arrAleat.dat')
data2_imp  = np.genfromtxt('arrImp.dat')
umbral = 800

grafArr(data1_rand,'Rand [0,900]','fig1_dataRand.png')
grafArr(data2_imp,'Impares menos al umbral de ' + str(umbral),'fig2_dataImp.png')
