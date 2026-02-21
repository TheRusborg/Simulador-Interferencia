import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from create_plots import create_plots
#from create_sliders import create_sliders

class MainWindow(QMainWindow):
    def __init__(self):
        """
        This method is the construct method for a class. It initializes the attributes 
        and serves for the basic config.
        """
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        """
        This optional (and renamable) method separates the config of the UI from the logic of the 
        initialization of the class. It helps keeping the code organized and maintainable
        """
        self.create_widgets()   # Methods within the class
        self.setup_layouts()
        self.setup_sliders()
        
        # Call create_plots with initial slider values
        slider_values = self.get_slider_values()
        create_plots(self, **slider_values)   # Pass initial values

        # Title properties
        self.title.setText("Simulador d'interferència")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size: 30px; font-weight: bold; margin: 20px;")

        # Text properties
        self.text.setText("Lorem ipsum dolor sit amet consectetur adipiscing elit \ndonec est tempor, lacus gravida massa taciti \n" \
                            "orci nibh ante sem leo molestie feugiat, venenatis \nsuscipit fusce cursus ad sapien nostra primis quisque. \n"
                            )
        self.text.setAlignment(Qt.AlignLeft)
        self.text.setStyleSheet("font-size: 20px; margin: 20px;")

        # Slider properties
        self.slider3_title.setText("Wavelength (λ)")
        self.slider3_title.setStyleSheet("font-size: 16px; font-weight: bold; min-width: 180px;")

        self.slider4_title.setText("Screen distance (D)")
        self.slider4_title.setStyleSheet("font-size: 16px; font-weight: bold; min-width: 180px;")

        self.slider1_title.setText("Slit separation (a)")
        self.slider1_title.setStyleSheet("font-size: 16px; font-weight: bold; min-width: 180px;")

        self.slider2_title.setText("Slit width (b)")
        self.slider2_title.setStyleSheet("font-size: 16px; font-weight: bold; min-width: 180px;")

        value_style = "font-size: 16px; font-weight: bold; min-width: 80px; padding: 5px;"
        self.slider1_value.setStyleSheet(value_style)
        self.slider2_value.setStyleSheet(value_style)
        self.slider3_value.setStyleSheet(value_style)
        self.slider4_value.setStyleSheet(value_style)

    def create_widgets(self):
        """
        Method for creating all the widgets on the main window.
        """
        # Text widgets
        self.title = QLabel()
        self.text = QLabel()
        self.slider1_title = QLabel()
        self.slider2_title = QLabel()
        self.slider3_title = QLabel()
        self.slider4_title = QLabel()
        self.slider1_value = QLabel("2.0 μm")   # Slider labels
        self.slider2_value = QLabel("0.2 μm")
        self.slider3_value = QLabel("520 nm")
        self.slider4_value = QLabel("2.0 m")

        # Image widgets
        self.image1 = QLabel()
        self.image1.setAlignment(Qt.AlignCenter)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "Patro_de_difraccio.png")
        pixmap = QPixmap(image_path)
        self.image1.setPixmap(
            pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )

        # Sliders
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider3 = QSlider(Qt.Horizontal)
        self.slider4 = QSlider(Qt.Horizontal)

        # Matplotlib figures
        self.figure1 = Figure(figsize=(6, 5), dpi=100)
        self.canvas1 = FigureCanvas(self.figure1)

        self.figure2 = Figure(figsize=(6, 5), dpi=100)
        self.canvas2 = FigureCanvas(self.figure2)
        
        # Containers
        self.central_widget = QWidget()
        
        self.simulation_container = QWidget()
        self.pattern_container = QWidget()
        self.intensity_container = QWidget()
        self.slider_container = QWidget()

        self.other_container = QWidget()
        self.title_container = QWidget()
        self.image1_container = QWidget()
        self.text_container = QWidget()
    
    def setup_layouts(self):
        """
        Method for configuring the layouts on the main window.
        """
        self.setGeometry(1400, 900, 1400, 900)
        self.setWindowTitle("Simulador de Interferencia")

        # Config of the main_layout
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        # Elements on the main_layout
        self.layout.addWidget(self.simulation_container, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.other_container, alignment=Qt.AlignRight)
        self.layout.addStretch()

        # Config of the simulation_layout (sublayout)
        self.simulation_layout = QVBoxLayout(self.simulation_container)
        self.simulation_layout.setContentsMargins(75, 30, 25, 30)   # window padding
        # Elements on the main sublayout (simulation_layout)
        self.simulation_layout.addWidget(self.pattern_container)
        self.simulation_layout.addWidget(self.intensity_container)
        self.simulation_layout.addWidget(self.slider_container)

        # Config of the pattern_layout (sublayout)
        self.pattern_layout = QVBoxLayout(self.pattern_container)
        self.pattern_container.setMaximumSize(500, 350)
        # Elements on the pattern_layout
        self.pattern_layout.addWidget(self.canvas1, alignment=Qt.AlignCenter)

        # Config of the intensity_layout (sublayout)
        self.intensity_layout = QVBoxLayout(self.intensity_container)
        self.intensity_container.setMaximumSize(500, 350)
        # Elements on the intensity_layout
        self.intensity_layout.addWidget(self.canvas2, alignment=Qt.AlignCenter)

        # Config of the slider_layout
        self.slider_layout = QVBoxLayout(self.slider_container)
        self.slider_container.setFixedHeight(150)
        self.slider_container.setMaximumWidth(600)
        # Crear filas para cada slider
        self.create_slider_row(self.slider3_title, self.slider3, self.slider3_value, 0)
        self.create_slider_row(self.slider4_title, self.slider4, self.slider4_value, 1)
        self.create_slider_row(self.slider1_title, self.slider1, self.slider1_value, 2)
        self.create_slider_row(self.slider2_title, self.slider2, self.slider2_value, 3)

        # Config of the other_layout (sublayout)
        self.other_layout = QVBoxLayout(self.other_container)
        self.other_layout.setContentsMargins(75, 30, 25, 30)   # window padding
        # Elements on the main sublayout (other_layout)
        self.other_layout.addWidget(self.title_container)
        self.other_layout.addWidget(self.image1_container)
        self.other_layout.addWidget(self.text_container)
        
        # Config of the title_layout
        self.title_layout = QVBoxLayout(self.title_container)
        self.title_container.setFixedHeight(100)
        self.title_container.setMaximumWidth(600)
        # Elements on the title_layout
        self.title_layout.addWidget(self.title, alignment=Qt.AlignLeft)

        # Config of the image1_layout
        self.image1_layout = QVBoxLayout(self.image1_container)
        self.image1_layout.setContentsMargins(15, 20, 15, 20)
        self.image1_container.setMaximumHeight(500)
        self.image1_container.setMaximumWidth(600)
        # Elements on the image1_layout
        self.image1_layout.addWidget(self.image1, alignment=Qt.AlignCenter)

        # Config of the text_layout
        self.text_layout = QVBoxLayout(self.text_container)
        self.text_layout.setContentsMargins(15, 20, 15, 20)
        self.text_container.setMaximumHeight(300)
        self.text_container.setMaximumWidth(600)
        # Elements on the text_layout
        self.text_layout.addWidget(self.text, alignment=Qt.AlignRight)

    def setup_sliders(self):
        """
        Config of the value and range of the sliders.
        """
        # Slider 1: Separation between slits (1μm to 10μm)
        self.slider1.setMinimum(1)           # 1μm
        self.slider1.setMaximum(100)         # 10μm
        self.slider1.setValue(20)            # 2μm by default
        self.slider1.setMinimumWidth(300)

        # Slider 2: Width of the slit (0.1μm to 1μm)
        self.slider2.setMinimum(1)           # 0.1μm
        self.slider2.setMaximum(100)         # 1μm 
        self.slider2.setValue(20)            # 0.2μm by default
        self.slider2.setMinimumWidth(300)

        # Slider 3: Wavelength (400nm to 700nm)
        self.slider3.setMinimum(400)         # 400nm (violeta)
        self.slider3.setMaximum(700)         # 700nm (red)
        self.slider3.setValue(520)           # 520nm by default (green)
        self.slider3.setMinimumWidth(300)

        # Slider 4: Distance to the screen (0.1m to 5m)
        self.slider4.setMinimum(1)           # 0.1m
        self.slider4.setMaximum(50)          # 5m
        self.slider4.setValue(20)            # 2m by default
        self.slider4.setMinimumWidth(300)

        # Setup initial values
        self.update_slider_values()

        # Connect the signal of the sliders
        self.slider1.valueChanged.connect(self.slider_change)
        self.slider2.valueChanged.connect(self.slider_change)
        self.slider3.valueChanged.connect(self.slider_change)
        self.slider4.valueChanged.connect(self.slider_change)

    def update_slider_values(self):
        """
        Updates the labels with the current values of the sliders.
        """
        self.slider1_value.setText(f"{self.slider1.value() / 10.0:.1f} μm")
        self.slider2_value.setText(f"{self.slider2.value() / 100.0:.2f} μm")
        self.slider3_value.setText(f"{self.slider3.value()} nm")
        self.slider4_value.setText(f"{self.slider4.value() / 10.0:.1f} m")

    def get_slider_values(self):
        """
        Returns the current slider values in proper physical units.
        """
        slit_separation = self.slider1.value() / 10.0 * 1e-6   # μm to m
        slit_width = self.slider2.value() / 100.0 * 1e-6       # μm to m  
        wavelength = self.slider3.value() * 1e-9               # 10^-9 (520nm verde)
        screen_distance = self.slider4.value() / 10.0          # slider units to m
    
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
        title.setFixedWidth(250)  # Aumentado para texto más largo
        row_layout.addWidget(title)
        
        # Slider en el centro
        row_layout.addWidget(slider)
        
        # Valor a la derecha
        value_label.setAlignment(Qt.AlignRight)
        value_label.setFixedWidth(100)  # Aumentado para mejor visualización
        row_layout.addWidget(value_label)
        
        # Agregar esta fila al layout principal
        self.slider_layout.addLayout(row_layout)


def window():
    """
    This method creates and runs the main application window.
    """
    root = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(root.exec_())


if __name__ == "__main__":
    window()