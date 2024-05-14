integers_one = {}
integers_two = {}

integers_one = int( input ("Enter your first collection of integres: "))
integers_one['values'] = list(map(int, integers_one.split))
integers_two = int(input ("Enter you second collection: "))
integers_two['values'] = list(map(int, integers_two.split))

print(integers_one)