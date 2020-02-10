# 02 Statements Test

'''
Q1:
Use for, .split(), and if to create a Statement that will 
print out words that start with 's':
'''

st = 'Print only the words that start with s in this sentence'
list1 = st.split()
for word in list1:
    if word[0] == 's':
        print(word)

'''
Q2:
Use range() to print all the even numbers from 0 to 10.
'''

for i in range(0,11):
    if i%2 == 0:
        print(i)

'''
Q3:
Use a List Comprehension to create a list of all numbers
between 1 and 50 that are divisible by 3.
'''
list2 = [num for num in range(1,51) if num%3 == 0]
print(list2)

'''
Q4:
Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
'''
st = 'Print every word in this sentence that has an even number of letters'
list3 = st.split()
for word in list3:
    if len(word)%2 == 0:
        print("even")

'''
Q5:

Write a program that prints the integers from 1 to 100. But for multiples of 
three print "Fizz" instead of the number, and for the multiples of five print 
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
'''
for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

'''
Q6:

Use a List Comprehension to create a list of the first letters of 
every word in the string below:
'''

st = 'Create a list of the first letters of every word in this string'
list4 = [word[0] for word in st.split()]
print(list4)
