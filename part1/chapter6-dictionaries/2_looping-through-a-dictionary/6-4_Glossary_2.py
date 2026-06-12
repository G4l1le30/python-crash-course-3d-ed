"""
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of print() calls with a loop that runs through
the dictionary's keys and values. When you're sure that your loop works, add five more python terms to your glossary.
When you run your program again, these new words and meaning should automatically be included in the output.
"""

programming_words = {
    "get": "To fetch something",
    "key": "unique identifier",
    "value": "key's corresponding data",
    "dictionary": "A connected pieces of realted information stored",
    "pair": "Connection between key and value",
    "callable": "A callable is an object that can be called, possibly with a set of arguments (see argument), with the following syntax:",
    "class": "A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.",
    "concurrency": "The ability of a computer program to perform multiple tasks at the same time.",
    "coroutine": "Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point.",
    "CPython": "The canonical implementation of the Python programming language, as distributed on python.org.",
}

for word in programming_words.keys():
    print(f"{word} in python dictionary means {programming_words[word]}")
