def test():
    print("hey")

test()

def tester(name):
    print("hello", name)

tester("John")

def add(a, b):
    print(a+b)

add(5, 10)

def welcome():
    print("Welcome to the function tutorial!")

for i in range(3):
    welcome()

def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)

def evenorodd(num):
    if num %2 ==0:
        return "Even"
    else:
        return "Odd"

even_odd_result = evenorodd(100)
print(even_odd_result)
