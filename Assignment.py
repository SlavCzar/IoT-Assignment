import random
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

#Station1
st1_temp = TBDeviceMqttClient(host="demo.thingsboard.io", username='st1_temp', password='st1_temp', client_id='st1_temp')
st1_humd = TBDeviceMqttClient(host="demo.thingsboard.io", username='st1_humd', password='st1_humd', client_id='st1_humd')
st1_rainHt = TBDeviceMqttClient(host="demo.thingsboard.io", username='st1_rainHt', password='st1_rainHt', client_id='st1_rainHt')
st1_winddir = TBDeviceMqttClient(host="demo.thingsboard.io", username='st1_winddir', password='st1_winddir', client_id='st1_winddir')
st1_windInt = TBDeviceMqttClient(host="demo.thingsboard.io", username='st1_windInt', password='st1_windInt', client_id='st1_windInt')
st1_co2 = TBDeviceMqttClient(host="demo.thingsboard.io", username='st1_co2', password='st1_co2', client_id='st1_co2')

#Station2
st2_temp = TBDeviceMqttClient(host="demo.thingsboard.io", username='st2_temp', password='st2_temp', client_id='st2_temp')
st2_humd = TBDeviceMqttClient(host="demo.thingsboard.io", username='st2_humd', password='st2_humd', client_id='st2_humd')
st2_rainHt = TBDeviceMqttClient(host="demo.thingsboard.io", username='st2_rainHt', password='st2_rainHt', client_id='st2_rainHt')
st2_winddir = TBDeviceMqttClient(host="demo.thingsboard.io", username='st2_winddir', password='st2_winddir', client_id='st2_winddir')
st2_windInt = TBDeviceMqttClient(host="demo.thingsboard.io", username='st2_windInt', password='st2_windInt', client_id='st2_windInt')
st2_co2 = TBDeviceMqttClient(host="demo.thingsboard.io", username='st2_co2', password='st2_co2', client_id='st2_co2')

st1_temp.connect()
st1_humd.connect()
st1_rainHt.connect()
st1_winddir.connect()
st1_windInt.connect()
st1_co2.connect()

st2_temp.connect()
st2_humd.connect()
st2_rainHt.connect()
st2_winddir.connect()
st2_windInt.connect()
st2_co2.connect()


while True:
    telemetry_st1_temp = {"temperature": random.randint(-50,50)}
    telemetry_st1_humd={ "humidity":random.randint(0,100) }
    telemetry_st1_co2={ "Co2 sensor" :random.randint(300,2000)}
    telemetry_st1_rainHt= { "rain height": random.randint(0,50)} 
    telemetry_st1_winddir={"wind direction": random.randint(0,360)}
    telemetry_st1_windInt = {"wind Intensity": random.randint(0,100)}

    telemetry_st2_temp = {"temperature": random.randint(-50,50)}
    telemetry_st2_humd={ "humidity":random.randint(0,100) }
    telemetry_st2_co2={ "Co2 sensor" :random.randint(300,2000)}
    telemetry_st2_rainHt= { "rain height": random.randint(0,50)} 
    telemetry_st2_winddir={"wind direction": random.randint(0,360)}
    telemetry_st2_windInt = {"wind Intensity": random.randint(0,100)}

    st1_temp.send_telemetry(telemetry_st1_temp)
    st1_humd.send_telemetry(telemetry_st1_humd) 
    st1_co2.send_telemetry(telemetry_st1_co2) 
    st1_rainHt.send_telemetry(telemetry_st1_rainHt) 
    st1_winddir.send_telemetry(telemetry_st1_winddir) 
    st1_windInt.send_telemetry(telemetry_st1_windInt) 

    st2_temp.send_telemetry(telemetry_st2_temp)
    st2_humd.send_telemetry(telemetry_st2_humd) 
    st2_co2.send_telemetry(telemetry_st2_co2) 
    st2_rainHt.send_telemetry(telemetry_st2_rainHt) 
    st2_winddir.send_telemetry(telemetry_st2_winddir) 
    st2_windInt.send_telemetry(telemetry_st2_windInt) 
