def new_client():
    while True:
     user_firstname = input("Enter your first name: ")
     user_lastname = input("\nEnter your last name: ")
     user_password = input("Enter your password. It must be four digits and between 1000 and 9999: ")
     for user_password in range(1000,9999):
        password_confirm = input("Confirm your password: ")
        for password_confirm in range(1000,9999):
            if password_confirm == user_password:
                print("Password set successfully")
                return password_confirm
        else:
            print("Passwords do not match, kindly try again")
     else:
        print("pin entered is not within the range, kindly try again")
     user_data = [user_firstname, user_lastname, password_confirm]
     return user_data    
    
    



def main_menu():
    print("Welcome to NEO bank, your trusted banking service")
    print("Good morning Mr. ")





print("Welcome to NEO bank\n")
print("If you are a customer, press 1 and if you are a new client, press 2")
user_response = input("\nresponse: ")
if user_response == '2':
    new_client()
    main_menu()
elif user_response == '1':
    main_menu()





    