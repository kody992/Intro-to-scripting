"""
Kody Crane
3/1/22
Q1
"""

user_String = input("enter a string to be converted into morse code ")

morse_Code_String = ""

morse_Code_Conversion = {" ": " ",
                        ",": "--..-",
                        ".": ".-.-.-",
                        "?": "..--..",
                        "0": "-----",
                        "1": ".----",
                        "2": "..---",
                        "3": "...--",
                        "4": "....-",
                        "5": ".....",
                        "6": "-....",
                        "7": "--...",
                        "8": "---..",
                        "9": "----.",
                        "A": ".-",
                        "B": "-...",
                        "C": "-.-.",
                        "D": "-..",
                        "E": ".",
                        "F": "..-.",
                        "G": "--.",
                        "H": "....",
                        "I": "..",
                        "J": ".---",
                        "K": "-.-",
                        "L": ".-..",
                        "M": "--",
                        "N": "-.",
                        "O": "---",
                        "P": ".--.",
                        "Q": "--.-",
                        "R": ".-.",
                        "S": "...",
                        "T": "-",
                        "U": "..-",
                        "V": "...-",
                        "W": ".--",
                        "X": "-..-",
                        "Y": "-.-",
                        "Z": "--.."}

user_String = user_String.upper()
for character in user_String:

    if(character in morse_Code_Conversion):
        morse_Code_String = morse_Code_String + morse_Code_Conversion[character] + " " #I added another space as it would be difficult to differenciate letters in a work otherwise
                                                                                        #so 3 spaces is space single space is letter seperators
    
print(morse_Code_String)

