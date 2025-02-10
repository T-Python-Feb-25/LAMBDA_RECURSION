"""# LAB_RECURSION_LAMBDA


#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Note: use `map()` with a `lambda funciton`
"""
## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

def vowels_counter(text:str)->int:
    index=len(text)-1
    counter=0
    vowels=["a","e","i","o","u"]
    if index==-1:
        return 0
    if text[index].lower() in vowels:  
        counter =1
    return counter+ vowels_counter(text[:index]) 

print(f"the vowels number is :{vowels_counter("I love python")}")

## 2) Given a list of numbers : `[40,35, 10, 15, 20]`
numbers= [40,35,10,15,20]
new_list=list(map(lambda num:num*num,numbers))
print(new_list)
