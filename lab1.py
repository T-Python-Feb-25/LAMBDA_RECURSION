def vowels(c):
    if not c:
        return 0
    first_char = c[0]
    if first_char in 'aeiouAEIOU':
        return 1 + vowels(c[1:])
    else:
        return vowels(c[1:])

word = "I love python"
print(vowels(word))