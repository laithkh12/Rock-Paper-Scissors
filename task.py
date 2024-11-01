import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)         
'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)           
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)                       
'''

game_images = [rock, paper, scissors]

userChoice = int(input("What do you choose? 0 -> rock, 1-> paper, 2 -> scissors\n"))
print(game_images[userChoice])

computerChoice = random.randint(0, 2)
print(f'Computer chose: {computerChoice}\n{game_images[computerChoice]}')

if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number. You lose.")
elif userChoice == 0 and computerChoice == 2:
    print("You Win.")
elif computerChoice == 0 and userChoice == 2:
    print("You Lose.")
elif computerChoice > userChoice:
    print("You lose.")
elif userChoice > computerChoice:
    print("You Win.")
elif computerChoice == userChoice:
    print("It's a tie.")
