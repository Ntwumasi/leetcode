# Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

# def sort_two_arrays(arr1, arr2):
#     arr3 = arr1 + arr2
    # arr3.sort()

    # print(sort_two_arrays(["can","bottle"],["bucket","container"]))

    # lol good try nokio


def combine_two_sorted_arrays(arr1,arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i +=1
        else:
            ans.append(arr2[j])
            j +=1
    while i < len(arr1):
        ans.append(arr1[i])
        i +=1
    while j < len(arr2):
        ans.append(arr2[j])
        j +=1
    return ans

print(combine_two_sorted_arrays([1,5,8],[2,3,4,6,7]))
