#Este programa calcula las oscilaciones de un sistema masa resorte utilizando el metodo de Euler simple
import matplotlib.pyplot as plt

#Esta funcion calcula e imprime punto por punto el sistema resorte masa 
def ResorteMasaEuler1(tiempo_inicial, tiempo_final,posicionx_inicial, velocidadx_inicial,k,masa,delta):
    posicionx_anterior = posicionx_inicial
    velocidadx_anterior = velocidadx_inicial
    tiempo = 0
    plt.ion()
    while tiempo != tiempo_final:
        tiempo = tiempo + delta
        velocidadx_siguiente = velocidadx_anterior - (k/masa)*posicionx_anterior*delta
        posicionx_siguiente = posicionx_anterior + velocidadx_siguiente - 0.5*(k/masa)*posicionx_anterior*(delta**2)
        plt.scatter(tiempo,posicionx_siguiente) 
        plt.pause(0.05)
    
        velocidadx_anterior = velocidadx_siguiente
        posicionx_anterior = posicionx_siguiente





posicionx_inicial = 30
velocidadx_inicial = 10 
k = 10
masa = 2
delta = 0.01
tiempo_inicial = 0 
tiempo_final = 30


ResorteMasaEuler1(tiempo_inicial, tiempo_final,posicionx_inicial, velocidadx_inicial,k,masa,delta)


    
    
