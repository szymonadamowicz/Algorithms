def quick_sort(arr):
    lenght = len(arr)
    lower = []
    greater = []
    if lenght <= 1:
        return arr
    else:
        pivot = arr.pop()
    for i in arr:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quick_sort(lower) + [pivot] + quick_sort(greater)
print(quick_sort([2,1,3,7]))