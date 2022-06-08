
class Character:
    # Player's name field.
    char_name = ""

    # Player's gender field.
    gender = ""

    # Player's nationality field.
    country_origin = ""

    # A player's bank balance always starts at £50. Balance is cast as a float to cater for negative values, in case
    # the player runs out of money before arriving at the Premier Inn.
    balance = 50

    # A player's energy always starts at 100. Energy is also cast as a float in order to cater for negative values,
    # in case the player runs out of energy before arriving at the Premier Inn.
    energy = 100

    # A player's backpack will begin empty and will remain so, should they not purchase any items
    backpack = []

    # A player's location will be determined by whether they have reached each checkpoint.

    c1_reached = False

    c2_reached = False

    c3_reached = False

    def __init__(self, char_name, gender, co, balance, energy, c1_reached, c2_reached, c3_reached):
        self.char_name = char_name
        self.gender = gender
        self.co = co
        self.balance = balance
        self.energy = energy
        self.c1_reached = c1_reached
        self.c2_reached = c2_reached
        self.c3_reached = c3_reached

# Getters, setters and other methods for character class attributes

# Name

    def getName(self):
        return self.char_name

    def setName(self, char_name):
        self.char_name = char_name

# Gender

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

# Country of origin

    def getCO(self):
        return self.co

    def setCO(self, co):
        self.co = co

# Balance

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def incrBalance(self, amount):
        self.balance += amount

    def decrBalance(self, amount):
        self.balance -= amount

# Energy

    def getEnergy(self):
        return self.energy

    def setEnergy(self, energy):
        self.energy = energy

    def incrEnergy(self, amount):
        self.energy += amount

    def decrEnergy(self, amount):
        self.energy -= amount

# Show both balance and energy

    def showRemaining(self):
        print(f"\nYou currently have £{self.balance} and {self.energy} energy.\n")

# Checkpoints reached

    def reachedC1(self):
        self.c1_reached = True

    def pastC1(self):
        return self.c1_reached

    def reachedC2(self):
        self.c2_reached = True

    def pastC2(self):
        return self.c2_reached

    def reachedC3(self):
        self.c3_reached = True

    def pastC3(self):
        return self.c3_reached

    def resetProgress(self):
        self.c1_reached = False
        self.c2_reached = False
        self.c3_reached = False

# Backpack / Inventory

    def addToBackpack(self, item_name):
        print(f"** {item_name} added to backpack **")
        self.backpack.append(item_name)

    def includeItem(self, item_name):
        self.backpack.append(item_name)

    def clearBackpack(self, item_name):
        self.backpack.pop(item_name)

    def getBackpack(self):
        return self.backpack

    def printBackpack(self):
        print("Lets have a look...\n")
        if len(self.backpack) > 0:
            for item_name in self.backpack:
                print(f"{item_name}")
        else:
            print("You have no items in your backpack.")

    def checkIfBought(self, item_name):
        has_purchased = False
        item = str(item_name)
        if item in self.backpack:
            has_purchased = True
        return has_purchased


player_x = Character("", "", "", 50, 100, False, False, False)
