# #a dictionary store data in key value pairs

# cricket_players = {
#     "name": "Virat Kohli",
#     "age": 34,
#     "team": "India"}

# print(cricket_players["name"])

# cricket_players["age"] = 37

# print(cricket_players["age"])

# cricket_players["role"] = "Batsman"

# print(cricket_players["role"])

# #print the count of the keys
# count = 0
# for key in cricket_players:
#     print(cricket_players[key])
#     count += 1

# print("Total number of keys in the dictionary:", count)

# print(cricket_players.get("name"))

# #find the key retired from the dictionary
# found = False
# if "retired" in cricket_players:
#     print(found)
# else:
#     print(found)

# Sum Ages

# employees = [
#     {"name" : "Ismail", "age":25},
#     {"name" : "John", "age":30},
#     {"name" : "David", "age":35}     
# ]

# sum = 0

# for employee in employees:
#    sum = sum + employee["age"]

# print(sum)
employees = [
    {"name" : "Ismail", "age":25},
    {"name" : "John", "age":30},
    {"name" : "David", "age":35}     
]

# oldest_employee = employees[0]

# for employee in employees:
#    if employee["age"] > oldest_employee["age"]:
#       oldest_employee = employee

# print(oldest_employee["name"])

for employee in employees:
    if employee["name"][0] == "D":
        print(employee["name"])
   