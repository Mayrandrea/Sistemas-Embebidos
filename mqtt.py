import paho.mqtt.client as mqtt

from random import randint

def conectado(client, userdata, flags, rc):
    print ("Conectado con el código de resultado: " + str (rc))  
    client.subscribe ("mayra.leon@unach.edu.ec/t1")

def mensaje (client, userdata, msg):
    print (msg.topic + "" + str (msg.payload))
    #client.publish('correo/topico','recibido:'+msg.payload.decode('utf-8'))
    mensaje=msg.payload.decode('utf-8')
    if mensaje=='ON':
        print('encendido')
    if mensaje=='OFF':
        print('apagado')

client = mqtt.Client ()
client.username_pw_set ( 'mayra.leon@unach.edu.ec' , 'Valeska2016+' )
client.on_connect = conectado
client.on_message = mensaje

client.connect ("maqiatto.com", 1883, 60)

client.loop_forever()