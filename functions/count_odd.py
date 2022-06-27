# waf to add and display all the odd numbers from start and end values given as parameters 
#use range function to generate list of no.

 1.
def check_odd(m,n):
  a = list(range(m,n))

  for i in a:
        if i % 2 != 0:
              print(i , 'is a odd number')
              
check_odd(30,40)