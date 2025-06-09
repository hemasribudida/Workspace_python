from collections import Counter

paragraph = """Comprehensions are a feature of Python which I would really miss if I ever have to leave it. 
Comprehensions are constructs that allow sequences to be built from other sequences.
Several types of comprehensions are supported in both Python 2 and Python 3."""


normalized_text = paragraph.lower()

word_list = normalized_text.split()

frequency = Counter(word_list)

unique_count = len(frequency)

print(f"Number of unique words: {unique_count}\n")

for w, c in frequency.items():
    print(f"{w}: {c} times")
