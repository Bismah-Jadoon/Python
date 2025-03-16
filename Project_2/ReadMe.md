Here’s a simple and clear **README** file for your number-guessing game.  

---

# 🎯 Number Guessing Game  

## 📌 About  
This is a simple Python game where the program randomly selects a number between **1 and 100**, and the user has to guess it. The program provides hints to guide the user:  
- If the guess is **too high**, it says: _"Enter a lower number"._  
- If the guess is **too low**, it says: _"Enter a higher number"._  
- When the user **guesses correctly**, the program displays the correct number and the total number of guesses made.  

## 🛠 Requirements  
- Python 3.x  
- The `random` module (built-in)  

## 🚀 How to Run  
1. Save the script as `guessing_game.py`.  
2. Open a terminal or command prompt.  
3. Run the script using:  
   ```bash
   python guessing_game.py
   ```
4. Keep guessing the number until you find the correct one! 🎉  

## 📜 Code Explanation  
- The program generates a **random number** using `randint(1, 100)`.  
- It initializes a **guess counter** and a variable `a` to store user input.  
- A **while loop** keeps running until the correct guess is made.  
- It provides **hints** after each incorrect guess.  
- Finally, it **displays the total number of guesses** made.  

## 🎮 Sample Run  
```
Guess the number between 1 and 100: 50  
Enter a lower number  
Guess the number between 1 and 100: 25  
Enter a higher number  
Guess the number between 1 and 100: 30  
Enter a lower number  
Guess the number between 1 and 100: 27  
You guessed the correct number 27!  
Your guesses are: 4  
```

## 🎯 Have Fun Guessing! 😃  

---

Let me know if you need any modifications! 🚀
