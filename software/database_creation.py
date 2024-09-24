import sqlite3

mydb = sqlite3.connect('diagonis.db')
mycursor = mydb.cursor()

mycursor.execute('''
    CREATE TABLE IF NOT EXISTS History(
        ID TEXT,
        NAME TEXT,
        AGE TEXT,
        RESULT TEXT,
        DATE TEXT
    )
''')

mydb.commit()
