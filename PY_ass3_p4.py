"""
Name:   Kody Crane
Date:   2/15/22
Part:   4
"""

class student:
    def __init__(self, name, g1, g2, g3, g4, g5, g6):
        self.stu_Name = name
        self.stu_g1 = g1
        self.stu_g2 = g2
        self.stu_g3 = g3
        self.stu_g4 = g4
        self.stu_g5 = g5
        self.stu_g6 = g6
        self.stu_Total = g1+g2+g3+g4+g5+g6
        self.stu_average = (self.stu_Total)/6 
    
    #getters
    def get_g1(self):
        return self.stu_g1
        
    def get_g2(self):
        return self.stu_g2
        
    def get_g3(self):
        return self.stu_g3
        
    def get_g4(self):
        return self.stu_g4
        
    def get_g5(self):
        return self.stu_g5
        
    def get_g6(self):
        return self.stu_g6
      
    def get_avg(self):
        return self.stu_average
        
    def get_total(self):
        return self.stu_Total
        
    #setters
    def set_g1(self, grade):
        self.stu_g1 = grade
        
    def set_g2(self, grade):
        self.stu_g2 = grade
        
    def set_g3(self, grade):
        self.stu_g3 = grade
        
    def set_g4(self, grade):
        self.stu_g4 = grade
        
    def set_g5(self, grade):
        self.stu_g5 = grade
        
    def set_g6(self, grade):
        self.stu_g6 = grade
    
    def calc_Avg(self):
        self.stu_average = self.stu_Total/6
    
    def calc_Total(self):
        self.stu_Total = g1+g2+g3+g4+g5+g6
        
    def display(self):
        print(self.stu_Name, self.stu_g1, self.stu_g2, self.stu_g3, self.stu_g4, self.stu_g5, self.stu_g6, self.stu_Total, self.stu_average)
        
if __name__ == "__main__":
    
    import random
    
    student_Names = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o", "p", "q", "r","s","t","u","v","w", "x", "y",]
    
    student_1 = student(student_Names[0], random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))

    student_List = []
    
    for i in range(0,25):
        student_List.append(student(student_Names[0], random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)))
    
    sorted_Student_List = student_List
    
    while student_List:
        smallest_Value = student_List[0].get_avg()
        for j in range(0,25):
            if student_List[j].get_avg() < smallest_Value:
                smallest_Value = student_List[j].get_avg()
        student_List.remove(smallest_Value)
        sorted_Student_List.remove(smallest_Value)
        sorted_Student_List.append(smallest_Value)

    