#requirements - given an array of numbers, find a number that appears an odd number of times|

input = [1,1,1,2,2] 

# looks at all numbers, tells you know which one is in the list odd # of times
def find_number_of_odd_count (numbers):
    for num in numbers:

        num_count = get_count(num, numbers)

        if is_odd(num_count):
            return num

# returns true/false whether or not a number is odd
def is_odd (number):
    if number % 2 == 0:
        return false
    if number % 2 != 0:
        return true

# get the number of times a number is in a list
def get_count (needle, haystack):
    return

