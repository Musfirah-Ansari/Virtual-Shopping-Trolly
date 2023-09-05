import random as r
from items import mainLst


class Load:
    def __init__(self):

        # Stores the randomly selected items
        # This will be used by the Child class 'Selection' to show the exact same menu to the user
        self.lst = []

    # To randomly select 10 items from 'mainList' present in 'Items.py'
    def choose(self):

        count = 1
        while True:

            # Choosing random items
            x = r.choice(mainLst)
            if count < 11:

                # A check to confirm that no item is shown more than once in the menu i.e. no item is stored more than once in self.lst
                if x not in self.lst:
                    if count != 10:
                        print(f" {count})\t{x[0]}, Rs. {x[1]}, Stock({x[2]})")
                    else:
                        print(f"{count})\t{x[0]}, Rs. {x[1]}, Stock({x[2]})")

                    # To insert all the randomly selected items into self.lst
                    self.lst.append(x)
                    count += 1

                # If the item is already there is self.lst, then loop will jump to next iteration
                else:
                    continue

            # Loop breaks when exactly 10 items are appended in self.lst
            else:
                break
