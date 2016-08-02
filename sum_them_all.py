def sum_them_all(array_int):
	sum = 0
	for ele in array_int:
		sum += ele
	return sum

t = int(raw_input().strip())
array_int = []
for a0 in xrange(t):
    n = int(raw_input().strip())
    array_int.append(n)
print sum_them_all(array_int)
