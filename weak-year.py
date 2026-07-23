import calendar

year = 2026


is_leap = calendar.isleap(year)

weeks = 53 if is_leap else 52

print(f"Year: {year}")
print(f"Leap Year: {is_leap}")
print(f"Total Weeks: {weeks}")