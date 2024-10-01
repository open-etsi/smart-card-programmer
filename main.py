from stc_gui.stc_view.stc_view.view import MainWindow
from PyQt6.QtWidgets import QApplication
import os, sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
