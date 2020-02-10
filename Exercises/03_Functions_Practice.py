def lesser_of_two_evens(a,b):
    '''
    returns the lesser of two given numbers if both numbers are even, but 
    returns the greater if one or both numbers are odd
    
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5
    '''
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

def animal_crackers(text):
    '''
    takes a two-word string and returns True if both words begin with 
    same letter
    
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
    '''
    ls = text.split()
    return ls[0][0].upper() == ls[1][0].upper()


def makes_twenty(n1, n2):
    '''
    Given two integers, return True if the sum of the integers is 20 or 
    if one of the integers is 20. If not, return False
    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False
    '''
    return n1+n2 == 20 or n1 == 20 or n2 == 20

def old_macdonald(name):
    '''
    Write a function that capitalizes the first and fourth letters of a name
    old_macdonald('macdonald') --> MacDonald
    '''
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

def master_yoda(text):
    '''
    Given a sentence, return a sentence with the words reversed
    
    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'
    '''
    ls = text.split()
    ls = ls[::-1]
    return ' '.join(ls)
    
def almost_there(n):
    '''
    Given an integer n, return True if n is within 10 of either 100 or 200
    
    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    '''
    return abs(n-100) <= 10 or abs(n-200) <= 10

def has_33(nums):
    '''
    Given a list of ints, return True if the array contains 
    a 3 next to a 3 somewhere.
    
    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
    '''
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def paper_doll(text):
    '''
    Given a string, return a string where for every character in the original 
    there are three characters
    
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
    '''
    new = ''
    for char in text:
        new += char*3
    return new

def blackjack(a,b,c):
    '''
    Given three integers between 1 and 11, if their sum is less than or equal 
    to 21, return their sum. If their sum exceeds 21 and there's an eleven, 
    reduce the total sum by 10. Finally, if the sum (even after adjustment) 
    exceeds 21, return 'BUST'
    
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
    '''
    total = sum((a,b,c))
    if total > 21 and 11 in (a,b,c):
        total -= 10
    if total <=21:
        return total
    else:
        return 'BUST'

def summer_69(arr):
    '''
    Return the sum of the numbers in the array, except ignore sections of 
    numbers starting with a 6 and extending to the next 9 (every 6 will be 
    followed by at least one 9). Return 0 for no numbers.
    
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14
    '''
    sum = 0
    i = 0
    while i < len(arr):
        if arr[i] == 6:
            while arr[i] != 9:
                i+=1
            i+=1
        else:
            sum += arr[i]
            i += 1
    return sum

def spy_game(nums):
    '''
    Write a function that takes in a list of integers and returns 
    True if it contains 007 in order
    
    spy_game([1,2,4,0,0,7,5]) --> True
    spy_game([1,0,2,4,0,5,7]) --> True
    spy_game([1,7,2,0,4,5,0]) --> False
    '''
    a = first_0(nums)
    b = second_0(nums, a)
    c = third_7(nums, b)
    
    if len(nums) not in (a,b,c):
        return True
    return False

def first_0(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            return i
        i += 1
    return len(nums) # a number large enough if not found

def second_0(nums, i):
    i += 1
    while i < len(nums):
        if nums[i] == 0:
            return i
        i += 1
    return len(nums)

def third_7(nums, i):
    i += 1
    while i < len(nums):
        if nums[i] == 7:
            return i
        i += 1
    return len(nums)






def count_primes(num):
    '''
    Return the number of primes that exist up to and including a given num
    
    count_primes(100) --> 25
    Note that 0 and 1 are not prime
    '''
    num_of_prime = 0
    i = 1
    while i <= num:
        if prime(i):
            num_of_prime += 1
        i += 1
    return num_of_prime        

def prime(num):
    '''
    Return True if prime, False if not prime
    '''
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3,num//2+1,2):
        if num % i == 0:
            return False
    return True
