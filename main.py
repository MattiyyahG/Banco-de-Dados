import mysql.connector as db
import paho.mqtt.client as mqtt 
import time

username = "buda"
password = "password"
prov_msg_luz = ""
prov_msg_Temp = ""
prov_msg_CO2 = ""

final_data = ""
final_CO2 = ""
final_luz = ""
final_Temp = "" 

connect = db.connect(
    user=username,
    password=password,
    host='localhost'

)

cursor = connect.cursor()

def create_db():
    table = '''CREATE TABLE IF NOT EXISTS lens.sensores(
        id INT NOT NULL AUTO_INCREMENT,
        data DATETIME NOT NULL, 
        co2 INT NOT NULL,
        temperatura INT NOT NULL,
        luz INT NOT NULL,
        PRIMARY KEY (id)
    );'''
    
    try:
        cursor.execute(table)
        print("Tabela criada")
    except db.Error as e:
        print(f"Erro criando tabela: {e}")

# Cria um Dicionário onde serão inseridas as informações 

def tratamento(a): 
    # função onde os dados são separandos e inserindos no dicionário
    
    global final_CO2
    global final_luz
    global final_Temp
    global final_data

    if a[0] == 'L':
        luz_mensagem = a
        luz_mensagem = luz_mensagem.split(" ")
        luz = int(luz_mensagem[1])
        final_luz = luz

    if a[0] == 'T':

        temp_mensagem = a
        temp_mensagem = temp_mensagem.split(" ")
        temp = int(temp_mensagem[1])
        hora_temp = temp_mensagem[5].replace("]-","")
        data_temp = temp_mensagem[7].replace("]","")
        data_temp = data_temp.split("-")
        ano = data_temp[0]
        mes = data_temp[1]
        dia = data_temp[2]

        if len(dia)<2:
            dia = "0" + dia

        if len(mes)<2:
            mes = "0" + mes

        data_temp = ano + "-" + mes + "-" + dia
        final_data = data_temp + " " + hora_temp
        final_Temp = temp
        
    if a[0] == 'C':

        co2_mensagem =  a
        co2_mensagem = co2_mensagem.split(" ")
        co2 = int(co2_mensagem[1])
        final_CO2 = co2
    
def on_message(client, userdata, message): 
    # Função de recebimento das mensagens do broker onde a função "tratamento" está inserida
    if str(message.payload.decode('utf-8'))[0] == 'L':
        global prov_msg_luz 
        prov_msg_luz = str(message.payload.decode('utf-8'))
        return tratamento(prov_msg_luz)
    
    if str(message.payload.decode('utf-8'))[0] == 'T':
        global prov_msg_Temp 
        prov_msg_Temp = str(message.payload.decode('utf-8'))
        return tratamento(prov_msg_Temp)
    
    if str(message.payload.decode('utf-8'))[0] == 'C':
        global prov_msg_CO2 
        prov_msg_CO2 = str(message.payload.decode('utf-8'))
        return tratamento(prov_msg_CO2)

mqttBroker = 'test.mosquitto.org'
client = mqtt.Client('API_test')
client.connect(mqttBroker)

def insert_values():
    # values é uma lista
    # exemplo: INSERT INTO sensores (data, co2, temperatura, luz) VALUES('2023-07-24 16:34:50', 678, 22, 74);
    cursor.execute("USE lens;")

    base_query = f"INSERT INTO sensores (data, co2, temperatura, luz) VALUES('{final_data}', {final_CO2}, {final_Temp}, {final_luz})"
    #query = base_query + values[0] + ',' + values[1] + ',' + values[2] + ',' + values[3] + ');'
    try: 
        cursor.execute(base_query)
        connect.commit()
        print("Valores inseridos: ", final_data, final_CO2, final_Temp, final_luz)
    except db.Error as e:
        print(f"Erro inserindo dados na tabela sensores: {e}")

create_db()

#connect.close()

# Conexão com o broker

while(True):
    client.loop_start()
    client.subscribe('Labnet/Luz')
    client.subscribe('Labnet/CO2')
    client.subscribe('labnet/TEMP')
    client.on_message = on_message
    time.sleep(2)
    client.loop_stop()
    #values = [final_data, final_CO2, final_Temp, final_luz]
    insert_values()
    time.sleep(300)

# Configuração de recebimneto de mensgem do topico "Labnet/Luz"