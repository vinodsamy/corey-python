lists=[0,1,2,3,4,5,6,7,8,9]

# syntax is lists[start:end:step]
# start item is inclusive 
# end item is exclusive
# step is skip certail number of items in between 

print(lists[:])#copy of lists
print(lists[-1])# get last item from a lists

# print(lists[0:6])
# print(lists[:6])

print(lists[3:8])
print(lists[3:-2])#mix postive and negative index number to get the item


print(lists[1:9:2])
print(lists[-1:2:-2])

# NOTE: reverse the list
print(lists[::-1])

# NOTE:string slicing

my_website="https://vinodsamy.com"
print(my_website[::-1])

print(my_website[-4:])

print(my_website[8:])

print(my_website[8:-4])