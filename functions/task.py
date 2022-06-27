# waf to add and display all the odd numbers from start and end values given as parameters 
#use range function to generate list of no.s
  
# waf to count all the words, lines and characters in a given string passes as a parameter

# waf to find the longest word in a given string passes as parameter 

#  1.
# def check_odd(m,n):
#   a = list(range(m,n))

#   for i in a:
#         if i % 2 != 0:
#               print(i , 'is a odd number')
              
# check_odd(30,40)

#  2.


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

      





