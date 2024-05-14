divisible_by_ten = ()

num = int(input("Enter your number to be tested: "))

divisible_by_ten = num

test = num % 2

if test > 0:
    result = False
else:
    result = True

print (result)
