def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:  
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])


phrase = "I love python"
print(count_vowels(phrase))


numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda x: x * x, numbers))  
print(squared_numbers)  