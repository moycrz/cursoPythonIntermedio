from functools import reduce

#############Filter#############
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = [i for i in my_list if i%2 != 0]
print(odd)

odd = list(filter(lambda i: i%2 != 0, my_list))
print(odd)

#############Map#############
squares = [i**2 for i in range(1,6)]
print(squares)

my_list = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, my_list))
print(squares)

#############Reduce#############
my_list = [2, 2, 2, 2, 2]
all_multiplied = 1

for i in my_list:
    all_multiplied = all_multiplied * i

print(all_multiplied)


my_list = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)

