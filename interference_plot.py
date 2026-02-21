import numpy as np

class InterferenceCalculator:
    """
    Class to handle interference pattern calculations.
    """
    
    def __init__(self, I_o=10):
        self.I_o = I_o  # Maximum intensity
    
    def calculate_phase(self, x, screen_distance, slit_separation):
        """
        Calculate phase difference between rays at each point.
        """
        desfase = x * (slit_separation / screen_distance)
        return desfase
    
    def calculate_intensity(self, x, wavelength, screen_distance, slit_separation, slit_width):
        """
        Calculate intensity at a given position x.
        """
        # Avoid division by zero or invalid values
        if screen_distance == 0:
            return 0
            
        alpha = np.arctan(x / screen_distance) if screen_distance != 0 else 0
        sin_alpha = np.sin(alpha)
        
        # Interference term
        interference = (np.cos((np.pi * slit_separation * sin_alpha) / wavelength))**2
        
        # Diffraction term (avoid division by zero)
        beta = (np.pi * slit_width * sin_alpha) / wavelength
        # Use np.sinc which handles zero correctly: sinc(t) = sin(pi*t)/(pi*t)
        # So beta/pi gives us the argument for sinc
        diffraction = np.sinc(beta / np.pi)**2
        
        intensity = self.I_o * interference * diffraction
        return intensity
    
    def create_interference_pattern(self, wavelength, screen_distance, slit_separation, slit_width, 
                                   screen_width=0.3, screen_height=0.002, resolution=300):
        """
        Create a 2D interference pattern
        
        Returns:
            x: array of x positions
            y: array of y positions
            intensity_map: 2D array of intensity values
        """
        # Create coordinate grids
        m = int(2 * screen_width * resolution)
        n = int(screen_height * resolution)
        
        # Ensure we have at least a few points
        m = max(m, 100)
        n = max(n, 10)
        
        x = np.linspace(-screen_width, screen_width, m)
        y = np.linspace(-screen_height, screen_height, n)
        
        # Calculate intensity for each x position
        intensity_x = np.array([self.calculate_intensity(xi, wavelength, screen_distance, 
                                                         slit_separation, slit_width) / 4 * self.I_o 
                                for xi in x])
        
        # Create 2D array (same intensity for all y positions)
        # Shape should be (len(y), len(x)) for pcolormesh with default orientation
        intensity_map = np.tile(intensity_x, (n, 1))
        
        return x, y, intensity_map


def create_interference_plot(axes, wavelength=520e-9, screen_distance=2.0, 
                            slit_separation=20e-6, slit_width=2e-6):
    """
    Create the plot for the initial conditions of the interference pattern.
    """
    calculator = InterferenceCalculator()
    x, y, intensity_map = calculator.create_interference_pattern(
        wavelength, screen_distance, slit_separation, slit_width
    )
    
    # Create meshgrid for plotting - note the orientation
    # For pcolormesh, we want X and Y to be 2D arrays with shape (len(y), len(x))
    X, Y = np.meshgrid(x, y)
    
    # Create heatmap - use X, Y directly without transposing
    heatmap = axes.pcolormesh(X, Y, intensity_map, cmap='Greens_r', shading='auto')
    #axes.set_xlabel('x (m)')
    axes.set_ylabel('y (m)')
    #axes.set_title('Double-slit Interference Pattern')
    
    return heatmap, calculator


def update_interference_plot(axes, heatmap, calculator, wavelength, screen_distance, 
                            slit_separation, slit_width):
    """
    Update the interference pattern with new parameters.
    """
    x, y, intensity_map = calculator.create_interference_pattern(
        wavelength, screen_distance, slit_separation, slit_width
    )
    
    # Update heatmap data
    # For pcolormesh, we need to update both the coordinates and the array
    # or recreate the heatmap if the dimensions change
    heatmap.set_array(intensity_map.ravel())
    
    # If the dimensions changed significantly, we might need to recreate the heatmap
    # But for now, just update the array
    axes.figure.canvas.draw_idle()