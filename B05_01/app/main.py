import mysql.connector
import os
import time

def run_app():
    time.sleep(5)
    conn = mysql.connector.connect(
        host='mysql',
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test_data (id INT PRIMARY KEY, value INT)")

    cursor.execute("REPLACE INTO test_data (id, value) VALUES (2, 555)")
    conn.commit()

    print("=== Дані в таблиці test_data ===")
    cursor.execute("SELECT * FROM test_data")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_app()