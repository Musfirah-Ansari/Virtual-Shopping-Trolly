from Load import Load
from Login import Login
from Accounts import Accounts


class Interface(Accounts, Load):
    def __init__(self):

        print("********** WELCOME TO OUR ONLINE SHOPPING CART **********\n")
        while True:
            print("\nFollowing are the available options:\n1. Create an Account\n2. Login\n3. Exit")
            try:
                # To take an input integer i.e. 1, 2, or 3, from the user
                inp = int(input("-> "))

            # If the user enters a non-integer value, then except block will be invoked
            except ValueError:
                print("\nInvalid Entry!!!\n")
                continue

            # Constructor of 'Accounts' class will be invoked
            if inp == 1:
                super().__init__()

            # 'Login' class will be instantiated
            elif inp == 2:
                Login()

            # User will exit the 'Online Shopping Cart'
            elif inp == 3:
                print("Goodbye and have a nice day!")
                break

            # If the user enters an integer other than (1, 2, 3), then loop will jump to next iteration
            else:
                print("\nInvalid Entry!!!")


Interface()
