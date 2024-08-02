#!/usr/bin/python3
"""Function to check if all keys are unlocked"""


def canUnlockAll(boxes):
    """Function to check if all keys are unlocked"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]
    while keys:
        key = keys.pop(0)
        for k in boxes[key]:
            if k < n and not unlocked[k]:
                unlocked[k] = True
                keys.append(k)
    return all(unlocked)
