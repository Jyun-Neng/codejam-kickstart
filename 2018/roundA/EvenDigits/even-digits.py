def solve(N):
    size = 1
    tmp = N
    N_minus, N_plus = N, N
    plus, minus = 0, 0
    while tmp != 0:
        tmp //= 10
        size += 1
    if N % 2 == 1:
        N_plus += 1
        N_minus -= 1
        minus, plus = 1, 1
    for i in range(1, size):
        if (N_plus // (10 ** i)) % 2 == 1:
            num = 10 ** i - N_plus % (10 ** i)
            N_plus += num
            plus += num
        if (N_minus // (10 ** i)) % 2 == 1:
            num = N_minus % (10 ** i) + 2
            for j in range(1, i):
                num += (10 ** j)
            N_minus -= num
            minus += num
    return min(plus, minus)


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        N = int(input())
        print("Case #{}: {}".format(test, solve(N)))
