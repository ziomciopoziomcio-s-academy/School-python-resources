# Importing libraries
import math

# Definition of variables
check = False

# Presentation of the programme guidelines
print("The program is designed to calculate the possible solutions to the quadratic equation")
print("The program accepts integers and decimals")
print("NOTE: Use a dot NOT a comma to enter a decimal number!")

# Function definition


def floatcheck(check):
    try:
        float(check)
    except ValueError:
        return False


# Get 'a' and checking is it a number
while check != True:
    a = input("Enter a: ")
    if a.isnumeric():
        a = int(a)
        check = True
    elif floatcheck(a) != False:
        a = float(a)
        check = True
    else:
        print("The specified value is incorrect")
check = False
# Get 'b' and checking is it a number
while check != True:
    b = input("Enter b: ")
    if b.isnumeric():
        b = int(b)
        check = True
    elif floatcheck(b) != False:
        b = float(b)
        check = True
    else:
        print("The specified value is incorrect")
check = False
# Get 'c' and checking is it a number
while check != True:
    c = input("Enter c: ")
    if c.isnumeric():
        c = int(c)
        check = True
    elif floatcheck(c) != False:
        c = float(c)
        check = True
    else:
        print("The specified value is incorrect")

if a == 0:  # Checking for a is 0
    print("The given function is a linear function")
else:
    delta = b ** 2 - (4 * a * c)
    print(delta)
    if delta < 0:  # Checking is the delta less than 0
        print("This quadratic equation has no solutions")
    elif delta == 0:  # Checking is delta equal to 0
        x = -b / (2 * a)
        print("x amounts to ", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("x1 amounts to ", x1, " a x2 amounts to ", x2)

# Close of the programme
input("Press ENTER to close the program")
