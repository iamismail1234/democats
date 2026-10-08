try:
    num = 100 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    num = int("abc")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


try:
    print("A")
    num = 100 / 0
    print("B")
except ZeroDivisionError:
    print("Cannot divide by zero")

print("C")


#finally block is used to execute code regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
#else block is used to specify code that should be executed if no exceptions were raised in the try block. It is often used to perform actions that should only occur when the try block succeeds without errors.

try:
    print("A")

    result = 10 / 0 

except ZeroDivisionError:
    print("B")

else:
    print("C")

finally:
    print("D")

print("E")