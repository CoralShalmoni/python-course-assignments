# Asking the user to enter the height and the width of a rectangle:
height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area and perimeter
area = height * width
perimeter = 2 * (height + width) #The heigh twice and the width twice

# Printing the results:
print(f"Area of the rectangle: {area:.2f}")
print(f"Perimeter of the rectangle: {perimeter:.2f}")
