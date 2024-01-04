# Strings
message = 'Hello World!'
print(message)

my_message = "Bobby's world"
my_message = 'bobby\'s world'
print(my_message)

# we can access individual characters in a string using index
print(message[-2])
print(message[0: 5])

# the first index is included, whereas the second one in not
print(len(message))


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

print(message.upper())
print(message.lower())
print(message.count("l"))
print(message.find('a'))
print(message.replace("World", 'Universe'))
print(message.split(' '))

# greeting = "hello "
# name = input('Enter your name!')

# print(greeting + name + '!')

# print(42 + "Don't panic")
# we cannot concatenate a str with an int
print(str(42) + "Don't panic")

# print(f'{greeting.upper()} {name}!')

# print(dir(message))
# print(help(str.split))

x = 5.5
print(type(x))

a = 1    #integer
b = 3.14 #float
c = 4j   #complex
print(type(a), type(b), type(c))

num = 3
num += 1
print(num)

print(type(num))
num = 3.14
print(type(num))

# Arithmetic operators
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 % 2)
print(3 ** 2)

# Comparision operators : Returns a boolean
print(3 > 2)
print(3 < 2)
print(3 == 2)
print(3 != 2)
