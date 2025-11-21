# Trigram Language Model – Assignment Submission

This project is my implementation of a simple Trigram (N=3) Language Model for the Desible AI/ML Intern Assignment.

The goal of the project is to:
- Clean and process text
- Build trigram counts
- Learn word-to-word transitions
- Generate new text using probabilistic sampling
- Handle edge cases like empty text and short text
- Pass all provided tests

I have implemented the complete TrigramModel from scratch inside `src/ngram_model.py`.

---

## 🛠 How I Set Up and Ran the Project

### 1. Created a virtual environment

python3 -m venv .venv
source .venv/bin/activate


### 2. Installed the dependencies


pip install -r requirements.txt


The only dependency required was `pytest`.

---

## 🚀 How to Run the Model

### To train the model and generate text:


python src/generate.py


This script:
- Loads the example text from `data/example_corpus.txt`
- Fits the trigram model
- Prints generated text to the terminal

---

## 🧪 Running Tests

The assignment includes tests to check whether the TrigramModel works correctly.

To run all tests:


pytest tests/test_ngram.py


All tests pass successfully after the implementation.

---

## 📂 Project Structure



ml-assignment/
├── data/
│ └── example_corpus.txt
│
├── src/
│ ├── ngram_model.py # Main implementation of TrigramModel
│ ├── generate.py # Script to train + generate text
│ └── utils.py # Optional helper functions
│
├── tests/
│ └── test_ngram.py # Unit tests provided in assignment
│
└── evaluation.md # My written explanation of design choices

---
## ✨ What I Implemented

- Cleaned the input text (lowercasing, removing punctuation)
- Tokenized sentences and added start/end padding
- Built nested dictionaries to store trigram counts
- Implemented probabilistic sampling for text generation
- Handled empty-text and short-text edge cases properly
- Ensured compatibility with all test cases

---

## ✔ Current Status

- Trigram model fully implemented
- All tests are passing (`3 passed`)
- Code is clean, simple, and easy to understand
- Ready to submit# Trigram Language Model – Assignment Submission

This project is my implementation of a simple Trigram (N=3) Language Model for the Desible AI/ML Intern Assignment.

The goal of the project is to:
- Clean and process text
- Build trigram counts
- Learn word-to-word transitions
- Generate new text using probabilistic sampling
- Handle edge cases like empty text and short text
- Pass all provided tests

I have implemented the complete TrigramModel from scratch inside `src/ngram_model.py`.

---

## 🛠 How I Set Up and Ran the Project

### 1. Created a virtual environment

python3 -m venv .venv
source .venv/bin/activate


### 2. Installed the dependencies


pip install -r requirements.txt


The only dependency required was `pytest`.

---

## 🚀 How to Run the Model

### To train the model and generate text:


python src/generate.py


This script:
- Loads the example text from `data/example_corpus.txt`
- Fits the trigram model
- Prints generated text to the terminal

---

## 🧪 Running Tests

The assignment includes tests to check whether the TrigramModel works correctly.

To run all tests:


pytest tests/test_ngram.py


All tests pass successfully after the implementation.

---

## 📂 Project Structure



ml-assignment/
├── data/
│ └── example_corpus.txt
│
├── src/
│ ├── ngram_model.py # Main implementation of TrigramModel
│ ├── generate.py # Script to train + generate text
│ └── utils.py # Optional helper functions
│
├── tests/
│ └── test_ngram.py # Unit tests provided in assignment
│
└── evaluation.md # My written explanation of design choices

---
## ✨ What I Implemented

- Cleaned the input text (lowercasing, removing punctuation)
- Tokenized sentences and added start/end padding
- Built nested dictionaries to store trigram counts
- Implemented probabilistic sampling for text generation
- Handled empty-text and short-text edge cases properly
- Ensured compatibility with all test cases

---

## ✔ Current Status

- Trigram model fully implemented
- All tests are passing (`3 passed`)
- Code is clean, simple, and easy to understand
- Ready to submit