# 1 function takes a word and returns a number of vowels
def HowManyVowels(word:str) -> int:
    count = 0
    if len(word) == 0:
        return count 
    vowels = ['a','i','e','o','u']
    if word[0].lower() in vowels:
        count +=1
    return count + HowManyVowels(word[1:]) 

#test the function
while(True):
    phrase = input("Enter a phrase (0 to exit): ")
    if phrase == '0':break
    print(f"'{phrase}' continains {HowManyVowels(phrase)} vowels. ")


# 2 create new multipled list 
numbers = [40,35, 10, 15, 20]
multiplied_list = list(map(lambda lst:lst*lst,numbers))
print(f"original list is : {numbers}")
print(f"muliplied by itself : {multiplied_list}")