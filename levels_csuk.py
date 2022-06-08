# The levels_csuk file represents the world with which the Character instances interact with. Each level is declared
# as a method. The time package is used throughout to stagger the output of each level, thus improving the overall
# usability of the game.

from time import sleep
from character_csuk import Character

# At the top of the file, each of the possible items a player can collect are written as dictionaries to store each
# item's name, price and information about how it can assist the player throughout the game.

umbrella = {"item_name": "umbrella", "price": 14,
            "info": "Do bear in mind that the UK experiences a lot of rainfall - getting wet could be the\n"
                    "last thing you need when trying to conserve energy!\n"}

ukulele = {"item_name": "ukulele", "price": 16,
           "info": "Playing a ukulele could be a great way to busk in public places (particularly around\n"
                   "train stations) if you're a bit short for money!\n"}

phrase_book = {"item_name": "phrase book", "price": 17,
               "info": "Many people who come to the UK suddenly become aware of all the slang we brits\n"
                       "use! This little book may help your interactions with locals go just that bit smoother...\n"}

# After the items, the potential modes of transport a player can take from the airport are also written as dictionaries
# to store each mode of transport's price and energy that would be used during the journey; bus being the most tiring
# and taxi being the least.

bus = {"price": 5,
       "energy_required": 17}

train = {"price": 14,
         "energy_required": 11}

taxi = {"price": 42,
        "energy_required": 0}


# Save logic is included in the levels file, so it can be shadowed by the level methods that follow. The saveGame
# function can be called at three separate checkpoints throughout the game. The first two can be executed manually at
# the player's will. Meanwhile, the final checkpoint saves automatically when the game's outcome has been determined.

def saveGame(player1):
    with open("save_csuk.txt", "w") as f_obj:

        f_obj.write(f"{player1.getName()}\n")
        f_obj.write(f"{player1.getGender()}\n")
        f_obj.write(f"{player1.getCO()}\n")
        f_obj.write(f"{player1.getBalance()}\n")
        f_obj.write(f"{player1.getEnergy()}\n")
        f_obj.write(f"{player1.pastC1()}\n")
        f_obj.write(f"{player1.pastC2()}\n")
        f_obj.write(f"{player1.pastC3()}\n")

        f_obj.write("Backpack:")

        for i in player1.getBackpack():
            f_obj.write(f"\n{i}")

# For the first level, the character arrives in the UK at the airport and is taken to a WH Smith to buy some potentially
# useful items.


def playWHSmith(player1):

    print("Welcome to Pyford International Airport. I hope you had a comfortable flight!\n"
          "       __|__\n"
          "--------(_)--------\n"
          "  @  @       @  @ \n")

    # Aeroplane ascii art is taken from https://www.asciiart.eu/vehicles/airplanes

    sleep(3)

    print("Before you begin your journey across Pyford to find your Premier Inn, I would suggest\n"
          "stopping off at this reputable British store, WH Smith, to find some useful items to help\n"
          "you on your way...\n")

    sleep(5)

    while True:

        # Game receives input from user to explore each potential item on offer.

        select_item = input("Enter an item to find out its price and utility: <umbrella>, <ukulele> or <phrase book>:\n"
                            "->")

        # Player's input is sanitised to ensure case sensitivity doesn't impact the gameplay.

        select_item = select_item.lower()
        if select_item == "umbrella":
            print(f"""
                  .-^-.
                 /_/_\_\.
                ' ' | ` `
                    j

"""
                  # Umbrella ascii art is from https://www.asciiart.eu/clothing-and-accessories/umbrellas
                  
                  f"An {umbrella.get('item_name')} costs £{umbrella.get('price')}...\n"
                  f"{umbrella.get('info')}")
            sleep(3)

            # Let player know how much money and energy they have remaining.

            player1.showRemaining()

            # playWHSmith() method only breaks on the condition that the player chooses to purchase and item in the
            # following method purchaseItem().

            did_purchase = purchaseItem(select_item, player1)
            if did_purchase:
                break
            else:
                pass

        elif select_item == "ukulele":
            print(f"""
            ( o )==::
                       
"""
                  # Ukulele art is from https://just.4str.in/ascii-art-ukulele/
                  f"A {ukulele.get('item_name')} costs £{ukulele.get('price')}...{ukulele.get('info')}")
            sleep(3)

            # Let player know how much money and energy they have remaining.

            player1.showRemaining()

            # As stated above, playWHSmith() method only breaks on the condition that the player chooses to purchase
            # and item in the following method purchaseItem().

            did_purchase = purchaseItem(select_item, player1)
            if did_purchase:
                break
            else:
                pass

        elif select_item == "phrase book":
            print(f"""
                 _______
               /Oxford /,
              /English//
             /_______//
            (_______(/
            
"""
                  f"A {phrase_book.get('item_name')} costs £{phrase_book.get('price')}...{phrase_book.get('info')}")
            sleep(3)

            # Let player know how much money and energy they have remaining.

            player1.showRemaining()

            # As stated above, playWHSmith() method only breaks on the condition that the player chooses to purchase
            # and item in the following method purchaseItem().

            did_purchase = purchaseItem(select_item, player1)
            if did_purchase:
                break
            else:
                pass

        else:
            print("Input not recognised.\n")

    selectTransport(player1)


