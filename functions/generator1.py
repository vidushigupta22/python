
def get_cube(*args):
    for i in args:
        yield i**3  #so here yield stores the value in the memory which can be retrieved using loop and not by calling the function simply
        
for i in get_cube(1,5,87):
    print(i)
    
    
def acronym_generator(listofword):
    for word in listofword:
        wl = word.split()
        acr = ''
        for w in wl:
            acr = acr+w[0].upper()
        yield acr #here again it is storing one by one in the memory
        
words = ['Project Manager','Software Engineer', 'Database Administrator']
for acr in acronym_generator(words):
    print(acr)