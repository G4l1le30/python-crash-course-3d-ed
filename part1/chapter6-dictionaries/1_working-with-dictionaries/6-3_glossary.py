"""
A python dictionary can be used to model an actual dictionary.
However, to avoid confusion, lets call it a glossary

- Think of 5 programming words you've learned about in this previous chapters.
Use these words as the keys in your glossary, and store their meanings as values

- Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then it's meaning,
or print the word on one line then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning
pair in your output
"""

programming_words = {
    "get": "To fetch something",
    "key": "unique identifier",
    "value": "key's corresponding data",
    "dictionary": "A connected pieces of realted information stored",
    "pair": "Connection between key and value",
}

print(f"get in python dictionary means {programming_words['get']}")
print(f"key in python dictionary means {programming_words['key']}")
print(f"value in python dictionary means {programming_words['value']}")
print(f"dictionary in python dictionary means {programming_words['dictionary']}")
print(f"pair in python dictionary means {programming_words['pair']}")
