using System;

public class BodyTemperature
{
    public DateTime TimeStamp { get; set; }
    public float Temperature { get; set; }
}

public class Heart_Rate
{
    public DateTime TimeStamp { get; set; }
    public int HeartRate { get; set; }
}

public class BloodPressure
{
    public DateTime TimeStamp { get; set; }
    public int Systolic { get; set; }
    public int Diastolic { get; set; }
}

public class BloodOxygen
{
    public DateTime TimeStamp { get; set; }
    public int Oxygen { get; set; }
}

public class RespiratoryRate
{
    public DateTime TimeStamp { get; set; }
    public int Rate { get; set; }
}

public class Sweat
{
    public DateTime TimeStamp { get; set; }
    public int Level { get; set; }
}

public class Sugar
{
    public DateTime TimeStamp { get; set; }
    public int Level { get; set; }
}

public class Steps
{
    public DateTime TimeStamp { get; set; }
    public string StepCount { get; set; }
}

public class Emotion
{
    public DateTime TimeStamp { get; set; }
    public string CurrentEmotion { get; set; }
}

public class Stress
{
    public DateTime TimeStamp { get; set; }
    public int Level { get; set; }
}

public class GetResponse {

    // [JsonParameterName("Body_Temperature")]
    public BodyTemperature[] Body_Temperature {get;set;} = new BodyTemperature[0];
    public Heart_Rate[] Heart_Rate {get;set;} = new Heart_Rate[0];
    public BloodOxygen[] Blood_Oxygen {get; set;} = new BloodOxygen[0];
    public Sweat[] Sweat {get; set;} = new Sweat[0];
}