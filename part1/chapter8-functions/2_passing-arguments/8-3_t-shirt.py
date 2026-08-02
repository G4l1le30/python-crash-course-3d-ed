"""
Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


def make_shirt(size, message):
    print(
        f"The customer asked for a t-shirt with size of {size} and a message '{message}' on it"
    )


# function call using positional arguments
make_shirt("XL", "Python is fun!")

# function call using keyword arguments
make_shirt(message="I love Python!", size="M")
