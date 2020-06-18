"""print the number that only shows up once"""

arr = [1, 1, 2, 2, 3, 3, 7, 7, 9, 6, 6, 4, 4,]

def single_number(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i - 1] or arr[i] == arr[i + 1]:
            pass
        else:
            return arr[i]

print(single_number(arr))