# Method to confirm whether a player would like to buy an item having now view its price and information.


def purchaseItem(select_item, player1):

    # Initialise the flag to false so player begins with no items in their backpack.

    has_purchased = False

    while True:
        sleep(2)

        # Receives player's decision.

        buy_item = input(f"Would you like to purchase this {select_item}? Press <y> to buy or <n> to view other "
                         f"items...\n->")

        # Sanitise input to prevent case sensitivity impacting gameplay.

        buy_item = buy_item.lower()

        if buy_item == "y":

            # Initialise item_price before declaring a new local variable.

            item_price = 0
            if select_item == "phrase book":
                item_price = phrase_book.get("price")
            elif select_item == "ukulele":
                item_price = ukulele.get("price")
            elif select_item == "umbrella":
                item_price = umbrella.get("price")
            player1.decrBalance(item_price)
            print(f"Item purchased!")
            sleep(2)

            # Let player know how much money and energy they have remaining.

            player1.showRemaining()

            # Add selected item to players backpack.

            player1.addToBackpack(select_item)
            has_purchased = True
            break
        elif buy_item == "n":
            print("You chose not to buy this item.")
            break
        else:
            print("Input not recognised.")

    return has_purchased


def selectTransport(player1):

    # Call reachedC1() to change Character attribute to show it is now "True" that player has reached checkpoint 1.

    player1.reachedC1()

    sleep(2)

    print("\nYou have successfully reached checkpoint 1!\n")

    sleep(2)

    print("\nNow you've had the chance to equip yourself for your journey, let's pick a mode of transport to get to\n"
          "Pyford City Centre...\n")

    sleep(3)

# Give player options to choose a mode of transport, save the game manually or quit the game. If the player wishes,
# they may save their progress and then exit the game.

    while True:
        select_transport = input("Enter a mode of transport to view its price. Having past checkpoint 1, you can now\n"
                                 "save your progress.\n"
                                 
                                 "\nGet the <bus> to the main station\n"
                                 "Get the <train> to the main station\n"
                                 "Get a <taxi> straight to your Premier Inn!!\n"
                                 "Save game <save>\n"
                                 "Exit game without saving <exit>\n->")

        select_transport = select_transport.lower()

        # When the player selects a mode of transport, they will be able to read about the price and information of
        # each. A message will also be displayed, so they can view their balance before making a decision.

        if select_transport == "bus":
            print(f"Taking the bus will cost you £{bus.get('price')} and {bus.get('energy_required')} energy.")
            sleep(3)
            player1.showRemaining()

            # The while loop within the selectTransport() method only breaks on the condition that the player confirms
            # their mode of transport in the follow method takeTransport().

            took_transport = takeTransport(select_transport, player1)
            if took_transport:
                stationOptions(player1)
                break

        elif select_transport == "train":
            print(f"Taking the train will cost you £{train.get('price')} and {train.get('energy_required')} energy.")
            sleep(3)
            player1.showRemaining()

            took_transport = takeTransport(select_transport, player1)
            if took_transport:
                stationOptions(player1)
                break

        elif select_transport == "taxi":
            print(f"A taxi can get you to your hotel without using up any of your energy at all! ... But watch out\n"
                  f"for that hefty price tag of £{taxi.get('price')}...")
            sleep(3)
            player1.showRemaining()

            took_transport = takeTransport(select_transport, player1)
            if took_transport:
                enterPremier(player1)
                break

        elif select_transport == "save":
            saveGame(player1)
            print("You have saved your progress.\n")
            sleep(2)

        elif select_transport == "exit":
            print("You have left the game.\n")
            exit()

        else:
            print("Input not recognised.\n")


def takeTransport(select_transport, player1):

    # Initialise took_transport variable to ensure selectTransport() continues to loop prior to the player confirming
    # their preferred mode of transport.

    took_transport = False

    while True:

        # Get player's confirmation of their preferred mode of transport.

        confirm_transport = input(f"Would you like to proceed with getting a {select_transport}? <y> or <n>...\n->")

        # Sanitise player's input to avoid case sensitivity.

        confirm_transport = confirm_transport.lower()

        if confirm_transport == "y":

            # Initialise both transport_price and transport_energy before declaring each of them as local variables.

            transport_price = 0
            transport_energy = 0

            if select_transport == "bus":
                transport_price = bus.get("price")
                transport_energy = bus.get("energy_required")

            elif select_transport == "train":
                transport_price = train.get("price")
                transport_energy = train.get("energy_required")

            elif select_transport == "taxi":
                transport_price = taxi.get("price")
                transport_energy = taxi.get("energy_required")

            # Both the player's money and energy remaining are decreased accordingly once their decision has been
            # confirmed.

            player1.decrBalance(transport_price)
            player1.decrEnergy(transport_energy)
            print(f"Great, let's get you on your way!")
            sleep(2)

            # Let player know how much money and energy they have remaining.

            player1.showRemaining()
            print("""
                  ______________
                  |  Pyford     \.
                  |  3 miles    /
                  -------------/
                        | |                      
                        | |        
            """)

            # Ascii art is original.

            # Change took_transport to true to break while loop in selectTransport() method.

            took_transport = True
            break
        elif confirm_transport == "n":
            print("You have chosen not to take this mode of transport.")
            break
        else:
            print("Input not recognised.")

    return took_transport


