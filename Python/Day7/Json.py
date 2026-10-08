#JavaScript Object Notation

import json

#standard fomat to store data and exchange data

# {
#     name: "John",
#     age: 30,
#     city: "New York"
# }

#dictionary is stored as object in python
#json is stored as string/text in python

employee = {
    "name": "John",
    "age": 30
}

result = json.dumps(employee) #convert dictionary to json string
print(result)

student = '{"name": "Ismail", "age": 25}' #json string
output = json.loads(student) #convert json string to dictionary
print(output)