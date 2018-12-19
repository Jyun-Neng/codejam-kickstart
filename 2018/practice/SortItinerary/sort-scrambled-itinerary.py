def solve(tickets):
    itinerary = []
    order = []
    src = next(iter(tickets))
    while tickets: 
        dst = tickets[src]
        ticket = src + '-' + dst
        order.append(ticket)
        tickets.pop(src)    
        src = dst    
        if tickets.get(src) is None:
            if tickets:
                src = next(iter(tickets))
            itinerary = order + itinerary    
            order.clear()
    return itinerary 

t = int(input())
for test in range(1, t + 1):
    n = int(input())    
    tickets = {}
    for i in range(n):
        src = input()
        dst = input()
        tickets[src] = dst
    print("Case #{}: {}".format(test, ' '.join(solve(tickets))))
