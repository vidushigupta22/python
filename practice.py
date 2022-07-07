from asyncore import write


with open ('food_data.txt','a') as file: # create a file using with function
    file.write('this is a csv file')
    
file = open('food_data.txt','r') # read a file using loop
for i in file:
    print(i)
   