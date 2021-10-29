def simple_func():
  print('Hi, Function!')

simple_func()


def return_func():
  return 'Vinoth'

print(return_func())
print(return_func().upper())


# NOTE pass parameters

def normal_func(greeting):
  print(f"{greeting}, Function.")

normal_func('HOOOOO')

# NOTE pass parameters

def default_params_func(greeting,name='Vino'):
  print(f"{greeting}, Function.{name}")

default_params_func('HOOOOO','Ram')



# NOTE Arguments and keyword atguments how to pass to the function
def student_info(*args,**kwargs):
  print(args)
  print(kwargs)

student_info('Math','Art','test',name="vino",age=30)


# NOTE; unpacking arguments and keyword arguments


courses=['Math','Design']
info={'name':"vino",'age':26,'job':'SW'}

student_info(*courses,**info)