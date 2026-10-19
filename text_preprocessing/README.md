# Text Preprocessing Pipeline

## What it does
Takes a raw paragraph typed by the user and converts it into a cleaned list of tokens (words) with common stopwords removed, then counts how often each remaining word appears. Built using only core Python and the `re` module.

## Pipeline
lowercase -> strip punctuation -> tokenize -> remove stopwords -> count frequencies

## How to run
From inside the `text_preprocessing` folder:

```
python Text_Preprocessing_Pipeline.py
```

## Example
Input:
```
Run, run, run away very fast!Wait, wait, wait for me!No, no, no, we cannot go back!Would you like a longer story or a funny poem using this style?
```

Output (word frequencies):
```
{'run': 3, 'away': 1, 'very': 1, 'fast': 1, 'wait': 3, 'me': 1, 'no': 3, 'we': 1, 'cannot': 1, 'go': 1, 'back': 1, 'would': 1, 'you': 1, 'like': 1, 'longer': 1, 'story': 1, 'funny': 1, 'poem': 1, 'using': 1, 'style': 1}
```

## Bugs I hit and fixed
- **`text.lower()` had no effect:** strings are immutable, so `.lower()` returns a new string instead of changing the original. Fix: `text = text.lower()`.
- **Removing items while looping over the list:** calling `tokens.remove(i)` inside `for i in tokens` skips elements, because removing an item shifts the rest left while the loop counter keeps moving. Fix: build a new list (`clean_tokens`) instead of mutating the one being iterated.
- **`==` instead of `in` for stopword check:** `word == stopwords`