# Take limitation of tuple from user
limit = int(input("Enter the number of inner tuples: "))

# Take input for tuple from user
nums = []
for i in range(limit):
    inner_tuple = []
    for j in range(3):
        elem = int(input(f"Enter element {j+1} for inner tuple {i+1}: "))
        inner_tuple.append(elem)
    nums.append(tuple(inner_tuple))

# Calculate averages using list comprehension
def averages_list_comprehension(nums):
	avg = [sum(tup[i] for tup in nums) / len(nums) for i in range(3)]
	return avg
averages=averages_list_comprehension(nums)
# Print the result
print("Averages:", averages)


