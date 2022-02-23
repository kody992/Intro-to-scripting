"""
Name:   Kody Crane
Date:   2/15/22
Part:   2 & 3
"""

class employee:
    def __init__(self, first_Name, last_Name, ID_num, department, title):
        self.emp_First_Name = first_Name
        self.emp_Last_Name = last_Name 
        self.emp_ID_Num = ID_num
        self.emp_Department = department
        self.emp_Title = title 
        self.emp_Fullname = first_Name + " " + last_Name
        self.emp_Email = first_Name.lower() + "." + last_Name.lower()+ "@company.com"
    
    def display(self):
        print(self.emp_First_Name, " "< self.emp_Last_Name,"\t", self.emp_ID_Num,"\t", self.emp_Department,"\t", self.emp_Title,"\t", self.emp_Email)

if __name__ == "__main__":
    
    employee_1 = employee("Susan", "Meyers",47899,"Accounting","Vice Pres.")
    employee_2 = employee("Mark", "Jones",39119,"Info. Tech.","Programmer")
    employee_3 = employee("Joy", "Rogers",81774,"Manufacturing","Engineer")
    
    print("Name\t\t ID\t Dept.\t\t Title\t\t\tEmail")
    employee_1.display()
    employee_2.display()
    employee_3.display()
