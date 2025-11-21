# Evaluation – Trigram Language Model

This document explains the design choices I made while implementing the Trigram (N=3) Language Model for the AI/ML Intern Assignment.  
The entire solution is written from scratch using Python and simple data structures.

---

## 1. N-Gram Count Storage

I stored trigram counts using a nested dictionary:

```python
self.trigrams[w1][w2][w3] = count
```

To simplify initialization, I used Python’s `defaultdict`, so keys create themselves automatically.

Structure:

- `w1` → first word  
- `w2` → second word  
- `w3` → predicted next word  
- **value** → frequency of that trigram  

This structure is efficient and perfect for quick lookup during text generation.

---

## 2. Text Cleaning & Tokenization

My `clean_and_tokenize()` function performs:

1. Convert text to **lowercase**  
2. Remove punctuation (except `"."`, which marks sentence boundaries)  
3. Split text into sentences using `"."`  
4. Split each sentence into words

Example:

```text
"I am happy. You are here."
→ [["i", "am", "happy"], ["you", "are", "here"]]
```

This gives a clean list of tokenized sentences.

---

## 3. Sentence Padding

Padding helps the model learn valid sentence openings.

Each sentence is padded with:

- `"<s>"` twice at the start  
- `"</s>"` once at the end  

Example:

```text
<s> <s> i am happy </s>
```

Padding enables the model to learn sequences like:

- `<s> <s> i`
- `<s> i am`

This is essential for realistic text generation.

---

## 4. Handling Empty, Unknown & Short Text

To avoid errors:

- If input text is empty → mark the model as **not trained**
- If model is not trained → `generate()` returns an **empty string**
- Short sentences still get padded correctly
- This ensures all edge-case tests pass smoothly

This makes the model robust and predictable.

---

## 5. Trigram Counting

After padding each sentence, I extract trigrams by sliding a window:

```python
for i in range(len(padded) - 2):
    w1, w2, w3 = padded[i], padded[i+1], padded[i+2]
```

Each trigram is counted and stored inside the nested dictionary.

---

## 6. Text Generation (Probabilistic Sampling)

To generate text:

1. Start from the initial state:
   ```python
   w1 = "<s>"
   w2 = "<s>"
   ```
2. Look up all possible next words  
3. Convert counts → probabilities  
4. Sample the next word using:
   ```python
   random.choices(words, probabilities)
   ```
5. Stop when:
   - The model predicts `"</s>"`  
   - Or `max_length` is reached  

This produces non-deterministic but natural-looking sentences.

---

## 7. Why These Design Choices?

- **defaultdict**  
  Cleaner code, no need for key existence checks  
- **Simple regex cleaning**  
  Enough for assignment; avoids over-engineering  
- **Padding**  
  Required for realistic sentence beginnings  
- **Probabilistic sampling**  
  More natural than always picking the maximum count  
- **Graceful handling of empty input**  
  Ensures tests pass and avoids crashes  
- **Minimal, readable code**  
  Easy to evaluate and maintain  

---

## 8. Result Summary

- All **3 provided tests** passed successfully  
- Trigram counts are built correctly  
- Generation produces meaningful outputs  
- Code meets assignment requirements fully  
- The system behaves correctly for empty and short inputs  

---

This completes my implementation and evaluation of the Trigram Language Model.