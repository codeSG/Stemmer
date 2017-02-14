# Stemmer
# Stem Lookup
	Stemming is a core task for NLP which relates different forms of a given word to a main noun word. For highly inflected languages like Sanskrit, the task is even more ambiguous as words often have around two dozen possible forms which also varies depending on gender and their ending character.
Here, It reduces all possible inflected words to their word stem/main noun.
The function takes only inflected word in ‘Devanagari’ as input and return its word stem in same.

In [1]: from Stemming import stem
In [2]: stem('अस्य')
Out [2]: इदम्
In [3]: stem('विद्वद्भ्यः')
Out [3]: विद्वस्