# stationOptions() represents player's arrival at Pyford's main station, should they have chosen either the bus or
# train. After a brief intro to the location, the player must ultimately decide whether to busk at the station or skip
# the level to go to the pub.

def stationOptions(player1):

    print("You arrive at Pyford's bustling railway station. Other people are darting around in all directions.\n")

    sleep(4)

    print("There's nothing you'd like more than a coffee but you understand that you should keep moving...\n")

    sleep(4)

    print("As you near the station's exit, your ears become filled with the sound of a violin concerto. Standing\n"
          "around a solo busker is a crowd of at least 30 onlookers.\n")

    sleep(4)

    print("As the concerto comes to a close, you see the people rushing to give the musician any loose change...\n")

    sleep(4)

    print("At this point you feel tired from your journey but can't help to think that you could do with some\n"
          "extra cash to keep you afloat on your travels...\n")

    sleep(4)

    # Receive player's decision of whether they would like to busk or skip and go to the pub.

    while True:
        station_choice = input("Would you like to: busk and gain some potential cash <busk> or find a pub and recover\n"
                               "some energy <pub>?\n->")

        # Sanitise player input.

        station_choice = station_choice.lower()
        if station_choice == "busk":
            print("You're clearly not one to give in to stage fright... this should be fun!\n")
            borrowGuitar(player1)
            break
        elif station_choice == "pub":
            print("Fair enough, busking isn't for everyone... but you may now need to watch your spending...\n")
            playPub(player1)
            break
        else:
            print("Input not recognised.\n")


# If the player decides to busk, the game checks whether they bought a ukulele back at WH Smith. If they did, the game
# reminds them and congratulates them on their shrewd decision and allows them to continue to the selectSong() method.
# If the player didn't pick up a ukulele back at WH Smith, the game offers them the chance to borrow a guitar from
# another busker at the station. If the player decides the cost to borrow the guitar is too high, they can skip the
# level and go to the pub.


def borrowGuitar(player1):

    while True:

        # If the player has bought the ukulele.

        if player1.checkIfBought("ukulele"):
            print("I see you were wise an picked up a ukulele at WH Smith... Looks like you're good to warm up the\n"
                  "vocal chords!\n")
            selectSong(player1)
            break

        # If the player has not bought the ukulele.

        elif not player1.checkIfBought("ukulele"):
            print("It looks like you're short of an instrument to get going... That ukulele back at WH Smith would\n"
                  "have been useful!\n")
            sleep(2)
            print("There is a busker eating some lunch by the station entrance... Would you like to borrow their\n"
                  "guitar? This would cost you £20...\n")

        # Decision of whether to borrow the guitar or skip the level to save money.

        while True:
            sleep(3)

            # Remind player of their balance and energy.

            player1.showRemaining()
            sleep(2)
            borrow_guitar = input("Enter <borrow> to borrow or <pub> to skip this level and head straight to\n"
                                  "the pub\n->")

            if borrow_guitar == "borrow":
                player1.decrBalance(20)
                print(f"Let's get set up and ready to busk! You now have £{player1.getBalance()}.")
                selectSong(player1)
                break

            elif borrow_guitar == "pub":
                print("Okey dokey... Fortunately there's a nice pub just around the corner!")
                playPub(player1)
                break

            else:
                print("Input not recognised.")
        break


# If the player has chosen to busk, having already collected the ukulele, or chosen to borrow the guitar, they can now
# choose a song to play. The player will earn more money if the song was produced by a British artist and has sold the
# most records.

