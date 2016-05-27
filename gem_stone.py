"""
https://www.hackerrank.com/challenges/gem-stones

1. compare two at a time. - no
2. will hash map idea work? No
3. Use set intersections - yes!!!

3
abcdde
baccd
eeabg
"""
from sets import Set


def test_gem_stones():
    n = int(raw_input().strip())
    if n<0:
        return None
    array_str = []
    for i in range(n):
        string = str(raw_input().strip())
        if len(string) != 0 or not string.isspace():
            array_str.append(string)

    gem_stones = Set(array_str[0])
    for index in range(1,len(array_str)):
        c = Set(array_str[index])
        gem_stones =  gem_stones&(c)

    print len(gem_stones) if len(gem_stones)>0 else None


test_gem_stones()
