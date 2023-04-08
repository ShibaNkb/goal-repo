'''Data types for Numbers
integers - normal numbers
floats (3.5, -1) '''

# string concantenation using f(format) and {}.
# creates variables to hold values that can be used, have clean code and avoid repeatation.
# Be descriptive in the names for variables
# Reserved words in py cant be used as variable names.

to_minutes = 20 * 24 * 60
to_seconds = 20 * 24 * 60 * 60
unit_name = 'seconds'


print(20 * 24 * 60)
print(f'20 days are {20 * 24 * 60} minutes.')
print(f'20 days are {to_seconds} {unit_name}.')
