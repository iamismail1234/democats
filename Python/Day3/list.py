fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

print(fruits[0])  # Output: Apple

print(fruits)

fruits[1] = "Blueberry"  # Changing Banana to Blueberry
print(fruits)

print(fruits[-1])  # Output: Elderberry

fruits.remove("Date")  # Removing Date from the list
print(fruits)

fruits.append("Fig")  # Adding Fig to the end of the list
print(fruits)

for fr in fruits:
    print(fr)  # Output each fruit in the list

fruits.insert(2, "Cantaloupe")  # Inserting Cantaloupe at index 2
print(fruits)