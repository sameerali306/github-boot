import math
x=3.14
y=4
z=5

result=round(3.14)  #it round the given number to lower decimal place
result=abs(y) #the abs value show how far a number is from zero
result=pow(5,3) #the first number is base and the second number is power of it
result=max(x,y,z) #identify the max value from the values
result=min(x,y,z) #identify the min value from the given number
print(result)

print(math.pi)
radius=float(input("enter the radus of circle : "))
circumference=2*math.pi*radius
print(f"the circumference of circle is {round(circumference,1)}") #it round the circumference to 1 decimal place

radius=float(input("enter the radius of the circle :"))
area=math.pi*pow(radius,2)
print(f"the area of the circle is :{round(area,3)}")

A=float(input("enter the side A:"))
B=float(input("enter the side B:"))
C=math.sqrt(pow(A,2) * pow(B,2))
print(C)




