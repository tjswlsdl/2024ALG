from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapify(cards)

for _ in range(m) :
    x = heappop(cards)
    y = heappop(cards)

    heappush(cards, x + y)
    heappush(cards, x + y)

print(sum(cards))