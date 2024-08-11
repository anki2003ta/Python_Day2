lst_tuples= []
for i in range(4):
	print(f"Enter elements for tuple {i+1}:")
	tup = []
	# Take limitation of tuple from user
	limit = int(input("Enter the maximum number of elements in each tuple: "))

	for j in range(limit):
		elem = input(f"Element {j+1} (or 'stop' to finish): ")
		if(elem.lower() == 'stop'):
			break
		tup.append(int(elem))
	lst_tuples.append(tuple(tup))
print("List of Tuples:", lst_tuples)
# Convert each tuple to a list using list comprehension
list_of_lists = [list(tup) for tup in lst_tuples]

# Print the result
print("List of lists:", list_of_lists)
