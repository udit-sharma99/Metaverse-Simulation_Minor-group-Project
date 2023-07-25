import paho.mqtt.client as paho

broker_url = "broker.hivemq.com"
broker_port = 1883

TOPIC_SUB = "topic/pub"

def on_connect(client, userdata, flags, rc):
   print(rc)

def on_message(client, userdata, message):
   print("Message Recieved from Others: "+message.payload.decode())

client = paho.Client()
client.on_connect = on_connect
#To Process Every Other Message
client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe(TOPIC_SUB)

client.loop_forever()

