
num_meals = int(input("How many meals would you like to enter? "))


meal_names = []
calorie_amounts = []


for i in range(num_meals):
    meal = input(f"Enter the name of meal #{i + 1}: ")
    calories = int(input(f"Enter the calorie amount for {meal}: "))
    
    meal_names.append(meal)
    calorie_amounts.append(calories)
print("\nYou entered the following meals and calories:")
for i in range(num_meals):
    print(f"{meal_names[i]} - {calorie_amounts[i]} calories")

Total_calorie_intake=sum(calorie_amounts)
Average_calorie_per_meal=(sum(calorie_amounts))/(len(calorie_amounts))
calorie_limit=int(input("What is your daily calorie limit? "))

if(Total_calorie_intake>calorie_limit):
    print("Warning: Your calorie intake is higher than the daily limit")
else:
    print("you are within the limit")

print("\n===== Meal Summary Table =====")
print(f"{'Meal Name':<20}{'Calories':>10}")
print("-" * 30)

for i in range(num_meals):
    print(f"{meal_names[i]:<20}{calorie_amounts[i]:>10.2f}")

print("-" * 30)
print(f"{'Total Calories:':<20}{Total_calorie_intake:>10.2f}")
print(f"{'Average Calories:':<20}{Average_calorie_per_meal:>10.2f}")












    