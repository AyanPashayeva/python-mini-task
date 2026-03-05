user_name = input("What is your name? ")
user_age = int(input(f"Hi {user_name}, how old are you?"))
user_weight = float(input("Enter your weight in kg :"))
user_height = float(input("Enter your height in meters:"))
hourly_rate = float(input("Your hourly salary (AZN):"))
worked_hours = float(input("How many hours do you work per week?"))

#calculations
current_year = 2026
birth_year = current_year - user_age

#Height squared
bmi = user_weight / (user_height**2)

#Financial Calculations
total_salary = hourly_rate * worked_hours

#Health Status Analysis
if bmi < 18.5:
    status ="Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal weight"
else:
    status = "Overweight"
#Displaying result
print("Name:" , user_name)
print("Age:" , user_age)
print("Birth year:" , birth_year)
print("BMI result:" , bmi , f"({status})")
print("Health status:" , status)
print("Total salary:" , total_salary , "AZN")