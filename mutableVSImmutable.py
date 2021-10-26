# NOTE: Lists are mutable and ordered and allow duplicate values
courses=['History','Maths','Science','Chemistry']
courses2=courses
print(courses)
print(courses2)

courses2[0]='Art'

print(courses)
print(courses2)

print('************************************')

# NOTE:Tuples are ordered,immutable and allow duplicate vaues

syllabus=('History','Maths','Science','Chemistry')
syllabus2=syllabus
print(syllabus)
print(syllabus2)

# syllabus2[0]='Art'# this is throw an error because you can't mutate the tuples

print(syllabus)
print(syllabus2)


