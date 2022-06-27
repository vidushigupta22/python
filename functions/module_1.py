

import random

for i in range(10):
    print(random.random()) # provides values b/w 0 to 1
    
for i in range(10):
    print(random.randint(1,105),end = ' ')
    
simileys = ['😀','😋','🤗','🤩']
print(random.choice(simileys))

print(random.choices(simileys,k = 3)) # chooses multiple values randomly



