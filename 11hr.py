# try-except block, handling different types of exceptions
try:
    number = int(input("Enter a number: "))
    print(10/number)
except ZeroDivisionError:
    print("Not divisible by Zero!")
except ValueError:
    print("Invalid Input!")

try:
    num = int(input("Enter a number: "))  # This can raise ValueError
    result = 100 / num                      # This can raise ZeroDivisionError
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result is {result}")


try:
    num = int(input("Enter a number: "))  # May raise ValueError
    result = 100 / num                      # May raise ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")


try:
    num = int(input("Enter a number: "))  # May raise ValueError
    result = 100 / num                      # May raise ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")  # Executes if no exceptions occurred
finally:
    print("This will always execute.")

# No, `try` and `except` blocks in Python are not limited to handling just numbers.
# They can be used to catch and handle any type of exception that may occur in your code, including:

# - Value errors (e.g., trying to convert a string to an integer)
# - Index errors (e.g., accessing an out-of-bounds index in a list)
# - Key errors (e.g., accessing a nonexistent key in a dictionary)
# - File-related errors (e.g., attempting to open a file that doesn't exist)
# - Type errors and many others.

# You can customize your exception handling to catch specific exceptions
# or a general exception if you want to handle multiple types of errors. Here’s a simple example:
try:
    # Code that may cause an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# In this example, the `try` block is used to handle 
# input and division, and different `except` blocks catch various potential errors.