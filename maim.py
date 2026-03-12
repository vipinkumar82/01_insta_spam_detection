import sys
from PyQt5.QtWidgets import QApplication
from gui import SpamDetector

app = QApplication(sys.argv)
window = SpamDetector()
window.show()

sys.exit(app.exec_())