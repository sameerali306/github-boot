# append
# add items at the end of the list
list=["apple","mango","banana"]
print(list)
list.append("grape")
print(list)

# clear
# remove all the element from list
list=["sameer","shahzain","ali","saleem"]
print(list)
list.clear()
print(list)

# copy
student=["ali","shakeel","shahzain"]
print(student)
new=student.copy()
print(new)

# count
number=[1,2,3,4,5,4,6,]
print(number)
count=number.count(4)
print(count)

# extends
list=[1,2,3,4]
print(list)
list.extend([5,6,7,8])
print(list)

city=["lahore","karachi","multan","faisilabad"]
# print(city)
city.extend(["rawalpindi","peshwar","quetta"])
print(city)

# index
distric=["ghizer","hunza","nagar","gilgit"]
index=distric.index("nagar")
index=distric.index("gilgit")
print(index)

# insert
country=["pakistan","canada","america","africa"]
print(country)
country.insert(0,"china")
country.insert(1,"russia")
print(country)

# pop
ghizer=["gupis","yasin","punial","shiger"]
print(ghizer)
pop=ghizer.pop(3)
print(pop)

# remove
ghizer=["gupis","yasin","punial","shiger"]
ghizer.remove("shiger")
print(ghizer)

