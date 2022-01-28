# Declaration of variable values
x = float(0)
position = 1
list = []

# Function definition


def floatcheck(x):
    try:
        float(x)
    except ValueError:
        return False


# Presentation of the programme guidelines
print("The program sorts the numbers entered by the user")
print("The program accepts integers and decimals")
print("NOTE: Use a dot NOT a comma to enter a decimal number!")
print("To stop entering numbers, enter any value other than a whole number or decimal point")

# Inserting values into a list
while type(x) == float or type(x) == int:
    print("Give the number ", position, ":")
    x = input()
    if x.isnumeric():
        x = int(x)
        list.append(x)
    elif floatcheck(x) != False:
        x = float(x)
        list.append(x)
    position = position + 1

# Sorting list and returning results
list.sort()
print(list)

# Close of the programme
input("Press ENTER to close the program")
