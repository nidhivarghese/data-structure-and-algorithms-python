# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2
#
# [2, 1, 1, 2, 3, 5, 1, 2, 4]
# return 1
#
# [2, 3, 4, 5]
# return None

def firstRecurringCharUsingArr(arr):
    recChar = []
    for num in arr:
        if num in recChar:
            return num
        else:
            recChar.append(num)

    return None

def firstRecurringCharUsingMap(arr):
    recChar = dict()

    for num in arr:
        if num in recChar:
            return num
        else:
            recChar[num] = 1
    return None

arr = [2, 5, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurringCharUsingArr(arr))
print(firstRecurringCharUsingMap(arr))