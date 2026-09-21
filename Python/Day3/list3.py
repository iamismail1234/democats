# numbers = [10,20,30,40]
# correct_number = 30

# for num in numbers:
#     if num == correct_number:
#         print("Found the correct number:", num)
#         break

#find the count of numbers greater than 20 in the list
# numbers = [10,25,30,15,40]
# count = 0

# for num in numbers:
#     if num > 20:
#         count += 1

# print(count)

#find the largest odd number in the list
# numbers = [10,15,20,25,30,35]
# largest_odd_number = numbers[0]

# for num in numbers:
#     if not num % 2 == 0:
#         if num > largest_odd_number:
#             largest_odd_number = num

# print(largest_odd_number)

#find the average of the numbers in the list
# numbers = [10,20,30,40]
# total = 0

# for num in numbers:
#     total += num

# average = total / len(numbers)
# print(average)

numbers = [10,20,30,40]
largest_number = numbers[0]
second_largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num
    numbers.remove(largest_number)
    if num > second_largest_number:
        second_largest_number = num


print("Second largest number:", second_largest_number)

