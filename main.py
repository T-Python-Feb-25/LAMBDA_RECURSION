"""
LAB_RECURSION_LAMBDA
1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .
Example: given the phrase I love python , it should return : 4
2) Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number from the previous list mutliplied by itself.
print the new list.
Note: use map() with a lambda funciton

"""
def count_vowels(string):
  if not  string:
    return 0
  if string[0].lower() in  'a,e,i,o,u':
    return 1 + count_vowels(string[1:])
  else:
    return count_vowels(string[1:])

phrase = 'I love python'
print(count_vowels(phrase)) 

numbers = [40,35, 10, 15, 20]
result = list(map(lambda x: x * x, numbers))
print(result)