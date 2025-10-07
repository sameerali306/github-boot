# for loop =a for loop execute a condition for a given amount of time...
import time

# for count in reversed(range(1,100,2)):
#     print(count)    


# cardit_Card="123_1223_12233"
# for x in cardit_Card:
#     print(x)

# for count in range(1,20):
#     if count==10:
#         continue     #the continue key word is use to skip the number that is give or any condition
#     else:
#         print(count)

# for count in range(1,12):
#     if count==10:
#         break
#     else:
#         print(count)

my_Times=int(input("Enter the time in second :"))  

for x in range(my_Times,0,-1):
    seconds=x % 60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)