def create_new_acc():
     print("you choose 1-create new acccount")
     customer_file=open("customer_file.txt","a")
     transaction_file=open("transaction_file.txt","a")
     new_customer_id=str(input("enter new customer ID:"))
     new_customer_name=str(input("enter new customer NAME:"))
     new_customer_address=str(input("enter new customer ADDRESS:"))
     new_customer_phone=str(input("enter new customer PHONE:"))
     new_customer_pass=str(input("enter new customer PASS:"))
     new_customer_balance=str(input("enter new customer BALANCE:"))

     customer_file.write(new_customer_id+","+new_customer_name+","+new_customer_address+","+new_customer_phone+","
                         +new_customer_pass+","+new_customer_balance+"\n"+"\n")
     customer_file.close()
     transaction_file.write(new_customer_id+","+new_customer_balance+",Deposit\n"+"\n")
     transaction_file.close()
     print("***NEW ACCOUNT CREATED!***")
     print("RETURN TO MAIN MENU")
     main_menu()

def search_cust_data():
     print("you chose 2-search customer data")
     custom_id=str(input("enter customer ID:"))
     customer_file=open("customer_file.txt","r")
     for line in customer_file:
          search_customer=line.strip().split(",")
          if(custom_id==search_customer[0]):
               print("ID\t:"+search_customer[0]+"\nNAME\t:"+search_customer[1]+"\nADDRESS\t:"+search_customer[2]+"\nPHONE NUMBER\t:"+search_customer[3])
               print()
               print("RETURN TO MAIN MENU")
               print()
               main_menu()
               return True
     print("DATA NOT FOUND")
     print()
     print("RETURN TO MAIN MENU")
     print()
     main_menu()

def deposite_money():
     print("you chose: 3-DEPOSITE MONEY")
     deposite_id=str(input("ENTER YOUIR CUSTOMER ID:"))
     deposite_balance=str(input("enter the BALANCE to deposite"))
     deposite_pass=str(input("enter your PASS"))
     customer_file=open("customer_file.txt","r")
     transaction_file=open("transaction_file.txt","a")
     for line in customer_file:
          cust_deposite=line.strip().split(",")
          if(deposite_id==cust_deposite[0] and deposite_pass==cust_deposite[4]):
               transaction_file.write(deposite_id+","+deposite_balance+",deposite\n")
               transaction_file.close()
               print("money deposited")
               print("RETURN TO MAIN MENU")
               main_menu()
               return True
     print("YOU ENTERED WRONG PASSWORD")
     print("return to main menu")
     main_menu()
     return False


def withdraw_money():
     print("you chose 4-withdraw money")
     current_balance=balancee_view()
     print(current_balance)
     
     withdraw_id=str(input("ENTER YOUR CUSTOMER ID:"))
     withdraw_balance=str(input("enter the BALANCE to withdraw:"))
     withdraw_pass=str(input("ENTER YOUR PASS"))
     customer_file=open("customer_file.txt","r")
     transaction_file=open("transaction_file.txt","a")
     for line in customer_file:
          cust_withdraw=line.strip().split(",")
          if(withdraw_id==cust_withdraw[0] and withdraw_pass==cust_withdraw[4]):
               transaction_file.write(withdraw_id+",-"+withdraw_balance+",deposite\n")
               transaction_file.close()
               print("money withdraw done")
               print("return to main menu")
               main_menu()

     print("YOU ENTERED WRONG PASSWORD")
     print("return to main menu")
     main_menu()


def balance_view():
     print("you chose 5-view balance")
     current_balance=0
     view_id=str(input("enter your customer ID:"))
     transaction_file=open("transaction_file.txt","r")
     for line in transaction_file:
          view_balance=line.strip().split(",")
          if(view_id==view_balance[0]):
               current_balance=int(view_balance[1])+current_balance
            
     print("current balance:",current_balance)
     print("return to main menu")
     main_menu()

def balancee_view():
     
     current_balance=0
     view_id=str(input())
     transaction_file=open("transaction_file.txt","r")
     for line in transaction_file:
          view_balance=line.strip().split(",")
          if(view_id==view_balance[0]):
               current_balance=int(view_balance[1])+current_balance
            
     return(current_balance)
     main_menu()


def bank_balance():
     print("you chose 6-check total bank balance")
     current_balance=0
     transaction_file=open("transaction_file.txt","r")
     for line in transaction_file:
          view_balance=line.strip().split(",")
          current_balance=int(view_balance[1])+current_balance

     print("total bank balance:",current_balance)
     print("RETURN TO MAIN MENU")
     main_menu()
           




























def main_menu():
    print("1-create new account\n2-search customer data\n3-deposite money\n4-withdraw money\n5-view balamnce\n6-check total balance in bank")
    
    while True:
          choice=int(input("choose one option:"))
          match choice:
               case 1:
                    create_new_acc()
               case 2:
                    search_cust_data()
               case 3:
                    deposite_money()
               case 4:
                    withdraw_money()
               case 5:
                    balance_view()
               case 6:
                    bank_balance()
               case 7:
                    break
main_menu()              

               
             





     