"""
https://www.hackerrank.com/challenges/number-list

Sample Input
2
3 2
1 2 3 
3 1 
1 2 3 
Sample Output

3
5

"""
def number_list(input, k):
    output_list = []
    length_input = len(input)
    for length_determiner in range(length_input, 0, -1): # length of substring
        #print "length_determiner", length_determiner
        #total = 0
        max_element = 0
        for index in range(0, length_input-length_determiner+1):
            #print input[index:index+length_determiner]
            #total+=sum(v for v in input[index:index+length_determiner])
            max_element = max(input[index:index+length_determiner])
            if max_element>k:
                output_list.append(max_element)
    return len(output_list)

# if __name__ == "__main__":
#     array = [1,2,3]
#     print number_list(array, k=2)
#     print number_list(array, k=1)
n = int(raw_input().strip())
n_array = []
for e in range(n):
    array1 = map(int,raw_input().strip().split(' '))
    array2 = map(int,raw_input().strip().split(' '))
    n_array.append([array2, array1[1]])

for e in n_array:
    print number_list(e[0],e[1])