import os 
import datetime
def Read_Gen_num():
    file =open("Genarate_numbers.txt","r")
    X = file.readlines()
    file.close()
    return X

if os.path.isfile("Genarate_numbers.txt"):
    Automatic_numbers =Read_Gen_num()
    if Automatic_numbers :
        Auto_numbers=Automatic_numbers[0].split(",")       
        Ac_No= int(Auto_numbers[0])
        User_Id = int(Auto_numbers[1])
        Customer_Id = int(Auto_numbers[2])
        Admin_Id = int(Auto_numbers[3])    
    else :
        Ac_No,User_Id,Customer_Id,Admin_Id =  10000, 98000, 2000, 10010
else :
    Ac_No,User_Id,Customer_Id,Admin_Id =  10000, 98000, 2000, 10010
    
############..............Writing the Generated value in file ............##########
def Regenerate_Numbers():
    global Ac_No,User_Id,Customer_Id,Admin_Id
    G_file = open ("Genarate_numbers.txt","w")
    G_file.write(f"{Ac_No},{User_Id},{Customer_Id},{Admin_Id},\n")
    G_file.close ()  
    

###>>>>> Admin Id <<<<<###
def Ad_numbers():
    global Admin_Id
    Admin_Id+=1
    Regenerate_Numbers()
    return Admin_Id

    
###>>>>> User Id <<<<###
def Us_numbers():
    global User_Id
    User_Id +=1
    Regenerate_Numbers() 
    return User_Id
    
###>>>>> Account Number<<<<###
def Ac_numbers():
    global Ac_No
    Ac_No+=1
    Regenerate_Numbers()
    return Ac_No
   
###>>>>> Customer Number<<<<###
def Cu_numbers():
    global Customer_Id
    Customer_Id+=1
    Regenerate_Numbers()
    return Customer_Id
    
###....................creating time and date .............#####
def date_time():
    return datetime.date.today() 

###>>>>>>>>>>>>>>>>>>>>>>>>> Read Customer Info <<<<<<<<<<<####
def Read_customer_info():
    try :
        C_file = open("Customer_Info.txt","r") 
        x = C_file.readlines()
        C_file.close()
        return x  
    except FileNotFoundError :
        print("CUstomer_Info file not found")
        return []
###>>>>>>>>>>>>>>>>>>>>>>>>> Read User Info <<<<<<<<<<<####
def Read_User_info():
    try :
        C_file = open("User_info.txt","r") 
        A = C_file.readlines()
        C_file.close()
        return A
    except FileNotFoundError :
        print("User_Info file not found")
        return []
###.......................Read balance info ............### 
def Read_Balance_info():
    try:
        B_file= open("Balance_info.txt","r")
        P =B_file.readlines()
        B_file.close()
        return P
    except FileNotFoundError :
        print("CUstomer_Info file not found")
        return []
    #.................................................Creating New customer Account ....................................#
def New_Customer_Bank_Ac ():
    Ac_No =Ac_numbers()
    Us_Id =Us_numbers()
    Cu_Id =Cu_numbers()
    now = date_time()
    while True :
        try:
            Name = input ("Enter the Name: ")
            Age =int(input ("Enter the Age :"))
            Gender = input("Male or Female :")
            Address = input("Enter the Address: ")
            Balance =int(input("Enter the initial Deposit Value : "))
            
        except ValueError:
            print("Enter numbers only!!!")   
            continue
        #.......Password varification ........#
        while True:
            try:
                Password = int (input ("Enter 4 digit number password : ") )
                Conform_Password = int(input("Reenter the 4 digit number Password "))
            except ValueError:
                print("Enter numbers only!!!") 
                break  
        
            if Password==Conform_Password and Password>999 and Password < 10000:
                #Ok=input ("Type Yes for any changes, If not No :")
                print ("Your Account is created Sucessfully..")
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
                Regenerate_Numbers()
                break
        break
    ###...........Creating function for password protection and balance return  for customer menu.........###
def Customer_check(Ac_No,name):
    Cu = Read_customer_info()
    for i in Cu:
        for x in i:
            cu=x.split(",")
            if Ac_No ==int(cu[6]) and name==cu[2] :
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
        m=x.split(",")
        if Acc_number == m[0]:
            return  m[2]
        
