import datetime

# Check days 8 to 14 for the second Saturday of October 2026
for day in range(8, 15):
  
  if datetime.date(2026, 10, day).weekday() == 5:  # 5 means Saturday

    print("Second Saturday is on:", day)

    break