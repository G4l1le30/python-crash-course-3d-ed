"""
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""


def make_album(artist_name, title, song_number=None):
    album = {"name": artist_name, "title": title}
    if song_number:
        album["song_number"] = song_number
    return album


while True:
    print("Please tell me about the album:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist Name: ")
    if artist_name == "q":
        break

    album_name = input("Album title: ")

    album = make_album(artist_name, album_name)

    print(album)
