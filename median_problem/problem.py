def get_median(array):
    if not len(array):
        return None 
    med = int(len(array)/2)
    if not len(array)%2 :
        answer = (array[med - 1] + array[med])/2
        return int(answer) if answer.is_integer() else answer
    else:
        return array[med]

def truncate_arr(arr, med, is_less):
    if is_less:
        return arr[med: ]
    else:
        if len(arr)%2:
            return arr[ :med + 1]
        else:
            return arr[ :med]



def median_of_two_lists(arr1, arr2):
    if len(arr1) == 0 or len(arr2) ==0 or arr1[len(arr1) - 1] <= arr2[len(arr2) - 1]:
        arr1.extend(arr2)
        return get_median(sorted(arr1))

    if arr2[len(arr2) - 1] <= arr1[len(arr1) - 1]:
        arr2.extend(arr1)
        return get_median(sorted(arr2))
    
    med_1, med_2 = int(len(arr1)/2), int(len(arr2)/2)
    med1_less = False
    if arr1[med_1] <= arr2[med_2]:
        med1_less = True
    return median_of_two_lists(truncate_arr(arr1, med_1, med1_less), 
        truncate_arr(arr2, med_2, not med1_less))


arr0 = [1, 2, 3]
arr1 = [3, 4, 4, 5]
arr2 = [3, 4, 4, 5, 7, 9]

arr3 = [1, 4]
arr4 = [3, 6, 7, 9, 11, 14, 16]

arr5 = [24]
arr6 = [3, 7, 9, 10, 12, 15, 17, 18, 18]

assert(median_of_two_lists(arr0, arr1) == 3)
assert(median_of_two_lists(arr0, arr2) == 4)
assert(median_of_two_lists(arr3, arr4) == 7)
assert(median_of_two_lists(arr4, arr6) == 10.5)
assert(median_of_two_lists([], []) == None)
assert(median_of_two_lists([], [1, 2, 3]) == 2)
assert(median_of_two_lists([1, 2, 3], []) == 2)

print("All Tests Passed")