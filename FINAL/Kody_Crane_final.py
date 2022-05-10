def sortlist(unsortedList):
    for i in range(0, len(unsortedList)):
        for j in range(i+1, len(unsortedList)):
            if(unsortedList[j]>unsortedList[i]):
                switch(unsortedList, i, j)
                
def switch(listswitch, i, j):
    temp = listswitch[i]
    listswitch[i] = listswitch[j]
    listswitch[j] = temp

class products():
    __desc=[]
    __cost=[]
    __units=[]
    def add_product(self,d,u,c):
        self.__desc.append(d)
        self.__units.append(u)
        self.__cost.append(c)
    def save_products(self, filename):
        try:
                f = open(filename, "x")
                
        except:
                f = open(filename, "w")
        finally:
                for i in range(0, len(self.__desc)):
                    f.write(self.__desc[i])
                    f.write("\n")
                    f.write(self.__units[i])
                    f.write("\n")
                    f.write(self.__cost[i])
                    f.write("\n")
def find_fib(num):
    if(num>1):
        last_num=0
        print(last_num)
    if(num>2):
        next_num=1
        print(next_num)
    while(num>2):
        temp=last_num
        last_num=next_num
        next_num+=temp
        print(next_num)
        num-=1

if __name__ == "__main__":
    #question 1
    print("--------Q1--------")
    sortlist1=["z","m","n","a","c","i","g","x","t"]
    print(sortlist1)
        
    sortlist(sortlist1)
        
    print(sortlist1)
    
    #Question 4
    print("--------Q4--------")
    p_list = products()
    p_list.add_product("Jacket","40","59.95")
    p_list.add_product("Designer jeans","100","34.95")
    p_list.add_product("Shirt","200","24.95")
    p_list.save_products("products")
    print("products saved to file name products")

    #question 6
    print("--------Q6--------")
    fibnum=-1
    while(fibnum<0):
        try:
            fibnum=int(input("enter non negative for fibonacchi sequence"))
        except:
            print("enter a valid input")
            fibnum=-1
    find_fib(fibnum)
