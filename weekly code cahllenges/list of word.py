list_of_words = []

list_of_words = input ("Enter your list of words: ").split()

odd_list =[word for word in list_of_words if len(word) % 2 !=0 ]

print("Odd list of words: ", odd_list )