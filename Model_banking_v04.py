import os 
import datetime
#from tabulate import tabulate
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
    try :
        with open("Genarate_numbers.txt","w") as G_file :
            G_file.write(f"{Ac_No},{User_Id},{Customer_Id},{Admin_Id},\n")
    except FileNotFoundError:
        print("File not found !!!")
        return
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
        with open("Customer_Info.txt", "r") as C_file:
            x = C_file.readlines()
        return x 
    except FileNotFoundError :
        print("CUstomer_Info file not found !!!")
        return 
###>>>>>>>>>>>>>>>>>>>>>>>>> Read User Info <<<<<<<<<<<####
def Read_User_info():
    try :
       with open ("User_Info.txt", "r") as A_file:
            A = A_file.readlines()
            return A
    except FileNotFoundError :
        print("User_Info file not found !!!")
        return 
###......................Read balance info ............### 
def Read_Balance_info():
    try:
        with open ("Balance_info.txt","r") as B_file:
            B = B_file.readlines()
            return B
    except FileNotFoundError :
        print("Customer_Info file not found  !!!")
        return 
###................. Read Transaction histry ...........### 
def Read_History_info():
    try :
        with  open("History_info.txt", "r") as H_file:
            H = H_file.readlines()
            return H
    except FileNotFoundError :
        print("History_info file not found !!!")
        return
#.................................................Creating New customer Account ....................................#
def New_Customer_Bank_Ac ():
    
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
                change = input ("Type Yes if any changes ,if not No :" )
            except ValueError:
                print("Enter numbers only!!!") 
                break                 
            if change == "Yes" or change == "yes" :
                print("Please Re-enter carefully !!!")
                return       
            else :
                Password==Conform_Password and Password>999 and Password < 10000
                print ("Your Account is created Sucessfully..")
                Ac_No =Ac_numbers()
                Us_Id =Us_numbers()
                Cu_Id =Cu_numbers()
                now = date_time()
                #............Adding the user input in file .............#
                with open ("User_info.txt","a") as file :
                    file.write(f"U{Us_Id},{now},{Name},{Password},\n")
                #............  Adding the customer input to C_file .......#
                with open ("Customer_Info.txt","a")as C_files:
                    C_files.write(f"C{Cu_Id},{now},{Name},{Age},{Gender},{Address},Ac{Ac_No},U{Us_Id},\n") 
                #............  Adding the Balance input to B_file .......#
                with open ("Balance_info.txt","a") as B_file:
                    B_file.write(f"Ac{Ac_No},{now},{Balance},U{Us_Id},\n")
                #...............Adding the history input to H_file .........#
                Amount = 0 
                with open ("History_info.txt","a") as H_file:
                    H_file .write(f"Ac{Ac_No},{now},{Amount},{Balance},\n")
                    Regenerate_Numbers()
                break
        break
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
            try :
                with open("User_Info.txt", "a") as Current_user_add_file:
                    Current_user_add_file.write(c) 
            except UnboundLocalError:
                print ("File not found !!!")
###.........................................Function for Deposit ......................###
def Deposit(Amount,Acc_number):
    global Ac_No,User_Id,Customer_Id,Admin_Id
    now = date_time()
    Balance = Read_Balance_info()
    Dep_List = []
    for i in Balance :
        M= i .split (",")
        if Acc_number== M[0] :
            Old_Balance = M[2]
            if int(Old_Balance )> 0 :
                New_Balance = int (Amount) + int (Old_Balance)
                M[2] = str(New_Balance)
                print(f"Your amount is Deposited \n Your New Balance is {New_Balance}")
                convert_str = ",".join(M)
                Dep_List.append(f"{convert_str}")   
            else :
                print("Invalid Amount !!!")
                return
        else :
            Dep_List.append(i)           
    if Acc_number is None :
        print("Your Account not found !!!")
    else:
        try :
            with open("Balance_info.txt", "w") as file:
                file.writelines(Dep_List)
            with open ("History_info.txt","a") as H_file:
                H_file.write(f"{Acc_number},{now},{Amount},{New_Balance},\n")
        except UnboundLocalError:
            print ("File not found!!!")
            
        find_user(Acc_number)
        Regenerate_Numbers()
