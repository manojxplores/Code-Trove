x = 5.5
print(type(x))

a = 1    #integer
b = 3.14 #float
c = 4j   #complex
print(type(a), type(b), type(c))

x = '40'
print(int(x) + 2)

#Strings
a = 'hello'
print(a)

print(len(a))
# index gives the location of an element of a string
print(a[2:4])

for i in 'banana':
    print(i)

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

txt = 'the best things in life are free'
print('Life' in txt)
# we can use the 'in' keyword to ckeck if a certain phrase is present in a string
print('Life' not in txt)

#String methods
# string methods just return the modified version a string
# they donot change the original string
'''
.upper() --->converts a string into uppercase
.lower()
.strip() --->returns a trimmed version of a string
.replace( , )

'''

# Boolean values
'''
bool(0)       bool(123)
bool(False)   bool(True)
bool(())      bool("abc")
bool([])      bool(["apple", "cherry", "banana"])
bool({})
bool("")
'''
