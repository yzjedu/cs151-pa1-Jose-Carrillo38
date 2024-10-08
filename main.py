def forest_adventure():
    # Prompt user for their name
    player_name = input("Enter your name: ")

    # Introduction
    print("You decide to take a quiet stroll through the forest alone. After a couple of hours, you realize you’ve gone too far and are lost in the dense woods.")

    # First Choice with Bear
    print("Suddenly, a massive grizzly bear steps out from behind the trees, growling as it stares at you!")
    choice1 = input("What do you do? (1) Throw rocks at the bear, (2) Run as fast as you can, (3) Stay completely still: ")
    while choice1 != '1' and choice1 != '2' and choice1 != '3':
        print("Invalid choice, try again.")
        choice1 = input("What do you do? (1) Throw rocks at the bear, (2) Run as fast as you can, (3) Stay completely still: ")

    # Choose to Throw rocks
    if choice1 == '1':
        print("You grab a handful of rocks and hurl them at the bear. Bad idea. The bear roars angrily and charges at you!")
        choice2 = input("Do you (1) try to run or (2) try to climb a tree? ")
        while choice2 != '1' and choice2 != '2':
            print("Invalid choice, try again.")
            choice2 = input("Do you (1) try to run or (2) try to climb a tree? ")

        if choice2 == '1':
            print("The bear is much faster than you! It catches up in no time and, sadly, this is the end of your journey. The bear eats you.")
            return  # End the game if the player is eaten
        elif choice2 == '2':
            tree_height = int(input("How tall is the tree you chose to climb (in feet)? "))
            if tree_height > 15:
                print("You quickly climb up the tall tree, and the bear can’t reach you. You wait for it to leave.")
            else:
                print("The tree isn’t tall enough! The bear grabs you, and unfortunately, this is the end. You are eaten.")
                return  # End the game if the player is eaten

    # Choose to Run
    elif choice1 == '2':
        speed = float(input("How fast can you run (in miles per hour)? "))
        if speed > 20:
            print("You must be Usain Bolt! Somehow, you manage to outrun the bear and hide behind some bushes until it passes.")
        else:
            print("You try to run, but the bear is much faster. It catches up to you easily and sadly this is the end of your journey. The bear eats you.")
            return  # End the game if the player is eaten

    # Choose to Stay Still
    elif choice1 == '3':
        print("You stand frozen in place, holding your breath. The bear sniffs around, but after a few moments, it loses interest and goes off into the trees. You’re safe... for now.")

    # Second Choice (Divergence)
    print("After the bear leaves, you continue walking and soon come across a divergence in the path.")
    choice3 = input("Do you go (1) left or (2) right? ")
    while choice3 != '1' and choice3 != '2':
        print("Invalid choice, try again.")
        choice3 = input("Do you go (1) left or (2) right? ")

    # Choose Left or Right trails
    if choice3 == '1':
        print("You take the left path. After a while, you find a small, cozy cabin... but wait! It belongs to the bear you just escaped! You try to sneak away, but the bear spots you through the window. You’re caught again, and this time, there’s no escape.")
    elif choice3 == '2':
        print("You take the right path, and after some time, you see the edge of the forest! You've made it out safely. What a close call!")

    # End of game
    print(f"Congratulations, {player_name}! You've completed your adventure in the woods. Would you like to play again?")


# Start the game
forest_adventure()
