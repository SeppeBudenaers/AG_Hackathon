from datetime import datetime
from Database_Classes import *
import requests
import json
import time
import random
step = 0
date = datetime.now()
def read_config_file():
    config_file_path = './config.json'
    
    with open(config_file_path, 'r') as file:
        config_data = json.load(file)
        BodyTemperature = Body_temperature(TimeStamp=date, temperature=random.randint(35, 40))
        HeartRate =Heart_Rate(TimeStamp=date, HeartRate=random.randint(70, 85))
        BloodPressure = Blood_Pressure(TimeStamp=date, Systolic=config_data['Systolic'], Diastolic=config_data['Diastolic'])
        BloodOxygen = Blood_Oxygen(TimeStamp=date, Oxygen=random.randint(80, 97))
        RespiratoryRate = Respiratory_Rate(TimeStamp=date, RespiratoryRate=config_data['Respiratory_Rate'])
        Sweat1 = Sweat(TimeStamp=date, Sweat=config_data['Sweat'])
        Sugar1 = Sugar(TimeStamp=date, Sugar=config_data['Sugar'])
        Steps1 =Steps(TimeStamp=date, Steps=config_data['Steps'])
        Emotion1 = Emotion(TimeStamp=date, Emotion=config_data['Emotion'])
        Stress1 = Stress(TimeStamp=date, Stress=config_data['Stress'])
        
        serialized_data = {
            'Body_Temperature': BodyTemperature.to_dict(),
            'Heart_Rate': HeartRate.to_dict(),
            'Blood_Pressure': BloodPressure.to_dict(),
            'Blood_Oxygen': BloodOxygen.to_dict(),
            'Respiratory_Rate': RespiratoryRate.to_dict(),
            'Sweat': Sweat1.to_dict(),
            'Sugar': Sugar1.to_dict(),
            'Steps': Steps1.to_dict(),
            'Emotion': Emotion1.to_dict(),
            'Stress': Stress1.to_dict()
        }
    return json.dumps(serialized_data)

def send_data_to_server(data):
    url = 'http://127.0.0.1:8080/'
    params = {'data': data}
    
    response = requests.post(url, params=params)
    print(response.text)
    if response.status_code == 200:
        print('Data sent successfully')
    else:
        print('Failed to send data')

while True: 
    config_string = read_config_file()
    send_data_to_server(config_string)
    date = date + timedelta(seconds=10)
    time.sleep(10)
    