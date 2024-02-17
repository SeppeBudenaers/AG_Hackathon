from Database_Classes import *
from sqlalchemy import func
from openai import OpenAI

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

def Anomaly():
    #Panic Attack
    average_HeartRate = session.query(func.avg(Heart_Rate.HeartRate)).scalar()
    average_Sweat = session.query(func.avg(sweat.Sweat)).scalar()
    average_breathing_rate = session.query(func.avg(Breathing_Rate.BreathingRate)).scalar()

    average_last_hour_heart_rate = session.query(func.avg(Heart_Rate.HeartRate)).filter(Heart_Rate.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar()
    average_last_hour_sweat = session.query(func.avg(sweat.Sweat)).filter(sweat.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar()
    average_last_hour_breathing_rate = session.query(func.avg(Breathing_Rate.BreathingRate)).filter(Breathing_Rate.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar()
    
    if average_last_hour_breathing_rate > (average_breathing_rate * 1.2) and average_last_hour_heart_rate > (average_HeartRate*1.2) and average_last_hour_sweat > (average_Sweat*1.2):
        print('Panic Attack Detected')

    #fever and hypothermia
    average_body_temperature = session.query(func.avg(Body_temperature.temperature)).filter(Body_temperature.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar()
    if average_body_temperature > 38:
        print('Fever Detected')
    elif average_body_temperature < 35:
        print('Hypothermia Detected')
    
    #steps
    average_monthly_steps = session.query(func.avg(Steps.steps)).filter(Steps.TimeStamp >= datetime.now() - timedelta(days=30)).scalar()
    average_week_steps = session.query(func.avg(Steps.steps)).filter(Steps.TimeStamp >= datetime.now() - timedelta(days=7)).scalar()
    if average_week_steps < (average_monthly_steps * 0.5):
        print('Decreased Physical Activity Detected')
    
  
