"""
kody Crane
3/1/22
Q5
"""

string_Original = "this is the srting for the class"

#Part 1
string_1 = ""
capital_Next = True

for character in string_Original:
    if(capital_Next):
        string_1 += character.upper()
        capital_Next = False
    else:
        string_1 += character
        
    if(character == " "):
        capital_Next = True
print(string_1)
    

#Part 2
string_2 = ""
capital_Next = True

for character in string_Original:
    if(capital_Next):
        string_2 += character.upper()
        capital_Next = False
    elif(character == " "):
        capital_Next = True
    else:
        string_2 += character
    
print(string_2)
    
    
#Part 3
string_3 = ""
capital_Next = True
for character in string_Original:
    if(character.upper() == "S"):
        string_3 += "$"
        capital_Next = False
    elif(capital_Next):
        string_3 += character.upper()
        capital_Next = False
    else:
        string_3 += character
    
    if(character == " "):
        capital_Next = True
    
print(string_3)
    

#Part 4
string_4 = ""
temp_String = ""
string_Original+=" "
for character in string_Original:
    if(not(character.isspace())):
        temp_String+=character
    else:
        if(len(temp_String)>=4):
            string_4 += temp_String.capitalize() + " "
            temp_String = ""
        else:
            string_4 += temp_String + " "
            temp_String = ""
            
print(string_4)
