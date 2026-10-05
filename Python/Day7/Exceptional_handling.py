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

