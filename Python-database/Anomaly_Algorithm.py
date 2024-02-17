from Database_Classes import *
from sqlalchemy import func
from openai import OpenAI
import os

client = OpenAI()

def Anomaly():
    problem = ""
    #Panic Attack
    average_heart_rate = session.query(func.avg(Heart_Rate.HeartRate)).scalar() or 80
    average_sweat = session.query(func.avg(sweat.sweat)).scalar() or 500
    average_breathing_rate = session.query(func.avg(Respiratory_Rate.RespiratoryRate)).scalar() or 15

    average_last_hour_heart_rate = session.query(func.avg(Heart_Rate.HeartRate)).filter(Heart_Rate.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar() or 120
    average_last_hour_sweat = session.query(func.avg(sweat.sweat)).filter(sweat.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar() or 1000
    average_last_hour_breathing_rate = session.query(func.avg(Respiratory_Rate.RespiratoryRate)).filter(Respiratory_Rate.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar() or 25

    # Check if the averages meet the conditions for panic attack detection
    if (average_last_hour_breathing_rate > average_breathing_rate * 1.2) and (average_last_hour_heart_rate > average_heart_rate * 1.2) and (average_last_hour_sweat > average_sweat * 1.2):
        print('Panic Attack Detected')
        problem = ("his normal vitals are: heart rate: " + str(average_heart_rate) + " bpm, sweat: " + str(average_sweat) + " ml and breathing rate: " + str(average_breathing_rate) + " breaths per minute. his vitals have changed in the last hour to: heart rate: " + str(average_last_hour_heart_rate) + " bpm, sweat: " + str(average_last_hour_sweat) + " and breathing rate: " + str(average_last_hour_breathing_rate) + " breaths per minute.")
    #fever and hypothermia
    average_body_temperature = session.query(func.avg(Body_temperature.temperature)).filter(Body_temperature.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar() or 37
    if average_body_temperature > 38:
        print('Fever Detected')
        problem = ("he has a fever of " + str(average_body_temperature) + " degrees")
    elif average_body_temperature < 35:
        print('Hypothermia Detected')
        problem = ("his body temprature is low with" + str(average_body_temperature) + " degrees")
    
    #steps
    average_monthly_steps = session.query(func.avg(Steps.Steps)).filter(Steps.TimeStamp >= datetime.now() - timedelta(days=30)).scalar() or 0
    average_week_steps = session.query(func.avg(Steps.Steps)).filter(Steps.TimeStamp >= datetime.now() - timedelta(days=7)).scalar() or 0
    if average_week_steps < (average_monthly_steps * 0.5):
       print('Decreased Physical Activity Detected')
       problem = ("he normaly walks" +str(average_monthly_steps)+ "steps a day. he has been walking" + str(average_week_steps) + "steps a day for the last week. ")
    
    if problem != "":
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You are a sympathetic helper, `and we have discoverd strange behavior in our friend. our goal is figure out if it is a mental or pyshical issue to guide them to the right help. you are talking to the friend "},
            {"role": "user", "content": "the name of the friend is Jhon Doe. please start the process. "+ problem},
        ] 
        )
        return completion.choices[0].message
    
  
  
    