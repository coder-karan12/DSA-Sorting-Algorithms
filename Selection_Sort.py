arr = [50,10,20,80,90,100,70,25]

def find_Max(arr,last):
    max = 0
    for x in range(1,last+1):
        if arr[max] < arr[x]:
            max = x
    return max


def Selection_Sort(arr):

    last = len(arr)-1

    while last > 0:
        maxindex = find_Max(arr,last)
        temp = arr[last]
        arr[last] = arr[maxindex]
        arr[maxindex] = temp
        last = last - 1
    return arr


print(Selection_Sort(arr))