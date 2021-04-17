
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)



def partition(arr, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i+1


n = int(input("enter list number :"))
arr = []
for i in range(0, n):
    a = int(input("enter value " + str(i) + ": "))
    arr.append(a)

print("the entered list is ", arr)

quicksort(arr, 0, n-1)
print("performed quicksort ")
print("the sorted list is ", arr)