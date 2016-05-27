"""
https://www.hackerrank.com/challenges/the-love-letter-mystery/
"""

def test_number_of_changes_to_palindrome():
    n = int(raw_input().strip())
    array_str = []
    for i in range(n):
        string = str(raw_input().strip())
        if len(string) != 0:
            array_str.append(string)

    for element in array_str:
        print number_of_changes_to_palindrome(element)



def number_of_changes_to_palindrome(string):
    if not string or len(string)==0 or string.isspace():
        return 0
    total_diff = 0
    length = len(string)
    for index in range(length/2):
        start_index = index
        end_index = length-start_index-1
        #assume if it is alphabetically
        diff = abs(ord(string[start_index])-ord(string[end_index]))
        total_diff += diff
    return total_diff

print number_of_changes_to_palindrome("abc")
print number_of_changes_to_palindrome("abcba")
print number_of_changes_to_palindrome("abcd")
print number_of_changes_to_palindrome("cba")
test_number_of_changes_to_palindrome()
