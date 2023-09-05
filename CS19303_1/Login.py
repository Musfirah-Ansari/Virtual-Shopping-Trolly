from User import User


class Login:
    def __init__(self):

        self.name = ""
        self.password = ""

        # To store all user's account info from 'AccountInfo.txt'
        self.lst = []
        self.count = 0

        # This method will be called automatically when the class instantiate
        self.checkLogin()

    # This method ask the user to enter name and password
    def checkLogin(self):

        self.name = input("Enter Username: ")
        self.password = input("Enter Password: ")
        print("Checking ... ")
        input()

        # To verify that whether there is an account with the same name and password stored in 'AccountInfo.txt'
        self.verify()

    def verify(self):

        with open("AccountInfo.txt", "rt+") as f:
            f.seek(0)
            for i in f.readlines():
                self.lst.append(i.strip("\n").split("-"))

            # Methods to confirm whether the enter username and password matches with any of the saved accounts
            self.checkUsername()
            self.checkPassword()

            # This code executes if the username and password matches
            if self.count == 2:

                # 'User' class will be instantiated
                # 'logged' is passed as an arg. to tell that the current user is a logged-in user
                User(self.name, self.password, "logged")

            # This block executes if the entered username and password matches none of the saved usernames and passwords
            else:
                print("Username or Password does not match !!!")

    # self.count is used to confirm that both username and password matches with the saved records
    def checkUsername(self):

        for i in self.lst:
            if i[0] == self.name:
                self.count += 1
                break

    def checkPassword(self):

        for i in self.lst:
            if i[1] == self.password:
                self.count += 1
                break
