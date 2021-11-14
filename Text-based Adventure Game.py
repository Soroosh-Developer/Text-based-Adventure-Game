while True:
    answer = input("What you like to play ?  (Y/N) ").lower().strip()
    if answer == "y":
        answer = input("You reach a crossroads, would you like to left or right?").lower().strip()
        if answer == "left":
            answer = input("You encounter a dragon, would you like to run or attack? ").lower().strip()
            if answer == "attack":
                print("The dragon killed you. You lost!!!")
            else:
                print("Good choice, you made it away safely.")
        elif answer == "right":
            answer = input("You encounter a bear, would you like to run or attack? ").lower().strip()
            if answer == "attack":
                print("The bear killed you. You lost!!!")
            else:
                answer = input("You crossed the bear, would you like to left or right?").lower().strip()
                if answer == "right":
                    print("You came across a troll and the troll killed you.")
                else:
                    print("Good choice, you made it away safely.")
        else:
            print("Invalid choice, you lost!!!")
    else:
        print("That's so bad")
