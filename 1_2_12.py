import math

x = int(input("Enter x-coordinate of center: "))
y = int(input("Enter y-coordinate of center: "))
r = int(input("Enter radius: "))

px = int(input("Enter x-coordinate of point: "))
py = int(input("Enter y-coordinate of point: "))

distance = math.sqrt(math.pow(px - x, 2) + math.pow(py - y, 2))

if distance < r:
    print("Point lies inside the circle")
elif distance == r:
    print("Point lies on the circle")
else:
    print("Point lies outside the circle")
