Ac_No=10001
User_Id = 98001
Customer_Id = 2001
Admin_Id = 110010
import datetime
###>>>>> Admin Id <<<<<###
def Ad_numbers():
    global Admin_Id
    for id in range(1):
        id = Admin_Id
        Admin_Id+=1
        return id 
    
###>>>>> User Id <<<<###
def Us_numbers():
    global User_Id
    for Use_Id in range(1) :
        Use_Id =User_Id
        User_Id +=1 
        return Use_Id
    
###>>>>> Account Number<<<<###
def Ac_numbers():
    global Ac_No
    for Account_No in range(1):
        Account_No= Ac_No
        Ac_No+=1
        return Account_No
    
###>>>>> Customer Number<<<<###
def Cu_numbers():
    global Customer_Id
    for Cu_Id in range(1) :
        Cu_Id =Customer_Id
        Customer_Id+=1
        return Cu_Id
    
###....................creating time and date .............#####
def date_time():
    return datetime.date.today() 

###>>>>>>>>>>>>>>>>>>>>>>>>> Read Customer Info <<<<<<<<<<<####
def Read_customer_info():
    C_file = open("Customer_Info.txt","r") 
    x = C_file.readelines()
    C_file.close()
    return x  

###>>>>>>>>>>>>>>>>>>>>>>>>> Read User Info <<<<<<<<<<<####
def Read_User_info():
    C_file = open("User_info.txt","r") 
    A = C_file.readelines()
    C_file.close()
    return A
 
###.......................Read balance info ............###
def Read_Balance_info():
    B_file= open("Balance_info.txt","r")
    P =B_file.readlines()
    B_file.close()
    return P

    #.................................................Creating New customer Account ....................................#
def New_Customer_Bank_Ac ():
    while True :
        try:
            Name = input ("Enter the Name: ")
            Age =int(input ("Enter the Age :"))
            Gender = input("Male or Female :")
            Address = input("Enter the Address: ")
            Balance =int(input("Enter the initial Deposit Value : "))
            #.......Password varification ........#
            while True:
                Password = int (input ("Enter 4 digit number password : ") )
                Conform_Password = int(input("Reenter the 4 digit number Password "))
                if Password==Conform_Password and Password>999 and Password < 10000:
                    Ok=input ("Type Yes for any changes, If not No :")
                    if Ok =="Yes" or Ok =="yes":
                        print ("Be carefull while entering!!!")    
                        New_Customer_Bank_Ac()    
                break 
   
        except ValueError:
            print("Enter numbers only!!!")
            
        print ("Your Account is created Sucessfully..")
        Ac_No =Ac_numbers()
        Us_Id =Us_numbers()
        Cu_Id =Cu_numbers()
        now = date_time()
    #............Adding the user input in file .............#
        file = open("User_info.txt","a")
        file.write(f"U{Us_Id},")
        file.write(f"{now},")
        file.write(f"{Name},")
        file.write(f"{Password},\n")
        file.close()     
    
    #............  Adding the customer input to C_file .......#
        C_file=open ("Customer_Info.txt","a")
        C_file.write(f"C{Cu_Id},")
        C_file.write(f"{now},")
        C_file.write(f"{Name},")
        C_file.write(f"{Age},")
        C_file.write(f"{Gender},")
        C_file.write(f"{Address},")
        C_file.write(f"Ac{Ac_No},")
        C_file.write(f"U{Us_Id},\n")
        C_file.close()

        
    #............  Adding the Balance input to B_file .......#
        B_file  = open("Balance_info.txt","a")
        B_file.write(f"Ac{Ac_No},")
        B_file.write(f"{now},")
        B_file .write(f"{Balance},")
        B_file.write(f"U{Us_Id},\n")
        B_file .close()   
        break
        
    ###...........Creating function for password protection and balance return  for customer menu.........###
