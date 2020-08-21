#!/bin/python3

import math
import os
import random
import re
import sys
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    orderList = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search('[a-z]@gmail',emailID):
            orderList.append(firstName)
    orderList.sort()
    for item in orderList:
        print (item)




if __name__ == '__main__':
    N = int(input())
    orderList = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search('[a-z]@gmail',emailID):
            orderList.append(firstName)
    orderList.sort()
    for item in orderList:
        print (item)
