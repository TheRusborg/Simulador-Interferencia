import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets, QtCore

from interference_plot import create_interference_plot
from intensity_plot import create_intensity_plot

class MplCanvas(FigureCanvas):
    """
    This class handles Matplotlib canvas for embedding in the QtApplication.
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.setParent(parent)
        # Make it focusable and set size policy
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

def setup_left_panel(self, centralwidget):
    """
    Setup the left side of the screen with the matplotlib plots and the sliders.
    """
    # First vertical layout (left)
    self.verticalLayoutWidget_3 = QtWidgets.QWidget(centralwidget)
    self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(60, 30, 631, 741))
    self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

    self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
    self.verticalLayout_1.setContentsMargins(5, 5, 5, 5)
    self.verticalLayout_1.setSpacing(10)
    self.verticalLayout_1.setObjectName("verticalLayout_1")

    # Matplotlib plots
    setup_matplotlib_plots(self)
    
    # Grid layout with sliders
    setup_sliders_grid(self)

def setup_matplotlib_plots(self):
    """
    Setup matplotlib canvases for interference and intensity patterns
    """
    
    # Interference plot (2D heatmap)
    self.interference_plot = MplCanvas(self.verticalLayoutWidget_3, width=6, height=4, dpi=100)
    self.interference_plot.setObjectName("interference_plot")
    self.interference_heatmap, self.interference_calculator = create_interference_plot(
        self.interference_plot.axes
    )
    self.interference_plot.fig.tight_layout()
    # Add colorbar - store it as an attribute so we can update it if needed
    self.interference_colorbar = self.interference_plot.fig.colorbar(
        self.interference_heatmap, ax=self.interference_plot.axes, orientation='horizontal'
    )
    self.interference_colorbar.set_label('Intensity (I/I₀)')
    
    # Intensity plot (1D line)
    self.intensity_plot = MplCanvas(self.verticalLayoutWidget_3, width=6, height=4, dpi=100)
    self.intensity_plot.setObjectName("intensity_plot")
    self.intensity_line, self.intensity_calculator = create_intensity_plot(
        self.intensity_plot.axes
    )
    self.intensity_plot.fig.tight_layout()

    # Add to vertical layout
    self.verticalLayout_1.addWidget(self.interference_plot)
    self.verticalLayout_1.addWidget(self.intensity_plot)

def setup_sliders_grid(self):
    """
    Setup all sliders and labels in a grid layout
    """
    self.gridLayout_1 = QtWidgets.QGridLayout()
    self.gridLayout_1.setObjectName("gridLayout_1")
    self.gridLayout_1.setVerticalSpacing(10)

    # Create all sliders and labels
    create_sliders(self)
    create_slider_labels(self)
    create_slider_values(self)
    
    # Set slider ranges and initial values (all ranges must be integers)
    # Slider 1: Wavelength in nm (380-750)
    self.Slider_1.setRange(380, 750)
    self.Slider_1.setValue(520)
    
    # Slider 2: Screen distance in cm (10-500)
    self.Slider_2.setRange(10, 500)
    self.Slider_2.setValue(200)
    
    # Slider 3: Slit separation in μm (1-100)
    self.Slider_3.setRange(1, 100)
    self.Slider_3.setValue(20)
    
    # Slider 4: Slit width in 0.1 μm steps (1-100 represents 0.1-10.0 μm)
    self.Slider_4.setRange(1, 100)  # 1 = 0.1 μm, 100 = 10.0 μm
    self.Slider_4.setValue(20)  # 20 = 2.0 μm
    
    # Add widgets to grid
    self.gridLayout_1.addWidget(self.Slider_1, 0, 1, 1, 1)
    self.gridLayout_1.addWidget(self.Slider_2, 1, 1, 1, 1)
    self.gridLayout_1.addWidget(self.Slider_3, 2, 1, 1, 1)
    self.gridLayout_1.addWidget(self.Slider_4, 3, 1, 1, 1)

    self.gridLayout_1.addWidget(self.slider_label_1, 0, 0, 1, 1)
    self.gridLayout_1.addWidget(self.slider_label_2, 1, 0, 1, 1)
    self.gridLayout_1.addWidget(self.slider_label_3, 2, 0, 1, 1)
    self.gridLayout_1.addWidget(self.slider_label_4, 3, 0, 1, 1)
    
    self.gridLayout_1.addWidget(self.slider_value_1, 0, 2, 1, 1)
    self.gridLayout_1.addWidget(self.slider_value_2, 1, 2, 1, 1)
    self.gridLayout_1.addWidget(self.slider_value_3, 2, 2, 1, 1)
    self.gridLayout_1.addWidget(self.slider_value_4, 3, 2, 1, 1)

    self.verticalLayout_1.addLayout(self.gridLayout_1)
    
    # Add a stretch at the end to keep everything at the top
    self.verticalLayout_1.addStretch()

def create_sliders(self):
    """
    Create all slider widgets.
    """
    self.Slider_1 = QtWidgets.QSlider(self.verticalLayoutWidget_3)
    self.Slider_1.setOrientation(QtCore.Qt.Horizontal)
    self.Slider_1.setObjectName("Slider_1")
    
    self.Slider_2 = QtWidgets.QSlider(self.verticalLayoutWidget_3)
    self.Slider_2.setOrientation(QtCore.Qt.Horizontal)
    self.Slider_2.setObjectName("Slider_2")
    
    self.Slider_3 = QtWidgets.QSlider(self.verticalLayoutWidget_3)
    self.Slider_3.setOrientation(QtCore.Qt.Horizontal)
    self.Slider_3.setObjectName("Slider_3")
    
    self.Slider_4 = QtWidgets.QSlider(self.verticalLayoutWidget_3)
    self.Slider_4.setOrientation(QtCore.Qt.Horizontal)
    self.Slider_4.setObjectName("Slider_4")

def create_slider_labels(self):
    """
    Create label widgets for the slider descriptions.
    """
    self.slider_label_1 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_label_1.setObjectName("slider_label_1")
    self.slider_label_1.setStyleSheet("font-weight: bold; font-size: 11pt;")
    
    self.slider_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_label_2.setObjectName("slider_label_2")
    self.slider_label_2.setStyleSheet("font-weight: bold; font-size: 11pt;")
    
    self.slider_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_label_3.setObjectName("slider_label_3")
    self.slider_label_3.setStyleSheet("font-weight: bold; font-size: 11pt;")
    
    self.slider_label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_label_4.setObjectName("slider_label_4")
    self.slider_label_4.setStyleSheet("font-weight: bold; font-size: 11pt;")

def create_slider_values(self):
    """
    Create label widgets for the slider values.
    """
    self.slider_value_1 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_value_1.setObjectName("slider_value_1")
    self.slider_value_1.setStyleSheet("font-weight: bold; font-size: 11pt;")
    
    self.slider_value_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_value_2.setObjectName("slider_value_2")
    self.slider_value_2.setStyleSheet("font-weight: bold; font-size: 11pt;")
    
    self.slider_value_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_value_3.setObjectName("slider_value_3")
    self.slider_value_3.setStyleSheet("font-weight: bold; font-size: 11pt;")
    
    self.slider_value_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
    self.slider_value_4.setObjectName("slider_value_4")
    self.slider_value_4.setStyleSheet("font-weight: bold; font-size: 11pt;")