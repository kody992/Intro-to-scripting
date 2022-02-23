"""
Kody Crane
2/22/22
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
        print(self.emp_First_Name, " ", self.emp_Last_Name,"\t", self.emp_ID_Num,"\t", self.emp_Department,"\t", self.emp_Title,"\t", self.emp_Email)

    def get_ID(self):
        return self.emp_ID_Num
    
    def get_Name(self):
        return self.emp_Fullname
    
    def get_Dept(self):
        return self.emp_Department
    
    def get_Title(self):
        return self.emp_Title

if __name__ == "__main__":
    
    employee_1 = employee("Susan", "Meyers",47899,"Accounting","Vice Pres.")
    employee_2 = employee("Mark", "Jones",39119,"Info. Tech.","Programmer")
    employee_3 = employee("Joy", "Rogers",81774,"Manufacturing","Engineer")
    
    employee_Dict = {   employee_1.get_ID(): {"Name": employee_1.get_Name(), "Dept.": employee_1.get_Dept(), "Title": employee_1.get_Title()}, 
                        employee_2.get_ID(): {"Name": employee_2.get_Name(), "Dept.": employee_2.get_Dept(), "Title": employee_2.get_Title()}, 
                        employee_3.get_ID(): {"Name": employee_3.get_Name(), "Dept.": employee_3.get_Dept(), "Title": employee_3.get_Title()}}
    
    continue_Loop = 1
    
    while(continue_Loop == 1):
        user_Choice = input("pick an option: \n1. Look Up\n2.Add New\n3.Change Existing\n4.Delete\n5.Exit\n")
        
        if (user_Choice[0] == "1"):
            check_Key = int(input("Enter employee ID: "))
            if(check_Key in employee_Dict):
                print(employee_Dict[check_Key])


        elif (user_Choice[0] == "2"):
            print("Enter employee information: ")
            f_Name = input("First Name: ")
            l_Name = input("Last Name: ")
            id_Num = int(input("ID Number: "))
            dept = input("Dept.: ")
            title = input("Title: ")
            temp_Employee = employee(f_Name, l_Name, id_Num, dept, title)
            employee_Dict[temp_Employee.get_ID()] = {"Name": temp_Employee.get_Name(), "Dept.": temp_Employee.get_Dept(), "Title": temp_Employee.get_Title()}
            
            
        elif (user_Choice[0] == "3"):
            check_Key = int(input("Enter employee ID you wish to edit: "))
            if(check_Key in employee_Dict):
                print("enter new values:")
                employee_Dict[check_Key]["Name"] = input("First Name: ") + " " + input("Last Name: ")
                employee_Dict[check_Key]["Dept."] = input("Dept.: ")
                employee_Dict[check_Key]["Title"] = input("Title: ")
        
        elif (user_Choice[0] == "4"):
            check_Key = input("Enter employee ID you wish to delete: ")
            if(check_Key in employee_Dict):
                print(employee_Dict.pop(check_Key), "\nDELETED")
            
        elif (user_Choice[0] == "5"):
            continue_Loop = 0
        
        else:
            print("Enter a valid option")
    
    
