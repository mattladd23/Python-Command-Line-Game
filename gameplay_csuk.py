# The gameplay python file includes classes and functions from each of the character and levels files along with
# additional packages such as time and country list to improve the usability of the game.

from character_csuk import Character
from levels_csuk import playWHSmith, selectTransport, pubOrCosta, enterPremier
from time import sleep
from country_list import countries_for_language

# The whole game is called within a class to draw together aspects of the game setup of such as creating a new game or
# loading a saved game.


class CsukGame:

    def __init__(self):
        pass

    # The constructor is left as pass because each of the play, new game and load game each possess rather different
    # attributes.

    def playCSUK(self, player1):

        # The game title CULTURE SHOCK is displayed to indicate to the user that the game is running.

        print("CULTURE SHOCK UK\n")

        # A while loop is used to re-prompt the user in case they enter invalid input.

        while True:
            player_choice = input("Please select an option:\n"
                                  
                                  "\nNew Game - <new>\n"
                                  "Load Game - <load>\n->")

            # The player's input is converted to lower case to ensure that the player doesn't need to worry about case
            # sensitivity.

            player_choice = player_choice.lower()
            if player_choice == "new":

                # An instance of player_x is passed through the function because the instance of player 1 is yet to
                # have been created.

                game.newGame(player_x)
                break
            elif player_choice == "load":
                with open("save_csuk.txt") as f_obj:

                    # The player data is first checked to see whether any previous user has saved their credentials.

                    contents = f_obj.read()
                    if contents == "":
                        print("No saved player data has been found!")
                    else:
                        game.loadGame()
                        break
            else:
                print("Invalid input.")

    def newGame(self, player1):

        # Upon starting a new game, the rules are gradually read to the player. The sleep function is used to stagger
        # each piece of information, preventing the player from being overwhelmed.

        print("Welcome to Culture Shock UK!\n")
        sleep(2)
        print("The aim of the game is plain and simple - get from Pyford International Airport to your Premier Inn\n"
              "with enough money and energy left over!\n")
        sleep(5)
        print("Remember - you'll need £10 left over to pay for your room deposit... so spend your money wisely!\n")
        sleep(3)
        print("You'll also need 20 energy to complete your reservation and get settled in your room.\n")
        sleep(3)
        print("You will start the game with £50 and 100 energy.\n")
        sleep(2)
        print("All valid commands will be presented to you between echelons <like so>. Write your commands next to\n"
              "the illustrative arrow (->).\n")
        sleep(4)
        print("Depending on the path you take to the Premier Inn, you will have either one or two checkpoints at\n"
              "which you'll be able to manually save your progress and/or quit the game.\n")
        sleep(4)
        print("Your progress will be saved automatically once you arrive at the Premier Inn.\n")
        sleep(3)
        print("Ready??\n")
        sleep(2)
        print("Let's go!\n")

        # The character creation process begins here. The game collects the player's name, gender and country of origin.

        # The process starts with character name creation below.

        while True:
            char_name = input("Please start by entering your name...\n->")

            # The player's name is sanitise to make sure the game always displays it in title case.

            char_name = char_name.title()
            if len(char_name) < 25 and char_name != "":
                print(f"Nice to meet you {char_name}! It's great to have you here in the UK!\n")
                player1.setName(char_name)
                break
            else:
                print("Names must not be left blank or contain more than 25 characters.\n")

        # Character gender creation

        while True:
            gender = input("Could you please enter your gender ('m' or 'f'):\n->")
            gender = gender.lower()
            if gender == "m" or gender == "f":
                player1.setGender(gender)
                break
            else:
                print("Invalid input.\n")

        # Character country of origin creation

        while True:

            # The 'countries_for_language' library enables the game to check whether the player has entered a real
            # country to add to the realism of the game.

            list_countries = dict(countries_for_language("en"))
            countries = list_countries.values()

            co = input(f"\nSo {char_name}, where have you flown from today? Please enter a country.\n->")

            # The player's input is sanitised and converted into title case to agree with the case sensitivity of how
            # the country names are stored in the library.

            co = co.title()

            if co in countries:
                player1.setCO(co)
                print(f"\nLovely. I hear {co} is nice at this time of the year!")
                sleep(2)
                print(f"\nLet's play Culture Shock UK!\n")
                sleep(2)
                playWHSmith(player1)
                break
            else:
                print(f"Hmmm, I'm afraid that doesn't ring a bell... Please enter a valid country.\n")

    def loadGame(self):

        # The load function begins by locating and reading each line of the 'save_csuk.txt' file. Each line index is
        # then passed through the player_data variable. Each player credential is stored on a separate line.

        with open("save_csuk.txt") as f_obj:
            lines = f_obj.readlines()
        list_of_lines = list(lines)

        player_data = []

        for x in list_of_lines:
            x = x.strip("\n")
            player_data.append(x)

        # Each attribute of a given instance of the character class is assigned to a particular index of the
        # player_data variable.

        player1 = Character(player_data[0], player_data[1], player_data[2], int(player_data[3]), int(player_data[4]),
                            player_data[5], player_data[6], player_data[7])

        load_balance = int(player_data[3])
        player1.setBalance(load_balance)

        load_energy = int(player_data[4])
        player1.setEnergy(load_energy)

        # The player's 'backpack'/inventory is loaded by storing the item name and appending it back to the 'backpack'
        # variable. The 'includeItem' function performs the same task as 'addToBackpack' but doesn't notify the user,
        # to allow for a smoother loading of the game.

        if player_data[9] == "umbrella":
            player1.includeItem("umbrella")
        elif player_data[9] == "ukulele":
            player1.includeItem("ukulele")
        elif player_data[9] == "phrase book":
            player1.includeItem("phrase book")

        # Each player_data index [5] through to [7] contains the flags of whether the player has passed each checkpoint.
        # If a flag is assigned to "True", the appropriate function is called depending on where the player is in the
        # game.

        if player_data[7] == "True":
            player1.reachedC3()
            print(f"Welcome back {player1.getName()}!")
            enterPremier(player1)

        elif player_data[6] == "True":
            player1.reachedC2()
            print(f"Welcome back {player1.getName()}!")
            pubOrCosta(player1)

        elif player_data[5] == "True":
            player1.reachedC1()
            print(f"Welcome back {player1.getName()}!")
            selectTransport(player1)


# An instance of Character is declared as player_x to represent the player prior to creating a character. The
# subsequent use of player1 represents the player using a character that has already been created.

# player = Character("", "", "", 50, 100, False, False, False)
player_x = Character("", "", "", 50, 100, False, False, False)

game = CsukGame()
game.playCSUK(player_x)
