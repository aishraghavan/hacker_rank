"""
https://www.hackerrank.com/challenges/making-anagrams
asdf
awert
7

abc
acb

imkhnpqnhlvaxlmrsskbyyrhwfvgteubrelgubvdmrdmesfxkpykprunzpustowmvhupkqsyjxmnptkcilmzcinbzjwvxshubeln
wfnfdassvfugqjfuruwrdumdmvxpbjcxorettxmpcivurcolxmeagsdundjronoehtyaskpwumqmpgzmtdmbvsykxhblxspgnpgfzydukvizbhlwmaajuytrhxeepvmcltjmroibjsdkbqjnqjwmhsfopjvehhiuctgthrxqjaclqnyjwxxfpdueorkvaspdnywupvmy
102
"""


def making_anagrams_hash_map(str1, str2):
	hash_map = {}
	# print len(str1)
	# print len(str2)
	if len(str1)> len(str2):
		return len(str1)
	else:
		return len(str2)

	for ele in str1:
		if ele not in hash_map.keys():
			hash_map[ele] = 1
		else:
			hash_map[ele] += 1
	for ele in str2:
		if ele in hash_map.keys():
			hash_map[ele] = abs(hash_map[ele]-1)
		else:
			hash_map[ele] = 1

	print hash_map
	return abs(sum(hash_map.values()))

string1 = str(raw_input().strip())
string2 = str(raw_input().strip())

print making_anagrams_hash_map(string1, string2)