# variables are containers for storing data values

# python is completely object oriented and not "staticslly types"

# every variable in py is an object

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
variable names must only contain alpha-numeric values or underscore char
'''

myVariableName = 'John' #--->camel case
MyVariableName  = 'John' #--->Pascal case
my_variable_name = 'John' # --->snake case

# we can assign mulitples values to multiple variables in a single line

x, y, z, = 1, 2, 3
print(x, y, z)

# we can assign similar values to multiple variables as well
 
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
    print('python is ' + x)
myfunc()

height = 1.79
weight = 68.7

bmi = weight / height**2
print(int(bmi))
print(type(bmi))