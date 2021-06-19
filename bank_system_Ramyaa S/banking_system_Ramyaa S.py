#### Functions inside the Bank management system
'''
1. Login features
2. Credit and Debit amount
3. Transfer fund
4. Checking the balance
5. Editing Profile
6. Creating the account
7. Logout features
'''
class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 5000
        self.TransferCash = False

    def register(self, name, ph, password):
        cash = self.cash
        conditions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! Please enter 10 digit number")
            conditions = False
        
        if len(password) <= 8 or len(password) > 18:
            print("Enter Password greater than or equat to 8 and less than 18 character")
            conditions = False

        if conditions == True:
            print("Account created successfully")
            self.client_details_list = [name, ph, password, cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")
    
    def login(self, name, ph, password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name
            else:
                print("Wrong Details")

    def credit(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt","r")as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))
                print("Amount credited successfully")
        else:
            print("Enter the correct value of amount")

    def Transfer_fund(self, amount, name, ph):
        with open(f"{name}.txt","r")as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TransferCash = True

        if self.TransferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")
            
            with open(f"{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("Amount Transfered Successfully to",name,"-",ph)
            print("Balacne left =",left_cash)
            self.cash = left_cash

    def debit(self, amount):
        if amount > 0:
            self.cash -= amount
            with open(f"{name}.txt","r")as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))
                print("Amount debited successfully")
        else:
            print("Enter the correct value of amount")        

    def password_change(self, password):
        if len(password) <= 8 or len(password) > 18:
            print("Enter password greater than or equal to 8 and less than 18 character")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print("new Password set up successfully")

    def ph_change(self , ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("new Phone number set up successfully")

if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to my Bank")
    print("1.Login")
    print("2.Creata a new Account")
    user = int(input("Make decision: "))

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1.Credit amount")
                print("2.Debit amount")
                print("3.Check Balcane")
                print("4.Tranfer amount")
                print("5.Edit profile")
                print("6.Logout")
                login_user = int(input())
                if login_user == 1:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.credit(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                
                if login_user == 2:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.debit(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                
                elif login_user == 3:
                    print("Balacne =",Bank_object.cash)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 4:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Transfer_fund(amount,name,ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif login_user == 5:
                    print("1.Password change")
                    print("2.Phone Number change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 6:
                    break
                        
                
    if user == 2:
        print("Creating a new  Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.register(name, ph, password)


#### Output
'''
Welcome to my Bank
1.Login
2.Creata a new Account
Make decision: 1      
Logging in  
Enter Name: Ramyaa
Enter Phone Number: 1234567891
Enter password: root123456
Ramyaa logged in
1.Credit amount
2.Debit amount
3.Check Balcane
4.Tranfer amount
5.Edit profile
6.Logout
1
Balance = 4000
Enter amount: 6000
Amount credited successfully

1.back menu
2.Logout
1
1.Credit amount
2.Debit amount
3.Check Balcane
4.Tranfer amount
5.Edit profile
6.Logout
2
Balance = 10000
Enter amount: 1000
Amount debited successfully
1.back menu
2.Logout
1.Credit amount
2.Debit amount
3.Check Balcane
4.Tranfer amount
5.Edit profile
6.Logout
3
Balacne = 9000
1.back menu
2.Logout
1
1.Credit amount
2.Debit amount
3.Check Balcane
4.Tranfer amount
5.Edit profile
6.Logout
4
Balance = 9000
Enter amount: 2000
Enter person name: Priya
Enter person phone number: 9876543210
Amount Transfered Successfully to Priya - 9876543210
Balacne left = 7000
1.back menu
2.Logout
1
1.Credit amount
2.Debit amount
3.Check Balcane
4.Tranfer amount
5.Edit profile
6.Logout
6
'''