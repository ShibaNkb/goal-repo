# * While loops keep the program running and accepting values.
# * Loops execute the same logic multiple times, hiw many times is stated in the condition of the loop.
# * Python has 2 loops commands; While & For loops.
# * Change conditions from True inorder to exit program.


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


'''while True:
    user_input = input('Hey user, enter a number of days and i will convert it to hours.\n') 
    validate_and_execute ()'''       

user_input = ""  # create a variable that a while loop 1st runs.
while user_input != "exit":   # a condition that will run until user types the exit.
    user_input = input('Hey user, enter a number of days and i will convert it to hours.\n') 
    validate_and_execute ()  