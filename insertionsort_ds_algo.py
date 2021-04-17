# insertion sort

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # selecting a key element
        j = i -1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # soring
            j -= 1
        arr[j+1] = key


n = int(input("enter list number :"))
arr = []
for i in range(0, n):
    a = int(input("enter value "+ str(i) + ": "))
    arr.append(a)

print("the entered list is ", arr)

insertionsort(arr)
print("performed insertionsort ")
print("the sorted list is ", arr)
