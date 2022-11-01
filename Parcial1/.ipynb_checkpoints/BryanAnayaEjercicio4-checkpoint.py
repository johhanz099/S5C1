print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 4 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

# Ejercicio4
# Solucione, usando el metodo de LeapFrog, la ecuacion de 2do orden del enunciado del parcial
# Construya la solucion hasta t=10 (y seleccione un dt apropiado).
#tome como condiciones iniciales x(0)=-1.0 y v(0)=1.0
#haga una grafica de su solucion x en funcion de t y comparela con la funcion analitica (sol_ana)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def sol_ana(t, x0, v0):
    return (np.exp(-2.0*t))*(x0*np.cos(3.0*t)+(1.0/3.0)*(2.0*x0+v0)*np.sin(3.0*t))


