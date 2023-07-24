import mysql.connector as db

username = "buda"
password = "password"

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


def insert_db(values):
    # values é uma lista
    base_query = "INSERT INTO sensores (data, co2, temperatura, luz) VALUES("
    query = base_query + values[0] + ',' + values[1] + ',' + values[2] + ',' + values[3] + ');'
    try:
        cursor.execute(query)
        print("Valores inseridos: ", values)
    except db.Error as e:
        print(f"Erro inserindo dados na tabela sensores: {e}")


create_db()

connect.close()
