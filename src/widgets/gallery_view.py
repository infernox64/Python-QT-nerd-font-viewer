from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QGridLayout
from PySide6.QtCore import Qt

class CollapsibleSection(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 5, 0, 5)
        
        # Section Toggle Button
        self.btn = QPushButton(f"▼ {title}")
        self.btn.setCheckable(True)
        self.btn.setChecked(True)
        self.btn.setStyleSheet("""
            QPushButton {
                text-align: left; 
                font-weight: bold; 
                padding: 8px; 
                background: #333; 
                color: white; 
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover { background: #444; }
        """)
        self.btn.clicked.connect(self.toggle)
        
        # Grid Content
        self.content = QFrame()
        self.grid = QGridLayout(self.content)
        self.grid.setSpacing(5)
        
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.content)

    def toggle(self):
        is_visible = self.btn.isChecked()
        self.content.setVisible(is_visible)
        self.btn.setText(f"{'▼' if is_visible else '▶'} {self.btn.text()[2:]}")

    def force_expand(self):
        """Used during search to show hidden matches."""
        self.btn.setChecked(True)
        self.content.setVisible(True)
        self.btn.setText(f"▼ {self.btn.text()[2:]}")