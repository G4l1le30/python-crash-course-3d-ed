"""
Write if-elif-else chain that determines a person's stage of life. set a value for the variabel age, and then:
If age less than 2 years old, print that person is a baby
If at least 2 years old but less than 4, print that person is a toddler
If at least 4 yo but less than 13, print that person is a kid
If at least 13 yo but less than 20, print that person is a teenager
If at least 20 yo but less than 65, print that person is and adult
If 65 or older, elder
"""

age = 64

if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are an elder")
