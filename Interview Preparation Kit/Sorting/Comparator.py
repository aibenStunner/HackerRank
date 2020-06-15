from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "{} {}".format(self.name, self.score)
        
    def comparator(a, b):
        if a.score == b.score and a.name == b.name:
            return 0
        if a.score == b.score:
            return 1 if a.name > b.name else -1
        return -1 if a.score > b.score else 1

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)



"""BASIC QUICKSORT"""
# def quicksort(arr):
#     sort(arr, 0, len(arr)-1)
#     return arr

# def sort(arr, left, right):
#     if left >= right:
#        return
#     pivot = arr[(left+right)//2]
#     index = partition(arr, left, right,  pivot)
#     sort(arr, left, index-1)
#     sort(arr, index, right)

# def partition(arr, left, right, pivot):
#     while left <= right:
#         while arr[left] < pivot:
#             left += 1
#         while arr[right] > pivot:
#             right -= 1
#         if left <= right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1 
#     return left


