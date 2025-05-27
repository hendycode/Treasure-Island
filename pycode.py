print("Welcome to treasure Island")
direction = input("So your mission today is to find the treasure. Have a great time hunting. \nWould you like to go left or right? ").lower()

if direction == "left":
    swwa = input("Would you like to swim or wait? ")
    if swwa == "wait":
        doorc = input("Which color door wou.ld you like to go past. Is it the red, blue or yellow door? ").lower()
        if doorc == "red":
            print("Burned by fire. Game Over.")
        elif doorc == "yellow":
            print("Congratulations. You win!")
        elif doorc == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over")
    else: 
        print("You have been attacked by a trout. Game Over.")

else:
    print("You have fell into a hole. Game over.")