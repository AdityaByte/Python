# Tuples in python
'''
In a list in python we can change an element but if we want to not to change the element we use tuples
'''

tup1 = (1,2,3)
# tup[0] = 6 this throws an error
print(tup1[0] , tup1 , type(tup1) , sep="  ||  ")

# converting a tuple into a list
list1 = list(tup1)
print(list1)
