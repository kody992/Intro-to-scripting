"""
kody crane
2/22/22
part 2
"""

if __name__ == "__main__":
    
    number_Set = []
    
    print("enter 20 numbers")
    
    for i in range(0, 20):
        number_Set.append(int(input()))
    
    
    
    
    
    print("Smallest Value", min(number_Set))
    print("Largets Value: ", max(number_Set))
    print("Total: ", sum(number_Set))
    print("Average: ", sum(number_Set)/20)
