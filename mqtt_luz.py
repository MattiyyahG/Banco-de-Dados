import paho.mqtt.client as mqtt
import time

def on_message(client,userdata,message):
    luz_mensagem = str(message.payload.decode("utf-8"))
    luz_mensagem = luz_mensagem.split(" ")
    luz = luz_mensagem[1]
    hora_luz = luz_mensagem[4].replace("]-","")
    data_luz = luz_mensagem[6].replace("]","")
    
mqtt_broker = "test.mosquitto.org"
client = mqtt.Client("API_luz")
client.connect(mqtt_broker)

client.loop_start()
client.subscribe("Labnet/Luz")
client.on_message=on_message
time.sleep(20)
client.loop_stop()