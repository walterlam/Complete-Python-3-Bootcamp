# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:52:46 2020

@author: walte
"""

# Q1
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Type error occured')
except:
    print('Error appeared')
else:
    print('No error')

# Q2
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('y cannot be zero')
except:
    print('Other errors')
else:
    print(z)
    print('no error')
finally:
    print('All done')
    
# Q3
def ask():
    '''
    ask for an integer input and print the square of it
    '''
    while True:
        try:
            result = int(input('Input an integer: '))
        except TypeError:
            print('Type error occured')
            continue
        except:
            print('Other errors')
        else:
            print('The square of your num: {}'.format(result**2))
            break