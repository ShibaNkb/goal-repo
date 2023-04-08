# Functions are blocks of code used to avoid repeating the same logic
# Parameters - giving information to functions, input parameters in the brackets, many parameters separated by comma.

to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_name = 'seconds'
unit_name1 = 'minutes'

def days_to_units (num_of__days, custome_msg):
    print(f'{num_of__days} days are {num_of__days * to_seconds} {unit_name}.')
    print(custome_msg)
   

days_to_units(20, "Awesome!")   # call the function.
days_to_units(35, 'Looks great!')

''' * Scope- only available from inside the region its created.
    * Global scope- created outside the function or in a diff file.
    * Local scope- created n only used within that function.'''