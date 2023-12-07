# variables are containers for storing data values
x = 5
y = 'John'
print(x, y)
# x = 'sally'
# print(x, y)

#Type casting
print(type(x))
print(type(y))

#variable names are case-sensitive
a = 4
A = 'sally'

'''
variable names are case-sensitive
variable names must start with a letter or underscore but not with a number
variable name cannot be a python keyword
'''

myVariableName = 'John' #--->camel case
MyVariableName  = 'John' #--->Pascal case
my_variable_name = 'John' # --->snake case

x, y, z, = 1, 2, 3
print(x, y, z)

x = y = z = 10
print(x, y, z)
print(x + y + z)

a = 'dont panic'
b = 42
# print(a + b) --->cannot combine a string with a number
print( a + str(b))

#Global variables--->can be used both inside and outside a function
x = 'awesome'

def myfunc():
    print('python is' + x)
myfunc()
