def perevorot(m):
    for i in range(len(m)):
        for j in range(i, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for i in range(len(m)):
        m.reverse()
    return m
def main():
    n = int(input())
    m = []
    r = []
    delit = []
    spiral = []
    for i in range(n):
        r = input().split()
        for j in range(len(r)):
            r[j] = int(r[j])
        m.append(r)
    for i in range(4):
        for j in range(1,n):
            spiral.append(m[0][j])
        m = perevorot(m)
    k = spiral[-1]
    spiral.pop(-1)
    spiral = [k] + spiral

    print(spiral)
if __name__ == "__main__":
    main()