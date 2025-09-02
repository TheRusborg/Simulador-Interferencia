import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import matplotlib.colors as colors
import math


# Se definen los parámetros necesarios para los cálculos
screen_width = 0.3
screen_height = 0.02

Iluminacion_o = 10
wavelength = 520*10**(-10)    #520nm
screenDist = 2
slitSeparation = 0.000002
slitWidth = 0.0000002


def Desfase(x, screenDist=screenDist, slitSeparation=slitSeparation):
    desfase = x*(slitSeparation/screenDist)
    return desfase


def Intensidad(x, wavelength=wavelength, screenDist=screenDist,
               slitSeparation=slitSeparation, slitWidth=slitWidth):
    
    desfase = Desfase(x, screenDist=screenDist, slitSeparation=slitSeparation)
    alpha = np.arctan(x/screenDist)
    # intensidad = 2*Iluminacion_o*(1+np.cos((2*np.pi*desfase)/wavelength))
    intensidad = Iluminacion_o*((np.cos((np.pi*slitSeparation*np.sin(alpha))/wavelength))**2)*((np.sin(np.pi*slitWidth*np.sin(alpha)/wavelength))/(np.pi*slitWidth*np.sin(alpha)/wavelength))**2
    return intensidad


 
# Plot

### Asignar un color para cada (x,y)
res = 2000
m, n = int(2*screen_width*res), int(2*screen_height*res)
x = np.linspace(-screen_width, screen_width, m)
y = np.linspace(-screen_height, screen_height, n)

arr_intensidad = np.zeros((m,n))

for i,val in enumerate(x):
    for j in range(n):
        intensidad = Intensidad(val)/4*Iluminacion_o
        arr_intensidad[i][j] = intensidad
arr_intensidad = arr_intensidad[:-1, :-1]


y,x=np.meshgrid(y, x)



fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)


# follwing step plots the heatmap of 2D-array A
graph = ax.pcolormesh(x, y, arr_intensidad, cmap ='Greens_r')

# following step adds the scale of the heatmap to the figure
plt.colorbar(graph, orientation='horizontal')

# Sliders
ax_slider1 = plt.axes([0.18, 0.24, 0.65, 0.03])  # [left, bottom, width, height]
wavelength_slider = widgets.Slider(ax_slider1, "Wavelength", 380*10**(-10), 700*10**(-10), valinit=wavelength)


ax_slider2 = plt.axes([0.18, 0.17, 0.65, 0.03])  # [left, bottom, width, height]
screen_slider = widgets.Slider(ax_slider2, "Screen distance", 0.1, 5, valinit=screenDist)


ax_slider3 = plt.axes([0.18, 0.10, 0.65, 0.03])  # [left, bottom, width, height]
slitSeparation_slider = widgets.Slider(ax_slider3, "Slit separation", 0.000001, 0.00001, valinit=slitSeparation)


ax_slider4 = plt.axes([0.18, 0.03, 0.65, 0.03])  # [left, bottom, width, height]
width_slider = widgets.Slider(ax_slider4, "Slit width", 0.0000001, 0.000001, valinit=slitWidth)




# Función de actualización
def update_wavelength(val,m=m, n=n, width=screen_width, height=screen_height):
    x = np.linspace(-width, width, m)
    y = np.linspace(-height, height, n)
    a = wavelength_slider.val
    arrIntensidad_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        for j in range(n):
            intensidad = Intensidad(valor, wavelength=a)/4*Iluminacion_o
            arrIntensidad_new[i][j] = intensidad
    arrIntensidad_new = arrIntensidad_new[:-1, :-1]
    
    graph.set_array(arrIntensidad_new.ravel())  # actualizar los valores
    fig.canvas.draw_idle()


def update_screenDistance(val,m=m, n=n, width=screen_width, height=screen_height):
    x = np.linspace(-width, width, m)
    y = np.linspace(-height, height, n)
    a = screen_slider.val
    arrIntensidad_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        for j in range(n):
            intensidad = Intensidad(valor, screenDist=a)/4*Iluminacion_o
            arrIntensidad_new[i][j] = intensidad
    arrIntensidad_new = arrIntensidad_new[:-1, :-1]
    
    graph.set_array(arrIntensidad_new.ravel())  # actualizar los valores
    fig.canvas.draw_idle()
    
    
def update_slitSeparation(val,m=m, n=n, width=screen_width, height=screen_height):
    x = np.linspace(-width, width, m)
    y = np.linspace(-height, height, n)
    a = slitSeparation_slider.val
    arrIntensidad_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        for j in range(n):
            intensidad = Intensidad(valor, slitSeparation=a)/4*Iluminacion_o
            arrIntensidad_new[i][j] = intensidad
    arrIntensidad_new = arrIntensidad_new[:-1, :-1]
    
    graph.set_array(arrIntensidad_new.ravel())  # actualizar los valores
    fig.canvas.draw_idle()
    
    
def update_slitWidth(val,m=m, n=n, width=screen_width, height=screen_height):
    x = np.linspace(-width, width, m)
    y = np.linspace(-height, height, n)
    a = width_slider.val
    arrIntensidad_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        for j in range(n):
            intensidad = Intensidad(valor, slitWidth=a)/4*Iluminacion_o
            arrIntensidad_new[i][j] = intensidad
    arrIntensidad_new = arrIntensidad_new[:-1, :-1]
    
    graph.set_array(arrIntensidad_new.ravel())  # actualizar los valores
    fig.canvas.draw_idle()
    
    

wavelength_slider.on_changed(update_wavelength)
screen_slider.on_changed(update_screenDistance) 
slitSeparation_slider.on_changed(update_slitSeparation) 
width_slider.on_changed(update_slitWidth) 


plt.show()