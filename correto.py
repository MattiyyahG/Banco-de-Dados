import sqlite3

# Conectando ao banco de dados (será criado um arquivo chamado "exemplo.db")
conn = sqlite3.connect('sensor_data.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Criando uma tabela chamada "usuarios"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_sensores (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      valor INTEGER,
      data INTEGER,
      hora INTEGER
      )
''')

# Inserindo dados na tabela
cursor.execute('INSERT INTO dados_sensores (nome, valor, data, hora) VALUES (?, ?, ?, ?)', ('CO2', 25, 10/23, 21))
cursor.execute('INSERT INTO dados_sensores (nome, valor, data, hora) VALUES (?, ?, ?, ?)', ('Temperatura', 30, 10/23, 21))
cursor.execute('INSERT INTO dados_sensores (nome, valor, data, hora) VALUES (?, ?, ?, ?)', ('Luminosidade', 35, 10/23, 21))

# Commitando as alterações
conn.commit()

# Fechando a conexão com o banco de dados
conn.close()
