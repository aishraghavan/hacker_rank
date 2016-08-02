"""
https://www.hackerrank.com/challenges/two-strings
"""

def two_strings_simple(str1, str2):
    if not str1 or not str2:
        return False

    for ele in str1:
        for i in range(len(str2)):
            if ele == str2[i]:
                return True
    return False

def two_strings_hash_map(str1, str2):
    if not str1 or not str2:
        return False
    hash_map = {}
    for ele in str1:
        hash_map[ele] = hash_map.get(ele,0) +1

    for ele in str2:
        if ele in hash_map.keys():
            return True
    return False


def test_get_input():
    n = int(raw_input().strip())
    array_str = []
    for i in range(n):
        string1 = str(raw_input().strip())
        string2 = str(raw_input().strip())
        if len(string1) != 0:
            array_str.append((string1, string2))
    

    for element in array_str:
        print "Calling two_strings_simple with {0} and {1}".format(element[0], element[1])
        print "Result : {0}".format(two_strings_simple(element[0], element[1]))
        print "Calling two_strings_hash_map with {0} and {1}".format(element[0], element[1])
        print "Result : {0}".format(two_strings_hash_map(element[0], element[1]))


def print_and_format(str1, str2):
    print "input : str1 = {0}, str2 = {1}".format(str1, str2)
    print "Calling two_strings_simple"
    print "Result : {0}".format(two_strings_simple(str1, str2))
    print "Calling two_strings_hash_map"
    print "Result : {0}".format(two_strings_hash_map(str1, str2))

if __name__ == "__main__":
    # print_and_format("hello", "world")
    # print_and_format("hi", "world")
    test_get_input()
    """
    2
    hello
    world
    hi
    world
    """