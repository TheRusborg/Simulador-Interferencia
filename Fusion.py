import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

#En este pprograma se fusiona tanto el programa de Intensidad como el de Interferencia.
#Por este motivo habra secciones identicas a ambos programas.

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






###Parte de càlculo de intensidad



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

#Hasta aquí la parte común de ambos programas.






#Ahora toca hacer la pantalla conjunta de ambos programas.


# Primero, se añaden las intensidades en un array, para el programa de intensidad.
arr_intensidad = np.zeros((m,n))
for i,val in enumerate(x):
    for j in range(n):
        intensidad = Intensidad(val)/4*I_o
        arr_intensidad[i][j] = intensidad

# Se usa la función meshgrid para hacer dos matrices con todos los puntos distribuidos.
xx,yy=np.meshgrid(x,y)




#Ahora toca hacer el plot combinado de ambos programas.

# Se preparan los subplots y los ejes.

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 6), sharex=True)  #se puede canviar si se quiere al lado o encima.
plt.subplots_adjust(bottom=0.35, hspace=0.3) # hspace es la separacion entre graficos.


ax1.set_title('Patrón de difracción')
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
# plt.text(-.38, .0016 , '©TheRusborg', fontsize=8)


# Se hace un "heatmap" usando las matrices obtenidas con meshgrid y se le asigna a cada posición una intensidad.
# El método .T transpone la matriz.
heatmap = ax1.pcolormesh(xx.T, yy.T, arr_intensidad, cmap ='Greens_r')

# Se crea una barra con la escala de color del "heatmap".
plt.colorbar(heatmap, orientation='horizontal')




## Segundo plot para la intensidad

ax2.set_title('Patrón de difracción')
ax2.set_xlabel('x (m)')
ax2.set_ylabel('I (I/$I_o$)')



intensidad_graf = []
for val in x:
    intensidad = Intensidad(val)/4*I_o
    intensidad_graf.append(intensidad)


graph, = plt.plot(x, intensidad_graf)













# Sliders

ax_slider1 = plt.axes([0.18, 0.21, 0.65, 0.03])  # [left, bottom, width, height]
wavelength_slider = widgets.Slider(ax_slider1, "Wavelength [m]", 380*10**(-10), 700*10**(-10), valinit=wavelength)


ax_slider2 = plt.axes([0.18, 0.15, 0.65, 0.03])  # [left, bottom, width, height]
screen_slider = widgets.Slider(ax_slider2, "Screen distance [m]", 0.1, 5, valinit=screenDist)


ax_slider3 = plt.axes([0.18, 0.09, 0.65, 0.03])  # [left, bottom, width, height]
slitSeparation_slider = widgets.Slider(ax_slider3, "Slit separation [m]", 0.000001, 0.00001, valinit=slitSeparation)


ax_slider4 = plt.axes([0.18, 0.03, 0.65, 0.03])  # [left, bottom, width, height]
width_slider = widgets.Slider(ax_slider4, "Slit width [m]", 0.0000001, 0.000001, valinit=slitWidth)



# Función de actualización para ambas gràficas
def update(val,m=m, n=n, width=screen_width):
    x = np.linspace(-width, width, m)
    
    arrIntensidad_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        for j in range(n):
            intensidad = Intensidad(valor, wavelength=wavelength_slider.val, screenDist=screen_slider.val, slitSeparation=slitSeparation_slider.val, slitWidth=width_slider.val)/4*I_o
            arrIntensidad_new[i][j] = intensidad
    
    heatmap.set_array(arrIntensidad_new.ravel())  # actualizar los valores
    fig.canvas.draw_idle()


def update2(val,m=m, n=n, width=screen_width):
    x = np.linspace(-width, width, m)
    
    intensidad_new = np.zeros((m,n))
    for i,valor in enumerate(x):
        intensidad_new = Intensidad(valor, wavelength=wavelength_slider.val, screenDist=screen_slider.val, slitSeparation=slitSeparation_slider.val, slitWidth=width_slider.val)/4*I_o
        intensidad_graf[i] = intensidad_new
    
    graph.set_ydata(intensidad_graf)  # actualizar los valores
    fig.canvas.draw_idle()

    
wavelength_slider.on_changed(update)
screen_slider.on_changed(update) 
slitSeparation_slider.on_changed(update) 
width_slider.on_changed(update) 

wavelength_slider.on_changed(update2)
screen_slider.on_changed(update2) 
slitSeparation_slider.on_changed(update2) 
width_slider.on_changed(update2) 



plt.show()