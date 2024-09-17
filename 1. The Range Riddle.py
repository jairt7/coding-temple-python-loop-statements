# 1. The Range Riddle
import random

moods = ["manic", "depressed", "lonely", "anxious", "tired", "sick", "hungry", "frustrated"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_count = 0
for day in days_of_week:
    print("On", days_of_week[day_count] + ", you were feeling", random.choice(moods) + ".")
    day_count += 1