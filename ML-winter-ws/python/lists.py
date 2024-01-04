# lists are used to store multiple values in a single variable
mylist = ['apple', 'banana', 'cherry']
print(mylist)

# we can access an item in a list using index
mylist[1] = 'orange'
print(mylist)
print(len(mylist))

list2 = [1, 2, 4, 5, 6]
list3 = [True, False, False, True]
list4 = ['abc', True, 42, 3.14, ['apple', 'cherry']]


courses = ['math', 'history', 'phy', 'BE']
print(courses)
print(len(courses))

print(courses[2])
print(courses[-1])
print(courses[0 : 2])

for x in courses: 
    print(x)

print(type(courses))
print(dir(courses))

# courses.append('biochem')
# Insert method to add an item at a specific index
courses.insert(2, 'biochem')
print(courses)
