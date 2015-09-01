from Adafruit_ADS1x15 import ADS1x15
from requests.auth import HTTPDigestAuth
import requests, json, time
import hashlib

with open("/home/pi/tr_raspberry/credentials.json") as credentials:
    credential = json.load(credentials)

h = hashlib.sha512()

username = credential["username"]
h.update(credential["password"])
password = h.hexdigest()

addr = "https://52.28.164.86/data" # Poner direccion de AWS
header = {"Content-type":"application/json", "Accept":"text/plain"}

AdcPort = 0x00
Gain = 4096
SamplingRate = 250
CO2Channel = 0
TemperatureChannel = 1
adc = ADS1x15(ic = AdcPort)

WorkingTemperature = 49

# log 400ppm, 400ppm voltage, slope (between 400 and 40000)
CO2EcuationParams = [2.602, 0.380, -0.0729]
CO2SensorGain = 8.5

def VoltsToPpm(Measurement):
	Measurement = Measurement/CO2SensorGain
	return(pow(10, ((Measurement - CO2EcuationParams[1]) / CO2EcuationParams[2]) + CO2EcuationParams[0]))

def VoltsToTemperature(Measurement):
	return Measurement*100

def SendData():
	concentration = VoltsToPpm(MakeMeasurement(CO2Channel))
	measurement = {"concentration":concentration}
	JsonData = json.dumps(measurement, sort_keys=True)
	Request = requests.post(addr,auth=HTTPDigestAuth(username, password), data=JsonData, headers=header, verify=False)
	return concentration

def MakeMeasurement(Channel):
	return(adc.readADCSingleEnded(Channel, Gain, SamplingRate)/1000)
 
while 1:
	co2 = VoltsToPpm(MakeMeasurement(CO2Channel))
	temp = VoltsToTemperature(MakeMeasurement(TemperatureChannel))
	print("Temperature: " + str(temp))
	print("CO2: " + str(co2))
	while(VoltsToTemperature(MakeMeasurement(TemperatureChannel)) >= WorkingTemperature):
		print(SendData())
		time.sleep(10)
	time.sleep(2)
