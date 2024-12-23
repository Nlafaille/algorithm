baseprice = float(input('How much is the base price? '))
weight = float(input('What is the weight? '))
distance = float(input('What is the distance? '))

if distance < 250:
    discount = 0
elif 250 <= distance < 500:
    discount = 0.10
elif 500 <= distance < 1000:
    discount = 0.15
elif 1000 <= distance < 2000:
    discount = 0.20
elif 2000 <= distance < 3000:
    discount = 0.35
elif 3000 <= distance:
    discount = 0.50

cost = baseprice * weight * distance * (1 - discount)

print(f'The shipping cost is {cost}')