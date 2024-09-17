# 2. Double Scoop with Nested Loops
import random

moods = ["manic", "depressed", "lonely", "anxious", "tired", "sick", "hungry", "frustrated"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times_of_day = ["morning", "afternoon", "evening"]
day_count = 0
time_count = 0
for day in days_of_week:
    for time in times_of_day:
        if time_count == 3:
            time_count = 0
            day_count += 1
        print("On", days_of_week[day_count], times_of_day[time_count] + ", you were feeling", random.choice(moods) + ".")
        time_count += 1