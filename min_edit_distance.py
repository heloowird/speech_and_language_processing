#coding: utf-8
#author: heloowird

import os
import sys

def print_distance_table(str1, str2, tbl, sep=" "):
    for i in range(0, len(str2)+2):
        for j in range(0, len(str1)+2):
            if i == 0 and j == 0:
                print("{:1}".format(" "), end=sep)
            elif i == 0 and j == 1:
                print(" {}".format("#"), end=sep)
            elif i == 1 and j == 0:
                print("#", end=sep)
            elif i == 0 and j > 1:
                print(" {}".format(str1[j-2]), end=sep)
            elif i > 1 and j == 0:
                print("{}".format(str2[i-2]), end=sep)
            else:
                print("{:2}".format(tbl[i-1][j-1]), end=sep)
        print()

def cal_min_edit_distance(str1, str2):
    if str1 is None or str2 is None:
        raise Exception("None arguments")

    if not len(str1):
        return len(str2)

    if not len(str2):
        return len(str1)

    distance_table = [[0 for j in range(len(str1)+1)] for i in range(len(str2)+1)]
    for j in range(len(str1)+1):
        distance_table[0][j] = j 
    for i in range(len(str2)+1):
        distance_table[i][0] = i 

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            distance_table[i][j] = min(
                distance_table[i-1][j]+1,
                distance_table[i][j-1]+1, 
                distance_table[i-1][j-1] + (0 if str2[i-1] == str1[j-1] else 2)
            )

    return distance_table

def main():
    str1 = "execution"
    str2 = "intention"
    distance_table = cal_min_edit_distance(str1, str2)
    print("str1: {}\nstr2: {}\nthe min edit distance of \"{}\" and \"{}\": {}".format(str1, str2, str1, str2, distance_table[len(str2)][len(str1)]))
    print("the min distance table:")
    print_distance_table(str1, str2, distance_table) 

if __name__ == "__main__":
    main()
