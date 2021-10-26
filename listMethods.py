courses=['History','Maths','Science','Chemistry']
courses1=['Edu','Physics']

# NOTE: List Methods
# add the item to given index value
courses.insert(1,'Art')
print(courses)
print('**********************************')

# to add end of the list
courses.append('NeroScience')
print(courses)
print('**********************************')

# to concate two lists
courses.extend(courses1)
print(courses)
print('**********************************')

courses.remove('Art')
print(courses)
print('**********************************')

del courses[-1]
print(courses)
print('**********************************')


courses.pop()
print(courses)
print('**********************************')

popped=courses.pop()
print('pooped',popped)
print('**********************************')

courses.reverse()
print(courses)
# reverse an another way
# print(courses[::-1])
print('**********************************')


# NOTE: sorting a list ascending ALters the list

myFavNumbers=[4,3,2,1,5,8]
myFavNumbers.sort()
print(myFavNumbers)
print('**********************************')

# NOTE: sorting a list decending  alter the list

myFavNumbers=[4,3,2,1,5,8]
myFavNumbers.sort(reverse=True)
print(myFavNumbers)
print('**********************************')

# NOTE: without alter 

new_sortedList=sorted(courses);
print('new sorted list without chaning orginial value',new_sortedList)

# NOTE: to get the index of given Value
print('**********************************')

findIndex=courses.index('Chemistry')
print('index value of value',findIndex)

# NOTE to get True or False value if item is exits in list

print('Art' in courses)

print('**********************************')

# NOTE: for loop

for course in courses:
  print('course: ',course)


# NOTE: for loop with counter value

for index,course in enumerate(courses):
  print(f'{index} course: {course} ')
print('**********************************')

  # NOTE: for loop with counter value starts with 1

for index,course in enumerate(courses,start=1):
  print(f'{index} course: {course} ')

print('**********************************')

# NOTE: How to separte with , or - or anything you want 
fruits=['apples','figs','blueberry','straberry','pineapple']

separeated_str=', '.join(fruits)
print('separated string by ,',separeated_str)

# NOTE: reverse separated string to list
reverse_to_list=separeated_str.split(', ')
print('reverse separated str',reverse_to_list)