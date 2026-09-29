# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1

# for i in range(1, 6):
#     x =int(i*(i+1)/2)
#     print(x)

# num = 5
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# for row in range(1, 6):
#     for col in range(row):
#         print("*", end="")
#     print()  # Move to the next line after each row

# for row in range(1, 6):
#     for col in range(row):
#         print(row, end="")
#     print()  # Move to the next line after each row

for row in range(5, 0, -1):
    for col in range(row):
        print(row, end="")
    print()  # Move to the next line after each row
