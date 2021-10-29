months=[0,31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap_year(year):
  if year%4==0:
    return True
def days_of_month(year,month):
    if not 1<= month <=12:
      return 'Not valid'
    if is_leap_year(year) and month==2:
      return 29
    return months[month]


print(days_of_month(2017,3))
print(days_of_month(2017,2))
print(days_of_month(2020,2))


