# Using one of the programs you wrote in this chapter, add a several lines to the end of the program that do the following:
# - Print the message "The first three items in the list are: ". Then use a slice to print the first three items from that programs list
# - Print the message "Three items from the middle of the list are: ". Then use a slice to print three items from the middle of the list
# - Print the message "The last three items in the list are: ". Then use a slice to print the last  three items in the list


# From 4-7_threes.py
# make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list

# list comprehension that stores multiples of 3 from 3 to 30
multiples_of_threes = [i * 3 for i in range(3, 31)]

for multiples_of_three in multiples_of_threes:
    print(multiples_of_three)

middlePrev = int(
    len(multiples_of_threes) / 2 - 1
)  # ambil nilai di tengah list, kurangi satu
middleNext = int(
    len(multiples_of_threes) / 2 + 2
)  # ambil nilai di tengah list, di tambah satu, agar list berhenti menghitung satu angka didepan tengah list

print(f"The first three items in the list are: {multiples_of_threes[:3]}")
print(
    f"Three items from the middle of the list are: {multiples_of_threes[middlePrev:middleNext]}"
)
print(f"The last three items in the list are: {multiples_of_threes[-3:]}")
print(f"Whole list are: {multiples_of_threes}")
