
# program that calculate hypotenuse

# functions are defined by def keyword
# and then we can use these defined function by calling them
# function manages error
#they are more readable

def hypotenuse():
    p = float(input('enter the length of first side'))

    b = float(input('enter the length of second side'))

    h = (p**2 + b**2)**0.5

    print('perpendicular', p)
    print('base', b)
    print('hypotenuse', h)



#calling
hypotenuse()