# String in python - in python string is treat as an object
# string is generally an array or characters or you can say that it is a list of characters

String1 = "aditya pawar"
String2 = '''
Multi line string
'''
print(String1[1:3]) # starts from 1st index and go to the previous value of 3 index
print(String1[-2:]) # returns - ar
print(String1[:-2]) # returns - aditya paw
print(String1.capitalize()) # returns - Aditya pawar
print(String1.find('y')) # returns the index -4
print(String1.find('ntg')) # returns -1 not found
print(String1.replace('aditya' , 'adi')) # returns - adi pawar Note - all instances are replaced to the new string
