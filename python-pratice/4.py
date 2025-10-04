import math
# radius=float(input("enter the radius of sphere : "))
# volume=4/3*math.pi*pow(radius,3)
# print(round(volume))

height=float(input("enter the height of cylinder : "))
radius=float(input("enter the radius of cylinder : "))
cylinderVolume=2*math.pi*height*radius+2*math.pi*pow(radius,2)
print(round(cylinderVolume,2))
