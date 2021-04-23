#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Locked boxes.
    * Boxes list
    """
    if not boxes:
        return False
    if len(boxes) == 1:
        if type(boxes[0]) != list:
            return False
    for b in boxes:
        if type(b) != list:
                return False
    box_numbers = [num for num in range(1, len(boxes))]
    box_keys = []
    for index_of_box in range(1, len(boxes)):
        for box in boxes:
            if type(box) != list:
                return False
            if boxes.index(box) != index_of_box:
                for key in box:
                    if key == index_of_box:
                        box_keys.append(key)
    if set(box_numbers) == set(box_keys):
        return True
    else:
        return False