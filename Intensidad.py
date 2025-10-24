import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

# Se definen los parámetros necesarios para los cálculos
# Todas las unidades están en Sistema Internacional.
screen_width = 0.3
screen_height = 0.001

# I_o es la intensidad máxima (en el zero).
I_o = 10

wavelength = 520*10**(-10)
screenDist = 2
slitSeparation = 0.000002
slitWidth = 0.0000002
N_rejillas = 10


# Se calcula el desfase entre los rayos de cada rejilla.
def Desfase(x, screenDist=screenDist, slitSeparation=slitSeparation):
    desfase = x*(slitSeparation/screenDist)
    return desfase


# Se define la función para calcular la intensidad en cada punto x del espacio.
def Intensidad(x, wavelength=wavelength, screenDist=screenDist,
               slitSeparation=slitSeparation, slitWidth=slitWidth):
    
    desfase = Desfase(x, screenDist=screenDist, slitSeparation=slitSeparation)
    alpha = np.arctan(x/screenDist)
    # intensidad = 2*Iluminacion_o*(1+np.cos((2*np.pi*desfase)/wavelength))
    intensidad = I_o*((np.cos((np.pi*slitSeparation*np.sin(alpha))/wavelength))**2)*((np.sin(np.pi*slitWidth*np.sin(alpha)/wavelength))/(np.pi*slitWidth*np.sin(alpha)/wavelength))**2
    return intensidad

 
# Se prepara y se hace el plot de los datos.
# Se define la resolución de la imagen. Es la cantidad de puntos relativa al ancho y alto de la pantalla.
res = 3000
m, n = int(2*screen_width*res), int(2*screen_height*res)
x = np.linspace(-screen_width, screen_width, m)
y = np.linspace(-screen_height, screen_height, n)

## Segundo plot

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

plt.title('Patrón de difracción')
ax.set_xlabel('x (m)')
ax.set_ylabel('I (I/$I_o$)')
# plt.text(-.42, 30 , '©TheRusborg', fontsize=8)

intensidad_graf = []
for val in x:
    intensidad = Intensidad(val)/4*I_o
    intensidad_graf.append(intensidad)


graph, = plt.plot(x, intensidad_graf)

# Función de actualización 2
def update2(val,m=m, n=n, width=screen_width):
    x = np.linspace(-width, width, m)
    
    intensidad_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        intensidad_new = Intensidad(valor, wavelength=wavelength_slider.val, screenDist=screen_slider.val, slitSeparation=slitSeparation_slider.val, slitWidth=width_slider.val)/4*I_o
        intensidad_graf[i] = intensidad_new
    
    graph.set_ydata(intensidad_graf)  # actualizar los valores
    fig.canvas.draw_idle()


# Sliders
ax_slider1 = plt.axes([0.18, 0.21, 0.65, 0.03])  # [left, bottom, width, height]
wavelength_slider = widgets.Slider(ax_slider1, "Wavelength [m]", 380*10**(-10), 700*10**(-10), valinit=wavelength)


ax_slider2 = plt.axes([0.18, 0.15, 0.65, 0.03])  # [left, bottom, width, height]
screen_slider = widgets.Slider(ax_slider2, "Screen distance [m]", 0.1, 5, valinit=screenDist)


ax_slider3 = plt.axes([0.18, 0.09, 0.65, 0.03])  # [left, bottom, width, height]
slitSeparation_slider = widgets.Slider(ax_slider3, "Slit separation [m]", 0.000001, 0.00001, valinit=slitSeparation)


ax_slider4 = plt.axes([0.18, 0.03, 0.65, 0.03])  # [left, bottom, width, height]
width_slider = widgets.Slider(ax_slider4, "Slit width [m]", 0.0000001, 0.000001, valinit=slitWidth)


wavelength_slider.on_changed(update2)
screen_slider.on_changed(update2) 
slitSeparation_slider.on_changed(update2) 
width_slider.on_changed(update2) 


plt.show()