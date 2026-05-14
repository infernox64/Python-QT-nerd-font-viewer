#!/usr/bin/env python3.13
from fontTools.ttLib import TTFont
import sqlite3

def generate_full_db(ttf_path, db_path):
    font = TTFont(ttf_path)
    # The 'cmap' table maps Unicode ordinals to glyph names
    cmap = font['cmap'].getBestCmap()
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS glyphs (char TEXT, name TEXT, hex TEXT, family TEXT)')
    
    entries = []
    for code, name in cmap.items():
        # Filter for Nerd Font PUA range or name prefixes
        if name.startswith('nf-') or code > 0xE000:
            char = chr(code)
            hex_val = f"{code:x}"
            
            # Logic-based categorization
            family = "Misc"
            if "mdi" in name: family = "Material Design"
            elif "fa" in name: family = "Font Awesome"
            elif "dev" in name: family = "Devicons"
            elif "weather" in name: family = "Weather"
            
            entries.append((char, name, hex_val, family))
            
    c.executemany('INSERT INTO glyphs VALUES (?,?,?,?)', entries)
    conn.commit()
    conn.close()

generate_full_db("resources/FiraCode_NF.ttf", "glyphs.db")