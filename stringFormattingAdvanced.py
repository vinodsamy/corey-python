person={'name':'vinoth','age':26}


lists=['vinoth',26]

print("My name is {} and I am {} years old.".format(person['name'],person['age']))

print("My name is {0[name]} and I am {1[age]} years old.".format(person,person))
print("My name is {0[name]} and I am {0[age]} years old.".format(person))

print('***********************************************')

print("My name is {0[0]} and I am {0[1]} years old.".format(lists))

print('***********************************************')


# NOTE:Person class
class Person():
  def __init__(self,name,age):
      self.name=name
      self.age=age
  

p1=Person('vinoth',26)
print("My name is {0.name} and I am {0.age} years old.".format(p1))
print('***********************************************')
# NOTE:unpacking dict 
print("My name is {name} and I am {age} years old.".format(**person))

print('***********************************************')
# NOTE:to start with zero 
for i in range(1,11):
  sentence="The value of i is {:02}".format(i)
  print(sentence)

print('***********************************************')

# NOTE: this is kind of js toFixed method
pi=3.14274748
print("Pi value is {:.2f}".format(pi))

print("Pi value is {:.3f}".format(pi))
print('***********************************************')

sentence1="1MB is in Bytes {}".format(1000**2)
sentence1="1MB is in Bytes {:,}".format(1000**2)
sentence1="1MB is in Bytes {:,.2f}".format(1000**2)
print(sentence1)

print('***********************************************')
# NOTE: DATE Formating

import datetime

my_birth_date=datetime.datetime(1995,2,9,10,00,00)

print("MY BIRTH DATE IS {}".format(my_birth_date))
print("After formated date ")
print("MY BIRTH DATE IS {:%B %d, %Y}".format(my_birth_date))

print('***********************************************')

sentence2="{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} day of the year.".format(my_birth_date)
print(sentence2)