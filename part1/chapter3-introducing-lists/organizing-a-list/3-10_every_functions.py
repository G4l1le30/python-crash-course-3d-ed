"""
think of things you could store in a list. For example, you could make a list
of mountains, rivers, countries, cities, languages, or anything else you'd like.
Write a program that creates a list containing these items, than uses each functions introduced in this 
chapter at least once.
"""

# 3-6 => insert, append
# 3-7 => pop, del
# 3-8 => sorted, sort, reverse
# 3-9 => len


songs = [
    'always', 
    'hungry eyes', 
    'making love out of nothing at all',
    'bed of roses',
    'back in black',
    'everything u are',
    'cincin'
    ]

print(f"i have {len(songs)} right now, they are {songs}")

#insert and append
songs.insert(1,"arteri")
print(f"i also like {songs[1]}.")

songs.append("thunderstruck")
print(f"and {songs[-1]}")

# sorted, sort

print(f"so now my favorites songs in reverse-alphabetical oder are {sorted(songs, reverse=True)}")
songs.sort()

