hours_worked = int(input('How many hours were worked? '))
total_car_sold_per_week = int(input('Total number of cars sold for the week? '))

basesalary = 36.25
if hours_worked > 37:
    regular_hours = 37
    overtime_hours = hours_worked -37
    salary = regular_hours * basesalary + overtime_hours * (basesalary * 1.5)
    salary_bonus = basesalary * 1.5
else:
    salary = hours_worked * basesalary

if total_car_sold_per_week > 5:
    car_bonus = (total_car_sold_per_week - 5) * 200
else:
    car_bonus = 0

total_salary = salary + car_bonus

print(f'The salary is {total_salary}')