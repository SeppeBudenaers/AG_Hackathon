from Database_Classes import *
from sqlalchemy import func
def Anomaly():
    #
    average_HeartRate = session.query(func.avg(Heart_Rate.HeartRate)).scalar()
    
    average_last_hour_heart_rate = session.query(func.avg(Heart_Rate.HeartRate)).filter(Heart_Rate.TimeStamp >= datetime.now() - timedelta(hours=1)).scalar()
        
    
