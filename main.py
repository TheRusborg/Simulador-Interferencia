# -*- coding: utf-8 -*-

### cd Documentos/Programming/Python/GUI/Simulador-interferencia
### pyinstaller main.py (dist)
### pyinstaller -F main.py (.exe)

from PyQt5 import QtCore, QtWidgets, QtGui
import numpy as np

from mucho_texto import retranslateUi
from left_panel import setup_left_panel
from right_panel import setup_right_panel

from interference_plot import update_interference_plot
from intensity_plot import update_intensity_plot

class Ui_MainWindow(object):
    """
    códifgo ordenado
    """
    def setupUi(self, MainWindow):
        """
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 810)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create all widgets
        setup_left_panel(self, self.centralwidget)
        setup_right_panel(self, self.centralwidget)

        # Set the central widget
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Set initial state
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Translate all widgets (text definition)
        retranslateUi(self, MainWindow)


# ===== MainApp CLASS HERE =====
class MainApp(QtWidgets.QMainWindow):
    """Main application class with interactive functionality"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect slider signals
        self.ui.Slider_1.valueChanged.connect(self.update_plots)
        self.ui.Slider_2.valueChanged.connect(self.update_plots)
        self.ui.Slider_3.valueChanged.connect(self.update_plots)
        self.ui.Slider_4.valueChanged.connect(self.update_plots)
        
        # Update value labels with proper formatting
        self.ui.Slider_1.valueChanged.connect(
            lambda v: self.ui.slider_value_1.setText(f"{v} nm"))
        self.ui.Slider_2.valueChanged.connect(
            lambda v: self.ui.slider_value_2.setText(f"{v} cm"))
        self.ui.Slider_3.valueChanged.connect(
            lambda v: self.ui.slider_value_3.setText(f"{v} μm"))
        
        # Slider 4: value is in 0.1 μm steps, so divide by 10 to get actual μm
        self.ui.Slider_4.valueChanged.connect(
            lambda v: self.ui.slider_value_4.setText(f"{v/10:.1f} μm"))
        
        # Initial plot update
        self.update_plots()
    
    def update_plots(self):
        """
        Update both plots with current slider values
        k"""
        # Get current values and convert to meters
        wavelength = self.ui.Slider_1.value() * 1e-9  # nm to m
        screen_distance = self.ui.Slider_2.value() / 100  # cm to m
        slit_separation = self.ui.Slider_3.value() * 1e-6  # μm to m
        
        # Slider 4: value is in 0.1 μm steps, so convert to meters
        slit_width = (self.ui.Slider_4.value() / 10) * 1e-6  # (0.1 μm steps) to m
        
        # Update interference plot (2D heatmap)
        if hasattr(self.ui, 'interference_heatmap') and hasattr(self.ui, 'interference_calculator'):
            update_interference_plot(
                self.ui.interference_plot.axes,
                self.ui.interference_heatmap,
                self.ui.interference_calculator,
                wavelength,
                screen_distance,
                slit_separation,
                slit_width
            )
        
        # Update intensity plot (1D line)
        if hasattr(self.ui, 'intensity_line') and hasattr(self.ui, 'intensity_calculator'):
            update_intensity_plot(
                self.ui.intensity_plot.axes,
                self.ui.intensity_line,
                self.ui.intensity_calculator,
                wavelength,
                screen_distance,
                slit_separation,
                slit_width
            )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())