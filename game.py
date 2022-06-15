import random

# function to write the game, store and recall for looping
def play():
    user_input = input("Select your choice?['R', 'P', 'S']:\n")
    user_input = user_input.upper()
    list = ['R', 'P', 'S']
    computer = random.choice(list)
    if user_win (user_input, computer):
       print("Player({}) : CPU({})\nPlayer wins!".format(user_input, computer)) 
    if cpu_win (user_input, computer):
       print("Player({}) : CPU({})\nCPU wins!".format(user_input, computer))
    if user_draw (user_input, computer):
       print("Player({}) : CPU({})\nIt is a tie!".format(user_input, computer)) 
       play()
    if user_input not in list:
       print("Invalid Selection! Try again!")
       play()

# function to define if user wins
def user_win(Player, CPU):
    # return true if the player beats the CPU
    # winning conditions: r>s, s>p, p>r
    if (Player == 'R' and CPU == 'S') or (Player == 'S' and CPU == 'P') or (Player == 'P' and CPU == 'R'):
        return True

# function to define if CPU wins
def cpu_win(Player, CPU):
    # return true if the CPU beats the user
    # winning conditions: r>s, s>p, p>r
    if (Player == 'S' and CPU == 'R') or (Player == 'P' and CPU == 'S') or (Player == 'R' and CPU == 'P'):
        return True

# function to define if user draws
def user_draw(Player, CPU):
    if Player == CPU:
        return True

# explaining the rules of the game to the users
print("Welcome to Rock-Paper-Scissors Game\n" \
      "R stands for Rock\n" \
      "P stands for Paper\n" \
      "S stands for Scissors\n\n" \
      "Rules of the Game:\n" \
      "1. Rock crushes Scissors, Scissors cuts Paper and Paper covers Rock\n" \
      "2. You choose one of the three options, the CPU chooses one randomly\n" \
      "3. The winner will be displayed.\n" \
      "Good luck!\n"
      )

while True:
    # user selects input
    user_input = input("Select your choice?['R', 'P', 'S']:\n")
    user_input = user_input.upper() # convert the input to uppercase in case user entered lowercase
    
    # computer selects choice using the random choice function
    list = ['R', 'P', 'S']
    computer = random.choice(list)
    
    # decides if user wins
    if user_win (user_input, computer):
        print("Player({}) : CPU({})\nPlayer wins!".format(user_input, computer)) 
    
    # decides if cpu wins
    if cpu_win (user_input, computer):
        print("Player({}) : CPU({})\nCPU wins!".format(user_input, computer))
    
    # decides if it is a draw
    if user_draw (user_input, computer):
        print("Player({}) : CPU({})\nIt is a tie!".format(user_input, computer)) 
        play() # return the function that stores the game and act as loop and starts the game all over
    
    if user_input not in list:
        print("Invalid Selection! Try again!")
        play() # return the function that stores the game and act as loop and starts the game all over
    proceed = input("Do you wish to continue? [Enter 1 for Yes and 2 for No]: ")
    if proceed == "1":
        continue
    else:
        break