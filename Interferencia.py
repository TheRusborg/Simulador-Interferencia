import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import matplotlib.colors as colors
import math



# Se definen los parámetros necesarios para los cálculos
ancho = 0.3
alto = 0.02

Iluminacion_o = 10
long_onda = 520*10**(-10)    #520nm
dist_pantalla = 2
dist_rejillas = 0.000001
size_rejillas = 0.00001


def Desfase(x):
    # desfase = (abs(((ancho/2)-x))/(ancho/2))*(dist_rejillas/dist_pantalla)      # Máximo principal en centro
    desfase = x*(dist_rejillas/dist_pantalla)     # Máximo principal en 0
    return desfase


def Intensidad(x, long_onda=long_onda):
    desfase = Desfase(x)
    intensidad = 2*Iluminacion_o*(1+np.cos((2*np.pi*desfase)/long_onda))
    return intensidad


'''
def Pintar(x):
    intensidad = Intensidad(x)
    desfase = Desfase(x)
    # pygame.draw.line(screen, (54+intensidad*2, 255-intensidad, intensidad*2, intensidad/(4*Iluminacion_o)), (x, 0), (x, altura), 1)

    pygame.draw.line(surface, (0, 255, 0, (intensidad/(4*Iluminacion_o))*255), (x, 0), (x, altura), 1)
    print(intensidad/(4*Iluminacion_o))
'''
 
 
# Plot

### Asignar un color para cada (x,y)

res = 2000
m, n = int(2*ancho*res), int(2*alto*res)
x = np.linspace(-ancho, ancho, m)
y = np.linspace(-alto, alto, n)

transparencia = np.zeros((m,n))

for i,val in enumerate(x):
    for j in range(n):
        intensidad = Intensidad(val)/4*Iluminacion_o
        transparencia[i][j] = intensidad
transparencia = transparencia[:-1, :-1]


y,x=np.meshgrid(y, x)



fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)


# follwing step plots the heatmap of 2D-array A
graph = ax.pcolormesh(x, y, transparencia, cmap ='Greens')

# following step adds the scale of the heatmap to the figure
plt.colorbar(graph, orientation='horizontal')

# Slider
ax_slider = plt.axes([0.18, 0.1, 0.65, 0.03])  # [left, bottom, width, height]
lambda_slider = widgets.Slider(ax_slider, "lambda", 380*10**(-10), 700*10**(-10), valinit=long_onda)


# Función de actualización
def update(val,m=m, n=n, ancho=ancho, alto=alto):
    x = np.linspace(-ancho, ancho, m)
    y = np.linspace(-alto, alto, n)
    a = lambda_slider.val
    transparencia_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        for j in range(n):
            intensidad = Intensidad(valor, a)/4*Iluminacion_o
            transparencia_new[i][j] = intensidad
    transparencia_new = transparencia_new[:-1, :-1]
    
    graph.set_array(transparencia_new.ravel())  # actualizar los valores
    fig.canvas.draw_idle()

lambda_slider.on_changed(update)


plt.show()
