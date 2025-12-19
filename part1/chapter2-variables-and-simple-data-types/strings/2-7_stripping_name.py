# Use a variable to represent a person's name, and include some whitespace characters at the beginning and the end of the name
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace and the name is displayed.
# Then print the name using each of the three stripping function, lstrip(), rstrip(), and strip()

person = " \t Karin\n "

print(person)
print(f"{person.lstrip()}\n{person.rstrip()}\n{person.strip()}")
