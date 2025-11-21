# Evaluation – Trigram Language Model

This document explains the design choices I made while implementing the Trigram (N=3) Language Model for the AI/ML Intern Assignment. I built everything from scratch using only Python and simple data structures.

---

## 1. How I Stored N-Gram Counts

I used a nested dictionary structure:

self.trigrams[w1][w2][w3] = count

To make this easier, I used `defaultdict` from Python’s collections module:

- The first key is the first word (w1)
- The second key is the second word (w2)
- The final key is the possible next word (w3)
- The value is the count of how many times the trigram appears

This structure is simple, efficient, and perfect for fast lookup during generation.

---

## 2. Text Cleaning and Tokenization

I cleaned the text in the following steps:

1. Converted everything to **lowercase**
2. Removed punctuation except periods (`.`) because periods help identify sentence endings
3. Split the text into sentences using the period
4. Split each sentence into words

I wrote a helper method `clean_and_tokenize()` that returns a list of tokenized sentences.

Example:


"I am happy. You are here."
→ [["i", "am", "happy"], ["you", "are", "here"]]


---

## 3. Padding Sentences

Each sentence was padded with:

- `"<s>"` twice at the beginning  
- `"</s>"` once at the end  

This makes trigram formation easier and ensures the model knows how sentences start and end.

Example:

<s> <s> i am happy </s>

Padding lets the model learn valid sentence openings like:

<s> <s> i
<s> i am

---

## 4. Handling Unknown, Empty, and Short Text

- If the input text is empty, I simply mark the model as **not trained**.
- If the model isn’t trained, `generate()` returns an **empty string**.
- This ensures the tests for empty text and short text pass without errors.
- Short sentences still get padded, so they work normally.

---

## 5. Trigram Counting

After padding each sentence, I looped through it:

for i in range(len(padded) - 2):
(w1, w2, w3)

Each trigram is counted and stored in the nested dictionary.

---

## 6. Generating Text (Probabilistic Sampling)

To generate text:

1. Start with:

w1 = "<s>"
w2 = "<s>"

2. Look up all possible next words from the trigram dictionary
3. Convert trigram counts → probabilities
4. Use `random.choices()` to sample the next word based on probability
5. Stop generating when:
- The model predicts `"</s>"`
- Or we reach `max_length`

This makes the generation non-deterministic and more natural.

---

## 7. Why These Choices?

- **defaultdict** → easy, readable, avoids key errors  
- **Simple regex cleaning** → enough for assignment, avoids complexity  
- **Padding** → essential for good sentence starts  
- **Probability-based sampling** → better than picking the largest count  
- **Graceful handling of empty input** → required to pass tests  
- **Small and clean codebase** → easy to understand and review  

---

## 8. Result

- All 3 test cases passed successfully  
- The model trains correctly on the sample corpus  
- Text generation works and produces meaningful outputs  
- Code is simple, readable, and fully meets assignment guidelines  

This completes the implementation of the Trigram Language Model.