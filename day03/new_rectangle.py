import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python rectangle.py <height> <width>")
    sys.exit(1)

# Get height and width from command line arguments
height = float(sys.argv[1])
width = float(sys.argv[2])

# Calculating the area and perimeter
area = height * width
perimeter = 2 * (height + width)

# Printing the results
print(f"Area of the rectangle: {area:.2f}")
print(f"Perimeter of the rectangle: {perimeter:.2f}")
