
a = [2,3,1,3,5,6,7,8,9,5]
num = 10 # now we want to add 10 in all the itmes present in list

# we will use map function in lambda and then convert it into the list --> we cam do this in one line instead of loop

h = list(map(lambda i : i + num, a)) # so from a , values will be retrieve one by one and will get store in i and upon i , num will added

print(h)

# add two list

a = [1,2,3,4,5]
b = [6,7,8,9,10]

c = list(map(lambda x,y : x + y, a,b))
print(c)


# now filter function in lambda retrieves the values as per the condition 

x = [2,3,3,3,3,3,2,2,4,4,3] # here we want to retrieve only 3
x = list(filter(lambda i : i == 3, x))

print(x)

# now wap to get the numbers from 1 to 1001 divisble by both 3 and 5 

x = list(range(1,1001))

x35 = list(filter(lambda h : h % 3 ==0 and h % 5 ==0, x))
print(x35)