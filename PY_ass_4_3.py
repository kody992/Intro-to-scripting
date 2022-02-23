"""
Kody Crane
2/22/222
part 3
"""

if __name__ == "__main__":
    
    numbers_list = {}
    size = 20
    for i in range(1, 21):
        numbers_list[i] = i*i
    
    user_Choice = int(input("enter number 1 - 20\n"))
    
    print(numbers_list[user_Choice])