def selectSong(player1):

    sleep(2)

    print("Now, here's an important decision for you. You have an instrument, you have a good spot from which to \n"
          "busk. But which song do you chose to perform?\n")

    sleep(2)

    print("Choose wisely, a good British crowd pleaser could prove very lucrative for you here...\n")

    sleep(2)

    # Give the player the three songs they can select.

    while True:
        song_choice = input("Let's say the only three songs you know off by heart are as follows: ..."
                            "which one do you choose?\n"

                            "\n<a> - 'I Want It That Way' - The Backstreet Boys\n"
                            "<b> - 'Bohemian Rhapsody' - Queen\n"
                            "<c> - 'Candle in the Wind' - Elton John\n->")

        # Sanitise user input to prevent case sensitivity.

        song_choice = song_choice.lower()

        # When each song is selected, the game will display some lyrics from each track sequentially before informing
        # the player how much money they earned and why.

        # OPTION A  - 'I Want It That Way' - The Backstreet Boys

        if song_choice == "a":
            print(f"{player1.getName()}: 'Ain't nothing but a mistake...'\n")
            sleep(2)
            print(f"{player1.getName()}: 'Tell me why...'\n")
            sleep(2)
            print(f"{player1.getName()}: 'I never want to hear you say...'\n")
            sleep(3)
            print(f"{player1.getName()}: 'I want it that way!...'\n")
            sleep(2)
            player1.incrBalance(8)
            print("Well done on picking a crowd pleaser... however you could have walked away with more cash if\n"
                  "you had chosen a British artist! Nevertheless, £8 isn't a bad sum of money.")
            sleep(3)

            # Inform player of their new balance, having earned some extra cash.

            player1.showRemaining()

            # Take player to next decision.

            pubOrCosta(player1)
            break

        # OPTION B - 'Bohemian Rhapsody' - Queen

        elif song_choice == "b":
            print(f"{player1.getName()}: 'Oh mama mia, mama mia, mama mia, let me go...'\n")
            sleep(2)
            print(f"{player1.getName()}: 'Beelzebub has a devil put aside for me, for me...'\n")
            sleep(2)
            print(f"{player1.getName()}: 'For meee!...'\n")
            sleep(2)
            player1.incrBalance(21)
            print("Bohemian Rhapsody is one of the most iconic British tracks and topped the UK singles chart\n"
                  "for 9 weeks back in 1975. Great choice! The public seem to be impressed with your vocal\n"
                  "abilities and have given you £21!")
            sleep(3)

            # Inform player of their new balance, having earned some extra cash.

            player1.showRemaining()

            # Take player to next decision.

            pubOrCosta(player1)
            break

        # OPTION C - 'Candle in the Wind' - Elton John

        elif song_choice == "c":
            print(f"{player1.getName()}: 'And I would've liked to know you...'\n")
            sleep(2)
            print(f"{player1.getName()}: 'But I was just a kid...'\n")
            sleep(2)
            print(f"{player1.getName()}: 'Your candle burned out long before...'\n")
            sleep(2)
            print(f"{player1.getName()}: 'Your legend ever did!...'\n")
            sleep(2)
            player1.incrBalance(35)
            print("Elton John's Candle in the Wind is actually the best selling British track of all time...\n"
                  "You've hit the jackpot here... and walked away with £35 in your back pocket!\n")
            sleep(3)

            # Inform player of their new balance, having earned some extra cash.

            player1.showRemaining()

            # Take player to next decision.

            pubOrCosta(player1)
            break
        else:
            print("Input not recognised.")


# The player now has the choice of going to the pub or to costa coffee to recover some energy.

def pubOrCosta(player1):

    # The player has now also reached checkpoint 2, meaning they have the option to save their progress manually
    # and/or quit the game.

    player1.reachedC2()

    sleep(2)

    print("You have successfully reached checkpoint 2!\n")

    while True:

        sleep(2)

        # Give player options to go to the pub, go to costa coffee, save their progress and/or quit the game.

        busk_choice = input("Where would you like to go next to recover some energy?\n"

                            "\nThe White Horse Pub <pub> or\n"
                            "Costa Coffee <costa>\n"
                            "Save game <save>\n"
                            "Exit without saving <exit>\n->")

        # Sanitise player input to prevent case sensitivity.

        busk_choice = busk_choice.lower()

        if busk_choice == "pub":
            print("\nYou see the hanging sign for the White Horse only about 200 yards adjacent to the railway "
                  "station and head over...")

            # Take player to next method on the way to the pub.

            rainedOn(player1)
            break

        elif busk_choice == "costa":
            print("\nAccording to a friendly passerby, the nearest costa coffee is a 5 minute walk away.")
            sleep(2)
            print("\nThis walk should be plain sailing...\n")
            sleep(3)

            # Take player to next method on the way to costa coffee.

            crossRoad(player1)
            break

        elif busk_choice == "save":
            saveGame(player1)
            print("You have saved your progress.\n")

        elif busk_choice == "exit":
            print("You have left the game.\n")
            exit()

        else:
            print("Please enter a valid option <pub> or <costa>\n")


# The crossRoad() method is situated on the player's route to costa coffee. After a verbal and visual introduction to
# the level, the player is given the choice to cross the road looking left first or looking right first. The aim of
# this level is to inform the player of side of the road on which vehicles drive in the UK.

def crossRoad(player1):

    print("...But on your route to Costa Coffee, you need to cross a major road that runs through Pyford...\n")
    sleep(2)
    print("""    
            ___  ,--.  __________________________/   ,   /_______
               ~'O---O'
             _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _
                      ______                      'O---O'~
             _______< Pyford|_____        __________________________
                       ||        /   ,   /                      
            """)

    # Ascii art is derived from https://www.asciiart.eu/buildings-and-places/other

    sleep(2)
    print("To make matters worse, the traffic lights at the crossing are broken!\n")
    sleep(2)

    while True:

        # Receive player's decision to look left or right.

        cross_choice = input("Cross the road safely by looking the correct way first...\n"
                             "\nEnter <left> to cross looking left first\n"
                             "Enter <right> to cross looking right first\n->")

        # Sanitise player's input to avoid case sensitivity.

        cross_choice = cross_choice.lower()

        # Choice to look left first.

        if cross_choice == "left":
            print("OUCHHH! You step out looking the wrong way and a motorcyclist has clipped you!\n")
            sleep(3)
            print("It is worth remembering that here in the UK vehicles drive on the left...\n")
            sleep(3)
            player1.decrEnergy(35)
            print("Luckily the motorcycle wasn't travelling too quickly and you're not in need of\n"
                  "medical attention... you have, however, lost 35 energy...\n")
            sleep(3)
            print("Fortunately Costa Coffee is only a minute away!\n")
            sleep(2)

            # Remind player of their remaining energy after the collision.

            player1.showRemaining()

            # Take player to costa coffee level.

            playCosta(player1)
            break

        # Choice to look right first.

        elif cross_choice == "right":
            print("Nicely done. You clearly realise that here in the UK we drive on the left-hand side\n"
                  "of the road!\n")
            sleep(3)
            print("You can now continue your route to Costa Coffee!\n")
            playCosta(player1)

            # Take player straight to costa coffee level.

            break
        else:
            print("Input not recognised.\n")


