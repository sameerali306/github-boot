# food=input("Enter your food and (q to quit) :")

# while not food=="q":
#     print(f"you like {food}")
#     food=input("Enter your food and (q to quit) :")
# print("Bye")    


# count=int(input("Enter a number :"))

# while count <10:
#     print(f"your count is : {count}")
#     count +=1
# print("Your counting is complete")    

secret_number=3
guess=None
attempt=0

while not guess==secret_number:
    print(f"Try again : Your guess is wrong you have {attempt} left:") 
    guess=int(input("enter your gusses your guss must batween 1 and 10 :"))
    attempt +=1

print("Congrats ! your guess is right....")     