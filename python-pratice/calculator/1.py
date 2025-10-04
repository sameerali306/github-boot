num1=float(input("Enter ist number : "))
operator=input("enter an operator (+,-,*,/) : ")
num2=float(input("Enter 2nd number : "))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else :
    print(f"the {operator} that the user is selected is invalid")    
