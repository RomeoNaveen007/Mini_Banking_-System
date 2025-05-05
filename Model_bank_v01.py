"""Ac_No=10001
User_Id = 98001
Customer_Id = 2001
Admin_Id = 110010
import datetime
#.................................................Creating customer Account ....................................#
def New_Customer_Bank_Ac ():
    global Ac_No
    global User_Id
    global Customer_Id
    while True :
        try:
            Name = input ("Enter the Name: ")
            Age =int(input ("Enter the Age :"))
            Gender = input("Male or Female :")
            Address = input("Enter the Address: ")
            Balance =int(input("Enter the initial Deposit Value : "))
            #.......Password varification ........#
            while True:
                Password = int (input ("Enter 4 digit password : ") )
                Conform_Password = int(input("Reenter the Password "))
                if Password==Conform_Password and Password>999 and Password < 10000:
                    print ("Your Account is created Sucessfully..")
                    break
        except ValueError:
            print("Enter numbers only!!!")
            #.......Account number generation .......#
        
        for i in range(1):
            Account_No= Ac_No
            Ac_No+=1
            #...........User Id Creation ..............#
        for u in range(1) :
            Us_Id =User_Id
            User_Id+=1 
            #...........Custemer Id creation ..............#
        for c in range(1) :
            Cu_Id =Customer_Id
            Customer_Id+=1
        break
           
 #............Adding the input in file .............#
    file = open("User_info.txt","a")
    file.write(f"C{Customer_Id},")
    file.write(f"Ac{Account_No},")
    file.write(f"{Name},")
    file.write(f"{Age},")
    file.write(f"{Gender},")
    file.write(f"{Address},")
    file.write(f"{Password},")
    file.write(f"U{Us_Id}\n")
    file.close()       
    
    Bal_file  = open("Balance_info.txt","a")
    Bal_file .write(f"{Balance}\n")
    Bal_file .close()   
    
#.......Adding the record in list........#
"""
def Info_list ():
    file =open ("User_info.txt","r")
    Infomation_list = file .readlines()
    file.close()
    
    Bal_file =open ("Balance_info.txt","r")
    Inform_list = Bal_file .readlines()
    file.close()
    print(Inform_list)
    print(Infomation_list)
    """
###....................creating time and date .............#####

def date_time():
    return datetime.date.today()     
                   
###................................customer Menu- Driven Interface .......................................................###

def Customer_Menu():
    while True :
        print("1= Create Account ")
        print("2= Deposit Money ")
        print("3= Withdraw Money ")
        print("4= Check Balance   ")
        print("5= Transaction Histry ")
        print("6= Exit ")
        Menu_Num = int(input ("Enter the Menu Number "))
        if Menu_Num == 1 :
            New_Customer_Bank_Ac() 
        elif Menu_Num==2:
            pass
        elif Menu_Num==3 :
            pass
        elif Menu_Num==4:
            pass
        elif Menu_Num==5:
            pass
        elif Menu_Num==6:
            print ("Thank you for using our Mini banking !!!")
            break
        else :
            print("Invalid Customer menu number!!!") 
             
#................Creating Admin Account ..........#
def Admin ():
    global Admin_Id
    global User_Id 
    Admin_Name =input("Enter the Admin Name :") 
    Admin_Password = input("Enter the Admin Password :")
    Ad_Confirm_Password = input("Re-Enter the Admin Password :")
    if Admin_Password == Ad_Confirm_Password :
        print("Your Admin ID and Admin Password is created Sucessfully!!!")
        pass    #####...............should create Admin main menu and call the function here ......####
    
    now= date_time()
    
    file =open("Admin_Infomation.txt","w")
    file.write(f"{now},")
    file.write(f"Ad{Admin_Id},")
    file.write(f"{Admin_Name},")
    file.write(f"U{User_Id},")
    file.write(f"{Admin_Password},\n")
    file.close()
    
    file =open("User_Info.txt","w")
    file.write(f"{now},")
    file.write(f"U{User_Id},")
    file.write(f"{Admin_Name},")
    file.write(f"{Admin_Password},\n")
    file.close()
    
    for id in range(1):
        id = Admin_Id
        Admin_Id+=1
        
    for Use_Id in range(1) :
        Use_Id =User_Id
        User_Id +=1 
        
    
def First_Interface():
    for i in range(1):
        print("Create your Admin Account!")
        Ad_Ac= Admin ()
        
        
def Second_Interface ():
    while True:
        print("1 = Admin Account ")
        print("2 = Customer Account ")
        INTPUT=int(input("Enter the Interface Number "))
        if INTPUT==1 :
            file =open ("Admin_Infomation.txt","r")
            Admin_info = file .readline()
            file.close()
            Ad_info=Admin_info.split(",")
            
            while True:
                Ad_Id=input("Enter the Admin Name :")
                Ad_pass=input("Enter the admin password :")
                if Ad_Id== Ad_info[2] and Ad_pass==Ad_info[4]:
                    print("Welcome Admin!!!")
                    pass    #####...............should create Admin main menu and name the function name ......####
                #else :
                #   print("Incorrect login")
                break
        elif INTPUT==2:
            Customer_Menu()           
        else :
            print("Enter the Valid Interface Number !!!")
    
i=0     
while True:
    if i==0:    
        First_Interface()
        i+=1
    else :
        Second_Interface()
        
#Info_list()cls
    
        
            
"""