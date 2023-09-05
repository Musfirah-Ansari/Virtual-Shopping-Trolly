from Selection import Selection


class User:

    # Used to store name, pwd and current cart's items of current user in string format
    masterList = ""

    # Used to store name, pwd and cart's items of all users in list format
    globalList = []

    def __init__(self, name, password, state):

        self.values = state

        # To update the current cart of the user i.e. load the items of the current user from file if any to the current cart
        self.load(name, password)

        print(f"\n{name}, Welcome to Our Online Cart!")

        # Instantiating the 'Selection' class
        # As the 'Selection' class has no constructor, hence 'Load' class' constructor will be invoked
        self.current = Selection()
        self.value = False
        self.checkOutList = []
        self.checkOutValue = 0
        while True:
            print(f"\nFollowing are the available Options:\n1. View all "
                  f"Available Products\n2. View Your Shopping Cart\n3. Checkout\n4. View Shopping History\n5. Exit")
            try:
                # To take integer input i.e. 1, 2, 3, 4, or 5, from the user
                inp = int(input("-> "))

            # If the user enters a non-integer value, then except block will be invoked
            except ValueError:
                print("\nInvalid Entry!!!\n")
                continue

            # 'initiator' method of the 'Selection' class will be invoked
            # To show the menu of 10 randomly generated items present in the online shopping cart
            if inp == 1:
                self.current.initiator()

            # 'showlist' method of the current class will be invoked
            # To view the list of all items present in the current cart
            elif inp == 2:
                self.showList()

            # To Checkout from the 'Online Shopping Cart'
            elif inp == 3:
                if len(self.current.currentUserList) > 0:

                    # To tell no. of items currently in cart.
                    print(f"\nThere are currently {len(self.current.currentUserList)} Item(s) in your Cart !!!")

                    # self.checkOutList maintains the total price of each item in cart i.e. item's price * quantity
                    for i in range(len(self.current.currentUserList)):
                        x = self.current.currentUserList[i].split("-")[-1].split("(")[-1][0:-1]
                        self.checkOutList.append(x)

                    # self.checkOutValue stores the total amount which the user has to pay to buy all items present in current cart
                    for j in self.checkOutList:
                        self.checkOutValue += int(j)

                    print(f"Total Price of all Item(s) in your cart is {self.checkOutValue} Rupees.\nConfirm Check Out "
                          f"(Yes or No)? ")
                    check = input('-> ').lower()
                    if check == "yes":
                        print("\nYour Payment has been received !!!\n***** Thank you for shopping at our Online Cart "
                              "*****")

                        # After Checkout user's name, pwd, total payed amount etc. are saved in 'ShoppingHistory.txt'
                        with open("ShoppingHistory", "at+") as f:
                            f.write(f"{name}-{password}-{'-'.join(self.current.currentUserList)}-Total Payed Amount({self.checkOutValue})\n")

                        # This is done so that for any new user the count starts from zero
                        Selection.count = 0

                        # This is done to clear the current cart of the current user
                        Selection.currentUserList = []
                        break

                    else:

                        # If the user says no, then this method is invoked which displays the list of items in current cart
                        # self.values = 'notLogged'
                        self.showList()

                # This block executes when current cart is empty
                else:
                    print("\nZero Items in Cart! \n")

            # To view the shopping history of the current user (if any)
            elif inp == 4:

                # A check to confirm that the user is a logged-in user
                if state == "logged":
                    with open("ShoppingHistory", "rt+") as f:
                        f.seek(0)

                        # To store the shopping history of current user in lst
                        lst = []
                        for i in f.readlines():
                            lst.append(i.strip("\n").split("-"))

                        # This will execute if the lst is not empty
                        if len(lst) != 0:
                            count1 = 0
                            for j in lst:

                                # Displays the entire shopping history of the current user
                                if name == j[0] and password == j[1]:
                                    if count1 == 0:
                                        print("\nYour Shopping History: \n")

                                    count1 += 1
                                    print("-> " + '-'.join(j[2:]))

                            # This will execute it there were no matches
                            if count1 == 0:
                                print("\nYou have no shopping history!\n")

                        # This will execute if lst is empty
                        else:
                            print("\nYou have no shopping history! \n")

                # This runs if the user is a new user, as a new user cannot have a shopping history
                else:
                    print("\nYou have no shopping history! \n")

            # To leave the current class and jump back to the main 'Interface' class
            # If there are any items in the user's current cart, then they are saved in globalList and then written in file
            # This is done so that when the user logs-in, he is able to get back the items of his cart
            elif inp == 5:

                # A string which consist of current user's name, pwd and the items with info from the current cart
                User.masterList = name + "-" + password + "-" + '-'.join(self.current.currentUserList)

                # A check to confirm that the current cart is not empty
                if len(self.current.currentUserList) != 0:

                    # A check to confirm that the 'globalList' is not empty
                    if len(User.globalList) > 0:
                        count = 0

                        # Checking whether the globalList consist of the items of current user by comparing the username and password of the current user
                        for i in range(len(User.globalList)):
                            x = User.globalList[i].split("-")[0]
                            y = User.globalList[i].split("-")[1]
                            if (name != x) or (password != y):

                                # This will help us to know that there were no matches
                                count += 1

                            # This block will execute if the current user has a record and he is a logged-in user
                            if name == x and password == y and state == "logged":

                                # This is done so that to append only those items of the current user to globalList which are not there.
                                # B/c items which are already stored in globalList also appears in the current cart and if we append the entire current cart, then there would be duplicates
                                # To overcome this issue, the following code was helpful
                                length = len(User.globalList[i].split("-"))

                                # This dictionary is made by making an assumption that there are maximum 10 items in the current cart of the user
                                dic = {
                                    6: "1",
                                    10: "2",
                                    14: "3",
                                    18: "4",
                                    22: "5",
                                    26: "6",
                                    30: "7",
                                    34: "8",
                                    38: "9",
                                    42: "10"
                                }

                                # This block will only execute if items of current user were saved in 'UserCartInfo.txt' and they were appended to the current cart of the user
                                if self.value == "True":

                                    # To append only the unique items in globalList
                                    # This is done by using the key, value pairs of 'dic'
                                    User.globalList[i] = User.globalList[i] + "-" + '-'.join(self.current.currentUserList[int(dic[length]):])

                                # This will execute if the current user has no current cart items saved in 'UserCartInfo.txt'
                                else:
                                    User.globalList[i] += "-" + '-'.join(self.current.currentUserList)

                                # To revert the counter back to zero and break the loop
                                count = 0
                                break

                        # This block will execute if the user has no previous records i.e. he is a new user
                        if len(User.globalList) == count and state != "logged":

                            # Thus, the string 'masterList' will directly be appended to 'globalList'
                            User.globalList.append(User.masterList)

                        # To write the records of all users present in globalList to the 'UserCartInfo.txt'
                        # Write mode is selected instead of Append to reduce complexity in updating of records of the current carts of all users
                        with open("UserCartInfo", "wt+") as f:
                            for i in range(len(User.globalList)):
                                f.write(f"{User.globalList[i]}\n")

                    # If the globalList is empty, then this will execute
                    # Current cart items will directly be appended to globalList i.e. no need to search for existing records
                    # As the list is empty, it means that there are no records in globalList
                    if len(User.globalList) == 0:
                        User.globalList.append(User.masterList)

                        # To write the records in 'UserCartInfo.txt'
                        with open("UserCartInfo", "wt+") as f1:
                            f1.write(f"{User.globalList[0]}\n")

                # This block will execute if the current cart is empty
                # This also means that the user may have removed all items from his cart. Thus, the globalList and 'UserCartInfo.txt' are also updated
                # If there are any existing records of the current user, then all those records all deleted from the 'globalList'
                # Which also means that they are also removed from the 'UserCartInfo.txt'
                if len(self.current.currentUserList) == 0:
                    for i in range(len(User.globalList)):
                        x = User.globalList[i].split("-")[0]
                        y = User.globalList[i].split("-")[1]

                        # Matching username and password, so that the records of other users are not affected
                        if name == x and password == y:

                            # Deleting the records of current user
                            del User.globalList[i]

                    # Again updating the 'UserCartInfo.txt'
                    with open("UserCartInfo", "wt+") as f:
                        for i in range(len(User.globalList)):
                            f.write(f"{User.globalList[i]}\n")

                # Class variable of 'Selection' class is again set to zero
                # As it is a class variable, we have to manually reset it
                Selection.count = 0

                # To make the current cart empty, as the current user is exiting from the 'User' class
                Selection.currentUserList = []
                break

            # This block will execute if the input integer is out of range
            else:
                print("\nInvalid Entry!!!\n")

    # This method is responsible to show the items of the current cart to the user
    def showList(self):

        # This block will execute if the current cart of the user is empty
        if len(self.current.currentUserList) == 0:
            print("\nThere are currently 0 items in your cart! \n")

        # This will execute if the current cart is not empty
        else:
            print("Following item(s) are currently in your Cart:\n")

            # To print all items of the current cart
            for i in self.current.currentUserList:
                print(f"-> {i}")

            print("\nDo You want to remove an Item(Yes or No)? ")

            ip = input("-> ").lower()

            # To remove a specific item from the current cart
            if ip == "yes":
                try:
                    count = int(input("Which Item do you want to remove from your cart(1, 2, etc)?\n-> "))
                    if count > len(self.current.currentUserList):
                        print("Incorrect Item No. !!!")

                    # This block of code will remove the item from the current cart corresponding to the inserted item no. by the user
                    else:

                        # Confirmatory message to tell the user that the item has been removed
                        print(f"\n{''.join(self.current.currentUserList[count - 1].split('-')[0])} has been removed "
                              f"from your cart! \n")

                        # Removing item
                        del self.current.currentUserList[count - 1]

                        # value of self.values is changed so that when 'showList' is again invoked, there is no need to load the items again from the 'UserCartInfo.txt'
                        # Otherwise, there would be duplicates and more complexity in our application
                        self.values = "notLogged"

                except ValueError:
                    print("Invalid Item No. !!!")

                # If the item no is out of range then this block will execute

            else:
                pass

    def load(self, name, password):

        # A check to know whether the current user is a new user or a logged-in user
        if self.values == "logged":

            # To load the saved cart of the logged-in user from 'UserCartInfo.txt'
            with open("UserCartInfo", "rt+") as f:

                # Items will be stored in this list
                lst = []
                f.seek(0)
                for i in f.readlines():
                    lst.append(i.strip("\n").split("-"))

                # The key, value pairs in dictionary, count1 and count2 local variables are used in slicing the loaded cart
                # This is done to only extract the items with their info, as the saved cart also consist of the current user's username and password.
                count1 = 2
                count2 = 6

                # To decide the no. of iterations the for loop will make
                dic = {
                    6: "1",
                    10: "2",
                    14: "3",
                    18: "4",
                    22: "5",
                    26: "6",
                    30: "7",
                    34: "8",
                    38: "9",
                    42: "10"
                }
                for j in lst:
                    x = len(j)
                    if (j[0] == name) and (j[1] == password):

                        # 'dic' is used here
                        for i in range(int(dic[x])):
                            # This is done to know whether there are items of the current user saved in the .txt file or not
                            self.value = "True"

                            # To append the items of the current user in his current cart
                            Selection.currentUserList.append('-'.join(j[count1: count2]))

                            # updating the count1 and count2 so that the other items (if any ) are also included in current cart
                            count1 += 4
                            count2 += 4
