# #List Slicing
# numbers = [10, 20, 30, 40]

# print(numbers[0:5])

# print(numbers[2:])

# print(numbers[:3])

# print(numbers[-2:])
# total = 0
# for num in range(len(numbers)):
#     total= total + numbers[num]
#       # Output each number in the list
# print("Total:", total)  # Output the total sum of the numbers

# largest = numbers[0]
# for num in range(len(numbers)):
#     if numbers[num] > largest:
#         largest = numbers[num]
# print("Largest number is:", largest)

numbers = [10, 15, 20, 25, 30]
even_number_total = 0
for num in range(len(numbers)):
    if numbers[num] % 2 == 0:
        even_number_total += numbers[num]

print("Total of even numbers:", even_number_total)  # Output the total sum of even numbers
        
        
        