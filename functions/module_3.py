

import os
if not os.path.exists('data analysis'):  # it will check if the folder exists and if not then it will create a folder
    os.mkdir('data analysis') # a folder will be created
    
print('the current location')
print(os.getcwd()) # to check the current location you are working in

print(" the current directory content")
content = os.listdir()  # it will reveal all the files been created up till now even the hidden ones
print(content)

if os.path.isdir('data analysis'):
    print('data analysis is a directory')
    
if os.path.isfile('basics.ipynb'):
    print('basics.ipynb is a file')
    
print('size of pic',os.path.getsize('list.ipynb')//1024,'KB')   # it will tell the size of the file and one can convert it too into kb,bytes,mb,gb etc