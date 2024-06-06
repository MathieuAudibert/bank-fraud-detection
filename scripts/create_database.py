import sqlite3

def create_database(db_name, sql_file):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    with open(sql_file, 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created and populated successfully.")

if __name__ == "__main__":
    create_database('bank.db', '../data/create_bank_db.sql')
