import sqlite3

def init_db():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()

    # Create tables for rules and metadata
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY,
        rule TEXT NOT NULL UNIQUE
    )
    ''')

    conn.commit()
    conn.close()

def get_existing_rules():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rules')
    rows = cursor.fetchall()
    conn.close()

    return [{'id': row[0], 'rule': row[1]} for row in rows]

if __name__ == '__main__':
    init_db()