def Customer_check(Ac_No,name):
    Cu = Read_customer_info()
    for i in Cu:
        for x in i:
            cu=x.split(",")
            if Ac_No == cu[6] and name==cu[2] :
                print("Your Account Number is Correct !!!")
                u = Read_User_info ()
                for j in u :
                    for b in j :
                        m=b.split(",")
                        if b[0] ==cu[7]:
                            attempt =2
                            while attempt <3:
                                try :
                                    Pass = int (input("enter the Passward :"))
                                    if Pass == m[3]:
                                        print ("Your Password is Correct!!!")
                                        Ba = Read_Balance_info()
                                        for h in Ba :
                                            for m in h :
                                                if b[0]== m[3]:
                                                    return m[2]
                                    else :
                                        print("Incorrect password!!!")
                                except ValueError :
                                    print ("Enter Numbers only !!!")
                                print(f"Attempt left is :{attempt}")
                                attempt -=1
            else :
                print("Your Account Number and Name is Inccorrect !!!")
    
 ###......... Get balance ...........###                 
def get_Balance(Acc_number):     
    ba = Read_Balance_info()
    for x in ba :
        for y in x :
            if Acc_number == y[0]:
                return y[2]  
            else :
                print ("Incorrect Account Number !!!")
                
###.........................................Function for withdraw and Deposit ......................###
def with_dep(Balance,Amount,Menu_Num):
    if Menu_Num==2 :
        N_balance = Balance+Amount
        print("Your amount is Deposited")
        print(f"Your New Balance ia :{N_balance}")
        return N_balance
      
###................................Admin Menu- Driven Interface .......................................................###

def Admin_Menu():
    while True :
        print("1= Create Account ")
        print("2= Deposit Money ")
        print("3= Withdraw Money ")
        print("4= Check Individual Balance   ")
        print("5= Individual Transaction History ")
        print("6= Transfer Money ")
        print("7= Change Account Details")
        print("8= Delate Account ")
        print("9= Add Admin ")
        print("8= Total Transaction History ")
        print("9= Exit ")
        
        Menu_Num = int(input ("Enter the Menu Number "))
        if Menu_Num == 1 :
            New_Customer_Bank_Ac() 
        elif Menu_Num==2:
            try :
                Acc_number =input ("Enter the Account number :")
                Balance = get_Balance(Acc_number)
                Amount =int (input ("Enter the Amount to Deposit"))
                if Amount < Balance :
                    with_dep(Balance,Amount,Menu_Num)
                    
                else :
                    print ("Not sufficient Amount !!!")
            except ValueError:
                print("Enter Numbers only !!!")
            
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
    Admin_Name =input("Enter the Admin Name :") 
    Admin_Password = input("Enter the Admin Password :")
    Ad_Confirm_Password = input("Re-Enter the Admin Password :")
    if Admin_Password == Ad_Confirm_Password :
        print("Your Admin ID and Admin Password is created Sucessfully!!!")
        pass    #####...............should create Admin main menu and call the function here ......####
    
    now= date_time()
    Admin_Id = Ad_numbers()
    User_Id =Us_numbers()
    
    file =open("Admin_Infomation.txt","a")
    file.write(f"Ad{Admin_Id},")
    file.write(f"{now},")
    file.write(f"{Admin_Name},")
    file.write(f"{Admin_Password},")
    file.write(f"U{User_Id},\n")
    file.close()
    
    file =open("User_Info.txt","a")
    file.write(f"U{User_Id},")
    file.write(f"{now},")
    file.write(f"{Admin_Name},")
    file.write(f"{Admin_Password},\n")
    file.close()
    
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
                if Ad_Id== Ad_info[2] and Ad_pass==Ad_info[3]:
                    print("Welcome Admin!!!")
                    Admin_Menu()
                #else :
                    print("Incorrect login Retry")
                    break
        elif INTPUT==2:
            #Customer_Menu()  
            pass         
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
    
    
        
    
        
    
        
            
    
        
        

