def HowManyVowels(word:str) -> int:
    count = 0
    if len(word) == 0:
        return count 
    vowels = ['a','i','e','o','u']
    if word[0].lower() in vowels:
        count +=1
    return count + HowManyVowels(word[1:]) 
print(HowManyVowels("I love python"))

l = [1,2,3,4,5]
l2 = list(map(lambda lst:lst*2,l))
print(l)
print(l2)