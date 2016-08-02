"""
https://www.hackerrank.com/challenges/manasa-and-combinatorics
"""
def swap(array,i , j):
    array[i], array[j] = array[j], array[i]
    return array

list_of_valid_strings = []
def permutations_of_string_recursion(string, left, right):
    if left == right:
        temp = ''.join(string)
        print temp, is_valid(temp)

    else:
        for i in range(left, right+1):
            string = swap(string, left, i)
            permutations_of_string_recursion(string, left+1, right)
            string = swap(string, left, i)


def is_valid(string):
	#for index in range(len(string)):
	index = 0
	while index<len(string):
		if (index == 0 or index==len(string)-1) and string[index] =='A':
			return False
		# if string[index] =='A' check before and after
		elif string[index] =='A' and string[index-1] !='B' and string[index+1] != 'B':
			return False
		index += 1
	return True



# def generate_comnination_of_a_and_b(n, array):
# 	length_input = len(input)
# 	   for length_determiner in range(length_input, 0, -1): # length of substring
# 	       #print "length_determiner", length_determiner
# 	       #total = 0
# 	       max_element = 0
# 	       for index in range(0, length_input-length_determiner+1):
# 	           #print input[index:index+length_determiner]

permutations_of_string_recursion(['A','B','B'],0, 2)
#print is_valid('BAA')