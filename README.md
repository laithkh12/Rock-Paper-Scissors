# ✂️ Rock, Paper, Scissors Game

Welcome to the **Rock, Paper, Scissors** game! This classic hand game is played between two players, where each player simultaneously forms one of three shapes: rock, paper, or scissors. The game is simple and fun, making it a great way to pass the time!

---

## 📋 Features

- **User Interaction**: Players choose their shape by entering a corresponding number.
- **Randomized Computer Choice**: The computer randomly selects one of the three options.
- **Game Logic**: The game determines the winner based on the standard rules:
  - Rock crushes scissors.
  - Scissors cuts paper.
  - Paper covers rock.

---

## 🔍 Code Overview

The game is implemented using a simple command-line interface where the user inputs their choice, and the program handles the logic to determine the winner. Below is an overview of the code:

### Code Snippet

```python
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

userChoice = int(input("What do you choose? 0 -> rock, 1 -> paper, 2 -> scissors\n"))
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
```

## 📋 Usage Instructions
1. Clone the Repository:
```bash
git clone https://github.com/your-username/rock-paper-scissors
cd rock-paper-scissors
```
2. Run the Game: Execute the script in a Python environment:
```bash
python rock_paper_scissors.py
```
3. Follow the Prompts:
  - Choose your option by typing 0 for rock, 1 for paper, or 2 for scissors.
  - The program will display your choice, the computer's choice, and the result of the game.

## 🎮 Example Output
  Scenario 1: User Wins
  ```bash
  What do you choose? 0 -> rock, 1 -> paper, 2 -> scissors
0
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose: 2
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 

You Win.
```
Scenario 2: User Loses
```bash
What do you choose? 0 -> rock, 1 -> paper, 2 -> scissors
1
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)  
Computer chose: 2
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)  
You Lose.
```
Scenario 3: It's a Tie
```bash
What do you choose? 0 -> rock, 1 -> paper, 2 -> scissors
2
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Computer chose: 2
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
It's a tie.
```

## ⚙️ Customization  
  You can easily modify the game logic or add new features, such as:
    - Allowing multiple rounds.
    - Keeping score over several rounds.
    - Implementing a graphical interface using libraries like Tkinter or Pygame.

## 📜 License
  This project is licensed under the MIT License. See the LICENSE file for details.

Have fun playing! 🕹️✨
