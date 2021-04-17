
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):  # last element in each iteration is in correct order so n-i-1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # sorting


n = int(input("enter list number :"))
arr = []
for i in range(0, n):
    a = int(input("enter value " + str(i) + ": "))
    arr.append(a)

print("the entered list is ", arr)

bubblesort(arr)
print("performed bubblesort ")
print("the sorted list is ", arr)
