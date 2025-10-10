for y in range(5):
    for x in range(1,10):
        print(x, end=" ")
    print()    


rows=int(input("enter the number of rows :"))
column=int(input("enter the number of column :"))
symbol=input("enter the symbol :")

for x in range(rows):
    for y in range(column):
        print(symbol, end=" ")
    print() 
 

# collection of multiple value in one variable    
# list=order and changable duplicate are okk
# set = unorder  and immutable no duplicate
# truple= ordered and unchangable duplicate are okk fast 

fruits=["apple","orange","banana","cake"]
for x in fruits:
    print(x)

print(fruits[1])  # to access the second element of list
print(fruits[:3]) # to access all element infront of 3 not including 3
print(fruits[::2]) #to access every second element of list

# print(dir(fruits))
# print(help(fruits))

fruits[1]="pineapple"
for x in fruits:
     print(x)

fruits.append("pineapple")  #use to add an element
fruits.clear()  #use to clear a list
fruits.remove("orange") #use to remove an item from a list
fruits.insert(2,"mango") #use to insert an item in the specific index
fruits.copy() # use to copy a list in same way
fruits.remove("apple") # use to remove an element from a list
fruits.reverse() # reversed the order in which irem are set
fruits.sort(reverse=True) # it reversed the item in the ascending or descending order
fruits.pop() # it remove the last element of list
fruits2=fruits.count("apple") # it count how mwny time the item in list
print(fruits)

a=[1,2,3,4,5]
b=[6,7]
# a.extend(b) #the extend method is use to add element from one list to anather in this element of b are add on a
b.extend(a)
print(b)