# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    return n%2==0

print(is_even(3))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

print('Even!' if num%2==0 else 'Odd')