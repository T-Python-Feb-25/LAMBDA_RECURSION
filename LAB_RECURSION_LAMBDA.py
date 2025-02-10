#Task 1

def count_vowels(s:str) -> int:
    if not s:
        return 0
    return (s[0] in "aeiouAEIOU") + count_vowels(s[1:])

print(count_vowels("I love python"))

        





#Task 2

numbers = [40, 35, 10, 15, 20]

l = list(map(lambda x: x**2, numbers))

print(l)