###.........................................Function for Withdraw ......................### 
def Withdraw(Amount,Acount_num):
    global Ac_No,User_Id ,Customer_Id,Admin_Id
    now = date_time()
    Balance = Read_Balance_info()
    update = []
    for d in Balance:
        e= d.split(",")
        if e[0] == Acount_num :
            if  int(e[2]) < Amount:
                Old_Bal = e[2]
                New_Bal = int (Old_Bal) - int (Amount)
                e[2] = str(New_Bal)
                print(f"Your Withdraw is Sucessfull \n Your New Balance is {New_Bal} \n Please Take your Cash !!!")
                Con_str = ",".join(e)
                update.append(f"{Con_str}") 
            else :
                print("Amount is greater than Balance !!!")
            return
        else:
            update.append(d)     
    if Acount_num is None :
        print("Your Account not found !!!")
    else :
        try:
            with open("Balance_info.txt","w") as file :
                file .writelines(update)
            with open ("History_info.txt","a") as H_file:
                H_file.write(f"{Acount_num},{now},{Amount},{New_Bal},\n")
        except FileNotFoundError:
            print ("File not found !!!")
        find_user(Acount_num)
        Regenerate_Numbers()      
###.........................................4. function Total balance ...............###
def Total_Balance():
    x =0 
    Info = Read_Balance_info()
    for ba in Info :
        S = ba.split(",")
        x = x + int (S[2])
    print (f"Your total Balance is {x}")
###...........................................5. function Transfer Money .................###
def Transfer_Money(Dep_Ac_no):
    global Ac_No,User_Id,Customer_Id,Admin_Id
    now = date_time()
    try :
        Amount = int (input ("Enter the transfer Amount :"))
        Rec_Ac_no = input("Enter the Reciver's Account Number : ")
    except ValueError :
        print("Enter Numbers only !!!")
        return
    Dep_Balance =get_Balance(Dep_Ac_no)
    Rec_Balance = get_Balance(Rec_Ac_no)
    if Dep_Balance is None:
        print(" Depositer Account Not Found !!!")
        return
    elif Rec_Balance is None :
        print("Reciver Account Not Found !!!")
        return
    #####>>>>>>>>>> withdrawing from depositers account <<<<<<<<<<<<<###### 
    else :
        if int(Dep_Balance) < Amount:
            print(f"Your Amount is Not sufficient for Transaction !!! \n Your Balance is {Dep_Balance} \n Try Again !!!")
        else :
            Dep_New_Balance = int (Dep_Balance)- Amount 
            x = Read_Balance_info()
            transfer = []
            for i in x :
                S = i .split (",")
                if Dep_Ac_no == S[0]:
                    S[2]= str(Dep_New_Balance)
                    print (f"Your New Balance is {Dep_New_Balance}")
                    str_1 = ",".join(S)
                    transfer.append(f"{str_1}")
                else :
                    transfer.append(i)
            with open("Balance_info.txt","w") as file :
                file .writelines(transfer)
            with open ("History_info.txt","a") as H_file :
                H_file .write(f"{Dep_Ac_no},{now},{Amount},{Dep_New_Balance},\n")
            find_user(Dep_Ac_no) 
            ####>>>>>>>> Depositing in receivers account <<<<<<<<<<<<#######
            Rec_New_Balance = int(Dep_Balance) + Amount 
            print ("Your Amount is Transfered Sucessfully !!!")
            y = Read_Balance_info()
            new_Update = []
            for j in y:
                U = j.split(",")
                if  Rec_Ac_no == U[0]:
                    U[2]= str(Rec_New_Balance)
                    str_2 =",".join (U)
                    new_Update.append(f"{str_2}")
                else:
                    new_Update.append(j)
            with open ("Balance_info.txt","w") as file_x:
                file_x.writelines(new_Update)
            with open ("History_info.txt","a") as H_file :
                H_file .write(f"Ac{Rec_Ac_no},{now},{Amount},{Rec_New_Balance},\n")
            Regenerate_Numbers()    
            return
        ###...........................................5. Delete a specific Account .................###
def Delete (Ac_No):
    N = Read_customer_info()
    M= Read_Balance_info()
    for j in M :
        y = j.split (",")
        if Ac_No == y[0]:
            U = y[3]
            M.remove (j)
            break
    for i in N :
        x = i .split(",")
        if U == x[7] :
            N.remove(i)
            break           
    if Ac_No is None :
        print("Account Number Not Found !!!")
    with open ("Balance_info.txt","w") as file :
        file .writelines(M)
    with open ("Customer_Info.txt","w")as file_c:
        file_c.writelines(N)
    print("Account deleted Sucessfully !!!") 
