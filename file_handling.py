
# file handling is used for storing values which you want to read whenever you want
# usually if you dont store data using files then toh jab hum run krenge tab data show krega par jese hi hum vs code band kr denge toh sara data gayb ho jayega jo bhi enter kiya hua hai

# file = open('geek.txt','a') # w stands for write , a is append--> it prevents overwriting of data
# file.write("This is the write command\n")
# file.write("It allows us to write in a particular file\n")
# file.close()


# file = open('geek.txt', 'r')
# # This will print every line one by one in the file
# for line in file:
#   print (line)

with open('geek.txt','a') as file:
    # now you dont have to close alag se as indentation does that automatically
    file.write('ye ladka pagal hai')