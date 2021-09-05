"""
count the occurrences of words in string

ask for string, count how many of each word occures
"""

"""
test text
this is a collection of words of nice words this is a fun thing it is
"""

WORD_COUNT = {}

line_of_text = input("Text: ")
words = line_of_text.split()
for word in words:
    frequency = WORD_COUNT.get(word, 0)
    WORD_COUNT[word] = frequency + 1

words = list(WORD_COUNT.keys())
words.sort()

max_length = max(len(key) for key in WORD_COUNT)

for word in words:
    print("{:{}} : {}".format(word, max_length, WORD_COUNT[word]))
