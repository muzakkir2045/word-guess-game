# 🎮 Word Guessing Game  

A simple command-line **Word Guessing Game** written in Python, with **two versions** showing the evolution from a beginner-friendly style to a more compact, Pythonic implementation.  

---

## 📂 Versions  

### 🔹 v1 – Beginner Version  
- Straightforward `while` loop implementation.  
- Fixed number of turns (`12`).  
- Tracks missed guesses with a counter.  
- Good for understanding **loops, conditions, and string handling**.  

👉 File: `word_guessing_game_v1.py`  

---

### 🔹 v2 – Compact / Pythonic Version  
- Uses `for ... else` for cleaner lose condition handling.  
- Number of turns adapts dynamically: `len(word) + 2`.  
- Uses `all()` to check if all characters are guessed.  
- More concise and **Pythonic approach** to solving the same problem.  

👉 File: `word_guessing_game_v2.py`  

---

## 🚀 How to Run  

1. Clone this repo:  
   ```bash
   git clone https://github.com/your-username/word-guessing-game.git
   cd word-guessing-game
   
Run either version:
```bash
python word_guessing_game_v1.py
```
or

```bash
python word_guessing_game_v2.py
```
