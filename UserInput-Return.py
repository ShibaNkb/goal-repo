# * Input function is inbuilt in python.
# * Provide a parameter that tells a user what to do.

to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_name = 'seconds'
unit_name1 = 'minutes'

def days_to_units (num_of__days, custome_msg):
    print(f'{num_of__days} days are {num_of__days * to_seconds} {unit_name}.')
    print(custome_msg)
   
user_input = input('Hey user, enter a number of days and i will convert it to hours.\n')
print(user_input)