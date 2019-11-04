# Try Except, Learn Python - Full Course for Beginners [Tutorial]
# Catching error, Try-Except-Block

try:
    value = 10 / 0
    number = int(input("Enter a number : "))  # Int input
    print(number)
except ZeroDivisionError as err:  # Specify the error
    print(err)
except ValueError:  # If the input is not valid or other than int
    print("Invalid input")
