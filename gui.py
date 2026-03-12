# gui.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit,
    QPushButton, QLabel, QMessageBox
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from ml_model import predict_spam, ml_available


class SpamDetector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.apply_dark_theme()

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #121212; color: white; font-size: 14px; }
            QTextEdit {
                background-color: #1E1E1E;
                color: white;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton {
                background-color: #3A3A3A;
                color: white;
                border-radius: 6px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #4f4f4f; }
        """)

    def initUI(self):

        self.setWindowTitle("Instagram Spam Detector (ML Powered)")
        self.setGeometry(350, 150, 580, 520)

        self.setWindowIcon(QIcon("instagram icon.png"))

        self.main_layout = QVBoxLayout()

        # ===============================
        # IMAGE (Half Screen Fixed Height)
        # ===============================
        self.logo_label = QLabel(self)
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setMaximumHeight(self.height() // 2)

        self.pix = QPixmap("instagram icon.png")
        if self.pix.isNull():
            self.logo_label.setText("Logo Missing")
        else:
            self.update_logo()  # initial scaling

        self.main_layout.addWidget(self.logo_label)

        # ===============================
        # INPUT BOX
        # ===============================
        self.text_input = QTextEdit(self)
        self.text_input.setFixedHeight(80)
        self.text_input.setPlaceholderText("Enter Instagram post/comment here...")
        self.main_layout.addWidget(self.text_input)

        # ===============================
        # BUTTON
        # ===============================
        detect_btn = QPushButton("Detect Spam")
        detect_btn.clicked.connect(self.detect_handler)
        self.main_layout.addWidget(detect_btn)

        self.setLayout(self.main_layout)

    # Resize event to maintain 50% logo height
    def resizeEvent(self, event):
        self.logo_label.setMaximumHeight(self.height() // 2)
        self.update_logo()
        super().resizeEvent(event)

    def update_logo(self):
        scaled = self.pix.scaled(
            self.width() - 40,          # safe width
            self.height() // 2,         # max height = half window
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.logo_label.setPixmap(scaled)

    def detect_handler(self):
        text = self.text_input.toPlainText().strip()

        if not text:
            QMessageBox.warning(self, "Empty Input", "Please enter some text first.")
            return

        if not ml_available:
            QMessageBox.warning(self, "ML Model Missing",
                                 "Run test.py first to train the model.")
            return

        result = predict_spam(text)

        if result:
            QMessageBox.critical(self, "Spam Detected", "⚠ This message is detected as SPAM!")
        else:
            QMessageBox.information(self, "Safe Message", "✔ This message appears safe.")