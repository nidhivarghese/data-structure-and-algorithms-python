# Merge two sorted arrays [[0, 3, 4, 31], [4, 6, 30]]
# into:
# [0, 3, 4, 4, 6, 30, 31]


def mergeSorted(arr1, arr2):
    sortedArr = []
    i = 0
    j = 0

    while (i != len(arr1) and j != len(arr2)):
        if(arr1[i] < arr2[j]):
            sortedArr.append(arr1[i])
            i+=1
        else:
            sortedArr.append(arr2[j])
            j+=1

    if i != len(arr1):
        sortedArr += arr1[i: ]
    else:
        sortedArr += arr2[j: ]

    return sortedArr


arr1 = [1,3,5,7]
arr2 = [2,4,6,8,10,12]

print(mergeSorted(arr1, arr2))