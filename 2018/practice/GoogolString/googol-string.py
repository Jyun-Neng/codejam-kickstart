def solve(k):
    k_mod_8 = k % 8
    if (k_mod_8 == 0) or (k_mod_8 == 1) or (k_mod_8 == 4):
        return 0
    if (k_mod_8 == 2) or (k_mod_8 == 5) or (k_mod_8 == 6):
        return 1
    if k_mod_8 == 3:
        if (k // 8) % 2 == 0:
            return 0
        return 1
    if k_mod_8 == 7:
        k //= 8
        return solve(k)

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        k = int(input())
        print("Case #{}: {}".format(test, solve(k-1)))
