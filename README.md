# IoT-Assignment

## Steps Performed
1. Add virtual sensors to the Thingsboard, this is done manually
2. After the sensors are added, configure the MQTT Credentials for all the sensors. Since we have 2 environmental station, we need to configure 12 sensors.
3. Add the sensor widget to the ThingsBoard Dashboard, using the latest telemetry tab.
4. We use python code to do 2 things:
  i. Connect to the virtual sensors using MQTT Client.
  ii. Continously generate random values for the sensor, in the range specified.


## Code

![Code File](https://github.com/SlavCzar/IoT-Assignment/blob/main/Assignment.py)

##Dashboard

![Dashboard](https://github.com/SlavCzar/IoT-Assignment/blob/main/Dashboard.png)
