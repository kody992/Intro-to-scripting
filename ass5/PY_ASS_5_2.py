"""
kody crane
3/1/22
Q2
"""

user_String = input("enter a string to count vowels and consonants ")

vowel_Count = 0
consonant_Count = 0

for character in user_String.upper():
    if(character.isalpha()):
        if(character == "A" or character == "E" or character == "I" or character == "O" or character == "U"):
            vowel_Count += 1
        else:
            consonant_Count += 1
            
print("In the sting there were: \nVowels: ", vowel_Count, "\nConsonants: ", consonant_Count)