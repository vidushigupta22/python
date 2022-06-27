# waf to count all the words, lines and characters in a given string passes as a parameter

def count_words(st):
    
  a = st.split(' ')
  print('total words =', len(a)) #length of words

  b = ''
  rep = st.replace(' ',"")
  print(rep)

  for i in rep:
        b = b+i
  print('total characters = ', len(b)) # length of characters 
  
count_words('there is a bird on a tree')