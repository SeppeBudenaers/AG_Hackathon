from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
#Environmental Data

#Body Data
class Body_Temprature(Base):
    __tablename__ = 'Body_Temprature'
    TimeStamp = Column(DateTime, primary_key=True)
    Temprature = Column(Float)

class Heart_Rate(Base):
    __tablename__ = 'Heart_Rate'
    TimeStamp = Column(DateTime, primary_key=True)
    HeartRate = Column(Integer)

class Blood_Pressure(Base):
    __tablename__ = 'Blood_Pressure'
    TimeStamp = Column(DateTime, primary_key=True)
    Systolic = Column(Integer)
    Diastolic = Column(Integer)

class Blood_Oxygen(Base):
    __tablename__ = 'Blood_Oxygen'
    TimeStamp = Column(DateTime, primary_key=True)
    Oxygen = Column(Integer)

class Respiratory_Rate(Base):
    __tablename__ = 'Respiratory_Rate'
    TimeStamp = Column(DateTime, primary_key=True)
    RespiratoryRate = Column(Integer)

class sweat(Base):
    __tablename__ = 'sweat'
    TimeStamp = Column(DateTime, primary_key=True)
    sweat = Column(Integer)

class sugar(Base):
    __tablename__ = 'sugar'
    TimeStamp = Column(DateTime, primary_key=True)
    sugar = Column(Integer)

#Activity Data
class Steps(Base):
    __tablename__ = 'Steps'
    TimeStamp = Column(DateTime, primary_key=True)
    Steps = Column(String)

#Emotional Data
class Emotion(Base):
    __tablename__ = 'Emotion'
    TimeStamp = Column(DateTime, primary_key=True)
    Emotion = Column(String)

class Stress(Base):
    __tablename__ = 'Stress'
    TimeStamp = Column(DateTime, primary_key=True)
    Stress = Column(Integer)