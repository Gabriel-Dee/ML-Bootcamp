# Assumptions: file myUtilities.py exists in the folder 
# where we have this notebook. Also correct arguments are passed 
# to functions

import myUtilities  # do not include extension .py

print(f'Sum of 5 and 7 is: {myUtilities.addTwoNumbers(5, 7)}')
print(f'2 power 4 is: {myUtilities.power(2, 4)}')
print(f'Is 5 an odd number? {myUtilities.isOdd(5)}')
print(f'Is 6 an odd number? {myUtilities.isOdd(6)}')

print('\nAccess variables')
print(f'Value of x is {myUtilities.x}')
print(f'Value of variable countries is:\n {myUtilities.countries}')
