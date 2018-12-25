def solve(N, K, vals):
    E = sum(vals[0:N]) / N
    while K:
        left, right = 0, N - 1
        last_E = E
        E = 0
        while left <= right:
            mid = (left + right) // 2
            if vals[mid] <= last_E:
                left = mid + 1
            else:
                right = mid - 1
        if left == N:
            return last_E  # all of values are the same
        E = (last_E * left + sum(vals[left:N])) / N
        K -= 1
    return E


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        N, K = map(int, input().split())
        vals = list(map(int, input().split()))
        vals.sort()
        print("Case #{}: {}".format(test, solve(N, K, vals)))
