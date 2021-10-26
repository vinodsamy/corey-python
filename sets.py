# NOTE: Sets are unordered and don't have duplicate values

courses={'History','Maths','Science','Chemistry'}
courses1={'History','Maths','Art','Design'}
print(courses)

print('Maths' in courses)# this is best case to use sets in python


print(courses.intersection(courses1))#have common sets values
print(courses1.difference(courses))#have difffernce values from two sets
print(courses1.union(courses))#add together both sets