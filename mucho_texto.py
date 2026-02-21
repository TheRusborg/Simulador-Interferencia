from PyQt5 import QtCore

def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interference Simulator"))

        self.slider_label_1.setText(_translate("MainWindow", "Wavelength (λ)"))
        self.slider_label_2.setText(_translate("MainWindow", "Screen distance (D)"))
        self.slider_label_3.setText(_translate("MainWindow", "Slit separation (b)"))
        self.slider_label_4.setText(_translate("MainWindow", "Slit width (a)"))    

        self.slider_value_1.setText(_translate("MainWindow", "520 nm"))
        self.slider_value_2.setText(_translate("MainWindow", "200 cm"))
        self.slider_value_3.setText(_translate("MainWindow", "20 μm"))
        self.slider_value_4.setText(_translate("MainWindow", "2 μm"))

        #self.title.setText(_translate("MainWindow", "# **INTERFERENCE SIMULATOR**"))
        self.label_0.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed et ut velit vulputate\n" \
                                        "euismod faucibus mi, vehicula neque nullam dignissim magnis tempus. Vel fames \n" \
                                        "suscipit habitant morbi tempor placerat in, convallis penatibus libero pharetra \n" \
                                        "aptent inceptos iaculis dis, lacus praesent sollicitudin molestie mi himenaeos. \n" \
                                        "Volutpat dignissim montes mus potenti lobortis ullamcorper lacinia sodales \n" \
                                        "diam, ligula iaculis purus posuere orci arcu nam.\n"
                                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Experiment"))
        
        self.label_1.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed et ut velit vulputate\n" \
                                        "euismod faucibus mi, vehicula neque nullam dignissim magnis tempus. Vel fames \n" \
                                        "suscipit habitant morbi tempor placerat in, convallis penatibus libero pharetra \n" \
                                        "aptent inceptos iaculis dis, lacus praesent sollicitudin molestie mi himenaeos. \n" \
                                        "Volutpat dignissim montes mus potenti lobortis ullamcorper lacinia sodales \n" \
                                        "diam, ligula iaculis purus posuere orci arcu nam.\n"
                                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Wavelength"))
        self.label_2.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed et ut velit vulputate\n" \
                                        "euismod faucibus mi, vehicula neque nullam dignissim magnis tempus. Vel fames \n" \
                                        "suscipit habitant morbi tempor placerat in, convallis penatibus libero pharetra \n" \
                                        "aptent inceptos iaculis dis, lacus praesent sollicitudin molestie mi himenaeos. \n" \
                                        "Volutpat dignissim montes mus potenti lobortis ullamcorper lacinia sodales \n" \
                                        "diam, ligula iaculis purus posuere orci arcu nam.\n"
                                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Screen distance"))
        self.label_3.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed et ut velit vulputate\n" \
                                        "euismod faucibus mi, vehicula neque nullam dignissim magnis tempus. Vel fames \n" \
                                        "suscipit habitant morbi tempor placerat in, convallis penatibus libero pharetra \n" \
                                        "aptent inceptos iaculis dis, lacus praesent sollicitudin molestie mi himenaeos. \n" \
                                        "Volutpat dignissim montes mus potenti lobortis ullamcorper lacinia sodales \n" \
                                        "diam, ligula iaculis purus posuere orci arcu nam.\n"
                                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Slit separation"))
        self.label_4.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed et ut velit vulputate\n" \
                                        "euismod faucibus mi, vehicula neque nullam dignissim magnis tempus. Vel fames \n" \
                                        "suscipit habitant morbi tempor placerat in, convallis penatibus libero pharetra \n" \
                                        "aptent inceptos iaculis dis, lacus praesent sollicitudin molestie mi himenaeos. \n" \
                                        "Volutpat dignissim montes mus potenti lobortis ullamcorper lacinia sodales \n" \
                                        "diam, ligula iaculis purus posuere orci arcu nam.\n"
                                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "Slit width"))