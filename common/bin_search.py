def bin_search(elem, lst):
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (end+start)//2
        if lst[mid] < elem:
            start = mid+1
        elif lst[mid] > elem:
            end = mid-1
        else:
            return mid
    return -1




print(bin_search(9, [1,2,4,5,6,7,8]))
