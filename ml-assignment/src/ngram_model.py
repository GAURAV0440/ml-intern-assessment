import random
import re
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        # Store trigram counts in nested dict: counts[w1][w2][w3] = count
        self.trigrams = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.vocab = set()
        self.is_trained = False

    def clean_and_tokenize(self, text):
        """Lowercase, remove punctuation, split into tokens."""
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s\.]", "", text)   # keep letters, numbers, spaces, periods
        tokens = []

        # Split by period to detect sentence boundaries
        sentences = [s.strip() for s in text.split('.') if s.strip()]

        for s in sentences:
            words = s.split()
            if words:
                tokens.append(words)

        return tokens

    def fit(self, text):
        """
        Trains the trigram model on the given text.
        """
        if not text or text.strip() == "":
            # No training data → model should generate empty string
            self.is_trained = False
            return

        sentences = self.clean_and_tokenize(text)

        if not sentences:
            self.is_trained = False
            return

        for words in sentences:
            # Pad each sentence with 2 start tokens and 1 end token
            padded = ["<s>", "<s>"] + words + ["</s>"]

            # Count trigrams
            for i in range(len(padded) - 2):
                w1, w2, w3 = padded[i], padded[i+1], padded[i+2]
                self.trigrams[w1][w2][w3] += 1
                self.vocab.add(w3)

        self.is_trained = True

    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.
        """
        if not self.is_trained:
            return ""

        w1, w2 = "<s>", "<s>"
        output_words = []

        for _ in range(max_length):
            possible_next = self.trigrams[w1][w2]

            if not possible_next:
                break

            # Convert counts to probabilities
            words = list(possible_next.keys())
            counts = list(possible_next.values())
            total = sum(counts)
            probabilities = [c / total for c in counts]

            # Sample a word based on probability
            w3 = random.choices(words, probabilities)[0]

            if w3 == "</s>":
                break

            output_words.append(w3)

            # Move to next window
            w1, w2 = w2, w3

        return " ".join(output_words)
