from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class InfoPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(280)
        self.setObjectName("InfoPanel")
        self.setStyleSheet("""
            QFrame#InfoPanel { 
                background-color: #252526; 
                border-left: 1px solid #3e3e42;
            }
            QLabel { color: #cccccc; background: transparent; }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        self.header = QLabel("ICON DETAILS")
        self.header.setStyleSheet("color: #888; font-weight: bold; font-size: 10px; letter-spacing: 1px;")
        layout.addWidget(self.header)

        # Restored Large Preview Box
        self.preview_box = QFrame()
        self.preview_box.setFixedSize(150, 100) # Back to larger size
        self.preview_box.setStyleSheet("background: #1e1e1e; border: 1px solid #3e3e42; border-radius: 4px;")
        preview_layout = QVBoxLayout(self.preview_box)
        
        self.preview_label = QLabel("?")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setFont(QFont("FiraCode Nerd Font", 90)) # Larger font for preview
        self.preview_label.setStyleSheet("color: #ffffff; border: none;")
        preview_layout.addWidget(self.preview_label)
        layout.addWidget(self.preview_box)

        self.name_label = QLabel("Name: -")
        self.hex_label = QLabel("Hex: -")
        self.family_label = QLabel("Family: -")
        
        for label in [self.name_label, self.hex_label, self.family_label]:
            label.setWordWrap(True)
            label.setStyleSheet("font-size: 13px; color: #d4d4d4;")
            layout.addWidget(label)

        # Re-tucked buttons
        btn_style = """
            QPushButton {
                padding: 10px;
                background-color: #0e639c;
                color: white;
                border: none;
                border-radius: 2px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1177bb; }
        """
        
        self.copy_glyph_btn = QPushButton("Copy Glyph")
        self.copy_glyph_btn.setStyleSheet(btn_style)
        self.copy_glyph_btn.clicked.connect(self.copy_glyph)
        
        self.copy_unicode_btn = QPushButton("Copy Unicode")
        self.copy_unicode_btn.setStyleSheet(btn_style)
        self.copy_unicode_btn.clicked.connect(self.copy_unicode_escape)

        layout.addWidget(self.copy_glyph_btn)
        layout.addWidget(self.copy_unicode_btn)
        layout.addStretch()
        self.current_hex = ""

    def update_info(self, glyph):
        self.preview_label.setText(glyph.char)
        self.name_label.setText(f"<font color='#888'>Name:</font> {glyph.name}")
        self.hex_label.setText(f"<font color='#888'>Hex:</font> {glyph.hex_code}")
        self.family_label.setText(f"<font color='#888'>Family:</font> {glyph.family}")
        self.current_hex = glyph.hex_code

    def copy_glyph(self):
        QApplication.clipboard().setText(self.preview_label.text())

    def copy_unicode_escape(self):
        if self.current_hex:
            QApplication.clipboard().setText(f"\\u{self.current_hex}")