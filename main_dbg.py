import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLineEdit, QScrollArea, QGridLayout, QPushButton, 
                             QFrame, QLabel)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class CollapsibleSection(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.btn = QPushButton(f"▼ {title}")
        self.btn.setCheckable(True)
        self.btn.setChecked(True)
        self.btn.clicked.connect(self.toggle)
        
        self.content = QFrame()
        self.grid = QGridLayout(self.content)
        
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.content)

    def toggle(self):
        self.content.setVisible(self.btn.isChecked())
        self.btn.setText(f"{'▼' if self.btn.isChecked() else '▶'} {self.btn.text()[2:]}")

class NerdFontViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nerd Font Explorer")
        self.resize(1000, 700)

        # 1. Check pathing
        db_path = os.path.join("resources", "glyphs.db")
        print(f"Checking for DB at: {os.path.abspath(db_path)}")

        # 2. Initialize DB
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(db_path)
        if not self.db.open():
            print("CRITICAL: Could not open database file!")
            return
        print("Database opened successfully.")

        # UI Setup
        central = QWidget()
        self.setCentralWidget(central)
        self.main_layout = QVBoxLayout(central)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.sections_layout = QVBoxLayout(self.container)
        self.scroll.setWidget(self.container)
        self.main_layout.addWidget(self.scroll)

        self.load_families()

    def load_families(self):
        print("Loading families...")
        query = QSqlQuery("SELECT DISTINCT family FROM glyphs")
        
        while query.next():
            fam_name = query.value(0)
            print(f"Creating section for: {fam_name}")
            section = CollapsibleSection(fam_name)
            
            # Limit for testing so it doesn't freeze
            icon_query = QSqlQuery(f"SELECT char, name FROM glyphs WHERE family = '{fam_name}' LIMIT 100")
            row, col = 0, 0
            while icon_query.next():
                btn = QPushButton(icon_query.value(0))
                btn.setFixedSize(40, 40)
                # Ensure the font name matches exactly what's installed on your Nitro
                btn.setFont(QFont("FiraCode Nerd Font", 16)) 
                section.grid.addWidget(btn, row, col)
                col += 1
                if col > 10:
                    col = 0
                    row += 1
            
            self.sections_layout.addWidget(section)
        
        self.sections_layout.addStretch()
        print("UI Population Complete.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NerdFontViewer()
    window.show()
    print("Application window.show() called.")
    sys.exit(app.exec())