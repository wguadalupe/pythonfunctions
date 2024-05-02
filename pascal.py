def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(' '.join(map(str, row)).center(2*n))

print("Pascal's Triangle for 5 rows:")
pascal(5)
