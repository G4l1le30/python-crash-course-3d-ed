"""
We’re now working with examples that are complex enough that they can be extended in any number of ways.
Use one of the example programs from this chapter, and extend it by adding new keys and values,
changing the context of the program, or improving the formatting of the output.
"""

# from 6-6_polling.py

favorite_languages = {
    "jen": {
        "first": "c",
        "second": "c++",
        "third": "python",
    },
    "sarah": {
        "first": "rust",
        "second": "golang",
        "third": "c#",
    },
    "edward": {"first": "python", "second": "java"},
    "phil": {"first": "lua"},
}


names = ["jen", "phil", "josh", "kimi"]

for name in names:
    if name in favorite_languages:
        print(f"Thank you {name}, for responding")
    else:
        print(f"{name}, please take our poll!")

for name, favorite_language in favorite_languages.items():
    s = " is" if len(favorite_language) == 1 else "s are"
    print(f"{name}'s favorite language{s}: ")
    for rank, language in favorite_language.items():
        print(f"{rank}: {language}")
