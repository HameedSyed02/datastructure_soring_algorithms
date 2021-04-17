# read the data step-1
# select min  the data (temp) step-2
# sorting according to the min step-3

def selection_sort(arr, n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]: min = j
        arr[i], arr[min] = arr[min], arr[i]


# read the data step-1
n = int(input("enter list number :"))
arr = []
for i in range(0, n):
    a = int(input("enter value "+ str(i) + ": "))
    arr.append(a)

# output
print("the entered list is ", arr)
selection_sort(arr, n)
print("performed selection sort ")
print("the sorted list is ", arr)
