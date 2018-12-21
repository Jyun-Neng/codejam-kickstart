def solve(N, Q, array):
    new_array = []
    for i in range(0, N):
        new_array.append(array[i])
        for j in range(i + 1, N):
            e = new_array[-1] + array[j]
            new_array.append(e)

    new_array.sort()

    for q in range(0, Q):
        sums = 0
        L, R = map(int, input().split())
        for i in range(L - 1, R):
            sums += new_array[i]
        print(sums)
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        N, Q = map(int, input().split())
        array = list(map(int, input().split()))
        print("Case #{}:".format(test))
        solve(N, Q, array)
