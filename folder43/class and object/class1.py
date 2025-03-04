# by declare a variable and store a class and call it we create an object
# class person:
#     name="sameer ali"
#     age=20
# p1=person()
# print(person.name)    


# init function 
# class person1:
#     def __init__(self,name,age,eduction,hobby):
#         self.name=name
#         self.age=age
#         self.eduction=eduction
#         self.hobby=hobby
# detail=person1("sameer ali",20,"undergraduate","music playing circket") 
# print(detail.name) 
# print(detail.age)      


# class person2:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"my name is{self.name}and my age is{self.age}" 
# info=person2("shahzain",20) 
# print(info) 


class person3:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myFun(self):
        print("Hello my name is "+self.name) 
p3=person3("shakeel",30) 
p3.myFun()



