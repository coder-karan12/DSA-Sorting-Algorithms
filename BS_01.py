arr = [10,23,8,25,59,9,7,-3,-5,-55,-345,-11]

def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(Bubble_Sort(arr))
