arr = [1,2,3,4,5,6,7,8]
if(len(arr)%2 == 1):
    median = arr[int(len(arr)/2)]
else:
    median = (arr[int(len(arr)/2)-1] + arr[int((len(arr)/2))])/2
print(median)