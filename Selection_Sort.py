arr = [5, 4, 3, 1, 6, 8, 7, 10, 9, 2]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print arr

if __name__ == '__main__':
    from Basic import output

    print output
