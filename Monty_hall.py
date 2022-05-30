"""
Autor: Emirhan
Datum: 11.03.2022
Version: 0.1
"""

import random


def main():
    print("Hallo")
    total_wins = 0
    tries = 0

    for i in range(10000):
        winning_door = random.randint(1, 3) # int randTuer = zufallszahl von 1 - 3
        candidate_door = int(input("Welche Tür wählen Sie? (1, 2, 3) ")) # Tür die der Kanditat auswählt
        door_logic(winning_door, candidate_door)
        win = ask_change_door(candidate_door, winning_door)
        total_wins = check_if_won(win, total_wins)
        tries += 1

    prob = total_wins / tries
    print(str(prob))


"""
Prints a corresponding win/loose message
"""
def check_if_won(win, wins):
    if win:
        print("Glückwunsch, Sie haben ein Auto gewonnen. ")
        wins += 1
    else:
        print("Leider kein Glück gehabt.")
    return wins

"""
Asks the user if he wants to reconsider his decision.
"""
def ask_change_door(candidate_door, winning_door):
    ungueltige_eingabe = True
    win = False
    while (ungueltige_eingabe):
        wechseln = str(input("Möchten Sie die Türe wechseln? (ja oder nein) "))
        if wechseln == "ja":
            win = change_door(winning_door, candidate_door)
            ungueltige_eingabe = False
        elif wechseln == "nein":
            win != change_door(winning_door, candidate_door)
            ungueltige_eingabe = False
        else:
            print("Fehlerhafte eingabe...")
    return win

"""
Returns true if the doors do not match (because we change the door)
"""
def change_door(winning_door, candidate_door):
    if winning_door == candidate_door:
        return False
    else:
        return True


"""
Calls corresponding methods depending on the winning door
"""
def door_logic(winning_door, candidate_door):

    if winning_door == 1:
        choose_host_door1(candidate_door)
    elif winning_door == 2:
        choose_host_door2(candidate_door)
    elif winning_door == 3:
        choose_host_door3(candidate_door)

"""
Chooses a non-winning dor for the host
"""
def choose_host_door1(candidate_door):
    if candidate_door == 1:
        host_door = random.randint(2, 3)
    elif candidate_door == 2:
        host_door = 3
    elif candidate_door == 3:
        host_door = 2
    print("Der Host öffnet die Türe " + str(host_door) + ". Dahinter befindet sich eine Ziege")

"""
Chooses a non-winning dor for the host
"""
def choose_host_door2(candidate_door):
    if candidate_door == 1:
        host_door = 3
    elif candidate_door == 2:
        x = bool(random.getrandbits(1)) # Random boolean variable x
        if x:
            host_door = 1
        else:
            host_door = 3
    elif candidate_door == 3:
        host_door = 1
    print("Der Host öffnet die Türe" + str(host_door) + ". Dahinter befindet sich eine Ziege")

"""
Chooses a non-winning dor for the host
"""
def choose_host_door3(candidate_door):
    if candidate_door == 1:
        host_door = 2
    elif candidate_door == 2:
        host_door = 1
    elif candidate_door == 3:
        x = bool(random.getrandbits(1))  # Random boolean variable x
        if x:
            host_door = 1
        else:
            host_door = 2
    print("Der Host öffnet die Türe" + str(host_door) + ". Dahinter befindet sich eine Ziege")


if __name__ == '__main__':
    main()