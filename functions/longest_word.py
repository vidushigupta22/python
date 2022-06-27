
# waf to find the longest word in a given string passes as parameter 

def largest_word(a):

    b = a.split(' ')

    print(b)

    Word_len = 0

    for i in b:
        Each_len = len(i)
        if Each_len > Word_len:
            Word_len = Each_len
            st = i
    print('largest word,',st,'=',Word_len)
    
largest_word('idk man i am tired of all these things')