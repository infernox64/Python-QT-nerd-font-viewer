from src.models import Glyph
from PySide6.QtSql import QSqlQuery

# ... init_db function stays the same ...

def get_glyphs_by_family(family):
    query = QSqlQuery(f"SELECT char, name, hex, family FROM glyphs WHERE family = '{family}'")
    glyphs = []
    while query.next():
        # Using the model to wrap the data
        glyphs.append(Glyph(
            char=query.value(0),
            name=query.value(1),
            hex_code=query.value(2),
            family=query.value(3)
        ))
    return glyphs