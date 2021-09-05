def add_time(start, duration,day=""):
  week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  meridiem="AM" 
  if meridiem not in start:
     meridiem="PM"
  
  startData=start.split(":")
  startHour=int(startData[0].replace("PM","").strip())
  startMinute=int(startData[1].replace("PM","").replace("AM","").strip())
  if "PM" in start:
    startHour=startHour+12
  durationData=duration.split(":")
  durationHour=int(durationData[0])
  durationMinute=int(durationData[1])

  totalhours=(startHour+durationHour+int((startMinute+durationMinute)/60))
  days=int(totalhours/24)
  hours=totalhours%24
  minutes=(startMinute+durationMinute)%60
  
  
  try:
    day=week.index(day.lower())
  except:
    day=-1


  if minutes<10:
    minutes=f"0{minutes}"

  if hours>=12:
    meridiem="PM"
  else:
    meridiem="AM"



  hours=(hours%12)
  if(hours==0):
    hours=12
  
  if(days==0 and day==-1):
    return f"{hours}:{minutes} {meridiem}"
  if(days==1 and day==-1):
    return f"{hours}:{minutes} {meridiem} (next day)"
  if(days>1 and day==-1):
    return f"{hours}:{minutes} {meridiem} ({days} days later)"
  if(days==0):
   return f"{hours}:{minutes} {meridiem}, {week[(day+days)%7].capitalize() }"
  if(days==1):
   return f"{hours}:{minutes} {meridiem}, {week[(day+days)%7].capitalize() } (next day)"
  if(days>1):
   return f"{hours}:{minutes} {meridiem}, {week[((day+days)%7)].capitalize() } ({days} days later)"
