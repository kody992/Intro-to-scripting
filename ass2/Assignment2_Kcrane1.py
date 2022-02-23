"""
Author: Kody Crane
Date: 2/8/2022
"""


#Question 1 print out the asterisk steps

def question_1():
    grid1 = "*         ", "* *      ", "* * *    ","* * * * ", "* * * * *"
    
    grid2 = "        *", "      * *", "    * * *", "  * * * *", "* * * * *"
    
    for temp_Val in range(0,5):
        print(grid1[temp_Val])
        
    for temp_Val in range(0,5):
        print(grid2[temp_Val])
    

#Question 2 complete 2 math problems given 2 user numbers

def question_2(number_n, number_r):
    
    n_Factorial = 0
    r_Factorial = 0
    dif_factorial = 0
    loop_Counter = 0
    
    if(n<r or n<1 or r<1):
        print("Can not factorial a the difference of n and r\n try again where both are greater than 0 and n > r")
        
    else:
        while(loop_Counter < number_n):
            loop_Counter+=1
            n_Factorial+=loop_Counter
            
        
        loop_Counter = 0
        
        while(loop_Counter < number_r):
            loop_Counter+=1
            r_Factorial += loop_Counter
        
        loop_Counter = 0
        
        while(loop_Counter < (number_n - number_r)):
            loop_Counter+=1
            dif_factorial += loop_Counter
            
        total_1 = (n_Factorial) / (r_Factorial * dif_factorial)
        
        total_2 = (n_Factorial) / dif_factorial
        
        print("n!/(r!(n-r)! = ", total_1)
        print("n!/((n-r)! = ", total_2)


#Question 3 Sorts List

def question_3(origin_List):
    new_List = origin_List.copy()
    
    print("Old list:\n", origin_List)
    
    while origin_List:
        smallest_Value = origin_List[0]
        for j in origin_List:
            if j < smallest_Value:
                smallest_Value = j
        origin_List.remove(smallest_Value)
        new_List.remove(smallest_Value)
        new_List.append(smallest_Value)
        
    print("Sorted List:\n", new_List)


#Question 4 completing operations on a list

def question_4():
    num_List = [20, 68, 41, 88, 16, 40, 65, 97, 85]
    summation = 0
    
    for i in num_List:
        summation += i
        
    print("the summation of:\n", num_List, "\nis = ", summation)


#question_5 finds and prints all prime numbers between [2, 50]
def question_5():
    number=2
    loop_Counter= 5
    
    while(number<50):
        if (number % 2 != 0 and  number % 3 != 0):
            if(loop_Counter**loop_Counter>number):
                print(number)
            else:
                loop_Counter=5
                while(loop_Counter**loop_Counter <= number):
                    loop_Counter += 6
                    if (n % loop_Counter != 0 and n % (loop_Counter + 2) != 0):
                        print(number);
        number += 1
    
    
    

#question_7 finds if number is armstrong number
def question_7():
    number = int(input("enter a number > 0: "))
    order = len(str(number))
    
    total = 0
    
    temp_Val = number
    
    while temp_Val > 0:
        num_place = temp_Val%10
        total += num_place ** order
        temp_Val//= 10
    
    if(number==total):
        print("this is an armstrong number")
    else:
        print("this is not an armstrong number")


#question_8 finds fibbonacci number for provided int
def question_8():
    
    number_Fib = int(input("enter number for fibbonacci: "))
    loop_Counter = 3
    fib_Num_Previous = 0
    fib_Num_Current = 1
    fib_Num_Next = 1
    if number_Fib < 1:
        print("Number must be > 0")

    if number_Fib >= 1:
        print(fib_Num_Previous)
    
        if number_Fib >= 2:
            print(fib_Num_Current)
    
        
            if number_Fib >= 3:
                print(fib_Num_Next)
        
                while(loop_Counter<number_Fib):
                    
                    fib_Num_Previous = fib_Num_Current        
            
                    fib_Num_Current = fib_Num_Next        
            
                    fib_Num_Next = fib_Num_Previous + fib_Num_Current
                    
                    print(fib_Num_Next)
                    loop_Counter += 1


#question_9 edit of provided code prints even numbers 1 to 10

def question_9():
    
    loop_counter = 1
    while loop_counter <= 10:
        if loop_counter%2 == 0:
            print(loop_counter)
        loop_counter += 1 #Here we are increasing loop count by 1


#Main function to call all functions

if __name__ == "__main__":
    
    question_1()
    
    print()
    n = int(input("enter an interger where n > 0 "))
    r = int(input("enter an interger where r > 0 and r < n "))
    question_2(n, r)
    
    origin_List = [20, 68, 41, 88, 16, 40, 65, 97, 85]
    print()
    question_3(origin_List)
    
    print()
    question_4()
    
    print()
    question_5()
    
    print()
    question_7()
    
    print()
    question_8()
    
    print()
    question_9()



