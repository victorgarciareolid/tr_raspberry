from Adafruit_ADS1x15 import ADS1x15
from requests.auth import HTTPDigestAuth
import threading
import requests
import json

txt = open("credentials.txt")
username= txt.readline()
password = txt.readline()

addr = "http://localhost:3000" # Poner dirección de AWS
header = {"Content-type":"application/json", "Accept":"text/plain"}

AdcPort = 0x00
Gain = 4096
SamplingRate = 250
CO2Channel = 0
TemperatureChannel = 1
adc = ADS1x15(ic = AdcPort)

WorkingTemperature = 49

# Co2Concentration at 400ppm, Output Voltage at 400ppm, slope (between 400 and 40000)
CO2EcuationParams = []
CO2SensorGain = 8.5

def VoltsToPpm(Measurement):
    Measurement = Measurement/CO2SensorGain
    if(Measurement >= CO2EcuationParams[1]):
        return 400
    else:
        return(pow(10, Measurement - CO2EcuationParams[1] / CO2EcuationParams[2]) + CO2EcuationParams[0])

def VoltsToTemperature(Measurement):
    return Measurement / 10

def SendDataTemporarily():
    concentration = VoltsToPpm(MakeMeasurement(CO2Channel))

    measurement = {"concentration":concentration}
    JsonData = json.dumps(measurement, sort_keys=True)
    Request = requests.post(addr,auth=HTTPDigestAuth(username, password), data=JsonData, headers=header)

    threading.Timer(300, SendEveryNSeconds).start()

def MakeMeasurement(Channel):
    return adc.readADCSingleEnded(Channel, Gain, SamplingRate)

def main():
    while(VoltsToTemperature(MakeMeasurement(TemperatureChannel)) >= WorkingTemperature):
        SendDataTemporarily()

main()
