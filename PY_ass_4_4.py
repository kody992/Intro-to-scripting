"""
Kody Crane
2/22/222
part 4
"""
import random

if __name__ == "__main__":
    
    number_List = []
    
    for i in range(0,100):
        temp_Int = random.randint(0, 20)
        if(temp_Int not in number_List):
            number_List.append(temp_Int)
    
    number_List.remove(max(number_List))
    
    print("second largest number: ", max(number_List))