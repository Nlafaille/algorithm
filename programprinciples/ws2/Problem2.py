#Problem2
hours_per_day_input = input('Number of hours worked per day ')
days_per_week_input = input('Number of days worked in a week ')
annual_salary_input = input('Annual salary ')

hours_per_day = float(hours_per_day_input)
days_per_week = float(days_per_week_input)
annual_salary = float(annual_salary_input)

total = hours_per_day * days_per_week * 52

hourly_wage = annual_salary / total
print(f"${hourly_wage}")

# print(f"Length of park (m): {hours_per_day}")
# print(f"Width of park (m): {days_per_week}")
# print(f"Litres per square meter: {annual_salary}")
# print(f"Litres required = {hourly_wage}")