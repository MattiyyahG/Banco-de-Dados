import sqlite3
import paho.mqtt.client as mqtt

# Função para lidar com a mensagem recebida via MQTT

def on_message(client, userdata, msg):

    # Decodifica a mensagem recebida

    sensor_data = msg.payload.decode()

    sensor_data = sensor_data.split(" ")

    co2 = sensor_data[1]

    luminosidade = sensor_data[1]

    temperatura = sensor_data[1]

    hora = sensor_data[4].replace("]-","")

    data = sensor_data[6].replace("]","")

    # Divide a mensagem em valores separados

    values = sensor_data.split(',')

    temperatura = float(values[0])

    luminosidade = float(values[1])

    co2 = float(values[2])
    
    # Insere os valores no banco de dados

    conn = sqlite3.connect('sensor_data.db')

    cursor = conn.cursor()

    cursor.execute('INSERT INTO dados_sensores (temperatura, luminosidade, co2, data, hora) VALUES (?, ?, ?, ?, ?)',
                   (temperatura, luminosidade, co2, data, hora))
    
    conn.commit()

    conn.close()

# Configurações do broker MQTT

broker_address = 'test.mosquitto.org'

topic = 'Labnet/CO2'

# Conecta ao broker MQTT

client = mqtt.Client()

client.connect(broker_address)

# Associa a função de callback ao evento on_message

client.on_message = on_message

# Inscreve-se no tópico para receber as mensagens dos sensores

client.subscribe(topic)

# Inicia o loop para aguardar as mensagens

client.loop_start()