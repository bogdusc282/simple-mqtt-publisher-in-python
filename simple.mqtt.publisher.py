import paho.mqtt.client as mqtt

broker_user = "username"
broker_pwd = "password"
broker_host = "192.168.*.*"
broker_port = 1883 
publisher_topic = "/my/topic"
publisher_message = "message"

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.username_pw_set(broker_user, broker_pwd)
publisher.connect(broker_host, broker_port)

publisher.loop_start()


print(f"Publisher sends message: {publisher_message}")
publisher.publish(publisher_topic, publisher_message)
    
publisher.loop_stop()

publisher.disconnect()