import sqlite3

# Function to create and connect to the database
def create_database(db_name):
    conn = sqlite3.connect(db_name)  # Connects or creates the database
    cursor = conn.cursor()
    return conn, cursor

# Function to create a table
def create_table(cursor, table_name):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    print(f"Table '{table_name}' created successfully.")

def main():
    # Create the database and connect
    db_name = 'questions.db'  # You can change the database name if needed
    conn, cursor = create_database(db_name)
    
    # Create a table
    create_table(cursor, 'ACCT2110')  # Table name is 'ACCT2110'
    create_table(cursor, 'BMGT3510')  # Table name is 'BMGT3510'
    create_table(cursor, 'ECON4900')  # Table name is 'ECON4900'
    create_table(cursor, 'FIN3210')   # Table name is 'FIN3210'
    create_table(cursor, 'MKT3400')   # Table name is 'MKT3400'
    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
