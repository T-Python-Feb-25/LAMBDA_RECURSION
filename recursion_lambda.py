

def vowels(word):
    if not word:
        return 0
    if word[0] in 'aeiouAEIOU': #to make sure it takes lowercase and uppercase
        return 1 + vowels(word[1:])
    else:
        return vowels(word[1:])

word = "I love python"
print(vowels(word))



multiplication = lambda x: x * x

numbers:int = [40, 35, 10, 15, 20]
result:list = list(map(multiplication, numbers))
print(list(result))