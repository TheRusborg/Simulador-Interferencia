import numpy as np

class IntensityCalculator:
    """
    Class to handle intensity distribution calculations.
    """
    
    def __init__(self, I_o=10):
        self.I_o = I_o  # Maximum intensity
    
    def calculate_phase(self, x, screen_distance, screen_separation):
        """
        Calculate phase difference between rays at each point.
        """
        desfase = x * (screen_separation / screen_distance)
        return desfase
    
    def calculate_intensity(self, x, wavelength, screen_distance, screen_separation, slit_width):
        """
        Calculate the intensity at a given position x.
        """
        alpha = np.arctan(x / screen_distance)
        sin_alpha = np.sin(alpha)
        
        # Interference term
        interference = (np.cos((np.pi * screen_separation * sin_alpha) / wavelength))**2
        
        # Diffraction term (avoid division by zero)
        beta = (np.pi * slit_width * sin_alpha) / wavelength
        diffraction = np.where(np.abs(beta) < 1e-10, 1.0, (np.sin(beta) / beta)**2)
        
        intensity = self.I_o * interference * diffraction
        return intensity
    
    def create_intensity_distribution(self, wavelength, screen_distance, screen_separation, slit_width,
                                     screen_width=0.3, resolution=3000):
        """
        Create a 1D intensity distribution
        
        Returns:
            x: array of x positions
            intensity: array of intensity values
        """
        m = int(2 * screen_width * resolution)
        x = np.linspace(-screen_width, screen_width, m)
        
        intensity = np.array([self.calculate_intensity(xi, wavelength, screen_distance, 
                                                         screen_separation, slit_width) / 4 * self.I_o 
                                for xi in x])
        
        return x, intensity


def create_intensity_plot(axes, 
                          wavelength=520e-9, 
                          screen_distance=2.0, 
                         screen_separation=20e-6, 
                         slit_width=2e-6
                         ):
    """
    Create the plot for the initial intensity distribution.
    """
    calculator = IntensityCalculator()
    x, intensity = calculator.create_intensity_distribution(
        wavelength, screen_distance, screen_separation, slit_width
    )
    
    # Create line plot
    line, = axes.plot(x, intensity, 'b-', linewidth=2)
    axes.set_xlabel('x (m)')
    axes.set_ylabel('Intensity (I/I₀)')
    #axes.set_title('Intensity Distribution')
    axes.grid(True, alpha=0.3)
    axes.set_xlim(-0.3, 0.3)
    
    return line, calculator


def update_intensity_plot(axes, line, calculator, 
                          wavelength, 
                          screen_distance, 
                          screen_separation, 
                          slit_width
                          ):
    """
    Update the intensity distribution with new parameters.
    """
    x, intensity = calculator.create_intensity_distribution(
        wavelength, screen_distance, screen_separation, slit_width
    )
    
    # Update line data
    line.set_ydata(intensity)
    axes.figure.canvas.draw_idle()