# The playCosta() method initiates the costa coffee level during which the player is offered the choice to queue or
# jump the queue to order their drink.


def playCosta(player1):

    # Verbal and visual introduction to the costa coffee level.

    print("You stroll through the sliding doors of Costa Coffee. You really feel like you could do with a coffee.\n")
    sleep(3)
    print("""
                      )  (
                     (   ) )
                      ) ( (
                    _______)_
                 .-'---------|  
                ( C|/\/\/\/\/|
                 '-./\/\/\/\/|
                   '_________'
                    '-------'
    """)

    # Ascii art is taken from https://www.asciiart.eu/food-and-drinks/coffee-and-tea

    sleep(3)
    print("You notice there are about four customers forming a semi-orderly line but you notice there is a fair\n"
          "amount of space in front of the first customer...\n")
    sleep(3)

    # Choice of whether to queue or jump the queue. If the player chooses to queue, they are taken to the next method
    # where they order their drink. If they jump the queue, they can choose to argue or comply with the orders of the
    # member of staff.

    while True:

        # Receive player's choice.

        queue_choice = input("Do you...?\n"

                             "\n<jump> to get to the front of the queue - you have earned this coffee after all ...\n"
                             "<queue> to stand behind the last customer - who seems to be a bit distracted...\n->")

        # Sanitise player input.

        queue_choice = queue_choice.lower()

        if queue_choice == "jump":
            print("\nYou are met with angry looks from all directions. The barista assertively asks you to wait at\n"
                  "the back of the queue...\n")
            while True:
                back_or_stay = input("How do you respond to this?\n"

                                     "\n<comply> Politely comply with the barista and join the back of the queue\n"
                                     "<argue> She must be having a bad day... tell her she's overreacting...\n->")
                back_or_stay = back_or_stay.lower()
                if back_or_stay == "comply":

                    # If player chooses to comply, they proceed to the next decision within the costa coffee level.

                    print("Smart move, you shouldn't need to wait long to be served...\n")
                    coffeeChoice(player1)
                    break

                elif back_or_stay == "argue":

                    # If player chooses to argue, the costa coffee level is terminated as they are kicked out by the
                    # café's management staff. This decision costs the player 20 energy.

                    print("\nOh dear, your poor manners have seen you get kicked by the management staff...\n")
                    sleep(3)
                    print("No coffee for you I'm afraid...\n")
                    sleep(3)
                    print("You lost 20 energy from the shock of that encounter!\n")
                    sleep(3)

                    # Subtract 20 player energy.
                    player1.decrEnergy(20)

                    # Remind player of their remaining energy.
                    player1.showRemaining()

                    # Continue to next level.
                    ascendHill(player1)
                    break
                else:
                    print("Input not recognised.\n")
            break

        elif queue_choice == "queue":
            print("Smart move, you shouldn't need to wait long to be served...\n")

            # Player proceeds to select their preferred drink.
            coffeeChoice(player1)
            break
        else:
            print("Input invalid.\n")


# The coffeeChoice() method enables the player to choose a beverage depending on how much money they would like to
# spend and how much energy they are in need of.

def coffeeChoice(player1):

    while True:

        # Remind player of balance before buying decision.
        player1.showRemaining()

        # Give player beverage options.
        coffee_choice = input("Which coffee would you like?\n"
                              "\n<Single espresso>: £2, +6 energy\n"
                              "<Small latte>: £3, +8 energy\n"
                              "<Double espresso>: £4, +15 energy\n"
                              "<Large latte>: £5, +17 energy\n->")

        # Sanitise player input.
        coffee_choice = coffee_choice.lower()

        if coffee_choice == "small espresso":

            # Give player 6 energy.
            player1.incrEnergy(6)

            # Charge player £2
            player1.decrBalance(2)
            print("6 energy gained!")
            sleep(2)

            # Remind player of balance remaining.
            player1.showRemaining()
            sleep(2)

            # Proceed to next method.
            leaveCosta(player1)
            break

            # The structure above is repeated for each of the drink choices below.

        elif coffee_choice == "small latte":
            player1.incrEnergy(8)
            player1.decrEnergy(3)
            print("8 energy gained!")
            sleep(2)
            player1.showRemaining()
            leaveCosta(player1)
            break

        elif coffee_choice == "double espresso":
            player1.incrEnergy(15)
            player1.decrEnergy(4)
            print("15 energy gained!")
            sleep(2)
            player1.showRemaining()
            leaveCosta(player1)
            break

        elif coffee_choice == "large latte":
            player1.incrEnergy(17)
            player1.decrEnergy(5)
            print("17 energy gained!")
            sleep(2)
            player1.showRemaining()
            leaveCosta(player1)
            break

        else:
            print("Invalid input.\n")


