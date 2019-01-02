def solve(num):
    X = num
    x = [num % 10]
    num //= 10
    legal = 0
    while num != 0:
        x.append(num % 10)
        num //= 10
   
    for i, digit in enumerate(x):
        if i >= 1 and digit != 9:
            legal += digit * 8 * (9 ** (i - 1))
   
    if 9 in x[1:]:
        return legal

    for n in range(X - x[0], X + 1):
        if n % 9 != 0 and n % 10 != 9:
            legal += 1
    return legal         

t = int(input())
for test in range(1, t + 1):
    F, L = map(int, input().split())
    print("Case #{}: {}".format(test, solve(L) - solve(F - 1)))
