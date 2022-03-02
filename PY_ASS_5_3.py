"""
kody crane
3/1/22
Q3
"""


#part 1

#user_String = input("enter a string to count letters numbers and symbols: ")
user_String = "P@#yn26at^&i5ve"
alph_Count = 0
number_Count = 0
symbol_Count = 0

for character in user_String:
    if(character.isalpha()):
        alph_Count += 1
    elif(character.isnumeric()):
        number_Count += 1
    elif(not(character.isspace())):
        symbol_Count += 1


print("In the sting there were: \nLetters: ", alph_Count, "\nnumbers: ", number_Count, "\nsymbols: ", symbol_Count)


#part 2
#user_String = input("enter a string to remove symbols: ")
user_String = "/*Jon is @developer & musician"

no_Symbol_String = ""

for character in user_String:
    if(character.isalpha() or character.isnumeric() or character.isspace()):
        no_Symbol_String += character
        
print("string with no special symbols\n",no_Symbol_String)


#part 3

#user_String = input("enter a string to replace '-' with a space: ")

user_String = "Emma-is-a-data-scientist"

no_Hyphen_String = ""

for character in user_String:
    if(character == "-"):
        no_Hyphen_String += " "
    else:
        no_Hyphen_String += character

print("New String ", no_Hyphen_String)


#part 4

#user_String = input("enter a string to remove all consonants: ")

user_String = "Hello, have a good day"

consonant_Removed_String = ""

for character in user_String:
    if(character.isalpha()):
        if(character.upper() == "A" or character.upper() == "E" or character.upper() == "I" or character.upper() == "O" or character.upper() == "U"):
            consonant_Removed_String += character
    else:
        consonant_Removed_String += character
        
print("New String ", consonant_Removed_String)

