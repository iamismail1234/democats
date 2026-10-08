class Cricket:

    def __init__(self, name):
        self.name = name

    def team(self):
        print("India", self.name)

cri1 = Cricket("Ismail")

cri1.team()

#Class is a blue print of house
#Object is real house
#_init_ : used to initialize an object when its created
#self current object
#Attributes name and team , data stored inside the object
#Method is function inside a class
#Method calling: object.method()

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def disply(self):
#         print("Name : ", self.name)
#         print("Age: ", self.age)

# s1 = Student("Rahul", 20)
# s1.disply()

class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(self.brand)

c1 = Car("Audi")
c1.show_brand()

class BankAccount:
    def __init__(self, balance):
        self.balance=balance

    def deposit(self, amount):
        self.amount = amount

    def show_balance(self):
        print(self.balance+self.amount)

acc = BankAccount(1000)

acc.deposit(500)

acc.show_balance()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)


e1 = Employee("Ismail", 20000)
e2 = Employee("Usman", 10000)
e1.show() 
e2.show()   

class Calculator:
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1+self.num2)

    def sub(self):
        print(self.num1-self.num2)

cal1 = Calculator(10,8)
cal1.add()
cal1.sub()

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says Woof!")

d1 = Dog("Tommy")
d1.bark()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_result(self):
        if self.marks >= 40:
            print(self.name, ": Pass")
        else:
            print("Fail")

s1 = Student("Rahul", 45)
s1.show_result()

#Area of traingle

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.widht = width

    def area1(self):
        area_rc = self.lenght * self.widht
        print("Area : ",area_rc)

r1 = Rectangle(10,20)
r1.area1()


        




    

    
        

