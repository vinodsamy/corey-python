#NOTE: concatenation
name="vinoth"
print('Hi'+'My name is vinod')
print("this is  {}".format(name))
print(f"oh my gosh this is awesome {name}")

print('*************************')

# NOTE: using single and double quotes

print('Bobby\'s is great');
print("Vino's sensational")
print('*************************')

# NOTE: for create new line python string

print("""Hi, I am vinoth 
I am from india.this is awesome place to
live earn and enjoy the life!!""")
print('*************************')

# NOTE: To get the length of string
message="Hello World!!!"
print(len(message))
print('*************************')

# NOTE: To get particular index value 
print(message[0]);
print('*************************')


# NOTE: To get range of letter Pyhton slicing

print(message[0:5])
print(message[:5])
print(message[6:])
print('*************************')

# NOTE:String Methods
print(message.upper())
print(message.lower())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('l'))
# print(message.find('Universe'))if not find return -1


# NOTE: replace a word or letter
new_message=message.replace('World','Universe')
print(new_message)

print('*************************')

# NOTE: for definition of methods
# print(dir(message))
# print(help(str))
# print(help(str.lower))
