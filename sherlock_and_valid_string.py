"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string
"""
from sets import Set

def sherlock_and_valid_string(string):
	#incomplete
	hash_map = {}
	for ele in string:
		if ele in hash_map.keys():
			hash_map[ele] += 1
		else:
			hash_map[ele] = 1

	hash_map_set = Set(hash_map.values())
	if (len(hash_map_set) == 1):
		print "YES" 
	else:
		if len(hash_map_set) == 2:
			val1 = hash_map_set.pop()
			val2 = hash_map_set.pop()
			count_1 = 0
			count_2 = 0 
			for x in hash_map.values():
				if x == val1:
					count_1 +=1
				else:
					count_2 += 1
			print count_1, count_2
			if ((abs(count_2-count_1) == 1)or 
				(count_1 ==1 and count_2> 0) or
				(count_2 ==1 and count_1> 0)):
				print "YES"
			else:
				print "NO"
	#print "NO"

		#  and abs(hash_map_set.pop()- hash_map_set.pop()) == 1):
		# 	print "YES"
		# else:
		# print "NO"


string = str(raw_input().strip())
sherlock_and_valid_string(string)
