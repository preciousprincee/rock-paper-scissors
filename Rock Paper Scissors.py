import random
print("welcome to my game")

computer = 0
player = 0

option =  ["rock", "paper", "scissors"]

while True:
    
    player_input = input("type rock/paper/scissors or press q to quit: ").lower()
    if player_input == "q":
        break
    if player_input not in option:
       continue
           
    random_number = random.randint(0, 2)
# rock = 0  paper = 1  scissor = 2
    computer_pick = option[random_number]
    print("computer chose", computer_pick)
    
    if player_input == "rock" and computer_pick == "scissors":
        print("you win")
        player =+ 1
        
        
    elif player_input == "scissors" and computer_pick == "paper":
           print("you win")
           player =+ 1
        
        
    elif player_input == "rock" and computer_pick == "paper":
           print ("computer wins")
           computer =+ 1
        
        
    elif player_input == "paper" and computer_pick == "rock":
           print("you win")
           player =+ 1
         
        
    elif player_input == "paper" and computer_pick == "scissors":
           print("computer wins")
           computer =+ 1
        
        
    elif player_input == "scissors" and computer_pick == "rock":
           print("computer wins")
           computer =+ 1
        
        
    elif player_input == "scissors" and computer_pick == "paper":
           print("you win")
           player =+ 1
    else:
        print("Try again")

print("computer score", computer ,"and you score", player)
    



  
    
  

           
