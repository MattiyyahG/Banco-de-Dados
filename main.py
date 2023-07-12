import mysql.connector as db
import paho.mqtt.client as mqtt
import sqlite3
from time import time


username = ""

password = ""

connect = db.connect(

    user=username,

    password=password,

    host='localhost'

)

cursor = connect.cursor()

#def create_db():

#    try:

#        table = '''CREATE TABLE IF NOT EXISTS lens.sensores(
         
#            id INT NOT NULL AUTO_INCREMENT,

#            data DATETIME NOT NULL, 

#            co2 INT NOT NULL,

#            temperatura INT NOT NULL,

#            luz INT NOT NULL,

#            PRIMARY KEY (id)
            
#        );'''
#        cursor.execute(table)
#        print("Tabela criada")
#    except db.Error as e:
#        print(f"Erro criando tabela: {e}")


#create_db()

connect.close()

MQTT_HOST = 'test.mosquitto.org'

MQTT_PORT = 1883

MQTT_CLIENT_ID = 'Python MQTT client'

MQTT_USER = username

MQTT_PASSWORD = password

TOPIC = 'lens/CO2'

DATABASE_FILE = 'mqtt.db'


def on_connect(mqtt_client, user_data, flags, conn_result):

    mqtt_client.subscribe(TOPIC)


def on_message(mqtt_client, user_data, message):

    sensor_data = message.payload.decode('utf-8')

    sensor_data = sensor_data.split(" ")

    sensor = sensor_data[1]

    hora = sensor_data[4].replace("]-","")

    data = sensor_data[6].replace("]","")

    db_conn = user_data['db_conn']

    sql = 'INSERT INTO sensors_data (id, topic, sensor, data, hora, PRIMARY KEY (id)) VALUES (?, ?, ?, ?, ?)'

    cursor = db_conn.cursor()

    cursor.execute(sql, (id, message.topic, sensor, data, hora))

    db_conn.commit()

    cursor.close()


def main():

    db_conn = sqlite3.connect(DATABASE_FILE)

    sql = """

    CREATE TABLE IF NOT EXISTS lens.sensores (
    
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        topic TEXT NOT NULL,

        valor TEXT NOT NULL,

        data DATETIME NOT NULL, 

        PRIMARY KEY (id)

    )

    """
    cursor = db_conn.cursor()

    cursor.execute(sql)

    cursor.close()

    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)

    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    mqtt_client.user_data_set({'db_conn': db_conn})


    mqtt_client.on_connect = on_connect

    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_HOST, MQTT_PORT)

    mqtt_client.loop_forever()


main()