# leaveCosta() indicates that the player has now completed the costa coffee level and allows them to leave. The player
# is then taken to the 'home stretch' or the hill which leads them to the Premier Inn.

def leaveCosta(player1):

    print("Now you've refuelled with a sit down and some caffeine, you can continue on your route\n"
          "to your Premier Inn... not long now!\n")

    while True:
        leave_costa = input("Enter <leave> to leave Costa Coffee\n->")
        if leave_costa == "leave":
            ascendHill(player1)
            break
        else:
            print("Invalid input.\n")


# The rainedOn() method is situated on the player's route to the White Horse Pub. The idea of this level is to reward
# the player if they were mindful of British weather and picked up an umbrella back at WH Smith or punish them if they
# are wandering around without one.

def rainedOn(player1):

    # Verbal and visual introduction to level.

    print("\nYou take two steps before you feel a drop of rain hit you on the nose...\n")
    sleep(3)
    print("""
      __   _
    _(  )_( )_
   (_   _    _)
  / /(_) (__)
 / / / / / /
/ / / / / /   

    \n""")

    # Cloud and rain ascii art taken from https://www.asciiart.eu/nature/rains.

    # The checkIfBought() function checks whether 'umbrella' appears in the player's backpack.

    while True:

        if player1.checkIfBought("umbrella"):
            sleep(3)
            print("Good job on picking up the umbrella back at the airport or you would have arrived at the pub\n"
                  "soaking wet!\n")

            # Take player to pub level.
            playPub(player1)
            break

        elif not player1.checkIfBought("umbrella"):
            sleep(3)
            print("Oh dear! It looks like you'll have to tolerate the rain and keep walking to get to the pub...\n")
            sleep(2)
            print("It looks like you're learning the hard way about the reality of British weather!\n")
            sleep(2)
            print("The cold rain soaking through your clothes has cost you 10 energy!\n")

            # Reduce player's energy by 10.
            player1.decrEnergy(10)

            # Remind player of their energy remaining.
            player1.showRemaining()

            # Take player to pub level.
            playPub(player1)
            break


# The playPub() method initiates the pub level. This level tests the player's knowledge of the manner of ordering
# drinks in a British pub and of British slang.

def playPub(player1):

    # Verbal and visual introduction to the White Horse Pub.

    sleep(4)

    print("\nYou force your way past a stiff wooden door and are immediately hit by the scent of beer, sweat and\n"
          "an unfamiliar smell of fried food (SPOILER ALERT: this is probably the carvery...)\n")

    sleep(4)

    print("""
    __________________
    |THE WHITE HORSE |
    ------------------
     ______________
    |\ ___________ /|
    | |  /|,| |   | |
    | | |,x,| |   | |
    | | |,x,' |   | |
    | | |,x   ,   | |
    | | |/    |%==| |
    | |    /] ,   | |
    | |   [/ ()   | |
    | |       |   | |
    | |       |   | |
    | |       |   | |
    | |      ,'   | |
    | |   ,'      | |
    |_|,'_________|_| 
    
    """)

    # Ascii art is derived from https://ascii.co.uk/art/doors.

    sleep(4)

    print("Although the pub is relatively busy for the early afternoon, you notice there are still a fair number\n"
          "of tables available to sit at...\n")

    sleep(4)

    print("You're very aware that your check in at the Premier Inn is fairly soon so you're only stopping for a\n"
          "drink...\n")

    sleep(4)

    while True:

        # Receive player's choice of whether to sit and wait for a waiter or order at the bar.
        service_choice = input("To order a drink, do you:\n"

                               "\n<a> choose to sit at a table and wait for the bar staff to serve you\n"
                               "<b> stand at the bar, where the bar staff are preparing drinks\n->")

        # Sanitise input to avoid case sensitivity.
        service_choice = service_choice.lower()

        # If player chooses to wait at a table, they end up waiting a long time with no waiter ever showing up. They
        # are then approached by a pub-goer who is confused as to why they are not ordering at the bar.

        if service_choice == "a":
            print(".....\n")
            sleep(5)
            print("... 15 minutes pass by...\n")
            sleep(3)
            print("A stranger approaches you...\n")
            sleep(3)
            print("Stranger: just sitting there isn't gonna get you served any time soon mate...\n")
            sleep(3)

            # Nested while loop represents the player's response to the confused pub-goer.
            while True:

                # Receive player's response to pub-goer.
                ask_why = input("Would you like to:\n"

                                "\n<a> Ask what he means or\n"
                                "<b> Continue to wait at the table\n->")

                # Sanitise input.
                ask_why = ask_why.lower()

                # If player chooses to ask, the stranger kindly diverts them to the bar.

                if ask_why == "a":
                    print("Stranger: Ahhh I see. You're not from around here are you? In the UK it's common practice\n"
                          "to order your drinks at the bar!\n")
                    while True:
                        go_bar = input("Enter <bar> to head to the bar\n->")
                        go_bar = go_bar.lower()
                        if go_bar == "bar":

                            # Proceed to next decision.
                            viewDrinksMenu(player1)
                            break
                        else:
                            print("Invalid input.\n")
                    break

                # If player chooses to ignore the stranger's advice, they are never served, and it ends up costing them
                # 15 energy. The game then guides the player to the bar to order their drink.

                elif ask_why == "b":
                    sleep(2)
                    print("Stranger: 'Oh, you're actually gonna sit there and wait... never mind...'\n"
                          "You continue to sit at the table and your frustration from having to wait has cost\n"
                          "you 15 energy!\n")
                    sleep(4)

                    # Remove 15 energy from player.
                    player1.decrEnergy(15)
                    print(f"You now have {player1.getEnergy()} energy.")
                    sleep(2)

                    # Game guides player to the bar.
                    print("Here's a hint... In the UK you order your drinks at the bar when you're in a pub...\n")
                    sleep(2)

                    # Get input from player to take them to the bar.
                    while True:
                        go_bar = input("Enter <bar> to head to the bar\n->")
                        go_bar = go_bar.lower()
                        if go_bar == "bar":

                            # Proceed to next decision.
                            viewDrinksMenu(player1)
                            break
                    break
                else:
                    print("Invalid input.\n")
        elif service_choice == "b":
            print("You approach the bar confidently and catch the eye of the bar tender...\n")

            # Proceed to next decision.
            viewDrinksMenu(player1)
            break
        break


