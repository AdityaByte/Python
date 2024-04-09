# List in python - list is the collection of different datatype

colleges = [
    'NRI COLLEGE',
    'ORIENTAL COLLEGE',
    'LNCT COLLEGE',
    'TIT COLLEGE',
    'MANIT NIT'
]

print(colleges[0])
colleges[4] = "TRINITY COLLEGE"
print(colleges)
print(colleges[1:3]) # it gives the element inside the index

colleges.append("JNCT COLLEGE") # add a element at the last index
print(colleges)

list1 = [
    'table',
    'chair',
    'microphone',
    'zener diode'
]

list1.insert(3 , 'photo diode') # by this we can add an element to a list at a particular index
print(list1)
list1.remove('photo diode') # by this we can remove a method
print(list1)
print(list1 + ['pillow' , 'tubelight' , 'gas tube'])
print(list1)
print(len(list1)) # length of list -return
print(max(list1)) # last in dictionary
print(min(list1)) # first in dictionary
