from User import User


class Accounts(User):
    def __init__(self):

        self.username = ""
        self.password = ""
        self.firstName = ""
        self.lastName = ""
        self.address = ""
        self.lst = []
        self.nameCount = 0
        self.check = False
        self.collectInfo()
        self.saveInfo()

        # If self.check is False, then Constructor of 'User' class will be invoked
        # 'notLogged' is passed as an arg. to tell that the user has created a new account
        if not self.check:
            super().__init__(self.username, self.password, 'notLogged')

    # To collect all required information from the User
    def collectInfo(self):

        self.username = input("Enter a Username: ")
        self.password = input("Enter a Password: ")
        self.firstName = input("Enter First Name: ")
        self.lastName = input("Enter Last Name: ")
        self.address = input("Enter your Address: ")
        print()
        self.validate()

    # To verify that the user has not inserted an empty string in any of the given fields
    # if length of values of any of the input fields is Zero, then default values will be assigned to the respective fields.
    def validate(self):

        if len(self.username) == 0:
            self.username = "defaultUsername"
            print(f"-> '{self.username}' has been assigned as your Username!")

        if len(self.password) == 0:
            self.password = "defaultPassword"
            print(f"-> '{self.password}' has been assigned as your Password!")

        if len(self.firstName) == 0:
            self.firstName = "defaultFirstName"
            print(f"-> '{self.firstName}' has been assigned as your First Name!")

        if len(self.lastName) == 0:
            self.lastName = "defaultLastName"
            print(f"-> '{self.lastName}' has been assigned as your Last Name!")

        if len(self.address) == 0:
            self.address = "defaultAddress"
            print(f"-> '{self.address}' has been assigned as your Address!")

        input("\nPress any Key to Continue... ")

        self.checkInfo()

    # To store the information of all created accounts from 'AccountsInfo.txt' in self.lst
    def checkInfo(self):

        with open("AccountInfo.txt", "rt+") as f:
            f.seek(0)
            for i in f.readlines():
                self.lst.append(i.strip("\n").split("-"))

            self.checkUsername()

    # To verify that the entered username or the default username has not been taken
    def checkUsername(self):

        for i in self.lst:
            if i[0] == self.username:
                self.nameCount += 1
                break

    # To save the User's info in 'AccountInfo.txt'
    def saveInfo(self):

        # If the username is already taken, then value of self.check will become 'True'
        # As a result Parent Class' Constructor will not be invoked
        # If self.nameCount is not equal to zero, then it means that the username has been taken by some other user
        if self.nameCount != 0:
            print("\nUsername is already taken!\nPlease Try Again !!!\n")
            self.check = True

        # If the username is not taken, then all the information of the user will be saved in 'AccountsInfo.txt'
        else:
            with open("AccountInfo.txt", "at+") as f:
                f.write(f"{self.username}-{self.password}-{self.firstName}-{self.lastName}-{self.address}\n")
