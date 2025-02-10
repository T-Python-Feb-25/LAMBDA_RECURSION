#a function to count the number of vowels in a phrase
def count_vowels(phrase : str) -> int:
    vowles = ["a", "e", "i", "o", "u"]
    count = 0
# A loop to go through the phrase
    for i in phrase:
        if i.lower() in vowles or i.upper()in vowles:
            count += 1



    return (count)

print (count_vowels("I love python"))

print ("\n--------------- END OF (1) TASK-----------------\n")

#to cal the lambda function and store the value in a variable
multipications = lambda x: x*x

# to provide the number we would like to do the multipications on
list= [40,35, 10, 15, 20]

# A loop to go through all the numbers in the list then call the lambda function
for num in list:
    print(multipications(num), end ="   ")

print ()
'''
this is the first Python lab in the Course
Feb10, 2025
By Mohammed Albushaier
'''


