# Ben Woolsey
# UWYO COSC 1010
# Submission Date 11/5/2024
# Lab 8
# Lab Section: 11
# Help given from Lab section TA for num_check on problem 1


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def num_check(string_to_check):
    """Checks to see if a string is a integer or a float"""
    returnValue = False
    try:
        returnValue = float(string_to_check)
        returnValue = int(string_to_check)
    except:
        pass
    return returnValue

print(num_check("4.2"))

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false


def int_check(number):
    """checks to see if a number is an integer"""
    try:
         return int(number)
    except:
        pass
    return False

def slope_intercept(m, b, lowX, highX):
    """"Returns all values of y for give x range"""
    if int_check(lowX) == False or int_check(highX) == False:
        return False
    else: 
        y = []
        for x in range(int(lowX),(int(highX)+1)):
            new_value = float(m) * x
            new_value = float(new_value) + float(b)
            y.append(new_value)
        print(y)

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

entry = input("Enter variables separated by commas, type 'exit' to quit")
while entry.lower() != "exit":
    entry = entry.split(",")
    if num_check(entry[0]) != False and num_check(entry[1]) != False and int_check(entry[2]) != False and int_check(entry[3]) != False:
        slope_intercept(entry[0],entry[1],int(entry[2]),int(entry[3]))
    else: 
        print("There was an error")
    entry = input("Enter variables separated by commas, type 'exit' to quit")
    

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def square_root(number):
    """Takes a square root"""
    half = float(number) / 2
    return half

def quadratic(a,b,c):
    """Finds the quadrtaric formula"""
    newB = float(b) - (2*float(b))
    inside = (float(b) ** 2) - (4 * (float(a) * float(c)))
    answer_one = newB + ((square_root(inside)) / (2 * (float(a))))
    answer_two = newB - (square_root(inside)) / (2 * (float(a)))
    print(answer_one)
    print(answer_two)

entry = input("Enter variables separated by commas, type 'exit' to quit")
while entry.lower() != "exit": 
    entry = entry.split(",")
    if num_check(entry[0]) != False and num_check(entry[1]) != False and num_check(entry[2]) != False:
        quadratic(entry[0],entry[1],entry[2])
    else:
        print("There was an error")
    entry = input("Enter variables separated by commas, type 'exit' to quit")