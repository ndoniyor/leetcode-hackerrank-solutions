matrix = [[112, 42, 83, 119], [56, 125, 56, 49],[15, 78, 101, 43], [62, 98, 114, 108]]
x = len(matrix) - 1
for i in range (len(matrix)//2):
    if((matrix[i][i]+matrix[i][i+1])<(matrix[i][x-i]+matrix[i][x-i-1])):
        matrix[i].reverse()
print(matrix)