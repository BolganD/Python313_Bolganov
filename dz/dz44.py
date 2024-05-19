import sqlite3

prod_tpl = [
    ('Corn', 'Russia', 420500, 70, '0.5'),
    ('Meal', 'Russia', 175500, 90, '0.5'),
    ('Fish', 'Japan', 93000, 140, '2'),
    ('Bread', 'Finland', 103800, 100, '0.7'),
    ('Vegetables', 'Belarus', 680000, 40, '0.9'),
    ('Meat', 'Finland', 30500, 180, '0.7'),
]

with sqlite3.connect('store.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS first_dep(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        maker_country TEXT,
        count INTEGER,
        price INTEGER,
        comm TEXT
    )
    """)
    for prod in prod_tpl:
        cur.execute("INSERT INTO first_dep VALUES(NULL, ?, ?, ?, ?, ?)", prod)