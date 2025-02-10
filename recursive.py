# I love python

def vowelsNumber(phrase):
    if not phrase:
        return 0
    if phrase[0].lower() in "aeiou":
        return 1 + vowelsNumber(phrase[1:])
    if phrase[0].lower() not in "aeiou":
        return 0 + vowelsNumber(phrase[1:])
    
    
    
    
print(vowelsNumber("I love python"))




