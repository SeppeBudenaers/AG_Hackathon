using System;

public class BodyTemperature
{
    public DateTime TimeStamp { get; set; }
    public float Temperature { get; set; }
}

public class HeartRate
{
    public DateTime TimeStamp { get; set; }
    public int Rate { get; set; }
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
