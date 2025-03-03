# Snake, Water, Gun Game 🎮

## 📌 Introduction
Welcome to the **Snake, Water, Gun** game! This is a simple Python-based command-line game inspired by the classic hand game. The game is played between a **human** and the **computer**, where both randomly select one of the three choices. The winner is decided based on predefined rules.

## 🏆 Game Rules
- **Snake vs Water** → Snake drinks water → **Snake wins** ✅
- **Water vs Gun** → Gun drowns in water → **Water wins** ✅
- **Gun vs Snake** → Gun shoots snake → **Gun wins** ✅
- **Same choices** → It's a **draw** 🤝

## 🚀 How to Play
1. **Run the script** in Python.
2. **Enter your choice** when prompted (`Snake`, `Water`, or `Gun`).
3. The **computer will randomly pick** one of the three options.
4. The **result will be displayed**, indicating who won.
5. **Restart the game** to play again.

## 🛠 Code Explanation
The game is implemented using Python, where the logic is structured into different functions:

### 📌 Code Breakdown
#### 1️⃣ Computer's Choice
The function `computer()` uses the `random.choice()` function to pick a random selection from a predefined list:
```python
import random

def computer():
    options = ["Snake", "Water", "Gun"]
    return random.choice(options)
```
#### 2️⃣ Human's Choice
The function `Human()` asks for user input:
```python
def Human():
    choice = input("Enter your choice (Snake, Water, Gun): ")
    return choice.capitalize()
```
#### 3️⃣ Game Logic
The logic to determine the winner is implemented using `if-elif` conditions:
```python
if a == b:
    print("Match Draw!")
elif (a == "Snake" and b == "Water") or 
     (a == "Water" and b == "Gun") or 
     (a == "Gun" and b == "Snake"):
    print("Computer Wins!")
else:
    print("Human Wins!")
```
- If both choices are the same, it's a **draw**.
- If the computer's choice beats the human's choice according to the rules, the computer wins.
- Otherwise, the human wins.

## 💻 Requirements
- Python 3.x
- A terminal or command prompt

## 🔧 Installation & Execution
1. **Ensure Python is installed** on your system.
2. **Download or copy** the script into a file named `snake_water_gun.py`.
3. **Navigate to the script's directory** in your terminal.
4. **Run the script** with:
   ```sh
   python snake_water_gun.py
   ```
5. **Follow the prompts** and enjoy the game! 🎉

## 🎮 Example Gameplay
```
Enter your choice : Snake
Computer choose : Water
Human choose : Snake
Human Wins!! Snake drinks the water hence wins
```

## 🚀 Future Improvements
- Implement **multiple rounds & scoring system**.
- Add **input validation** to handle incorrect entries.
- Create a **Graphical User Interface (GUI)** for better experience.
- Allow the game to **continue until the player decides to quit**.
- Store game history to **track performance**.

## 🔍 Common Issues & Troubleshooting
- **Invalid Input:** If a player enters anything other than "Snake", "Water", or "Gun", the program may misbehave. Future updates will include input validation.
- **Random Choice Fairness:** The computer’s choice is purely random to maintain fairness.
- **Game Restart:** The game currently plays **one round per execution**. A future update will allow continuous play.

## 📜 License
This project is **open-source** and free to use. Feel free to **modify and enhance** it! 

## 👨‍💻 Author
Bismah-Jadoon

## 🤝 Contributing
Contributions are always welcome! 🎯 If you have any **ideas, improvements, or bug fixes**, feel free to submit a **pull request** or open an **issue** on GitHub.

---
*Enjoy the game and happy coding! 🎮🐍💦🔫*

