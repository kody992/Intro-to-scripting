#////////////////////////////////////////
#Kody Crane
#///////////////////////////////////////
print ("assignment 1:\n")


"""
Author: Kody Crane
Date: 1/30/22
Desc: displays personal Information currently hard coded but can be user input
"""

print ("Question 1:\n")

print ("Name:\n"
        "Address:\n"
        "City:\n"
        "State:\n"
        "Zip:\n"
        "Phone:\n")
        
#////////////////////////////////////////////////////////////////////////////////

"""
Author: Kody Crane
Date: 1/30/22
Desc: converts user input of square feet into acers
"""

print ("Question 2:\n")

square_Feet = float(input("enter the total square feet: "))

acers = square_Feet/43560

print (square_Feet, " square feet equals ", acers, "acers\n")

#////////////////////////////////////////////////////////////////////////////////

"""
Author: Kody Crane
Date: 1/30/22
Desc: displays cars distance traveled at various times for 70 mph
"""

print ("Question 3:\n")

car_Speed = 70

print ("car moving 70 miles per hour:\n",
        "6 hours:\t", 6*car_Speed, " miles\n",
        "10 hours:\t",10*car_Speed, " miles\n",
        "15 hours:\t",15*car_Speed, " miles\n")

#////////////////////////////////////////////////////////////////////////////////

"""
Author: Kody Crane
Date: 1/30/22
Desc: takes users input age and displays classification for that age
"""

print ("Question 4:\n")

age = int(input("Enter your age: "))

if(age>=0 and age<1):
    print("You are an infiant\n")
elif(age>=1 and age<13):
    print("You are a child\n")
elif(age>=13 and age<20):
    print("You are a teenager\n")
elif(age>=20):
    print("You are an adult\n")
else:
    print("invalid number\n")

#////////////////////////////////////////////////////////////////////////////////

"""
Author: Kody Crane
Date: 1/30/22
Desc: takes user input for each coin and displays if user got <, > or equal to 1 dollar
"""

print ("Question 5:\n")

print("Enter number of coins to equal a dollar: ")

pennies  = int(input("Number of pennies:\t"))
nickels  = int(input("Number of nickels:\t"))
dimes    = int(input("Number of dimes:\t"))
quarters = int(input("Number of quarters:\t"))

total = (pennies + nickels*5 + dimes*10 +quarters*25)/100

if(total==1):
    print("Congratulations you won!!\n")
elif(total>1):
    print("The number you entered is greater than 1 dollar\n")
elif(total<1):
    print("The number you entered is less than 1 dollar\n")
    

#////////////////////////////////////////////////////////////////////////////////

"""
Author: Kody Crane
Date: 1/30/22
Desc: takes user input year and displays if leap year of not
"""

print ("Question 6:\n")

year = int(input("enter the year: "))

if(year%100==0 and year%400==0):
    print("It is a leap Year, 29 days in feburary.\n")
elif(year%4==0):
    print("It is a leap Year, 29 days in feburary.\n")
else:
    print("It is not leap Year, 28 days in feburary.\n")


#////////////////////////////////////////////////////////////////////////////////

"""
Author: Kody Crane
Date: 1/30/22
Desc: take suser input of weight and height and classifies based on the BMI
"""

print ("Question 7:\n")

user_Weight= float(input("enter weight: "))
user_Height_Feet= int(input("enter feet: "))
user_Height_Inches= int(input("enter inches: "))
user_Height = user_Height_Feet*12 + user_Height_Inches

bmi = float(user_Weight*703 /user_Height**2)

if(bmi<18.5):
    print("Underweight accodring to bmi\n")
elif(bmi>=18.5 and bmi<=25):
    print("Ideal Weight accodring to bmi\n")
elif(bmi>25):
    print("Overweight accodring to bmi\n")

#////////////////////////////////////////////////////////////////////////////////

"""
Author: Kody Crane
Date: 1/30/22
Desc: displays various fields of a stock traders investment
"""

print ("Question 8:\n")

stock_price = 40.00
broker_Commission = .03
stock_Total = 2000

bought_Total = stock_price*stock_Total
broker_Bought_Commission = bought_Total*broker_Commission


#paid
print("Ammount joe paid for the stock:\t\t\t", bought_Total)
#paid broker bought
print("Ammount joe paid the broker for buying:\t\t",  broker_Bought_Commission)

stock_price = 42.75
sold_Total = stock_price *stock_Total
broker_Sold_Commission = sold_Total*broker_Commission
gross_Product = sold_Total-(bought_Total+broker_Bought_Commission+broker_Sold_Commission)
#sold For
print("Ammount joe sold the stock for:\t\t\t", sold_Total)
#paid broker sold
print("Ammount joe paid the broker for selling:\t",  broker_Sold_Commission)
#money left
print("Ammount joe earned:\t\t\t\t", gross_Product)

