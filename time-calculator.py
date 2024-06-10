def add_time(start, duration,day=False):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    new_time=""
    time=start[-2:]
    new_hour=int(start[:start.index(":")])
    new_mins=int(start[start.index(":")+1:start.index(":")+3])
    dur_hours=int(duration[:duration.index(":")])
    dur_mins=int(duration[duration.index(":")+1:])

    new_mins+=dur_mins
    if new_mins>=60:
        new_mins%=60
        new_hour+=1
    new_hour+=dur_hours
    if new_hour>=12:
        new_hour%=12 
        if new_hour==0:
            new_hour=12
        if dur_hours%24!=0 or new_hour==12:
            time = "PM" if time == "AM" else "AM"
            
    num_days=(dur_hours//24)+1 if (start[-2:]=="PM" and time=="AM") else (dur_hours//24)
    new_time+=str(new_hour)+":"+(str((new_mins)) if new_mins>9 else "0"+str(new_mins))+" "+time
    if day:
        today=days.index(day.capitalize())+num_days
        if today>=7:
            today%=7
        new_time+=", "+days[today]
        
    if num_days>0:
        new_time+=" ("+('next day)' if num_days==1 else str(num_days)+" days later)")
    return(new_time)



add_time('8:16 PM', '466:02', 'tuesday')
