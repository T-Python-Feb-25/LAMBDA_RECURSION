def func_recursion(word):
    vowels ="aeiouAEIOU" 
    count =sum (1 for char in word if char in vowels)
    return count
while True: 
 word = input("enter word or y to exit: " )
 if word=="y":
    break
 else:
    print( word ,"the count of vowels is :",{func_recursion( word )})

 






