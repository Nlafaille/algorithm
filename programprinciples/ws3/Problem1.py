mark_provided = float(input('How many marks? '))

if mark_provided >= 85:
    grade_awarded = 7
elif 75 < mark_provided < 85:
    grade_awarded = 6
elif 75 < mark_provided < 65:
    grade_awarded = 5
elif 65 < mark_provided < 50:
    grade_awarded = 4
else:
    grade_awarded = 'F'

print(f"Grade awarded: {grade_awarded}")