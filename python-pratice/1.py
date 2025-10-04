#variable = A variable is a container used to store a value in memory

full_name="sameer ali"
age=20
# print(f"hello {full_name} you are {age} year old .")

name="ali"
age=13
print("my name is {} and my age is {}".format(name,age))  #this is a old format before introduce of f string
                                                            #of including variable in strig
name="fariyal"
age=5
# print("my name is {f_name} and my age is {f_age}".format(f_name=name , f_age=age))

name="shahzain alam"
age=21
print("my name is %s and my age is %d year old" %(name,age)) #this is also aold method percent formatting  


#disadvantage of .format method
#hard to read with many value
name="sameer ali"
age=20
email="sammmerxyz"
id=20.4
password="ccddssdbgdg"
#print("my name is %s and my age is %d and my email is %s my id is %f and my password is %s" %(name ,age,email,id,password))

#type casting =the process of converting from one data type to anather is called type converting

name=""
age=20
floating=23.33
casting=int(floating)
int=float(age)
print(int)
print(type(int))
bool=bool(name)
print(bool)


