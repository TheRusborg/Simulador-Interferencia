import numpy as np
from matplotlib.figure import Figure
import time

def create_plots(main_window, 
                 slit_separation=None, 
                 slit_width=None, 
                 wavelength=None, 
                 screen_distance=None):
    """
    Create plots - OPTIMIZED FOR PERFORMANCE (mentira)
    """
    
    # Clear existing plots
    main_window.figure1.clear()
    main_window.figure2.clear()
    
    # ===== CANVAS 1: Interference Pattern =====
    ax1 = main_window.figure1.add_subplot(111)

    # VALORES CON 520nm (VERDE)
    if slit_separation is None:
        slit_separation = 0.000002      # 2μm
    if slit_width is None:
        slit_width = 0.0000002          # 0.2μm
    if wavelength is None:
        wavelength = 520*10**(-9)       # 520nm (GREEN)
    if screen_distance is None:
        screen_distance = 2.0           # 2m
    
    # Make sure that screen_distance is not zero
    screen_distance = max(screen_distance, 0.1)
    
    # Dimensiones de pantalla
    screen_width = 1.0
    screen_height = 0.001
    I_o = 10

    # OPTIMISATION: vectorized function for performance
    def intensidad_vectorizada(x, wavelength, screenDist, slitSeparation, slitWidth):
        # CORRECTION: avoid division by zero
        screenDist = max(screenDist, 0.1)
        alpha = np.arctan(x / screenDist)
        
        with np.errstate(divide='ignore', invalid='ignore'):
            # Interference term
            term_interference = np.cos((np.pi * slitSeparation * np.sin(alpha)) / wavelength) ** 2
            
            # Diffraction term
            sinc_arg = (np.pi * slitWidth * np.sin(alpha)) / wavelength
            term_diffraction = (np.sin(sinc_arg) / sinc_arg) ** 2
            term_diffraction = np.nan_to_num(term_diffraction, nan=1.0)
            
            intensidad = I_o * term_interference * term_diffraction
            
        return intensidad

    # OPTIMISATION: reduce resolution while moving the slider
    current_time = getattr(main_window, '_last_update_time', 0)
    new_time = time.time()
    time_diff = new_time - current_time
    main_window._last_update_time = new_time
    
    if time_diff < 0.1:
        res_x = 250
        res_y = 5
    else:
        res_x = 500
        res_y = 10
    
    m = max(int(2 * screen_width * res_x), 2)
    n = max(int(2 * screen_height * res_y), 2)
    
    x = np.linspace(-screen_width, screen_width, m)
    y = np.linspace(-screen_height, screen_height, n)

    intensity_x = intensidad_vectorizada(x, wavelength, screen_distance, slit_separation, slit_width) / (4 * I_o)
    
    # Create 2D array
    arr_intensidad = np.tile(intensity_x, (n, 1))

    # Create meshgrid for plotting
    xx, yy = np.meshgrid(x, y, indexing='xy')
    heatmap = ax1.pcolormesh(xx, yy, arr_intensidad, 
                            cmap='Greens_r', 
                            shading='auto')
    
    # Customize the plot
    #ax1.set_title('Patrón de difracción', fontsize=12, fontweight='bold')
    ax1.set_xlabel('x (m)', fontsize=11)
    ax1.set_ylabel('y (m)', fontsize=11)
    
    # Create colorbar
    cbar = main_window.figure1.colorbar(heatmap, ax=ax1, orientation='horizontal', pad=0.2)
    cbar.set_label('Intensidad')
    
    main_window.figure1.tight_layout()

    # ===== CANVAS 2: Intensity Distribution =====
    ax2 = main_window.figure2.add_subplot(111)
    x_line = np.linspace(-screen_width, screen_width, 750)
    intensity_line = intensidad_vectorizada(x_line, wavelength, screen_distance, slit_separation, slit_width) / (4 * I_o)
    
    ax2.plot(x_line, intensity_line, 'b-', linewidth=2)
    #ax2.set_title('Distribución de intensidad', fontsize=12, fontweight='bold')
    ax2.set_xlabel('x (m)', fontsize=11)
    ax2.set_ylabel('I (W)', fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    main_window.figure2.tight_layout()
    
    # Draw both canvases
    main_window.canvas1.draw()
    main_window.canvas2.draw()