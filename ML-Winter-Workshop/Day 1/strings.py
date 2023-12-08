print('hello world!!')

my_message = "Ash's world"
print(my_message)
# We can use triple quotes for multi-line strings

message = 'Hello world'
print(len(message))
print(message[0])     # Index represents the location of a specific character
print(message[len(message) - 1])
# print(message[12])  #Gives an error index > len(message)

# Slicing
print(message[0 : 5]) #Second index is excluded
print(message[6: ])

# String methods
'''
message.upper()
message.lower()
message.count('l')
message.find('l') --->Returns the index of a character
message.replace('world', 'universe')
'''
print(message.replace('world', 'universe'))

# String concatenation
greeting = 'hello '
name = input('enter your name :')
new_message = greeting + name 
print(new_message)

# String formatting
message = f'{greeting}, {name.upper()} welcome!!'
print(message)

print(dir(name)) #returns all methods & properties related to a specified object

