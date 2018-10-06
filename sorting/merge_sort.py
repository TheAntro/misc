import random


def merge_sort(sort_list):
	# Base case, a list of one or no elements:
	if (len(sort_list) <= 1):
		return sort_list

	# Recursive case, dividing list into two halves:
	left_list = sort_list[:len(sort_list)//2]
	right_list = sort_list[len(sort_list)//2:]

	# Recursively sort both sublists.

	left_list = merge_sort(left_list)
	right_list = merge_sort(right_list)

	return merge(left_list, right_list)


def merge(left, right):
	result = []

	while (len(left) > 0 and len(right) > 0):
		if (left[0] <= right[0]):
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))

	while (len(left) > 0):
		result.append(left.pop(0))
	while (len(right) > 0):
		result.append(right.pop(0))

	return result


unsorted = random.sample(range(100), 10)
print(unsorted)
sorted_list = merge_sort(unsorted)
print(sorted_list)
