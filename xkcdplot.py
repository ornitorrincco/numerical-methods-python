"""
example of plot of XKCD style with matplotlib for sine damped function
"""
import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    ax.set_xlim([0, 100])
    ax.set_ylim([-1, 1])
    
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.exp(-0.1 * (x - 5) ** 2)
    data = y

    plt.annotate(
        'Texto dentro de el cuadro,genial!!!',
        xy=(50,-0.9), arrowprops=dict(arrowstyle='->'), xytext=(1, 1))

    plt.plot(data)

    plt.xlabel('el eje de las x')
    plt.ylabel('el eje de las y')

    fig.text(
        0.5, 0.05,
        'Frase que se ve bonita al pie de la pagina',
        ha='center')



plt.show()
