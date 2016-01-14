from datetime import datetime, timedelta

now = datetime.now()
today = datetime(now.year, now.month, now.day)

difference = now - today

print("Seconds since midnight: " + difference)
