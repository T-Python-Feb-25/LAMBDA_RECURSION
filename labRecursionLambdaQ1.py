word=input ("enter a word") 

def find_vowels(word):
    vowels="aeiouAEIOU"
    if not word:
        return 0
    
    if word[0] in vowels:
        return 1 +find_vowels(word[1:])
    else:
        return find_vowels(word[1:])

print(find_vowels(word))