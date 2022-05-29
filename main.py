#IMPORTAÇÃO DOS MÓDULOS
import sys
import os
from gui.windows.ui_main_window import UI_MainWindow

#IMPORTAÇÃO QT CORE
from qt_core import *

#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora PySide6")

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
    
        #EXIBIR A APLICAÇÃO
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())