#the script

import shapes
import random

def main():
    # Generate random radius between 1 and 10
    radius = round(random.uniform(1, 10), 2)
    print(f"Circle with radius {radius}")
    print(f"Area: {shapes.circle_area(radius):.2f}")
    print(f"Circumference: {shapes.circle_circumference(radius):.2f}")
    
    print("\n----------------\n")

    # Generate random length and width between 1 and 15
    length = round(random.uniform(1, 15), 2)
    width = round(random.uniform(1, 15), 2)
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area: {shapes.rectangle_area(length, width):.2f}")
    print(f"Perimeter: {shapes.rectangle_perimeter(length, width):.2f}")

if __name__ == "__main__":
    main()

