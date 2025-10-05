# and (operter execute if both the condition are true)
# 0r (or operator is execute if one of the condition is true)
# nOT (not operator invert the condition)


age=int(input("Enter your age : "))
is_LoggedIn=True

if age>=18 and is_LoggedIn==True:
    print("You are welcome")
else:
    print("You are not eligible to login")   

temp=int(input("Enter the temperature :"))
is_ranning=input("is there ranning out side (TRUE or False):")

if temp<20 or is_ranning==True:
    print("we are going on a trip")
elif temp>20 or is_ranning==False:
    print("we are  going on a trip") 
else:
    print("we are not going on a trip ")       


UserName=input("Enter your UserName : ")
password=int(input("Enter your password : "))
Email=input("Enter your Email : ")

if UserName=="sameer ali" and password==123456 and Email=="sameer240@gmail.com":

    print("You have successfully login")
else:
    print("your username password or email is in correct")    


Name=input("Enter the student name :")
father=input("Enter the father name :")
marks=float(input("Enter the marks of student :"))

if Name=={Name} or father=={father} or marks>20:
    print("You are pass")
else:
    print("you are fail")    

