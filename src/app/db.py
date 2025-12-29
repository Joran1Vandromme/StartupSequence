import sqlite3


def init_db(db_path: str):
    
    """
    Maakt de database en tabellen aan als ze nog nie bestaan.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    sql_sequences = """
    CREATE TABLE IF NOT EXISTS sequences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT NOT NULL
    );
    """

    sql_steps = """
    CREATE TABLE IF NOT EXISTS steps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sequence_id INTEGER NOT NULL,
        step_order INTEGER NOT NULL,
        action_type TEXT NOT NULL,
        command TEXT NOT NULL,
        args TEXT NOT NULL,
        seconds INTEGER NOT NULL,
        enabled INTEGER NOT NULL,
        FOREIGN KEY(sequence_id) REFERENCES sequences(id)
    );
    """

    cur.execute(sql_sequences)
    cur.execute(sql_steps)

    conn.commit()
    cur.close()
    conn.close()