######>>>>>>>fuction used to identify the user and update in user file  in withdraw and deposit <<<<<<<<<<<<####
def find_user(Acc_number):
    global Ac_No,User_Id,Customer_Id,Admin_Id
    X =Read_customer_info()
    for a in X:
        b = a.split(",")
        if b[6] == Acc_number :
            Found_Userid = b[7]
    Finding_userid = Read_User_info()
    for c in Finding_userid :
        Z = c.split(",")
        if Found_Userid == Z[0]:
            Current_user_add_file =open("User_Info.txt","a")
            Current_user_add_file.write (c)
            Current_user_add_file.close ()
       
###.........................................Function for Deposit ......................###
def Deposit(Amount):
    Balance=0
    global Ac_No,User_Id,Customer_Id,Admin_Id
    Acc_number =input ("Enter the Account number :")
    #Balance = get_Balance(Acc_number)
    balance_Data =Read_Balance_info()
    for a in balance_Data:
        M = a.split(",")
        if Acc_number == M[0]:
            Balance = M[2]
            balance_Data. remove (a)
            file =open ("Balance_Info.txt","w")
            file .writelines(balance_Data)
            file .close ()
            
            
    if int(Balance) == 0 :
        print("Account Not Found !!!")
        return
    else:  
        New_Balance= int(Balance) + int(Amount)
        M[2] = New_Balance
        file = open("Balance_Info.txt","a")
        for i in M:
            M.pop()
            file .write (f"{i},")
        file.write ("\n")
        file .close ()
        print(M)  
###.........................................Function for Withdraw ......................### 
def Withdraw(Amount):
    global Ac_No,User_Id ,Customer_Id,Admin_Id
    Acount_num = input("Enter the Account Number :")
    Balance = Read_Balance_info()
    update = []
    for d in Balance:
        e= d.split(",")
        Bal = int(e[2])
        if Acount_num == e[0] and Bal < Amount:
            print(f"Your balance is {Bal} \n Amount not valid !!!")
            return
            
        elif Acount_num == e[0] and Bal > Amount:
            new_balance = Bal -Amount
            e[2] = str(new_balance)
            print (f"Your Withdraw is Sucessfull \n Your New Balance is {new_balance} \n Please take your cash ")
            update.append(",".join(e))
            file =open("Balance_info.txt","a")
            file.writelines(update)
            file.close() 
            find_user(Acount_num)
            Regenerate_Numbers() 
            break
    print("Account Not Found !!!")     
    
###.........................................4. function Total balance ...............###
def Total_Balance():
    x =0 
    Info = Read_Balance_info()
    for ba in Info :
        S = ba.split(",")
        x = x + int (S[2])
    print (f"Your total Balance is {x}")
    
###...........................................5. function Transfer Money .................###
def Transfer_Money():
    global Ac_No,User_Id,Customer_Id,Admin_Id
    Amount = int (input ("Enter the transfer Amount :"))
    Dep_Ac_no = input("Enter the depositer Account Number :")
    Rec_Ac_no = input("Enter the Reciver's Account Number : ")
    Dep_Balance =get_Balance(Dep_Ac_no)
    Rec_Balance = get_Balance(Rec_Ac_no)
    if Dep_Balance is None:
        print(" Depositer Account Not Found !!!")
        return
    elif Rec_Balance is None :
        print("Reciver Account Not Found !!!")
        return
        
    else :
        Dep_New_Balance = int (Dep_Balance)- Amount 
        x = Read_Balance_info()
        transfer = []
        for i in x :
            S = i .split (",")
            if Dep_Ac_no == S[0]:
                S[2]= str(Dep_New_Balance)
            transfer.append(",".join(S))
            file =open("Balance_info.txt","a")
            file.writelines(transfer)
            file.close() 
            find_user(Dep_Ac_no)
            Regenerate_Numbers() 
            break
        
        Rec_New_Balance = int(Dep_Balance) + Amount 
        y = Read_Balance_info()
        new_Update = []
        for j in y:
            U = j.split(",")
            if  Rec_Ac_no == U[0]:
                U[2]= str(Rec_New_Balance)
            new_Update.append(",".join(U))
            file =open("Balance_info.txt","a")
            file.writelines(new_Update)
            file.close() 
            find_user(Rec_Ac_no)
            Regenerate_Numbers() 
            break
        return  
 
    

