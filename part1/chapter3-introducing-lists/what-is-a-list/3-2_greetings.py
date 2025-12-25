# Start with the list you used in Exercise 3-1, but instead of just printing each person's name, Print a message to them 
#  The text of each message should be the same, but each message should be personalized with the person's name

names=['Darvesh', 'Haris', 'steven', 'bram', 'Karin', 'Kezia']

#Membuat pengulangan dari 0 sampai panjang list
for i in range (len(names)):
    # print hello dengan akses list sesuai index i
    print(f"Hello, {names[i].title()}!")

