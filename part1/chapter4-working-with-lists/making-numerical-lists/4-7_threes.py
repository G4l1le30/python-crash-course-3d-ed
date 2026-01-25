# make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list

# list comprehension that stores multiples of 3 from 3 to 30
multiples_of_threes= [i*3 for i in range(3,31)]

for multiples_of_three in multiples_of_threes:
    print(multiples_of_three)
