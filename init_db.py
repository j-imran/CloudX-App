import sqlite3

conn = sqlite3.connect('cloudx.db')
c = conn.cursor()

# Create a table
c.execute('''
          CREATE TABLE IF NOT EXISTS data
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          key TEXT NOT NULL,
          value TEXT NOT NULL)
          ''')

conn.commit()
conn.close()
