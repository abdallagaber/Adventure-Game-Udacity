import random
import time


def print_sleep(text):
    print(text)
    time.sleep(2)


def intro():
    # this is intro of the game
    print_sleep("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_sleep(f"Rumor has it that a {enemy} is somewhere around here, "
                 "and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep(f"In your hand you hold your trusty "
                f"(but not very effective) {weapon}.")


def house():
    # Things that happen to the player in the house
    print_sleep("You approach the door of the house.")
    print_sleep(f"You are about to knock when the door opens "
                f"and out steps a {enemy}.")
    print_sleep(f"Eep! This is the {enemy}'s house!")
    fighting(weapon)


def cave():
    # Things that happen to the player in the cave
    global cave_visited
    global weapon
    print_sleep("You peer cautiously into the cave.")
    if cave_visited:
        print_sleep("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    elif cave_visited is False:
        weapon = random.choice(weapons)
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep(f"You have found the {weapon}!")
        print_sleep(f"You discard your silly old dagger and "
                    f"take the {weapon} with you.")
    cave_visited = True
    print_sleep("You walk back out to the field.")
    choose_the_route()


def choose_the_route():
    # this is ask the player which route he want to go
    print_sleep("")
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()


def fighting(weapon):
    # this is the fight code
    print_sleep(f"The {enemy} attacks you!")
    if weapon == "dagger":
        print_sleep(f"You feel a bit under-prepared for this, "
                    f"what with only having a tiny {weapon}.")
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if weapon == "dagger":
            print_sleep(f"You do your best...")
            print_sleep(f"but your {weapon} is no match for the {enemy}.")
            print_sleep(f"You have been defeated!""")
        elif weapon == "sword" or weapon == "scimitar" or weapon == "ranseur":
            print_sleep(f"As the {enemy} moves to attack, "
                        f"you unsheath your new {weapon}.")
            print_sleep(f"The {weapon} shines brightly in your hand as "
                         "you brace yourself for the attack.")
            print_sleep(f"But the {enemy} takes one look at your"
                         "shiny new toy and runs away!")
            print_sleep(f"You have rid the town of the {enemy}. "
                         "You are victorious!")
    elif choice == '2':
        print_sleep("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        choose_the_route()


def play_again():
    # this is ask the player if he want to play again
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print_sleep("Thanks for playing! See you next time.")
            return 'game_over'
        elif choice == 'y':
            print_sleep("Excellent! Restarting the game ...")
            weapon = 'dagger'
            return 'run'
game_state = 'run'
while game_state == 'run':
    enemies = ['monster', 'bear', 'pirate', 'dragon']
    weapons = ['sword', 'scimitar', 'ranseur']
    enemy = random.choice(enemies)
    weapon = 'dagger'
    cave_visited = False
    intro()
    choose_the_route()
    game_state = play_again()