# The player now interacts with the bar staff, so they can see the drinks' menu.

def viewDrinksMenu(player1):

    while True:
        sleep(1)

        # Bar tender addresses player. Player enters input to view menu.
        drinks_menu = input("Bar staff: Hello there, what can I get for you? Enter <menu> to view menu.\n->")

        # Sanitise player input.
        drinks_menu = drinks_menu.lower()

        if drinks_menu == "menu":

            # Remind player of their remaining balance and energy.
            player1.showRemaining()

            # Display drinks' menu.
            print("\n-- Regular cup of tea: £2, +5 energy <reg tea>\n"
                  "-- Large cup of tea: £3, +8 energy <large tea>\n"
                  "-- Half pint of lager: £3, +7 energy <half>\n"
                  "-- Pint of lager: £5, +12 energy <pint>\n->")

            # Take player to next method.
            chooseDrink(player1)
            break
        else:
            print("Invalid input.\n")


# The player can now choose their preferred beverage, depending on how much money they have to spend and/or how much
# energy they would like to recover.

def chooseDrink(player1):

    sleep(2)

    while True:

        # Get player's choice of beverage.
        drink_choice = input("Which one would you like to order?\n->")

        # Sanitise input.
        drink_choice = drink_choice.lower()

        # Option - regular tea
        if drink_choice == "reg tea":

            # Give player 5 more energy.
            player1.incrEnergy(5)

            # Charge player £2.
            player1.decrBalance(2)
            print("5 energy gained!")
            sleep(2)

            # Remind player of their remaining balance and energy.
            player1.showRemaining()

            # Take player to next method.
            barEncounter(player1)
            break

            # Same conditional structure continues for each of the options "large tea", "half" and "pint".

        elif drink_choice == "large tea":
            player1.incrEnergy(8)
            player1.decrBalance(3)
            print("8 energy gained!")
            sleep(2)
            player1.showRemaining()
            barEncounter(player1)
            break
        elif drink_choice == "half":
            player1.incrEnergy(7)
            player1.decrBalance(3)
            print("7 energy gained!")
            sleep(2)
            player1.showRemaining()
            barEncounter(player1)
            break
        elif drink_choice == "pint":
            player1.incrEnergy(12)
            player1.decrBalance(5)
            print("12 energy gained!")
            sleep(2)
            player1.showRemaining()
            barEncounter(player1)
            break
        else:
            print("Invalid input\n")


# The barEncounter() method tests the player's existing knowledge of British slang but also rewards the player if they
# picked up a phrase book back at WH Smith.

def barEncounter(player1):

    sleep(2)

    # Initiation of interaction with another pub-goer at the bar.
    print("While you are waiting at the bar, a woman next next to you says, 'blimey, I'm pretty hammered'...\n")

    # While loop checks whether "phrase book" appears in player's backpack. If player has bought the phrase book, the
    # game hints to the player what the woman at the bar is saying. Otherwise, the player receives no hint and the game
    # progresses.
    while True:
        if player1.checkIfBought("phrase book"):
            print("You check your trusted phrase book and see that to be 'hammered' means 'drunk'... interesting...\n")
            break
        elif not player1.checkIfBought("phrase book"):
            print("That phrase book back in WH Smith would have come in handy right now...\n")
            break

    # Receive the player's reaction to reveal to the player what the woman meant.
    while True:

        # Get player's reaction.
        bar_reaction = input("How do you react?\n"

                             "\nEnter <nod> to smile politely and acknowledge her\n"
                             "Enter <alert> to let the bar staff know that she needs an ambulance\n->")

        # Sanitise input.
        bar_reaction = bar_reaction.lower()

        # Nod - correct decision
        if bar_reaction == "nod":
            print("\nWell done! 'Hammered', among many other strange expressions, is an expression for being rather\n"
                  "drunk.\n")

            # Player proceeds to next level.
            leavePub(player1)
            break

        # Alert - wrong decision.
        elif bar_reaction == "alert":
            print("\nNo real need to panic here. Being 'hammered' is only an expression to be rather drunk.\n"
                  "You may notice that some of us Brits can get a bit carried away while we're down at the pub.\n")

            # Player proceeds to next level.
            leavePub(player1)
            break
        else:
            print("Invalid input.\n")


