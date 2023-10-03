from random import randint
from time import sleep

tot = 0
jack = False
ace = False
djack = False
dace = False

def beginning():
    print("This is a command based blackjack!")
    print("Do you want to play with or without fiches? [y/n]")
    i = input("")  
    if i == "y":
        sleep(2)
        print("You currently have 200 fiches.")
        print("In each round, you can play with as many fiches as you want, as long as they are not 0.")
        sleep(3)
        fiches()


def fiches():
    totfiches = 200
    print("How many fiches will you play?")
    fiches = int(input(""))
    


def blackjack():
    global tot
    global ace
    global jack
    tot = 0
    whiler = 0
    sleep(2)
    print("the dealer will start distributing cards!")
    sleep(2)
    while whiler != 2:
        r = randint(1, 13)
        if r == 1:
            print("You got an ace!")
            ace = True
            tot += 1
        elif r == 2:
            print("You got a two!")
            tot += 2
        elif r == 3:
            print("You got a three!")
            tot += 3
        elif r == 4:
            print("You got a four!")
            tot += 4
        elif r == 5:
            print("You got a five!")
            tot += 5
        elif r == 6:
            print("You got a six!")
            tot += 6
        elif r == 7:
            print("You got a seven!")
            tot += 7
        elif r == 8:
            print("You got an eight!")
            tot += 8
        elif r == 9:
            print("You got a nine!")
            tot += 9
        elif r == 10:
            print("You got a 10!")
            tot += 10
        elif r == 11:
            print("You got a jack!")
            jack = True
            tot += 10
        elif r == 12:
            print("You got a queen!")
            tot += 10
        elif r == 13:
            print("You got a king!")
            tot += 10
        whiler += 1
        r = None
    dealer()    

def dealer():
        global dace
        global dtot
        global djack
        dtot = 0
        sleep(3)
        print("The dealer's getting cards for himself...")
        sleep(1)
        r = randint(1, 13)
        if r == 1:
            print("The dealer's got an ace and places a hidden card!")
            dtot += 1
            dace = True
            choise()
        elif r == 2:
            print("The dealer's got a two and places a hidden card!")
            dtot += 2
            choise()
        elif r == 3:
            print("The dealer's got a three and places a hidden card!")
            dtot += 3
            choise()
        elif r == 4:
            print("The dealer's got a four and places a hidden card!")
            dtot += 4
            choise()
        elif r == 5:
            print("The dealer's got a five and places a hidden card!")
            dtot += 5
            choise()
        elif r == 6:
            print("The dealer's got a six and places a hidden card!")
            dtot += 6
            choise()
        elif r == 7:
            print("The dealer's got a seven and places a hidden card!")
            dtot += 7
            choise()
        elif r == 8:
            print("The dealer's got an eight and places a hidden card!")
            dtot += 8
            choise()
        elif r == 9:
            print("The dealer's got a nine and places a hidden card!")
            dtot += 9
            choise()
        elif r == 10:
            print("The dealer's got a 10 and places a hidden card!")
            dtot += 10
            choise()
        elif r == 11:
            print("The dealer's got a jack and places a hidden card!")
            djack = True
            dtot += 10
            choise()
        elif r == 12:
            print("The dealer's got a queen and places a hidden card!")
            dtot += 10
            choise()
        elif r == 13:
            print("The dealer's got a king and places a hidden card!")
            dtot += 10
            choise()

def choise():
    global tot
    global ace
    global jack
    sleep(2)
    while tot <= 21:
        print("What will you do?")
        print("1. Additional card")
        print("2. Stop")
        print("3. Double")
        print("4. Divide")
        i = input("")
        if i == "1":
            r = randint(1, 13)
            if r == 1:
                print("You got an ace!")
                tot + 1
                if jack == True:
                    sleep(2)
                    print("You got a Blackjack!")
                    tot = 21
                    dealerend()
                    break
            elif r == 2:
                print("You got a two!")
                tot += 2
            elif r == 3:
                print("You got a three!")
                tot += 3
            elif r == 4:
                print("You got a four!")
                tot += 4
            elif r == 5:
                print("You got a five!")
                tot += 5
            elif r == 6:
                print("You got a six!")
                tot += 6
            elif r == 7:
                print("You got a seven!")
                tot += 7
            elif r == 8:
                print("You got an eight!")
                tot += 8
            elif r == 9:
                print("You got a nine!")
                tot += 9
            elif r == 10:
                print("You got a 10!")
                tot += 10
            elif r == 11:
                print("You got a jack!")
                if ace == True:
                    sleep(2)
                    print("You got a blackjack!")
                    tot = 21
                    dealerend()
                    break
                tot += 10
            elif r == 12:
                print("You got a queen!")
                tot += 10
            elif r == 13:
                print("You got a king!")
                tot += 10
        elif "2":
            break
    end()
    

