def count_vowels(text:str)->int:
    '''this function return how many vowels in word or phrase in txet no matter if it is lower case or uppercase
       args:
            text(str):this the text that will be count how many vowels in
       return
            int:it will be return the count of vowels in pharse or or word in intger          '''
    vowels='aeiou'
    if text=="":
        return 0
    else:
        return 1+count_vowels(text[1:]) if text[0].lower() in vowels else 0+count_vowels(text[1:])
print(count_vowels("I Love python"))
list_of_numbers=[40,35, 10, 15, 20]
new_list=list(map(lambda num:num*num,list_of_numbers))
print(new_list)