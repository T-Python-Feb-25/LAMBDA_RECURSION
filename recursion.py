
def count_vowels(phrase, index = 0):
    vowels = "aeiou"

    if index == len(phrase):
        return 0
    
    return (1 if phrase[index].lower() in vowels else 0) + count_vowels(phrase, index + 1)
    

phrase = "I love python"    
result = count_vowels(phrase)

print(result)
