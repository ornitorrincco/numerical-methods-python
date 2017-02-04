#Calcula e imprime la trayectoria de un tiro parabolico con las ecuaciones de cinematica

import matplotlib.pyplot as plt

#grafica en tiempo real
def TiroParabolicoEuler1(tiempo_inicial, tiempo_final,posiciony_inicial, velocidady_inicial,g,delta):
    
    posiciony_anterior = posiciony_inicial
    velocidady_anterior = velocidady_inicial
    tiempo = 0

    plt.ion()
    while tiempo != tiempo_final:
        tiempo = tiempo + delta
        velocidady_siguiente = velocidady_anterior - g*delta
        posiciony_siguiente = posiciony_anterior + velocidady_anterior - 0.5*g*(delta**2)
        a = plt.scatter(tiempo,posiciony_siguiente)
        plt.pause(0.05)
    
        velocidady_anterior = velocidady_siguiente
        posiciony_anterior = posiciony_siguiente

#calcula los puntos y luego grafica
def TiroParabolicoEuler2(tiempo_inicial, tiempo_final,posiciony_inicial, velocidady_inicial,g,delta):
    return 0



#condiciones iniciales

posiciony_inicial = 30
velocidady_inicial = 0 
g = 9.8
delta = 1
tiempo_inicial = 0 
tiempo_final = 30

TiroParabolicoEuler1(tiempo_inicial, tiempo_final,posiciony_inicial, velocidady_inicial,g,delta)
 

    
    

