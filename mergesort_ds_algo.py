# step-1 reading the data
# step-2 splitting the data
# step-3 merging the data

def merge_sort(arr):
    # step-2 splitting the data
    if len(arr) > 1:
        # half splitting
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # step 3 merge the data
        i, j, k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# step-1 read the data
n = int(input("enter list number :"))
arr = []
for i in range(0, n):
    a = int(input("enter value "+ str(i) + ": "))
    arr.append(a)

print("the entered list is ", arr)

merge_sort(arr)
print("performed mergesort ")
print("the sorted list is ", arr)
