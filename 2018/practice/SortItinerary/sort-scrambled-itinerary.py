def solve(n, tickets):
    itinerary = []
    while tickets: 
        src = next(iter(tickets))
        order = []
        while n != 0:
            dst = tickets[src]
            ticket = src + '-' + dst
            order.append(ticket)
            tickets.pop(src)    
            n -= 1    
            src = dst    
            if tickets.get(src) is None:
                break
        itinerary = order + itinerary    
    return itinerary 

t = int(input())
for test in range(1, t + 1):
    n = int(input())    
    tickets = {}
    for i in range(n):
        src = input()
        dst = input()
        tickets[src] = dst
    print("Case #{}: {}".format(test, ' '.join(solve(n, tickets))))
