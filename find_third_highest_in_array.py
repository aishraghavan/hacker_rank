from sys import maxint

def find_third_highest_in_array(array):
    minint = -maxint -2
    #print maxint, minint
    max_1 = minint
    max_2 = minint
    max_3 = minint
    for i in range(len(array)):
        if array[i]>max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = array[i]
        elif array[i]>max_2:
            max_3 = max_2
            max_2 = array[i]
        elif array[i]>max_3:
            max_3 = array[i]
    return max_3

def format_and_print(array, expected_output):
    print "Input: ", array, " Expected_output: ", expected_output
    output = find_third_highest_in_array(array)
    print output, (output==expected_output)

if __name__ == "__main__":
    input_arrays = [
        [7,3,12,14,6,8,1],
        [10,9,8,7,6,5,4,3,2,1],
        [10,9,8,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,10],
        [-3,-14,-6,-8,-12,-12,1]
    ]
    expected_output = [8, 8, 8, 8, -6]
    for i in range(len(input_arrays)):
        format_and_print(input_arrays[i], expected_output[i])
