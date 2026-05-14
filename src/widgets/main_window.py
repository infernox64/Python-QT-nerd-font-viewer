from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QScrollArea, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from src.database import get_families, get_glyphs_by_family
from .gallery_view import CollapsibleSection
from .info_panel import InfoPanel

class NerdFontViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nerd Font SQLite Explorer")
        self.resize(1280, 800)
        self.all_buttons = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # MAIN LAYOUT (Horizontal to fit the InfoPanel on the right)
        self.main_h_layout = QHBoxLayout(central_widget)

        # --- LEFT SIDE: Search + Gallery ---
        self.left_container = QWidget()
        self.left_layout = QVBoxLayout(self.left_container)
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search icons...")
        self.search_bar.textChanged.connect(self.filter_glyphs)
        self.left_layout.addWidget(self.search_bar)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.sections_layout = QVBoxLayout(self.scroll_content)
        self.scroll.setWidget(self.scroll_content)
        self.left_layout.addWidget(self.scroll)

        # --- RIGHT SIDE: Info Panel ---
        self.info_panel = InfoPanel()

        # Add Both to the horizontal split
        self.main_h_layout.addWidget(self.left_container)
        self.main_h_layout.addWidget(self.info_panel)

        self.load_ui()

    def load_ui(self):
        families = get_families()
        for family in families:
            section = CollapsibleSection(family)
            glyphs = get_glyphs_by_family(family)
            
            for i, glyph in enumerate(glyphs):
                btn = QPushButton(glyph.char)
                btn.setFixedSize(50, 50)
                btn.setFont(QFont("FiraCode Nerd Font", 20))
                
                # WIRE UP THE CLICK: Send this glyph data to the info panel
                btn.clicked.connect(lambda checked=False, g=glyph: self.info_panel.update_info(g))
                
                section.grid.addWidget(btn, i // 12, i % 12)
                self.all_buttons.append((btn, glyph.name.lower(), section))
            
            self.sections_layout.addWidget(section)
        self.sections_layout.addStretch()

    def filter_glyphs(self, text):
        search_term = text.lower().strip()
        visible_sections = set()

        for btn, name, section in self.all_buttons:
            is_visible = search_term in name
            btn.setVisible(is_visible)
            if is_visible:
                visible_sections.add(section)
                if search_term: section.force_expand()

        for i in range(self.sections_layout.count()):
            item = self.sections_layout.itemAt(i)
            widget = item.widget()
            if isinstance(widget, CollapsibleSection):
                widget.setVisible(widget in visible_sections if search_term else True)