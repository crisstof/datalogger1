import sqlite3

conn = sqlite3.connect("db.sqlite")
c = conn.cursor()

# Table pour les données capteur
c.execute(
    """
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_id INTEGER,
        value REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
)

# Reset pour test
c.execute("DELETE FROM sensor_data")

conn.commit()
conn.close()
