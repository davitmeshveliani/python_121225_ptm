weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}
import itertools
days_cycle = itertools.cycle(weekly_schedule.keys())
print("- Next day --> Press 'Enter' (To quit --> type 'q')")
while True:
    user_input = input()
    if user_input.lower() == 'q':
        break
    current_day = next(days_cycle)
    tasks = weekly_schedule[current_day]
    print(f"{current_day}: {', '.join(tasks)}")
# ///////////////////////////////////////////////

import itertools
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]
chain = itertools.chain(fruits, vegetables, dairy)
for num in chain:
    print(num)
###########################################

import itertools
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]
combin = itertools.product(clothes, colors, sizes)
for item in combin:
    print(f"{item[0]} - {item[1]} - {item[2]}")
