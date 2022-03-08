"""
Kody Crane
3/8/22
Q2
"""

if __name__ == "__main__":
    
    final_Text = ""
    
    loop_Counter = 1
    
    i = int(input("How many files do you want to open: "))
    
    
    #loop through user given i searching for files
    while(loop_Counter <= i):
        file_Name = "f" + str(loop_Counter) +".txt" #follow format for file name
        print(file_Name, " trying to open")
        try:
            f = open(file_Name, "r")
            print(file_Name, " open succesful")
            final_Text = final_Text + f.read() #append to final text for file
            f.close()
        except FileNotFoundError:#file not found 
            print(file_Name, " open failed")
        finally:#itterates 
            loop_Counter += 1
    
    try:
        f = open("final_file.txt", "x")
    except:
        f = open("final_file.txt", "w")
    finally:
        f.write(final_Text)