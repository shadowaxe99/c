```python
import os
import json
import sqlite3
from sqlite3 import Error

def quick_sync():
    database = r"TaskMaster/src/database.sqlite"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        select_all_tasks(conn)

def create_connection(db_file):
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Sync tasks with AI Wallet
    with open('TaskMaster/src/ai_wallet.py', 'w') as f:
        json.dump(rows, f)

quick_sync()
```