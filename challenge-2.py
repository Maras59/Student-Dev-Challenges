import math


# These are solutions to challenge 2

# Function to reverse a given string
def reverse_str(string):
    # Convert the string to an array and get the length for tidiness
    str_array = list(string)
    length = len(str_array)

    # We only need to iterate through one half of the string since we are
    # basically "flipping" the string around a central pivot
    for i in range(0, math.floor(length / 2)):
        temp = str_array[i]                         # Store current value temporarily
        str_array[i] = str_array[length - (i + 1)]  # Swap the current value with the value on the other half
        str_array[length - (i + 1)] = temp
    reverse = ""                                    # Convert the array back into a string by using
    return reverse.join(str_array)                  # the join function on an empty string and return


# Calculates the factorial of a number recursively 
# Factorial function: n * (n - 1) until n equals 1, if n is zero, we just return 1
def factorial(x):
    if x == 1 or x == 0:             # Base case
        return 1
    else:
        return x * factorial(x - 1)  # Recursive call


# Function that calculates the nth number in the fibonacci sequence    
# The recursive method of calculating the fibonacci sequence is incredibly costly so im using an array
# we will not be including 0 in our sequence
def fib(n):
    # Create an array to hold calculated values
    # Zero is in the list to aid with calculations, but is not considered as part of the sequence when returning
    f = list()
    f.append(0), f.append(1)
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])   # Since each calculated each value is stored in an array
    return f[n]                         # there is no need to recalculate values like with the recursive method


# Function that returns the greatest of 3 numbers
# Run through each number and pick up the largest one as you go, returning at the end
def greatest_of_three(x, y, z):
    greatest = x
    if greatest < y:
        greatest = y
    if greatest < z:
        greatest = z
    return greatest
