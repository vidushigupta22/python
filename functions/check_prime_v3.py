

def check_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return 'non prime'
    else:
        return 'prime'
    
#  print(check_prime(13))
 
for i in range(2,100):
     out = check_prime(i)
     print(i,out)