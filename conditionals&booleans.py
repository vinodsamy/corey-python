language="Python"

if language== 'Python':
  print('Language is Python')
elif language=='Javascript':
  print('Language is Javascript')
else:
  print('No match')

print('*******************************************')

# NOTE:and or not operators
user_role='Admin'
logged_in=False

if user_role=='Admin' and logged_in:
  print('Admin')
else:
  print('Lousy creds')
print('*******************************************')

if user_role=='Admin' or logged_in:
  print('Admin')
else:
  print('Lousy creds')
print('*******************************************')

if not logged_in:
  print('Please login')
else:
  print('Welcome')

print('*******************************************')


# NOTE: is object identity if object memory id same only return a True

a=[1,2,3]
b=[1,2,3]


print(id(a))
print(id(b))
print(a==b)

a=[1,2,3]
b=[1,2,3]


print(id(a))
print(id(b))
print(a is b)

a=[1,2,3]
b=a


print(id(a))
print(id(b))
# NOTE
print(a is b)
print('*******************************************')

print('*******************************************')


# NOTE:False values
# False
# None
# any numeric value zero(0)
# empty sequence whether it is '', [] or ()
# empty mapping. {}

# conditional=False
# conditional=None
# conditional=0
# conditional=''
# conditional=[]
# conditional=()
conditional={}


if conditional:
  print('Evaluated True')
else:
  print('Evaluated False')
