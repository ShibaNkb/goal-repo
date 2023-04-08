# * Input function is inbuilt in python.
# * Provide a parameter that tells a user what to do.
# * Return statements hold a value that can be put in a variable and called.
# * Casting is changing 1 data type into another eg from string to integer.


to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_name = 'seconds'
unit_name1 = 'minutes'

def days_to_units (num_of__days):
    return f'{num_of__days} days are {num_of__days * to_seconds} {unit_name}.'
    
user_input = input('Hey user, enter a number of days and i will convert it to hours.\n') #variable for input
user_input_number = int(user_input)       # variable for user_input to make number an integer

calculated_value = days_to_units(user_input_number)    # variable to call day_to_unit function
print(calculated_value)