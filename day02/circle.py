import math

#Asking the user to enter a number for radius of the circle:
radius = float(input("Enter the radius of the circle: "))

# Calculating the area and the circumference:
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Printing the results:
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
