from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from create_plots import create_plots

def create_sliders(self):
    """
    Create sliders - METHODS FOR SLIDER CREATING
    """

    def setup_sliders(self):
        """
        Config of the value and range of the sliders.
        """
        # Slider 1: Separation between slits (0.1μm to 10μm)
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(100)
        self.slider1.setValue(20)  # 2μm by default
        self.slider1.setMinimumWidth(400)

        # Slider 2: Width of the slit (0.01μm to 1μm)
        self.slider2.setMinimum(1)
        self.slider2.setMaximum(100)
        self.slider2.setValue(20)  # 0.2μm by default
        self.slider2.setMinimumWidth(400)

        # Slider 3: Wavelength (400nm to 700nm)
        self.slider3.setMinimum(400)
        self.slider3.setMaximum(700)
        self.slider3.setValue(520)  # 520nm by default
        self.slider3.setMinimumWidth(400)

        # Slider 4: Distance to the screen (0.5m to 5m)
        self.slider4.setMinimum(5)
        self.slider4.setMaximum(50)
        self.slider4.setValue(20)  # 2m by default
        self.slider4.setMinimumWidth(400)

        # Setup initial values
        self.update_slider_values()

        # Connect the signal of the sliders
        self.slider1.valueChanged.connect(self.slider_change)
        self.slider2.valueChanged.connect(self.slider_change)
        self.slider3.valueChanged.connect(self.slider_change)
        self.slider4.valueChanged.connect(self.slider_change)
        
    def get_slider_values(self):
        """
        Returns the current slider values in proper physical units.
        """
        # Convert slider values to physical units
        slit_separation = self.slider1.value() / 10.0 * 1e-6  # μm to m
        slit_width = self.slider2.value() / 100.0 * 1e-6      # μm to m  
        wavelength = self.slider3.value() * 1e-9              # nm to m
        screen_distance = self.slider4.value() / 10.0         # slider units to m

        return {
            'slit_separation': slit_separation,
            'slit_width': slit_width,
            'wavelength': wavelength,
            'screen_distance': screen_distance
        }
    
    def slider_change(self):
        """
        Handles the changes and updates the plots.
        """
        self.update_slider_values()

        # Pass slider values to create_plots
        slider_values = self.get_slider_values()
        create_plots(self, **slider_values)     # unpack the slider_values dict

    def create_slider_row(self, title, slider, value_label, row):
        """
        Creates horizontal rows for the titles and values of the sliders.
        """
        row_layout = QHBoxLayout()
        
        # Título a la izquierda
        title.setFixedWidth(180)  # Ancho fijo para alineación
        row_layout.addWidget(title)
        
        # Slider en el centro
        row_layout.addWidget(slider)
        
        # Valor a la derecha
        value_label.setAlignment(Qt.AlignRight)
        value_label.setFixedWidth(80)  # Ancho fijo para alineación
        row_layout.addWidget(value_label)
        
        # Agregar esta fila al layout principal
        self.slider_layout.addLayout(row_layout)
