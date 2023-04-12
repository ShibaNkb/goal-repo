# * Error handling- try/except is a code run only if that condition is true.
# * Try block- lets u test a block of code for errors.
# * Except block - catches the error and lets u handle it. - ValueError
# * Try/except covers multiple errors unlike if/else.
# * Try/Catch for other programming languages.

to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_name = 'seconds'
unit_name1 = 'minutes'


def days_to_units (num_of_days):
    return f'{num_of_days} days are {num_of_days * to_seconds} {unit_name}.'
    
   
def validate_and_execute ():
    try:
        user_input_number = int(user_input) 
        if user_input_number >0:                                
            calculated_value = days_to_units(user_input_number)    
            print(calculated_value)
        elif user_input_number == 0: 
             print("You entered a 0, please enter a valid number.")
        else:
            print('You entered a negative number, please enter positive number.')

    except ValueError:
        print("You entered a wrong value, Dont ruin my program!")
    
user_input = input('Hey user, enter a number of days and i will convert it to hours.\n') 
validate_and_execute ()         

