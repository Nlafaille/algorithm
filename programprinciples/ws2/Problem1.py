#Problem1
l = float(input('Please provide length of the park in meters '))
w = float(input('Please provide width of the park in meters '))
v = float(input('Please provide volume of concrete required in litres per square metre '))

concrete = l * w * v

print(f"Length of park (m): {l}")
print(f"Width of park (m): {w}")
print(f"Litres per square meter: {v}")
print(f"Litres required = {concrete}")

