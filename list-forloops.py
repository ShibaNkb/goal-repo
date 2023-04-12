# * Lists gives manyy values that are run separately by the program.
# * Syntax fo lists is [], with diff data types that are comma separated['sir', 9 , 2.5, True]
# * User input is always a string
# * .split is a function that takes user input as a parameter and gives a list data type.



to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_name = 'seconds'
unit_name1 = 'minutes'


def days_to_units (num_of_days):
    return f'{num_of_days} days are {num_of_days * to_seconds} {unit_name}.'
    
   
def validate_and_execute ():
    try:
        user_input_number = int(num_of_days_element) # changed the paramater
        if user_input_number >0:                                
            calculated_value = days_to_units(user_input_number)    
            print(calculated_value)
        elif user_input_number == 0: 
             print("You entered a 0, please enter a valid number.")
        else:
            print('You entered a negative number, please enter positive number.')

    except ValueError:
        print("You entered a wrong value, Dont ruin my program!")


user_input = ""  
while user_input != "exit":   
    user_input = input('Hey user, enter a number of days that are comma separated and  i will convert it to hours.\n') 
    for num_of_days_element in user_input.split(','): # .split takes user input as parameter n gives list data type
        validate_and_execute ()  