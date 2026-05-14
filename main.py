import sys
from PySide6.QtWidgets import QApplication
from src.database import init_db
from src.widgets.main_window import NerdFontViewer

DARK_THEME = """
QMainWindow, QDialog {
    background-color: #1e1e1e;
}
QWidget {
    background-color: #1e1e1e;
    color: #d4d4d4;
    font-family: 'Segoe UI', sans-serif;
}
/* This fixes the white backgrounds in the gallery area */
QScrollArea, QScrollArea > QWidget > QWidget {
    background-color: #1e1e1e;
    border: none;
}
QScrollArea QWidget#scroll_content {
    background-color: #1e1e1e;
}
QLineEdit {
    background-color: #2d2d2d;
    border: 1px solid #3e3e42;
    padding: 8px;
    border-radius: 4px;
    color: #eeeeee;
}
QScrollBar:vertical {
    border: none;
    background: #1e1e1e;
    width: 12px;
}
QScrollBar::handle:vertical {
    background: #3e3e42;
    border-radius: 6px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background: #4e4e52;
}
"""

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME) # Apply theme globally
    
    if not init_db("resources/glyphs.db"):
        sys.exit(1)
        
    window = NerdFontViewer()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()