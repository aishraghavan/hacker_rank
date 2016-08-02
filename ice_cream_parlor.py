"""
https://www.hackerrank.com/challenges/icecream-parlor

Sample Input
2
4
5
1 4 5 3 2
4
4
2 2 4 3
Sample Output

1 4
1 2
"""
from collections import namedtuple
from copy import deepcopy
Ice_cream = namedtuple('Ice_cream', ['money', 'array_cost'])

def ice_cream_choice(m, array_of_prices):
    #array_of_prices.sort()

    # if all the ice creams are costier than amount 'm'.
    if m<min(array_of_prices):
        return -1
    # for index in range(len(array_of_prices)):
    #     if array_of_prices[index]<0:
    #         return -1

    temp = deepcopy(array_of_prices)
    for index in range(len(array_of_prices)):
        first = array_of_prices[index]

        temp.remove(first)
        if m-first in temp:
            second = temp.index(m-first)
            print index+1, second+2
            return
    print -1, -1
    return

def test_ice_cream_choice():
    n = int(raw_input().strip())

    array_int = []
    for i in range(n):
        array_cost = []
        money = int(raw_input().strip())
        varities = int(raw_input().strip())
        if varities <=0:
            return -1
        array_cost = map(int,raw_input().strip().split(' '))
        # for i in range(varities):
        #     cost = int(raw_input().strip())
        array_int.append(Ice_cream(money, array_cost))

    for element in array_int:
        ice_cream_choice(element.money, element.array_cost)


# print ice_cream_choice(4, [-1,6,7])
# print ice_cream_choice(4, [20,6,7])
# print ice_cream_choice(4, [1, 4, 5, 3, 2])
test_ice_cream_choice()
