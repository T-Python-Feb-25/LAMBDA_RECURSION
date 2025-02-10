def countvowels(phrase:str):
    s=phrase.lower()
    if len(s) == 0:
        return 0
    elif s[0] in "aeiou":
        return 1+ countvowels(s[1:])
    else:
        return countvowels(s[1:])




r='I love python'
print(f"there is {countvowels(r)} vowels in '{r}'")