###....................................................6. Total Transaction History ...................#######################
def tot_trans_histroy():
    try :
        with open ("History_info.txt","r") as file :
            print(f"{'|Ac_No':<10}{' |Date':<12}{'  |Amount':<15}{'   |Balance':<20}|\n")
            lines = file.readlines()
    except FileNotFoundError:
        print("History_info file not found !!!") 
    for line2 in lines:
        line = line2.strip().split(',')
        print(f"|{line[0]:<10}|{line[1]:<12}|{line[2]:<15}|{line[3]:<20}|\n")            
#########>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Check Customer login <<<<<<<<<<<<<<<<<<<<<<<<<<##########
def Check_Customer_login(): 
    attempt =2
    while  attempt >0: 
        while True:
            X =Read_User_info()
            try :
                User_id= input("Enter the User ID :")
                Password = input("Enter the User Password :")
            except ValueError :
                print("Enter numbers only !!!")
                continue
            for i in X :
                user = i.strip().split (",")
                if user[0] == User_id and user[3]== Password :
                    print("Your User ID and Password is correct !!!")  
                    print(f"Welcome {user[2]} !!!")
                    Y = Read_customer_info()
                    for j in Y:
                        Ad_id = j.strip().split(",")
                        if user[0]== Ad_id[7]:
                            return Ad_id[6]                                              
            else :
                print ("Incorrect User ID and Password !!!")
                print (f"Attempt left is :{attempt}")
                attempt = attempt-1
            if attempt== 0:
                break 
            
####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>C_3 . Check Individual Balance <<<<<<<<<<<<<<<<<<<<<<<<<<<#####
def check_Cu_Balance (Ac_No):
    x = Read_Balance_info()
    for i in x :
        S = i.split(",")
        if Ac_No == S[0]:
            print (f"Your Account Balance is : {S[2]}")
            break
####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>C_4 . Individual transaction history <<<<<<<<<<<<<<<<<<<<<<<<<<<#####
def Indi_Trans_History(Ac_No):
    with open ("History_info.txt","r") as file :
        print(f"{'|Ac_No':<10}{'|Date':<12}{'|Amount':<15}{'|Balance':<20}|\n")
        for lines in file:
            line = lines.strip().split(',')
            if line[0] == Ac_No:
                print(f"|{line[0]:<10}|{line[1]:<12}|{line[2]:<15}|{line[3]:<20}|\n")
###................................Admin Menu- Driven Interface .......................................................###
def Admin_Menu():
    while True :
        print("Admin Menu number :") 
        print(" 1= Create Account \n 2= Deposit Money \n 3= Withdraw Money \n 4= Check Total Balance \n 5= Transfer Money \n 6= Total Transaction History \n 7= Delate Account \n 8= Add Admin \n 9= Exit ") 
        try :
            Menu_Num = int(input ("Enter the Admin Menu Number :"))
        except ValueError :
            print ("Enter Numbers only !!!")
        if Menu_Num == 1 :
            New_Customer_Bank_Ac() 
            
        elif Menu_Num==2:
            try :
                Amount = int (input ("Enter the Amount to Deposit :"))
                Acount_num = input("Enter the Account Number :")
                if Amount<0 :
                    print("Try Again !!! \n Amount is less than Zero")
                    continue 
                else :
                    Deposit(Amount,Acount_num)
            except ValueError:
                print("Enter Numbers only !!!")  
                           
        elif Menu_Num==3 :
            try :
                Amount = int (input ("Enter the Amount to Withdraw :"))
                Acount_num = input("Enter the Account Number :")
                if Amount<0 :
                    print("Try Again !!! \n Amount is less than Zero")
                else :
                    Withdraw(Amount,Acount_num)
            except ValueError:
                print("Enter Numbers only !!!") 
                
        elif Menu_Num==4:
            Total_Balance()
                
        elif Menu_Num==5:
            try:
                Ac_No= input("Enter the Account Number to Transfer :")
                Transfer_Money(Ac_No)
            except ValueError:
                print("Enter Numbers only !!!")
                
        elif Menu_Num==6:
            tot_trans_histroy()
            
        elif Menu_Num==7:
            try:
                Ac_No = input("Enter the Account Number to Delete :")
                Delete (Ac_No)
            except ValueError:
                print("Enter Numbers only !!!")    
                
        elif Menu_Num==8 :
            Admin()
            
        elif Menu_Num==9 :
            break
        
        else :
            print("Invalid Customer menu number!!!") 
            break
        