###................................Admin Menu- Driven Interface .......................................................###

def Admin_Menu():
    while True :
        print("1= Create Account ")
        print("2= Deposit Money ")
        print("3= Withdraw Money ")
        print("4= Check Total Balance ")
        print("5= Transfer Money ")
        print("6= Total Transaction History ")
        #print("7= Change Account Details")
        print("7= Delate Account ")
        print("8= Add Admin ")
        print("9= Exit ")
        
        Menu_Num = int(input ("Enter the Admin Menu Number :"))
        if Menu_Num == 1 :
            New_Customer_Bank_Ac() 
        elif Menu_Num==2:
            try :
                Amount =  input ("Enter the Amount to Deposit :")
                Deposit(Amount) 
                
            except ValueError:
                print("Enter Numbers only !!!")               
                
        elif Menu_Num==3 :
            try :
                Amount = int (input ("Enter the Amount to Withdraw :"))
                Withdraw(Amount)
                
            except ValueError:
                print("Enter Numbers only !!!") 
                
        elif Menu_Num==4:
            Total_Balance()
                   
        elif Menu_Num==5:
            Transfer_Money()
        elif Menu_Num==6:
            pass
        elif Menu_Num==7:
            pass
        elif Menu_Num==8 :
            pass
        elif Menu_Num==9 :
            break
        else :
            print("Invalid Customer menu number!!!") 
            break
            
###................................Customer Menu- Driven Interface .......................................................###
def Customer_Menu():
    while True:
        print("Customer Menu number :")
        print(" 1= Deposit Money ")
        print(" 2= Withdraw Money ")
        print(" 3= Check Individual Balance   ")
        print(" 4= Individual Transaction History ")
        print(" 5= Transfer Money ")
        C_num =int (input("Enter the customer Menu number :"))  
       
        if C_num ==1 :
            pass
        elif C_num ==2:
            pass
        elif C_num==3:
            pass
        elif C_num==4:
            pass
        elif C_num ==5:
            pass
        elif C_num==6 :
            break
        else :
            print("Invaalid Customer menu number !!!")

             
#................Creating Admin Account ..........#
def Admin ():
    global Ac_No,User_Id,Customer_Id,Admin_Id
    print("Create your Admin Account !!!")
    Admin_Name =input("Enter the Admin Name :") 
    Admin_Password = input("Enter the Admin Password :")
    Ad_Confirm_Password = input("Re-Enter the Admin Password :")
    if Admin_Password == Ad_Confirm_Password :
        print("Your Admin ID and Admin Password is created Sucessfully!!!")
        now= date_time()
        Admin_Id = Ad_numbers()
        User_Id =Us_numbers()
        
        file =open("Admin_Infomation.txt","a")
        file.write(f"Ad{Admin_Id},{now},{Admin_Name},{Admin_Password},U{User_Id},\n")
        file.close()
        
        file =open("User_Info.txt","a")
        file.write(f"U{User_Id},{now},{Admin_Name},{Admin_Password},\n")
        file.close()
        
        Regenerate_Numbers()
    
    
def First_Interface():
    if os.path.isfile("Admin_Infomation.txt"):
        Second_Interface()
    else :
        for i in range(1):
            Ad_Ac= Admin ()
           
def Second_Interface ():
    while True:
        print("1 = Admin Account ")
        print("2 = Customer Account ")
        try :
            INTPUT=int(input("Enter the Interface Number "))
        except ValueError:
            print("Enter numbers only !!!")
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
                else :
                    print("Incorrect login Retry")
                    break
                break
        elif INTPUT==2:
            #Customer_Menu()  
            pass         
        else :
            print("Enter the Valid Interface Number !!!")



    
i=0 
try :
    while True:
        if i==0:    
            First_Interface()
            i+=1
        else :
            Second_Interface()

finally :
    Regenerate_Numbers()
        
    
    
    
        
    
        
    
        
            
    
        
        

