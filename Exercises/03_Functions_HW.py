import math
def vol(rad):
    '''
    computes the volume of a sphere given its radius
    '''
    return 4/3 * math.pi * (rad)**3

def ran_check(num, low, high):
    '''
    Write a function that checks whether a number is in a 
    given range (inclusive of high and low)
    '''
    return low <= num <= high

def up_low(s):
    '''
    Write a Python function that accepts a string and calculates the 
    number of upper case letters and lower case letters.
    '''
    count_upper = 0
    count_lower = 0
    for char in s:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        else:
            pass
    print('No. of Upper case characters: {}'.format(count_upper))
    print('No. of Lower case characters: {}'.format(count_lower))

def unique_list(lst):
    '''
    Write a Python function that takes a list and returns a new list with 
    unique elements of the first list.
    
    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
    '''
    return list(set(lst))

def multiply(numbers):
    '''
    Write a Python function to multiply all the numbers in a list.
    
    Sample List : [1, 2, 3, -4]
    Expected Output : -24
    '''
    result = 1
    for num in numbers:
        result *= num
    return result

def palindrome(s):
    '''
    Write a Python function that checks whether a passed in string 
    is palindrome or not.
    
    Note: A palindrome is word, phrase, or sequence that reads the same 
    backward as forward, e.g., madam or nurses run.
    '''
    new_s = ''.join(s.split())
    return new_s == new_s[::-1]

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    '''
    Write a Python function to check whether a string is pangram or not.
    
    Note : Pangrams are words or sentences containing every letter of the 
    alphabet at least once.
    
    For example : "The quick brown fox jumps over the lazy dog"
    
    string.ascii_lowercase = 'abc...xyz'
    '''
    s = ''
    for char in str1:
        if char.isalpha():
            s += char.lower()
    return set(s) == set(alphabet)

    