###................................Customer Menu- Driven Interface .......................................................###
def Customer_Menu():      
    while True:
        print("Customer Menu number :")
        print(" 1= Deposit Money \n 2= Withdraw Money \n 3= Check Individual Balance \n 4= Individual Transaction History \n 5= Transfer Money \n 6= Exit ") 
        try :
            C_num =int (input("Enter the customer Menu number :"))
        except ValueError:
            print("Enter Numbers only !!!")
            return  
        if C_num ==1 :
            Ac_No = Check_Customer_login()    
            Amount =  input ("Enter the Amount to Deposit :")
            try :
                Deposit(Amount, Ac_No)     
            
            except ValueError:
                print("Enter Numbers only !!!") 

        elif C_num ==2:
            Ac_No = Check_Customer_login() 
            try :        
                Amount =  input ("Enter the Amount to Withdraw :")
                Withdraw(Amount,Ac_No)
            except ValueError:
                print("Enter Numbers only !!!")  
                
        elif C_num==3:
            Ac_No = Check_Customer_login()
            check_Cu_Balance(Ac_No)
                
        elif C_num==4:
            Ac_No = Check_Customer_login()
            Indi_Trans_History(Ac_No)
          
        elif C_num ==5:
            Ac_No = Check_Customer_login()
            Transfer_Money(Ac_No)
            
        elif C_num==6 :
            break
        
        else :
            print("Invaalid Customer menu number !!!")
              
#................Creating Admin Account ..........#
def Admin ():
    global Ac_No,User_Id,Customer_Id,Admin_Id
    print("Create a Admin Account !!!")
    while True:
        try :
            Admin_Name =input("Enter the Admin Name :") 
            Admin_Password = input("Enter the Admin Password :")
            Ad_Confirm_Password = input("Re-Enter the Admin Password :")
        except ValueError:
            print("Enter numbers only !!!")
        if Admin_Password == Ad_Confirm_Password :
            print("Your Admin ID and Admin Password is created Sucessfully!!!")
            now= date_time()
            Admin_Id = Ad_numbers()
            User_Id =Us_numbers()
            try :
                with open ("Admin_Infomation.txt","a") as file :
                    file.write(f"Ad{Admin_Id},{now},{Admin_Name},{Admin_Password},U{User_Id},\n")
                
                with open("User_Info.txt","a") as file :
                    file.write(f"U{User_Id},{now},{Admin_Name},{Admin_Password},\n")
            except FileNotFoundError:
                print ("file Not Found !!!")
            Regenerate_Numbers()
            Second_Interface()
            
        else:
            print("Password is not match !!!")
            continue
     
           
def First_Interface():
    if os.path.isfile("Admin_Infomation.txt"):
        Second_Interface()
    else :
        for i in range(1):
            Admin ()
            return
def Second_Interface ():
    while True:
        print(" 1 = Admin Account \n 2 = Customer Account \n 3 = Exit ")
        try :
            INTPUT=int(input("Enter the Interface Number :"))
        except ValueError:
            print("Enter interface numbers only !!!")
            return
        if INTPUT==1 :
            file =open ("Admin_Infomation.txt","r")
            Admin_info = file .readlines()
            file.close()
            while True:
                Ad_Id=input("Enter the Admin Name :")
                Ad_pass=input("Enter the admin password :")
                for k in Admin_info :
                    l= k.split(",")
                    if Ad_Id== l[2] and Ad_pass== l[3]:
                        print(f"Welcome {Ad_Id} !!!")
                        Admin_Menu()     
                               
                else :
                    print("Your Admin ID and Password is Incorrect !!!")
                break
                              
        elif INTPUT==2:
            Customer_Menu() 
            
        elif INTPUT==3 :
            print ("Thank You for Banking !!!")
            exit()
        

    
First_Interface()
