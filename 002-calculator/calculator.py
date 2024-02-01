from sum import sum
from subtraction import subtraction
from multiplication import multiplication
from division import division

while True:
    print("Welcome to calculator")

    # Get user input about what they want
    possibleOptions = ["sum", "sub", "mult", "div"]
    option = ""
    while option not in possibleOptions:
        option = input("Choose an option: sum, sub, mult, div: ").lower()
        if option not in possibleOptions:
            print("Invalid option, try again")

    # Get user input about the numbers to be used
    nums = []
    inputNum = 0.0
    while isinstance(inputNum, float):
        inputNum = input("Enter a number: (or 'q' to quit) ")
        try:
            inputNum = float(inputNum)
            nums.append(inputNum)
        except ValueError:
            break

    print("You chose: " + option)
    print("Numbers entered: " + str(nums))
    print("Result: ")
    if option == "sum":
        print(sum(nums))
    elif option == "sub":
        print(subtraction(nums))
    elif option == "mult":
        print(multiplication(nums))
    elif option == "div":
        print(division(nums))
