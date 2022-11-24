import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt("data.dat", delimiter = ",")

s_x =  data[:,0]
s_y = data[:,1]
tx = data[:,2]
ty = data[:,3]
jx = data[:,4]
jy = data[:,5]
sx = data[:,6]
sy = data[:,7]

#sx = sx[100:-100]
#tx = tx[100:-100]
#sy = sy[100:-100]
#ty = ty[100:-100]

#plt.figure()
#plt.plot(t,tx,label="tx(t)")
#plt.plot(t,ty,label="ty(t)")
#plt.legend()
#plt.savefig("tx_ty.png")
#plt.close()

plt.figure()
plt.plot(sx,sy,'-',label="Sol y(x)")
plt.plot(tx,ty,'-',label="Tierra y(x)")
plt.plot(s_x,s_y,'-',label="Sonda y(x)")
plt.plot(jx,jy,'-',label="Jupiter y(x)")
plt.legend()
plt.savefig("Simulacion.png")
plt.close()