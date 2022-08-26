arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
mainsum = 0
antisum = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i==j):
            mainsum += arr[i][j]
        if((i+j+1)==len(arr[0])):
            antisum += arr[i][j]
diff = abs(mainsum-antisum)
