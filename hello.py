# calculate the circumference of a circle with given radius
import math

radius = float(input("Enter the radius of circle(cm): "))
pi = math.pi
c = 2 * pi * radius


# calculate the Area of given circle
area = pi * pow(radius, 2)

choose = input("circumference(1) or area(2)?: ")

if choose == "1":
    print(f"The circumference is: {round(c, 2)}cm")
else:
    print(f"The area is: {round(area, 2)}cm")