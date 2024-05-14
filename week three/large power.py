large_power = ()


base = int(input("Enter the base number: "))
power = int(input("Enter the exponentiation: ")) 

large_power = base ** power

print (large_power)

if large_power > 5000:
    result = True
else:
    result = False
print(result)