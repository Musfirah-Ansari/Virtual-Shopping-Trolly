from Load import Load


class Selection(Load):
    currentUserList = []

    # To know that the user has viewed the menu at least once
    # After the menu has been viewed once, 'choose' method of the current class will be invoked to view the menu
    count = 0

    def initiator(self):

        # Selection.count = 0 means that the user is viewing the menu for the first time
        # 'choose' method of parent class 'Load' will be invoked
        if Selection.count == 0:
            Selection.count += 1
            super().choose()

        # This statement will run if the user is not visiting the menu for the first time
        else:

            # 'choose' method of current class will be invoked. Thus, this will override the choose method of parent class
            self.choose()

        self.userSelection()

    # This method will be invoked every time the user decides to view the menu
    def userSelection(self):

        while True:
            print("\nChoose an item from the given list (1-10):\nPress any other key to Go Back")
            try:

                # To select an item from the generated menu. It requires an integer input
                itemNo = int(input("-> "))

                # This block will run only when the input integer is in the given range i.e. (1-10)
                if 0 < itemNo <= 10:

                    # Selected Item along with the available stock will be displayed
                    print(f"How many {self.lst[itemNo-1][0]} you want to buy ({self.lst[itemNo-1][2]} in stock)?")

                    # To ask the user about the quantity of the selected item
                    quantity = int(input("-> "))

                    # A Check to confirm that the entered value is neither less than one nor greater than the available stock of that particular item
                    if (quantity > 0) and (quantity <= self.lst[itemNo-1][2]):
                        print(f"{quantity} {self.lst[itemNo - 1][0]} will cost {quantity * self.lst[itemNo - 1][1]} Rupees.")

                        # 'addItem' is invoked to add the selected item to the current cart of the user
                        self.addItem(itemNo, quantity)

                        # Confirmatory message to tell that the selected item has been inserted to the current cart
                        print(f"\n{self.lst[itemNo - 1][0]} has been added to your Cart! \n")

                        # To display the menu again
                        self.choose()

                    # This block will run if the quantity entered is either less than one or greater than the available stock of the selected item
                    else:
                        print("Invalid Entry!!!\nPlease Try Again\n")

                        # To display the menu again
                        self.choose()

                # This block will run if the input integer is out of range
                else:
                    print("Invalid Item No !!!")

                    # To display the menu again
                    self.choose()

            # If any non-integer value is inserted, then this except block will be invoked
            # It will break the loop
            except ValueError:
                break

    # To show same menu to the user when he asks
    def choose(self):

        count = 1

        # self.lst attribute is inherited from the 'Load' class
        # This is done to show the exact same menu to the user
        for i in self.lst:
            if count != 10:
                print(f" {count})\t{i[0]}, Rs. {i[1]}, Stock({i[2]})")
            else:
                print(f"{count})\t{i[0]}, Rs. {i[1]}, Stock({i[2]})")
            count += 1

    # This method is used to insert the selected item to the user's current cart
    def addItem(self, item, quantity):

        # To confirm whether the user wants to add the item to the cart or not
        inp = input("\nAdd to Cart? (Yes or No)\n-> ").lower()
        if inp == "yes":

            # Current Item along with quantity and other info will be inserted into the current cart of the user
            Selection.currentUserList.append(f"{self.lst[item-1][0]}-Price({self.lst[item-1][1]})-Quantity({quantity})-Total Price({self.lst[item-1][1] * quantity})")

            # To update the stock of the selected item
            self.lst[item-1][2] = self.lst[item-1][2] - quantity

        elif inp == "no":
            return

        else:
            print("\nInvalid Entry!!!\n")
