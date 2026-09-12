items = [10, 20, 30, 40, 50, 60]
#         0   1   2   3   4   5    ← indexes

print(items[2:5])    # [30, 40, 50]  → start at index 2, stop BEFORE index 5
print(items[:3])      # [10, 20, 30]  → no start given = start from 0, stop before index 3
print(items[::2])      # [10, 30, 50]  → no start/stop given = whole list, but skip by 2 (every 2nd item)


print(items[1:4])# [20,30,40]
print(items[:2]) #[10, 20]
print(items[3:])
print(items[::3])