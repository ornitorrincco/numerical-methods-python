import matplotlib.pyplot as plt
import numpy as np

#Ejemplo del libro de dos dimensiones

# vector de temperatura recorridos impares
U = np.zeros([500])
# vector de temperatura de recorridos pares
V = np.zeros([500])
#condiciones de frontera de U
U_condiciones = np.zeros([500])
#Condiciones de froneta de V
V_condiciones = np.zeros([500])
#vector para mantener los valores en la frontera a traves de la parter
superior de la region
Top = np.zeros([500])
#Lo mismo para los valores a traves de la parte inferior
Bottom = np.zeros([500])
#Mantiene los valores del lado derecho
Right = np.zeros([500])
#Mantiene los valores para el borde del lado izquierdo
Left = np.zeros([500])
#matriz de coeficientes para las U
U_coeficientes = np.zeros([500,3])
#matriz de coeficientes par alas V
V_coeficientes = np.zeros([500,3])
#numero de renglones de nodos en la reticula
Nrenglones = 15
#numero de columnas de nodos
Mcolumnas = 7
#difusividad termica = k/(c*densidad)
difusividad = 0.152
#intervalo espacial deltax y deltay
H = 0.125
#variable de tiempo
tiempo = 0
#valor maximod e tiempo para el que se desean los calculos
tmax = 20
#tamano de tiempo relacionado con deltax a traves de r
deltaT = 0
r = 0.5
#inicializacion del programa
for j in range(0,3):
    for i in range(0,500):
        U_coeficientes[i,j] = -1
        V_coeficientes[i,j] = -1
#se inicializa con las temperaturas en todas partes iguales a cero
for i in range(0,500):
    V[i] = 0.0
    Top[i] = 0.0
    Bottom[i] = 0.0
    Right[i] = 100.0
    Left[i] = 0.0
    U_condiciones[i] = 0
    V_condiciones[i] = 0
    #Las matrices de coeficientes se establecen al volver a escribir en la
    # diagonal y en ciertos terminos fuera de la diagonal
    mSize = Mcolumnas*Nrenglones

for i in range(0,mSize):
    U_coeficientes[i,1] = 1./r + 2
    V_coeficientes[i,1] = 1./r + 2

for i in range(Nrenglones - 1,mSize - 1 ,Nrenglones):
    U_coeficientes[i,2] = 0
    U_coeficientes[i+1,0] = 0

for i in range(Mcolumnas - 1,mSize - 1, Mcolumnas):
    V_coeficientes[i,2] = 0
    V_coeficientes[i+1,0] = 0

#ahora se obtienen los valores en los vectores en la frontera
for i in range(0,Nrenglones):
    U_condiciones[i] = Top[i]
    j = mSize - Nrenglones + i
    U_condiciones[j] = Bottom[i]

for i in range(0, Mcolumnas):
    j = (i - 1)*Nrenglones + 1
    U_condiciones[j] = U_condiciones[j] + Left[i]
    j = i*Nrenglones
    U_condiciones[j] = U_condiciones[j] + Right[i]

for i in range(0,Mcolumnas):
    V_condiciones[i] = Left[i]
    j = mSize - Mcolumnas + i
    V_condiciones[j] = Right[i]

for i in range(0, Nrenglones):
    j = (i - 1)*Mcolumnas + 1
    V_condiciones[j] = V_condiciones[j] + Top[i]
    j = i*Mcolumnas
    V_condiciones[j] = V_condiciones[j] + Bottom[i]

#Ahora se obtienen las descomposiciones LU de U_coeficientes y
# V_coeficientes
for i in range(1,mSize - 1):
    U_coeficientes[i-1,2] = U_coeficientes[i-1,2] / U_coeficientes[i-1,1]
    U_coeficientes[i,1] = U_coeficientes[i,1] - U_coeficientes[i,0]*U_coeficientes[i-1,2]
    V_coeficientes[i-1,2] = V_coeficientes[i-1,2] / V_coeficientes[i-1,1]
    V_coeficientes[i,1] = V_coeficientes[i,1] - V_coeficientes[i,0]*U_coeficientes[i-1,2]
    #Ahora se hacen las iteraciones hasta que el tiempo es igual a tMax
time = 0.0
dt = r/difusividad
    #calcular las rhs para las ecuaciones U y almacenar en el vector U
    #hacer primero los renglones superior e inferior
for i in range(0,Nrenglones):
    j = (i - 1)*Mcolumnas + 1
    U[i] = (1./r - 2)*V[j] + V[j+1] + U_condiciones[i]
    k = mSize - Nrenglones + i
    j = i*Mcolumnas
    U[k] = V[j - 1] + (1./r - 2)*V[j] + U_condiciones[k]
#Ahora para los otros
for i in range(1, Mcolumnas - 1):
    for j in range(0, Nrenglones):
        k = (i - 1)*Nrenglones
        L = i + (j - 1)*Mcolumnas
        U[k] = V[L - 1] + (1./r - 2)*V[L] + V[L + 1] + U_condiciones[k]
#ahora se obtiene la solucion para el recorrido impar
U[0] = U[0] / U_coeficientes[0,1]
for i in range(1,mSize):
    U[i] =( U[i] - U_coeficientes[i,0]*U[i - 1]) /U_coeficientes[i,1]

for i in range(0, mSize - 1):
    jfila = mSize - i
    U[jfila] = U[jfila] - U_coeficientes[jfila, 2]*U[jfila+1]
#Calcular las RHS para el recorrido par, almacenar en V. Hacer los renglones superior e inferior

for i in range(0,Mcolumnas):
    j = (i - 1)*Nrenglones + 1
    V[i] = (1./r - 2)*U[j] + U[j + 1] + V_condiciones[i]
    k = mSize - Mcolumnas + i
    j = i*Nrenglones
    V[k] = U[j - 1] + (1./r - 2)*U[j] + V_condiciones[k]
#ahora el resto de los rengones

for i in range(1,Nrenglones):
    for j in range(0,Mcolumnas):
        k = (i - 1)*Mcolumnas + j
        L = i + (j - 1)*Nrenglones
        V[k] = U[L - 1] + (1./r - 2)*U[L] + U[L + 1] + V_condiciones[k]
#Se obtiene la solucion para el recorrido par
V[0] = V[0] / V_coeficientes[0,1]
for i in range(1, mSize):
    V[i] = (V[i] - V_coeficientes[i,1]*V[i-1]) / V_coeficientes[i,1]
    
for i in range(0,mSize):
    jfila = mSize - i
    V[jfila] = V[jfila] - V_coeficientes[jfila,2]*V[jfila + 1]
    time = time + 2*dt
