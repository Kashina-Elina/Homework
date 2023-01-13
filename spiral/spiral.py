def perevorot(m, n):
    matrix = []
    matrix1 = []
    for i in range(n):
        matrix1.append([])
        for j in range(n):
            matrix.append(m[j][n - i - 1])
    for i in range(n):
        for j in range(n):
            matrix1[i].append(matrix[i * n + j])
    return matrix1


def main():
    n = int(input())
    first_matrix = []
    list2 = []
    list1 = []
    new_matrix = []
    spiral = []
    new_spiral = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        first_matrix.append(row)
    while n > 0:
        for i in range(4):
            for j in range(1, n):
                spiral.append(first_matrix[0][j])
            first_matrix = perevorot(first_matrix, n)
        k = spiral[-1]
        spiral.pop(-1)
        spiral = [k] + spiral
        new_spiral += spiral
        spiral = []
        for i in first_matrix:
            list2 += i
        list2 = list2[n + 1:-(n + 1)]
        if len(list2) == 1:
            new_spiral.append(list2[0])
            break
        for i in range(n - 2):
            for j in range(n - 2):
                list1.append(list2[0])
                list2 = list2[1:]
            new_matrix.append(list1)
            list1 = []
            list2 = list2[2:]
        n -= 2
        first_matrix = new_matrix
        new_matrix = []
    print(*new_spiral)


if __name__ == "__main__":
    main()
