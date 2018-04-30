import datetime
now=datetime.datetime.now()
print(now.year, now.month, now.day,now.hour, now.minute)
if now.hour>12:
    print("afternoon")
else:
    print("evening")