def end():
    global tot
    sleep(3)
    if tot <=21:
        dealerend()
    else:
        print("You lost!")
        print("You went over 21 points!")

def dealerend():
        global dace
        global dtot
        global djack
        sleep(2)
        print("The dealer reveals the hidden card...")
        r = randint(1, 13)
        if r == 1:
            print("It's an ace!")
            if djack == True:
                sleep(2)
                print("The dealer got a Blackjack!")
                dtot = 21
                nostal()
            dtot += 1
        elif r == 2:
            dtot += 2
            print("It's a two!")
        elif r == 3:
            dtot += 3
            print("It's a three!")
        elif r == 4:
            dtot += 4
            print("It's a four!")
        elif r == 5:
            dtot += 5
            print("It's a five!")
        elif r == 6:
            dtot += 6
            print("It's a six!")
        elif r == 7:
            dtot += 7
            print("It's a seven!")
        elif r == 8:
            dtot += 8
            print("It's an eight!")
        elif r == 9:
            dtot += 9
            print("It's a nine!")
        elif r == 10:
            dtot += 10
            print("It's a 10!")
        elif r == 11:
            dtot += 11
            print("It's a jack!")
            if dace == True:
                sleep(2)
                dtot = 21
                print("The dealer got a Blackjack!")
                nostal()
        elif r == 12:
            dtot += 12
            print("It's a queen!")
        elif r == 13:
            dtot += 13
            print("It's a king!")
        if dtot > 21:
            sleep(2)
            print("The dealer got more than 21 points, you won!")
            exit()
        dchoise()


def dchoise():
    global dtot
    while dtot <= 13:
        sleep(2)
        print("The dealer draws an additional card!")
        r = randint(1, 13)
        if r == 1:
            dtot += 1
            print("It's an ace!")
            break
        elif r == 2:
            dtot += 2
            print("It's a two!")
            break
        elif r == 3:
            dtot += 3
            print("It's a three!")
            break
        elif r == 4:
            dtot += 4
            print("It's a four!")
            break
        elif r == 5:
            dtot += 5
            print("It's a five!")
            break
        elif r == 6:
            dtot += 6
            print("It's a six!")
            break
        elif r == 7:
            dtot += 7
            print("It's a seven!")
            break
        elif r == 8:
            dtot += 8
            print("It's an eight!")
            break
        elif r == 9:
            dtot += 9
            print("It's a nine!")
            break
        elif r == 10:
            dtot += 10
            print("It's a 10!")
            break
        elif r == 11:
            dtot += 11
            print("It's a jack!")
            break
        elif r == 12:
            dtot += 12
            print("It's a queen!")
            break
        elif r == 13:
            dtot += 13
            print("It's a king!")
            break
        if dtot > 21:
            sleep(2)
            print("The dealer got more than 21 points, you won!")
            break
    if dtot == 13 and tot == 13:
        sleep(3)
        print("The dealer stops adding cards.")
        nostal()
    elif dtot in [14, 15, 16]:
        ra = randint(1, 2)
        if ra == 1:
            sleep(2)
            print("The dealer draws an additional card!")
            r = randint(1, 13)
            if r == 1:
                print("It's an ace!")
                dtot += 1
            elif r == 2:
                dtot += 2
                print("It's a two!")
            elif r == 3:
                dtot += 3
                print("It's a three!")
            elif r == 4:
                dtot += 4
                print("It's a four!")
            elif r == 5:
                dtot += 5
                print("It's a five!")
            elif r == 6:
                dtot += 6
                print("It's a six!")
            elif r == 7:
                dtot += 7
                print("It's a seven!")
            elif r == 8:
                dtot += 8
                print("It's an eight!")
            elif r == 9:
                dtot += 9
                print("It's a nine!")
            elif r == 10:
                dtot += 10
                print("It's a 10!")
            elif r == 11:
                dtot += 11
                print("It's a jack!")
            elif r == 12:
                dtot += 12
                print("It's a queen!")
            elif r == 13:
                dtot += 13
                print("It's a king!")
            if dtot > 21:
                sleep(2)
                print("The dealer got more than 21 points, you won!")
            nostal()
        elif ra == 2:
            print("The dealer stops.")
            nostal()
    elif dtot > 16 and dtot <= 21:
        print("the dealer stops.")
        nostal()


def nostal():
    global dtot
    global tot
    if dtot > tot:
        sleep(2)
        print("The dealer has " + str(dtot) + " points, you have " + str(tot) + " points.")
        print("You lost!")
    elif tot > dtot:
        sleep(2)
        print("The dealer has " + str(dtot) + " points, you have " + str(tot) + " points.")
        print("You won!")
    else:
        sleep(2)
        print("It's a draw! You and the dealer both got " + str(tot) + " points!")


blackjack()
