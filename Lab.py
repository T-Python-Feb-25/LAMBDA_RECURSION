print("\nThe first Question")
def recursion_vowels(phrase):
    try:
        if not phrase:  
            return ""
        first_char = phrase[0]
        vowels = "aeiouAEIOU"
        if first_char in vowels:
            return first_char + recursion_vowels(phrase[1:])
        else:
            return recursion_vowels(phrase[1:])
    except IndexError:
        print("The first index is empty")  
    except Exception as e:
        print(e)        
 

print(len(recursion_vowels("I love python")))
print(recursion_vowels("I love python"))

#2
print("\nThe second Question")
numbers=[40,35, 10, 15, 20]
mutliplied=map(lambda x:x*x , numbers)
print(list(mutliplied))
print("")

# mutliplied2=map(lambda x:x**2 , numbers)
# print(list(mutliplied2))


