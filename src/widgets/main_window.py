from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QScrollArea
from src.database import get_families, get_glyphs_by_family
from .gallery_view import CollapsibleSection
from PySide6.QtGui import QFont

class NerdFontViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nerd Font SQLite Explorer")
        self.resize(1000, 700)
        self.all_buttons = []

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search icons...")
        self.search_bar.textChanged.connect(self.filter_icons)
        layout.addWidget(self.search_bar)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        container = QWidget()
        self.sections_layout = QVBoxLayout(container)
        self.scroll.setWidget(container)
        layout.addWidget(self.scroll)

        self.load_ui()

    def load_ui(self):
        for family in get_families():
            section = CollapsibleSection(family)
            glyphs = get_glyphs_by_family(family)
            
            for i, g in enumerate(glyphs):
                btn = QPushButton(g['char'])
                btn.setFixedSize(45, 45)
                btn.setFont(QFont("FiraCode Nerd Font", 18))
                btn.setToolTip(f"{g['name']}\n{g['hex']}")
                section.grid.addWidget(btn, i // 12, i % 12)
                self.all_buttons.append((btn, g['name'].lower(), section))
            
            self.sections_layout.addWidget(section)
        self.sections_layout.addStretch()

    def filter_icons(self, text):
        search_term = text.lower()
        active_sections = set()
        for btn, name, section in self.all_buttons:
            visible = search_term in name
            btn.setVisible(visible)
            if visible: active_sections.add(section)
            
        for i in range(self.sections_layout.count()):
            widget = self.sections_layout.itemAt(i).widget()
            if isinstance(widget, CollapsibleSection):
                widget.setVisible(widget in active_sections)