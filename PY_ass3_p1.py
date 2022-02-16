"""
Name:   Kody Crane
Date:   2/15/22
Part:   1
"""

class car:
    def __init__(self, year, make, model):
        self.car_Year = year
        self.car_Make = make
        self.car_Model= model
        self.car_Speed= 0
    
    def get_Speed(self):
        return self.car_Speed
        
    def accelerate(self):
        self.car_Speed += 5
        print("accelerated to: ", self.get_Speed())
        
    def brake(self):
        if(self.car_Speed>0):
            self.car_Speed -= 5
            if(self.car_Speed==0):
                print("car has stopped")
            else:
                print("slowed down to: ", self.get_Speed())
        else:
            print("car is already stopped")
        

if __name__ == "__main__":
    
    print("enter cars information: ")
    init_Car_Year = int(input("\t\tYear: "))
    init_Car_Make = input("\t\tMake: ")
    init_Car_Model = input("\t\tModel:") 
    
    car1 = car(init_Car_Year, init_Car_Make, init_Car_Model)
    
    for i in range(0,5):
        car1.accelerate()
    
    print()
    
    for i in range(0,5):
        car1.brake()
    