# Create an empty list
my_list = []

# Prompt the user to enter integers
while True:
  num = input("Enter an integer (or 'done' to finish): ")
  if num.lower() == "done":
    break
  my_list.append(int(num))

# Compute the sum of the integers in the list
sum = 0
for num in my_list:
  sum += num

# Print the sum
print("The sum of the integers in the list is:", sum)