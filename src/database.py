from PySide6.QtSql import QSqlDatabase, QSqlQuery
from src.models import Glyph

def init_db(db_path):
    """Initializes the connection to the SQLite database."""
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_path)
    if not db.open():
        print(f"Database Error: {db.lastError().text()}")
        return False
    return True

def get_families():
    """Returns a list of unique font families from the DB."""
    query = QSqlQuery("SELECT DISTINCT family FROM glyphs")
    families = []
    while query.next():
        families.append(query.value(0))
    return families

def get_glyphs_by_family(family_name):
    """Returns a list of Glyph objects for a specific family."""
    query = QSqlQuery()
    # Use a prepared statement or f-string for the query
    query.prepare("SELECT char, name, hex, family FROM glyphs WHERE family = :family")
    query.bindValue(":family", family_name)
    query.exec_()
    
    glyphs = []
    while query.next():
        glyphs.append(Glyph(
            char=query.value(0),
            name=query.value(1),
            hex_code=query.value(2),
            family=query.value(3)
        ))
    return glyphs