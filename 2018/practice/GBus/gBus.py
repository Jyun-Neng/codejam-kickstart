def solve(gbus, cities):
    start = [cities[i*2] for i in range(0, gbus)]
    end = [cities[i*2+1] for i in range(0, gbus)]
    P = int(input())
    res = []
    for j in range(0, P):
        city = int(input())
        serves = 0
        for i in range(0, gbus):
            if city >= start[i] and city <= end[i]:
                serves += 1
        res.append(serves)        
    return res

if __name__ == '__main__':
    t = int(input()) 
    for test in range(1, t + 1):
        gbus = int(input())
        cities = list(map(int, input().split()))
        print("Case #{}: {}".format(test, ' '.join(map(str, solve(gbus, cities)))))
        input()    
