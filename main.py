Total_deposit = 18000
Total_meals = 300

def calculate_meal_rate(Total_deposit, Total_meals):
    if Total_meals == 0:
        return 0.0
    return Total_deposit / Total_meals
meal_rate = calculate_meal_rate(Total_deposit, Total_meals)
print("== Mess Overview ==")
print(f"Total deposit: {Total_deposit}BDT")
print(f"Total meals: {Total_meals}")
print(f"Currrent Meal Rate: {meal_rate:2f} BDT/meal")