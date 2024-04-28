import random

print("Welcome to the text adventure game!")
start = input("To start your adventure, press the Enter key")
print("You are walking down a forest path in the woods. You see a cat in front of you. What do you do?")

print("1. Pet the cat")
print("2. Kill the cat")

choice1 = 0
while True:
    choice1 = input()
    if choice1.isdigit():
        choice1 = int(choice1)
    else:
        print("please enter a number")
    if choice1 == 1:
        print("You pet the cat")
        break
    elif choice1 == 2:
        print("You kill the cat")
        break
    else:
        print("please make a valid decision")

choice2 = 0
if choice1 == 1:
    while True:
        print("you pet the cat and it purrs. in the distance you see a tiger. What do you do?")
        print("1. run away")
        print("2. fight it")
        choice2 = input()
        if choice2.isdigit():
            choice2 = int(choice2)
        else:
            print("Enter a valid number")
            continue
        if choice2 == 1:
            print("You run as fast as you can")
            break
        if choice2 == 2:
            print("You fight the tiger")
            break
        else:
            print("Enter a choice between 1 and 2")
            continue


if choice2 == 1:
    while True:
        print("You lose the tiger after running 5 miles. You reach a clear, cold river with shards of ice floating in it. You have never seen something so beautiful in your life. What do you do?")
        print("1. Take a drink out of the river")
        print("2. Decide not to trust the river and keep walking")
        choice2_a = input()
        if choice2_a.isdigit():
            choice2_a = int(choice2_a)
        else:
            print("Please choose a number.")
            continue
        if choice2_a == 1:
            print("You drink the ice cold water and immediatley die.")
            quit()
        elif choice2_a == 2:
            print("you keep walking and fall into a hole. The hole has millions of dollars and you are teleported back to your house with all the money.")
            break
        else:
            print("please choose a number 1 through 2")
            continue


        #below is if they choose to kill the cat
choice2_b = 0
if choice1 == 2:
    while True:
        print("You kill the cat and its soul leaves its body. A man approaches you with an angry look on his face. What do you do?")
        print("1. Laugh in his face")
        print("2. Ask what the issue is")
        choice2_b = input()
        if choice2_b.isdigit():
            choice2_b = int(choice2_b)
        else:
            print("Please enter a number")
            continue
        if choice2_b == 1:
            print("The man punches you so hard you socks fly off")
            break
        if choice2_b == 2:
            print("The man asks you why you killed the cat")
            break
        else:
            print("Please enter a number 1 through 2")
            continue
while True:
    if choice2_b == 1:
         print("You try to recover from the brutal punch. You find a golden sword on the ground and grab it. You look towards the man. What do you do?")
         print("1. Charge the man with the sword.")
         print("2. threaten the man")
         choice3_a = input()

         if choice3_a.isdigit():
            choice3_a = int(choice3_a)
         else:
            print("Please enter a number")
            continue
         if choice3_a == 1:
            random_num = random.randint(1,3)
            if random_num == 3:
                print("you charge the man and cut his head off in one slice")
                break
            elif random_num == 2:
                print("You charge the man and slice his chest, causing him to scream in pain")
                break
            elif random_num == 1:
                print("you charge the man and cut his arm, causing minor bleeding")
                break
            else:
                print("you charge the man and swing the sword, completley missing him. The man laughs in your face.")
                break

    if choice2_b == 2:
        while True:
            print("You ponder what possesed you to kill the innocent animal. Pick your answer:")
            print("1. It was a demon, you have to belive me. Please!!!")
            print("2. because I do what I want.")
            choice3_b = input()
            if choice3_b.isdigit():
             choice3_b = int(choice3_b)
            else:
             print("please enter a number")
             continue
            if choice3_b == 1:
             print("The man looks at you like a crazy person. He shakes his head and walks off, continuing with his day.")
             break
            if choice3_b == 2:
                print("The man Kicks you in the face.")
                break


        

