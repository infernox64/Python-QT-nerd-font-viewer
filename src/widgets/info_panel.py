from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class InfoPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(250)
        self.setStyleSheet("background-color: #f8f9fa; border-left: 1px solid #ccc;")
        
        layout = QVBoxLayout(self)
        
        self.title = QLabel("Icon Details")
        self.title.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        self.glyph_display = QLabel("")
        self.glyph_display.setAlignment(Qt.AlignCenter)
        self.glyph_display.setFixedSize(230, 150)
        self.glyph_display.setStyleSheet("background: white; border: 1px solid #ddd; border-radius: 8px;")
        
        self.name_label = QLabel("Name: -")
        self.hex_label = QLabel("Hex: -")
        self.family_label = QLabel("Family: -")
        
        layout.addWidget(self.title)
        layout.addWidget(self.glyph_display)
        layout.addWidget(self.name_label)
        layout.addWidget(self.hex_label)
        layout.addWidget(self.family_label)
        layout.addStretch()

    def update_info(self, glyph):
        """Updates the panel with a Glyph object from models.py"""
        self.glyph_display.setText(glyph.char)
        self.glyph_display.setFont(QFont("FiraCode Nerd Font", 72))
        self.name_label.setText(f"<b>Name:</b> {glyph.name}")
        self.hex_label.setText(f"<b>Hex:</b> {glyph.hex_code}")
        self.family_label.setText(f"<b>Family:</b> {glyph.family}")