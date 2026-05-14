import sys
from PySide6.QtWidgets import QApplication
from src.database import init_db
from src.widgets.main_window import NerdFontViewer

def main():
    app = QApplication(sys.argv)
    
    if not init_db("resources/glyphs.db"):
        sys.exit(1)
        
    window = NerdFontViewer()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()