#######################################################################
# $ python3 functions_practice.py
#
# Expected Output:
#
# Hello Don Waldoch!
#
# ['Item1', 'Number2', 'Carrot']
#
# First I eat an apple.
# Next I eat a sandwich.
# Next I eat a twinkie.
# My lunchbox is empty!
#
# My lunchbox is empty!
#
#######################################################################

# A function named hello() that prints a greeting to the user.
# This function should accept no arguments and returns nothing.
def hello():
    print("\nHello Don Waldoch!\n")

# A function named pack() that accepts three arguments,and returns
# a single list with the three arguments inside as list elements.
def pack(a, b, c):
    return [a, b, c]

# A function called eat_lunch(). This function should accept a list
# of any length, and print out a series of strings that say
# "First I eat __" (the first element of the list), and "Next I eat ___"
# (for the following elements in the list). If the list is empty,
# print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(lunch_list):
    preface = "\nFirst I eat"
    for i in lunch_list:
        print(f"{preface} {i}.")
        preface = "Next I eat"
    print("My lunchbox is empty!\n")

# Test each function:
hello()
print(pack("Item1", "Number2", "Carrot"))
eat_lunch(["an apple", "a sandwich", "a twinkie"])
eat_lunch([])
