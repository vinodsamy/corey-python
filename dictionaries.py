
# NOTE dict are mutable and allow duplicates values 
student={'name':'John','age':26,'courses':['Math','Science']}


# NOTE: to get a value in a diffenent ways
print(student['name'])
print(student.get('name'))
# print(student['phone'])# to avoid this error 
print(student.get('phone'))

print('**************************************************')
# NOTE: to update a value in differeent ways

# if you want to update single value
student['name']='saamy'
print(student)
print('**************************************************')

# if you want to update mutiple values at a time use update method

student.update({'name':'gatsy','age':28})
print(student)
print('**************************************************')

# NOTE: delete an item

del student['age']
print(student)

poppedDict=student.pop('courses')
print(student)
print(poppedDict)
print('**************************************************')

# NOTE: get length of dict
student1={'name':'John','age':26,'courses':['Math','Science']}

print(len(student1))
print('**************************************************')

# NOTE: get a keys 
print(student1.keys())
print('**************************************************')


# NOTE: get a values
print(student1.values())
print('**************************************************')



# NOTE: get a whole dict
print(student1.items())
print('**************************************************')

# NOTE: how to loop dictionaries
for key,value in student1.items():
  print(key,value)
print('**************************************************')
