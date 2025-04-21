import sys
import math

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

# Get the radius from command line argument
radius = float(sys.argv[1])

# Calculating the area and the circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Printing the results
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
