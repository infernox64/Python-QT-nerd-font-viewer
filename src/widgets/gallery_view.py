from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QGridLayout
from PySide6.QtGui import QFont

class CollapsibleSection(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.btn = QPushButton(f"▼ {title}")
        self.btn.setCheckable(True)
        self.btn.setChecked(True)
        self.btn.setStyleSheet("text-align: left; font-weight: bold; background: #e0e0e0;")
        self.btn.clicked.connect(self.toggle)
        
        self.content = QFrame()
        self.grid = QGridLayout(self.content)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.content)

    def toggle(self):
        self.content.setVisible(self.btn.isChecked())
        self.btn.setText(f"{'▼' if self.btn.isChecked() else '▶'} {self.btn.text()[2:]}")