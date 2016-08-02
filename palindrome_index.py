"""
https://www.hackerrank.com/challenges/palindrome-index

3
aaab
baa
aaa
Sample Output

3
0
-1
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_palindrome(string):
    i = 0
    j = len(string)-1
    while(i<j):
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def palindrome_index(string):
 	if is_palindrome(string):
 		return -1

 	for i in range(len(string)):
 		if(is_palindrome(string[:i]+string[i+1:])):
 			return i



#slow
# def longest_palindromic_substring_possible_better(string):
#     if string == None:
#         return None
#     length_string = len(string)
#     # 6,5,4,3
#     for index1 in range(length_string, 0, -1): # length of substring
#         for index2 in range(0, len(string)-index1+1):
#             temp_str = string[index2:index2+index1]
#             if is_palindrome(temp_str):
#             	#print temp_str, index2, ":", index2+index1, len(string)
#             	#complete string is palindrome
#             	if index1 == len(string):
#             		return -1
#             	else:
#             		#equal to 0
#             		if index2!=0:
#             			return index2-1
#             		# equal to length of string
#             		elif index1<len(string):
#             			return index1
#     return None

t = int(raw_input().strip())
array_of_strings = []
for a0 in xrange(t):
	string = str(raw_input().strip())
	array_of_strings.append(string)

for a0 in xrange(len(array_of_strings)):
	temp_str = array_of_strings[a0]
	#print is_palindrome(temp_str), longest_palindromic_substring_possible_better(temp_str)
	#print longest_palindromic_substring_possible_better(temp_str)
	print palindrome_index(temp_str)
