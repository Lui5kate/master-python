import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Samus!01',
        database='master_python',
        port=3306
    )
    
    cursor = database.cursor(buffered=True)

    return [database,cursor]