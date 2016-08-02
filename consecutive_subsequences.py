"""
https://www.hackerrank.com/challenges/consecutive-subsequences
"""
def continuos_sub_sequence_divisible_by_n(input, n):
    count_sol = 0
    length_input = len(input)
    for length_determiner in range(length_input, 0, -1): # length of substring
        #print "length_determiner", length_determiner
        total = 0
        for index in range(0, length_input-length_determiner+1):
            #print index, range(0, length_input-length_determiner)
            
            total+=sum(v for v in input[index:index+length_determiner])
            #print input[index:index+length_determiner], total
            #print total
            if total %n ==0:
                count_sol+= 1
            total = 0
    return count_sol
 
n = int(raw_input().strip())
n_array = []
for e in range(n):
    array1 = map(int,raw_input().strip().split(' '))
    array2 = map(int,raw_input().strip().split(' '))
    n_array.append([array2, array1[1]])

for e in n_array:
    print continuos_sub_sequence_divisible_by_n(e[0], e[1])

"""
5 3
1 2 3 4 1

output 
4
"""