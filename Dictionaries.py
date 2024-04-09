# Dictionaries in python
# Dictionaries is used to represent key values

name = {
    'aditya' : 20,
    'rahul' : 21,
    'lakshya': 22
}

print(name.keys()) # If we forget the keys and we want to see the keys
print(name.values()) # This will return the values
print(name['aditya']) # to get the value of the particuler key

name['lakshya'] = 23
print(name['lakshya'])
