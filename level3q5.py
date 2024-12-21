class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def addTime(time1,time2):
        Tminutes=time1.minutes+time2.minutes
        if Tminutes>=60:
            extrahour=Tminutes//60
            Tminutes=Tminutes%60
            
            Thour=time1.hours+time2.hours+extrahour
        else:
            Thour=time1.hours+time2.hours
            
        return f" {Thour} hours {Tminutes} minutes"    
    def displayMinutes(time):
        return time.hours*60+time.minutes
    def displayTime(time):
        return f"{time.hours} hours {time.minutes} minutes"
             
            
time1=Time(2,50)
time2=Time(1,20)
print("added two times",Time.addTime(time1,time2))
print("displaying time",Time.displayTime(time1))
print("displaying minutes",Time.displayMinutes(time2))