# The leavePub() method indicates that the player has completed the pub level.

def leavePub(player1):

    print("You now think to yourself that you should probably get back on the road...\n")

    # Player must enter "leave" to complete level.

    while True:
        leave_pub = input("Enter <leave> to leave the pub\n->")
        leave_pub = leave_pub.lower()
        if leave_pub == "leave":
            ascendHill(player1)
            break
        else:
            print("Input invalid.\n")


# ascendHill() represents the "home stretch" or final leg before the player arrives at the Premier Inn. If the player
# has managed to safeguard their energy, this level should not impact the outcome of the game. On the other hand, if
# they are low on energy, this hill climb could bring them below the required energy to complete their hotel
# reservation as the hill requires 15 energy to complete.

def ascendHill(player1):

    print("As you plod along you see a sign pointing down a quiet road stating 'Premier Inn'...\n")
    sleep(2)
    print("""
                   ____________
                  |  Premier   \.
                  |  Inn       /
                  ------------/
                        | |                      
                        | |     
    """)

    # Ascii art is original.

    sleep(2)
    print("You feel a huge rush of relief that you are almost there!\n")
    sleep(2)
    print("Then you see the big purple 'Premier Inn' entrance about 200 metres up the road...\n")
    sleep(2)
    print("... and also up a very steep hill... I hope you've managed to conserve an extra bit of energy!\n")
    sleep(2)
    print("You're going to need 15 energy to drag yourself and your backpack to the hotel foyer...\n")

    # Player must enter "go" to begin the hike up the hill.

    while True:

        # Receive player's input.
        ascend_hill = input("Enter <go> to continue up the hill\n->")

        # Sanitise player's input.
        ascend_hill = ascend_hill.lower()

        if ascend_hill == "go":

            # Reduce player energy by 15.
            player1.decrEnergy(15)
            print("Not long now...\n")

            # Proceed to premier inn.
            enterPremier(player1)
            break
        else:
            print("Invalid input.\n")


# The arrival at the Premier Inn indicates that the player has finished the game, but not whether they have won or lost
# just yet. If the player arrives with £10 or more and 20 energy or more, they win. If they arrive with any less of
# either attribute, they lose.

def enterPremier(player1):

    # Game checks whether the players balance and energy are greater than £10 and 20 respectively.

    if player1.getBalance() >= 10 and player1.getEnergy() >= 20:
        sleep(2)
        print("""
               _
             _|=|__________
            /   Premier    \.
           /      Inn       \.
          /__________________\.
           ||  || /--\ ||  ||
           ||[]|| | .| ||[]||
         ()||__||_|__|_||__||()
        ( )|-|-|-|====|-|-|-|( ) 
        ^^^^^^^^^^====^^^^^^^^^^^        
        """)

        # Ascii art derived from https://www.asciiart.eu/buildings-and-places/houses.

        sleep(2)
        print("And there you have it!\n")

        # Indication that player has reached the third and final checkpoint. The game is then saved automatically,
        # with the outcome of the game decided.
        player1.reachedC3()
        saveGame(player1)

        # Game congratulates player for winning and reveals their final balance and energy statistics before
        # terminating.

        sleep(2)
        print(f"Congratulations {player1.getName()}! You arrived in one piece at your Premier Inn with\n"
              f"£{player1.getBalance()} and {player1.getEnergy()} energy remaining. As previously mentioned, you\n"
              f"needed £10 of this to pay for your room cash deposit.\n")
        sleep(4)
        print("We hope you have enjoyed playing Culture Shock UK!\n")
        print("Have a great stay in the UK!\n")
        print("*** GAME COMPLETED ***\n")
        exit()

    # Game checks player's balance and energy.

    elif player1.getBalance() < 10 or player1.getEnergy() < 20:

        # Informs player that they have reached the end of the game.
        print(f"Congratulations {player1.getName()}! You arrived in one piece at your Premier Inn!\n")

        # Final checkpoint is reached and game is saved automatically.
        player1.reachedC3()
        saveGame(player1)

        # Game commiserates player as they have arrived at the hotel with either insufficient money or energy to carry
        # out their reservation. The game then reads the player their final statistics before terminating.

        sleep(2)
        print(f"Oh no! You have arrived with only £{player1.getBalance()} and {player1.getEnergy()} energy...\n")
        sleep(2)
        print("If you remember, you need £10 to pay for your room cash deposit and 20 energy to complete\n"
              "your reservation...\n")
        sleep(2)
        print("Sorry, you lost Culture Shock UK.\n")
        sleep(2)
        print("*** GAME OVER ***\n")
        exit()


player = Character("", "", "", 50, 100, False, False, False)
