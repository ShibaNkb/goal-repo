# * Validate what users enter in our programs to avoid crushing them or could be a security risk.
# * Conditionals can be true or false - Boolean Data types.
# * is.digit function filters out all values that are text, negatives, floats and etc

to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_name = 'seconds'
unit_name1 = 'minutes'


def days_to_units (num_of_days):
    return f'{num_of_days} days are {num_of_days * to_seconds} {unit_name}.'
    
   
def validate_and_execute ():
    if user_input.isdigit():    # .isdigit is calling a function to check that digits entered are valid.
        user_input_number = int(user_input) 
        if user_input_number >0:                                # NESTED IF/ELSE
            calculated_value = days_to_units(user_input_number)    
            print(calculated_value)
        elif user_input_number == 0: 
             print("You entered a 0, please enter a valid number.")

    else:
        print("You entered a wrong value, Dont ruin my program!")
    
user_input = input('Hey user, enter a number of days and i will convert it to hours.\n') 
validate_and_execute ()         # call the function

