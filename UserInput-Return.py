# * Input function is inbuilt in python.
# * Provide a parameter that tells a user what to do.
# * Return statements hold a value that can be put in a variable and called.


to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_name = 'seconds'
unit_name1 = 'minutes'

def days_to_units (num_of__days, custome_msg):
    return f'{num_of__days} days are {num_of__days * to_seconds} {unit_name}.'
   
   
my_var = days_to_units(20)
print(my_var)

user_input = input('Hey user, enter a number of days and i will convert it to hours.\n')
print(user_input)