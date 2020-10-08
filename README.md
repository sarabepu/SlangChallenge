# Slang Challenge: Engineering Intern 👩‍💻

This repository contains the solution to these functions:
- A simple function that given a piece of text and an integer n, it
returns the n-grams for that text.
- A simple function that given a piece of text and a integer n, it returns the most frecuent ngram in that text.

Both functions are solved in Python 3 and can be run as ``` python ngrams.py```
# Relevant decisions and considerations:
1) if the text is empty or n=0, the first function returns a list with an empty string. Since an empty set is a subset of every set I think an empty string is a ngram of every text.

2) if the length of the text is not greater or equal to n, the first function returns an empty. Since no ngram of that length will be found there.

2) The second function is case insensitive. Since Ngrams are widely used in NLP it wouldn't be convinient to distinguish between "A word" and "a word" since both mean the same

3) A hashtable is used in the second function because its complexity is O(1) when consulting

4) Both functions have complexity of O(len(text)) since the number of ngrams will never be greater than the length of the text (worst case is n=1)

5) I made a little interface so it's easier to debug and I'm supposing the text does not contain the special character "$"
