# x="awsome"
# def myFunc():
#     print("python is"+x)
# myFunc() 

# x="javascript"
# def fun():
#     x="python"
#     print("i learn" +x)
# fun()   
# print("i learn" +x) 

# the global key word change the value of the variable in global scope
x="handsome"
def Myfun():
    global x
    x="smart"
    print(x)
Myfun()    
print(x)
