import heapq
from l47_heapq_showtree import show_tree
from l46_heapq_heapdata import data
print('random:', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
