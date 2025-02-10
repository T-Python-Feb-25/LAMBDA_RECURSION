








def countrec(phrase):
    phrase = phrase.lower()
    vowels = "aeiou"
    if not phrase:
        return 0
    if phrase[0] in vowels:
        return 1 + countrec(phrase[1:])
    else:
        return countrec(phrase[1:])

phrase = "I love Python"
print(countrec(phrase))





numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

