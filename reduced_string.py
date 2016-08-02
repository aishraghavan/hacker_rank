
#Hacker rank solution:

def hacker_rank_reduced_string():
    string = str(raw_input().strip())
    if not string:
        return None
    count = 1
    index = 0
    output_str = ""
    while index<len(string)-1:
        
        #print index, string[index], string[index+1]
        # next char equal
        if string[index] == string[index+1]:
            count += 1
        #not equal
        else:
            #equal to 1 # odd number
            if count%2 == 1: #or count == 0:
                output_str += string[index]
            # even
            else:
                count = 1
        index += 1
    #print index, count,output_str
    #last index:
    if index + 1 == len(string):
        if count%2 == 1:# or count != 1:
            #print "if loop"
            output_str += string[index]

    #
    if not output_str:
        return "Empty String"
    return output_str

"""
input
=======
abbbccddd   =>abd
aabccddd    =>bd
abddd       =>abd
baab        =>bb
bb          =>Empty String
"""


# def reduced_string(str1):
#     if not str1:
#         return 
#     counter = 1
#     temp_str =[]
#     prev_char = None#str1[0]
#     for i in range(len(str1)):
#         print "prev_char : {0}, str1[i]: {1} and i: {2}, counter: {3}".format(prev_char, str1[i], i, counter)
#         if prev_char == str1[i]:
#             counter += 1
#         else:
#             print counter
#             if counter%2 ==1 and prev_char: #or counter ==0:
#                 print "appending :{0}, str: {1}".format(prev_char, str1[i])
#                 temp_str.append(prev_char)
#             counter = 1
#             prev_char = str1[i]
#     return ''.join(temp_str)

def reduced_string(str1):
    counter = 1
    temp_str =""
    index = 0
    print "length : {0}".format(len(str1))
    while index<len(str1):
        if index+1!= len(str1):
            #print index, str1[index], counter, temp_str
            if str1[index] == str1[index+1]:
                counter += 1
            else:
                if counter == 0 or counter %2==1:
                    temp_str += str1[index]
            #     #reset counter
                counter = 1
        else:
            #handle last case
            if counter %2==1:
                temp_str += str1[index]

        index += 1
    
    #print index, str1[index], counter
    
    return str(temp_str)


            
if __name__ == "__main__":
    # str1 = "abbbccddd"
    # print "input: {0}".format(str1)
    # print reduced_string(str1)
    # str2 = "aabccddd"
    # print "input: {0}".format(str2)
    # print reduced_string(str2)
    # str3 = "abddd"
    # print "input: {0}".format(str3)
    # print reduced_string(str3)
    print hacker_rank_reduced_string()