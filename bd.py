import mysql.connector as db

username = ""
password = ""

connect = db.connect(
    user=username,
    password=password,
    host='localhost'
)

cursor = connect.cursor()


def create_db():
    try:
        table = '''CREATE TABLE IF NOT EXISTS lens.sensores(
            id INT NOT NULL AUTO_INCREMENT,
            data DATETIME NOT NULL, 
            co2 INT NOT NULL,
            temperatura INT NOT NULL,
            luz INT NOT NULL,
            PRIMARY KEY (id)
        );'''
        cursor.execute(table)
        print("Tabela criada")
    except db.Error as e:
        print(f"Erro criando tabela: {e}")


create_db()

connect.close()
