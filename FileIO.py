# File IO - input output

# how to write in a file
file1 = open("sample.txt" , "wb") # wb - write mode
print(file1.mode)
print(file1.name)
file1.write(bytes("Hey there this is aditya pawar" , "UTF-8"))
file1.close()

# how to read in a file
file2 = open("sample.txt" , "r+")
text_to_read = file2.read()
print(text_to_read)
