#Este metodo calcula la difusion de calor en una barra de 0 a 2cm en una dimension con valores de frontera a 0°C
#mediante el metodo explicito

import numpy as  np
import matplotlib.pyplot as plt


def printMatrix(a):
   print "Matrix["+("%d" %a.shape[0])+"]["+("%d" %a.shape[1])+"]"
   rows = a.shape[0]
   cols = a.shape[1]
   for i in range(0,rows):
      for j in range(0,cols):
         print "%6.f" %a[i,j],
      print
   print      
   
#propiedad del medio
c = 0.11
p = 7.8
k = 0.13

#Puntos de medicion
deltax = 0.25

#
r = 0.5

#intervalo de tiempo segun r
deltat = (r*c*p*np.power(deltax,2))/k

#numero de pasos de tiempo
Pasos = 50

#numero de Divisiones
Puntos =  int(2/deltax)

#the first indice indica el tiempo y el segundo la posicion
u = np.zeros([Pasos + 1,Puntos + 1])

#condiciones de frontera
u[0][0] = 0
u[0][Puntos] = 0


#temperatura inicial de los puntos
u[0][1] = 25
u[0][2] = 50
u[0][3] = 75
u[0][4] = 100
u[0][5] = 75
u[0][6] = 50
u[0][7] = 25


#recordar que las fronteras no son afectadas para cambiar su temperatura
for j in range(0,Pasos):    
    for i in range(1,Puntos):
        u[j+1][i] = 0.5*(u[j][i+1] + u[j][i-1])



printMatrix(u)
#revierte la matriz en sus filas 
a = np.flipud(u)

plt.imshow(a, cmap='hot', interpolation='nearest')
plt.colorbar().set_label('Temperatura[C]')
plt.show()

#    time.sleep(1)
