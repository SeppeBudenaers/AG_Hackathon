from datetime import datetime
from Database_Classes import *
import requests
import json
import time
step = 0
date = datetime.now()
def read_config_file():
    config_file_path = './config.json'
    
    with open(config_file_path, 'r') as file:
        config_data = json.load(file)
        BodyTemperature = Body_temperature(TimeStamp=date, temperature=config_data['Body_Temperature'])
        HeartRate =Heart_Rate(TimeStamp=date, HeartRate=config_data['Heart_Rate'])
        BloodPressure = Blood_Pressure(TimeStamp=date, Systolic=config_data['Systolic'], Diastolic=config_data['Diastolic'])
        BloodOxygen = Blood_Oxygen(TimeStamp=date, Oxygen=config_data['Oxygen_Saturation'])
        RespiratoryRate = Respiratory_Rate(TimeStamp=date, RespiratoryRate=config_data['Respiratory_Rate'])
        Sweat = sweat(TimeStamp=date, sweat=config_data['sweat'])
        Sugar = sugar(TimeStamp=date, sugar=config_data['sugar'])
        steps =Steps(TimeStamp=date, Steps=config_data['steps'])
        emotion = Emotion(TimeStamp=date, Emotion=config_data['emotion'])
        stress = Stress(TimeStamp=date, Stress=config_data['stress'])
        
        serialized_data = {
            'Body_Temperature': BodyTemperature.to_dict(),
            'Heart_Rate': HeartRate.to_dict(),
            'Blood_Pressure': BloodPressure.to_dict(),
            'Blood_Oxygen': BloodOxygen.to_dict(),
            'Respiratory_Rate': RespiratoryRate.to_dict(),
            'sweat': Sweat.to_dict(),
            'sugar': Sugar.to_dict(),
            'steps': steps.to_dict(),
            'emotion': emotion.to_dict(),
            'stress': stress.to_dict()
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
    date = date + timedelta(days=1)
    time.sleep(10)
    