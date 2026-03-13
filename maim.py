# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui import SpamDetector

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpamDetector()
    window.show()
    sys.exit(app.exec_())
