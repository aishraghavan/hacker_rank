"""
https://www.hackerrank.com/challenges/merge-list

Combinations:
https://en.wikipedia.org/wiki/Combination
"""
# def merge_list(array1, array2):
def merge_list(len_array1, len_array2):
	# if not array1 or not array2:
	# 	return 
	# len_array1 = len(array1)
	# len_array2 = len(array2)
	return combination_calculation(len_array1+len_array2, len_array1)

dict_val = {}



# def combination_calculation(higher, lower):
# 	print higher, lower
# 	if dict_val.get((higher, lower)):
# 		return dict_val.get((higher, lower))
# 	if lower>higher:
# 		dict_val[(higher, lower)] = 0
# 		return 0
# 	if (higher == lower) or lower==0:
# 		dict_val[(higher, lower)] = 1
# 		return 1
# 	return 	(combination_calculation(higher-1, lower-1) +
# 			combination_calculation(higher-1, lower))

def combination_calculation(higher, lower):
	if dict_val.get((higher, lower)):
		return dict_val.get((higher, lower))
	if lower>higher:
		dict_val[(higher, lower)] = 0
		return 0
	if (higher == lower) or lower==0:
		dict_val[(higher, lower)] = 1
		return 1
	#calculation_1 = combination_calculation(higher-1, lower-1)
	#if calculation_1 >10:
	temp = (combination_calculation(higher-1, lower-1) +
			combination_calculation(higher-1, lower))
	dict_val[(higher,lower)] = temp
	return temp


def mod_n(n):
	return n %pow(10,9)+7
	return n %10+7




def factorial(n):
	"""
	To test
	for i in range(10):
		print "factorial(",i,")", factorial(i)
	"""
	if n ==0 or n ==1:
		return 1
	return n*factorial(n-1)


if __name__ == "__main__":
	
	# print "combination_calculation(4,4)", combination_calculation(4,4)
	# print "combination_calculation(4,3)", combination_calculation(4,3)
	# print "combination_calculation(4,2)", combination_calculation(4,2)
	# print "combination_calculation(4,1)", combination_calculation(4,1)
	# print "combination_calculation(4,0)", combination_calculation(4,0)
	# print dict_val

	# print merge_list(len([1,2,3]), len([4,5,6]))
	# print merge_list(len([1,2]), len([4,5]))

	t = int(raw_input().strip())
	array =[]
	for a0 in xrange(t):
	  n,k = raw_input().strip().split(' ')
	  n,k = [int(n),int(k)]
	  array.append((n,k))
	for ele in array:
		print merge_list(ele[0], ele[1])
	print dict_val

