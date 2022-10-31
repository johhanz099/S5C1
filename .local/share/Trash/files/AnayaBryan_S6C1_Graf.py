import numpy as np
import matplotlib.pylab as plt

def grafArr(arr,title):
	plt.plot(arr)
	plt.title(title)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.savefig('graf1.png')
	#plt.show()
	plt.close()

## grafArr([1,2,1,2,1,2,1,2,1])

data1_rand = np.genfromtxt('arrAleat.dat')
grafArr(data1_rand,'Rand [0,900]')
