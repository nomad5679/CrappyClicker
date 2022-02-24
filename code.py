# Source code for crappyclicker
import time
import random

money = 0
earn = 1
cpcprice = 30
doubleclickprice = 1000
doubleclick = 0
rebirth = 0
cpclevel = 0
dclevel = 0
missionprice = 30000
ticket1 = 0
autoclicker = 0
autoclickermoney = 0
autoclickerprice = 10000
start = time.time()

print("CrappyCLicker - v.1.0.0")

time.sleep(1)

input("""
CrappyClicker is the worst clicker game
you have ever seen. To play all you do is click 1 or 2.
You may be asking, "What is the goal?". The goal is simple.
Speedrun getting the finishing ticket. You can send your best
runs to nomad.#5679 on discord. Good luck!
and ENTER.
To start press ENTER 
""")

while True:
    if autoclicker == 1:
        start = time.time()
    selection = input("""
1 - Click!
2 - Shop
3 - Missions
4 - Balance
5 - Finish (Ticket Required)
""")
    if selection == "1":
        money += earn
        print("Clicked for " + str(earn) + " crap coins. You now have " + str(money) + " crap coins.")
    if selection == "2":
        print("""
Welcome to the shop!
You can buy and upgrade things here!
---------------------
1 - More CPC (Cash per click - +1)
2 - Doubleclick (Doubles CPC)
3 - Autoclicker (Puts a sum of money together between inputs - Max: 6)
4 - Finishing Ticket
""")
        print("CPC PRICE: " + str(cpcprice))
        print("DOUBLECLICK PRICE: " + str(doubleclickprice))
        print("AUTOCLICKER PRICE: " + str(autoclickerprice))
        print("FINISH TICKET PRICE: " + str(missionprice))
        buy = input("Enter the number to buy, nothing to skip: ")
        if buy == "1":
            if money >= cpcprice:
                print("Bought!")
                earn += 1
                money -= cpcprice
                cpcprice += 50
                cpclevel += 1
                if rebirth == 1:
                    earn += 1
                print("LEVEL: " + str(cpclevel))
            else:
                print("Not enough cash...")
        if buy == "2":
            if money >= doubleclickprice:
                print("Bought!")
                earn += earn
                cpcprice += 50
                doubleclick = 1
                money -= doubleclickprice
                doubleclickprice += doubleclickprice + doubleclickprice
                dclevel += 1
                if rebirth == 1:
                    earn += earn
                print("LEVEL: " + str(dclevel))
            else:
                print("Not enough cash...")
        if buy == "3":
            print("Autoclicker bought...")
            money -= autoclickerprice
            time.sleep(1)
            autoclicker = 1
        if buy == "4":
            if money >= missionprice:
                print("Ticket bought...")
                ticket1 = 1
                money -= missionprice
                missionprice += 20000
            else:
                print("Not enough money...")

    if selection == "3":
        missionchoose = random.randint(1, 3)
        print("""
MISSION BOARD
Press 1 to start mission, enter to leave
-------------
""")
        time.sleep(1)
        if missionchoose == 1:
            choose1 = input("GO GET THE MILK - $3000 ")
            if choose1 == "1":
                print("Mission started... Preparing.")
                time.sleep(1)
                milk1 = input("""
CHOOSE -
1 - Walk on the sidewalk (30s)
2 - Go down the alleyway (20s)
3 - Ask a stranger for a ride (5s)
""")
                if milk1 == "1":
                    sidewalk1 = random.randint(1, 20)
                    print("Walking down the street...")
                    print("30s Wait time")
                    time.sleep(30)
                    if sidewalk1 == 1:
                        print(
                            "Oh no bud... You died on the way. Sucks to be you. Get better ig. You also lost all your money :)")
                        money -= money
                    else:
                        print("You got the milk successfully...")
                        time.sleep(1)
                        print("3000 CrapCoins acquired!")
                        money += 3000

                if milk1 == "2":
                    sidewalk2 = random.randint(1, 9)
                    print("Going down the alleyway...")
                    print("20s Wait time")
                    time.sleep(20)
                    if sidewalk2 == 1:
                        print(
                            "You walked down the alleyway at the wrong time. You died and lost all your money. Get gud sometime.")
                        money -= money
                    else:
                        print("You got the milk successfully...")
                        time.sleep(1)
                        print("3000 CrapCoins acquired!")
                        money += 3000

                if milk1 == "3":
                    sidewalk3 = random.randint(1, 4)
                    print("Looking for a stranger to hitchhike...")
                    print("5s Wait time")
                    time.sleep(5)
                    if sidewalk3 == 1:
                        print(
                            "You hopped in a ride. Unfortunately you didn't go to the store. You went off a cliff and lost all your cash.")
                        money -= money
                    else:
                        print("You got the milk successfully...")
                        time.sleep(1)
                        print("3000 CrapCoins acquired!")
                        money += 3000

        if missionchoose == 2:
            choose1 = input("GET SNOW FROM ANTARTICA - $8000 ")
            if choose1 == "1":
                print("Mission started... Preparing.")
                time.sleep(1)
                snow1 = input("""
CHOOSE -
1 - Swim (45s)
2 - Fly (30s)
3 - Beg NASA to lend you a rocket (10s)
""")
                if snow1 == "1":
                    snowchoose1 = random.randint(1, 18)
                    print("Swimming...")
                    print("45s Wait time")
                    time.sleep(45)
                    if snowchoose1 == 1:
                        print("You died and lost your money. What'd you expect, you were swimming to Antartica!!")
                        money -= money
                    else:
                        print("Collected the snow sucessfully...")
                        time.sleep(1)
                        print("8000 CrapCoins acquired!")
                        money += 8000

                if snow1 == "2":
                    snowchoose2 = random.randint(1, 12)
                    print("Hopping on a plane...")
                    print("30s Wait time")
                    time.sleep(30)
                    if snowchoose2 == 1:
                        print(
                            "Turns out the pilot didn't go to flight school after all. Book a more expensive flight next time... Died and lost all your money too LOL")
                        money -= money
                    else:
                        print("Collected the snow sucessfully...")
                        time.sleep(1)
                        print("8000 CrapCoins acquired!")
                        money += 8000

                if snow1 == "3":
                    snowchoose3 = random.randint(1, 3)
                    print("Asking NASA for a rocket...")
                    print("10s Wait time")
                    time.sleep(10)
                    if snowchoose3 == 1:
                        print(
                            "NASA was done with you and brought you to Area 51 to be posessed. Maybe ask Elon Musk next time?? Lost all your money btw.")
                        money -= money
                    else:
                        print("Collected the snow sucessfully...")
                        time.sleep(1)
                        print("8000 CrapCoins acquired!")
                        money += 8000

        if missionchoose == 3:
            choose3 = input("COLLECT DEBT FROM SOMEONE - $1000 ")
            if choose3 == "1":
                print("Mission started... Preparing.")
                time.sleep(1)
                debt1 = input("""
CHOOSE -
1 - Drive (25s)
2 - Fly (15s)
3 - Teleport (5s)
""")
                if debt1 == "1":
                    debtdie1 = random.randint(1, 25)
                    print("Driving...")
                    print("25s Wait time")
                    time.sleep(25)
                    if debtdie1 == 1:
                        print(
                            "You ran a red light and crashed into a forklift. In the process you got spiked like a tomato. You died and lost all your money.")
                        money -= money
                    else:
                        print("You got the debt...")
                        time.sleep(1)
                        print("1000 CrapCoins acquired!")
                        money += 1000

                if debt1 == "2":
                    debt2 = random.randint(1, 15)
                    print("Hopping in the helicopter...")
                    print("15s Wait time")
                    time.sleep(15)
                    if debt2 == 1:
                        print(
                            "You forgot you didn't know how to fly... Ez death + Lost all your money. Ratio'd as some would say.")
                        money -= money
                    else:
                        print("You collected the debt...")
                        time.sleep(1)
                        print("1000 CrapCoins acquired!")
                        money += 1000

                if debt1 == "3":
                    sidewalk3 = random.randint(1, 6)
                    print("Learning teleportation...")
                    print("5s Wait time")
                    time.sleep(5)
                    if sidewalk3 == 1:
                        print(
                            "You teleported... Into a wall. Maybe next time you should spend more time learning. Died and lost all your coins.")
                        money -= money
                    else:
                        print("You collected the debt...")
                        time.sleep(1)
                        print("1000 CrapCoins acquired!")
                        money += 1000

    if selection == "4":
        print("Total CrapCoins: " + str(money))
        time.sleep(0.7)

    if selection == "5":
        if ticket1 == 1:
          print ("You have done the unthinkable...")
          time.sleep(1.5)
          print ("Finished the game. Woah.")
          time.sleep(1.5)
          print ("Congratulations, and thanks for playing the game.")
          time.sleep(1.5)
          print ("If you timed the run, submit it to me! - nomad.#5679 on discord.")
          time.sleep(2)
          exit()
        else:
            print("Nice try. You don't even have a ticket. Go buy one in the shop to enter.")

    if autoclicker == 1:
        end = time.time()
        autoclickermoney = end - start
        if autoclickermoney >= 0.2:
            autoearn = 1
        if autoclickermoney >= 2:
            autoearn = 2
        if autoclickermoney >= 4:
            autoearn = 3
        if autoclickermoney >= 6:
            autoearn = 4
        if autoclickermoney >= 9:
            autoearn = 5
        if autoclickermoney >= 12:
            autoearn = 6
        if autoclickermoney >= 20:
            autoearn = 8
        if autoclickermoney >= 30:
            autoearn = 12
        if autoclickermoney >= 40:
            autoearn = 14
        money += autoearn
        print ("AUTOCLICKER - EARNED " + str(autoearn) + " MONEY")
