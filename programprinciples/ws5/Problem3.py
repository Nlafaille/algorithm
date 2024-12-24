#Leap year and number of days calculation
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False
def calculate_total_days(year1, year2):
    number_of_days = 0
    normal_days = 365
    leap_days = 366

    for year in range(year1, year2 +1):
        if is_leap_year(year):
            number_of_days += leap_days
        else:
            number_of_days += normal_days
    return number_of_days

# inputs years
year1 = int(input("Year 1? "))
year2 = int(input("Year 2? "))

#output call
output = calculate_total_days(year1, year2)
print(f"Number of days are {output}")