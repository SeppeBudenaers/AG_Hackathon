from datetime import datetime
from Database_Classes import *
import requests
import json
import time
import random
step = 0
panic = 0
date = datetime.now()
def cpanic():
    print(pow(2, panic))
    return int(pow(2, panic))

def read_config_file():
    config_file_path = './config.json'
    
    with open(config_file_path, 'r') as file:
        config_data = json.load(file)

        rtemp = random.randint(-1, 2)
        rheart = random.randint(-5, 5)
        roxygen = random.randint(-5, 1)

        BodyTemperature = Body_temperature(TimeStamp=date, temperature=float(config_data['Body_Temperature'] + rtemp))
        HeartRate =Heart_Rate(TimeStamp=date, HeartRate=int(config_data['Heart_Rate'] + rheart + cpanic()))
        BloodPressure = Blood_Pressure(TimeStamp=date, Systolic=config_data['Systolic'], Diastolic=config_data['Diastolic'])
        BloodOxygen = Blood_Oxygen(TimeStamp=date, Oxygen=int(config_data['Oxygen_Saturation'] + roxygen))
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
            'Sweat': Sweat.to_dict(),
            'Sugar': Sugar.to_dict(),
            'Steps': steps.to_dict(),
            'Emotion': emotion.to_dict(),
            'Stress': stress.to_dict()
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
    print(config_string)
    send_data_to_server(config_string)
    date = date + timedelta(seconds=10)
    step = step + 1
    if step > 6:
        panic = panic+1
    time.sleep(10)
    