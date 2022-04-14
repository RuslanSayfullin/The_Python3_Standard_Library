import heapq
from l47_heapq_showtree import show_tree
from l46_heapq_heapdata import data
heap = []
print('random :', data)
print()
for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)