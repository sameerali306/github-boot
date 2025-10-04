#python weight converter
# weight=float(input("Enter your weight : "))
# unite=input("Kilogram or Pound? (K or L) :")

# if unite=="K":
#     weight=weight*2.205
#     unite="lbs"
#     print(f"Your weight is : {round(weight,1)} {unite}")
# elif unite=="L": 
#     weight=weight/2.205
#     unite="kgs"
#     print(f"Your weight is : {round(weight,1)} {unite}")   


unit=input("Is this temperature is in Celsius or Fahrenite (C or F) :")
temp=float(input("Enter the temperature :"))

if unit=="C":
    temp=round((9 * temp) / 5 +32,1)
    print(f"the temperature in fahrenite is {temp}\u00B0F")
elif unit=="F":
    temp=round((temp - 32) * 5/9,1)
    print(f"the temperature in celsius is {temp}\u00B0F")
else:
    print(f"the {unit} is invalid")    
