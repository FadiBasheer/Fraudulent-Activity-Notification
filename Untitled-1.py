
import math
import os
import random
import re
from statistics import median
import sys


def activityNotifications(expenditure, d):
    dictionary = {}

    # function to get median
    def get_median(idx):
        s = 0
        for i in range(201):
            freq = 0
            if i in dictionary:
                freq = dictionary[i]
            s += freq

            if s >= idx:
                return i

    result = 0

    for i in range(n):
        val = expenditure[i]

        if i >= d:
            med = get_median(d // 2 + d % 2)

            if d % 2 == 0:
                if val >= med + get_median(d // 2 + 1):
                    result += 1

            else:
                if val >= med * 2:
                    result += 1

        # add curent value in dictionary sliding window
        if val not in dictionary:
            dictionary[val] = 1
        else:
            dictionary[val] += 1

        # remove elemnt out of sliding window

        if i >= d:
            prev = expenditure[i - d]
            dictionary[prev] -= 1

    return result


if __name__ == "__main__":
    n = 9
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    result = activityNotifications(expenditure, 5)
    print(result)
