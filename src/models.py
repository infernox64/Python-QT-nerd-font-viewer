from dataclasses import dataclass

@dataclass
class Glyph:
    char: str
    name: str
    hex_code: str
    family: str

    @classmethod
    def from_db_row(cls, row):
        """Converts a SQLite row tuple into a Glyph object."""
        return cls(
            char=row[0],
            name=row[1],
            hex_code=row[2],
            family=row[3]
        )