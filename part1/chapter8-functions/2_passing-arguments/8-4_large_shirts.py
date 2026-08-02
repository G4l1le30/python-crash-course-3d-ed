"""
Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message,
and a shirt of any size with a different message.
"""


def make_shirt(message="I love Python", size="Large"):
    print(
        f"The customer asked for a t-shirt with size of {size} and a message '{message}' on it"
    )


# large size with default message
make_shirt()

# medium size with default message
make_shirt(size="Medium")

# any size with custom message
make_shirt("I love Cofee!", "Extra Large")
