#!/usr/bin/python3
"""This module defines pascal triangle with n rows"""


def pascal_triangle(n):
    """This methos will returns a list of lists of
    integers representing the Pascal’s triangle of n """
    if n <= 0:
        return []

    list_of_list = [[1]]
    for _ in range(1, n):
        prev_row = list_of_list[-1]
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        list_of_list.append(new_row)

    return list_of_list
