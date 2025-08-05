# 🧠 French Flashcards App 🇫🇷

A simple, interactive **language learning tool** built using Python and Tkinter.  
This app helps you memorize French vocabulary by showing flashcards that flip from French to English after a few seconds.  
Track your progress by removing the words you've already mastered!

---

## 🚀 Features

- ⏱️ **Auto-flipping flashcards** (French → English in 3 seconds)
- ✅ **Mark known words** to remove them from the learning pool
- 🔁 **Randomized word selection**
- 💾 **Saves your progress** in `words_to_learn.csv`

---

## 🗂️ Project Structure

<pre><code>
📦 Flashcard App
├── data/
│   ├── french_words.csv         # Original vocabulary list
│   └── words_to_learn.csv       # Dynamically updated list of unknown words
├── images/
│   ├── card_front.png           # Flashcard front image
│   ├── card_back.png            # Flashcard back image
│   ├── right.png                # Tick button icon
│   └── wrong.png                # Cross button icon
├── main.py                      # Main Python script
└── README.md                    # Project documentation
</code></pre>


---

## 💻 Installation

### Prerequisites

- Python 3 installed  
- `pandas` library installed:  
  ```bash
  pip install pandas

**Clone the Repository**

```bash
git clone https://github.com/yourusername/french-flashcards.git
cd french-flashcards
```

**Run the App**

```bash
python main.py
```

---

## 🧠 How It Works

1. The app tries to load `words_to_learn.csv`. If it doesn’t exist, it uses `french_words.csv`.
2. A random French word is displayed with the label **“French”**.
3. After 3 seconds, the card flips to reveal the English translation.
4. ✅ Press the right button if you know the word (it gets removed from the pool).
5. ❌ Press the wrong button to move to the next word.
6. Your updated vocabulary list is automatically saved to `words_to_learn.csv`.

---

## 📄 Sample CSV Format

```csv
  French,English
  partie,part
  où,where
  être,to be
  avoir,to have
```

---

## 🧾 To-Do Ideas

 - 🔊 Add audio pronunciation
 -  📊 Add word categories or difficulty levels
 -  🧑‍💻 Add user login to save individual progress
 -  🌍 Add support for more languages (e.g., Spanish, German)

---

## 🙏 Credits

- 🗂️ **Dataset Source**: Vocabulary list sourced from [Hermitd's account](https://github.com/hermitd) via **Wiktionary** and **GitHub**
- 🖼️ **Images & UI inspiration**: Taken from the [100 Days of Code - Python Bootcamp (Udemy)](https://www.udemy.com/course/100-days-of-code/)
- 🐍 Built using Python and Tkinter

---

## 📜 License

This project is open-source and available under the MIT License.

---

Happy coding! 🧠🇫🇷💻
