#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.
    """
    if not boxes:
        return False
    if len(boxes) == 1:
        if type(boxes[0]) != list:
            return False
    keys = [0]
    for num in keys:
        for x in boxes[num]:
            if x not in keys and x != num and x < len(boxes) and x != 0:
                keys.append(x)
    if len(keys) == len(boxes):
        return True
    return False
