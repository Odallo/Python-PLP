my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list = my_list[:1] + [15] + my_list[1:]

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

index = my_list.index(30)

print(index)

print(my_list)