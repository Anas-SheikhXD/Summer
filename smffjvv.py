fruits = ["apple", "banana"]

fruits.append("cherry")        # add to end → ["apple", "banana", "cherry"]
fruits.insert(1, "mango")       # insert at position 1 → ["apple", "mango", "banana", "cherry"]
fruits.remove("banana")         # removes by VALUE → ["apple", "mango", "cherry"]
popped = fruits.pop()            # removes LAST item, returns it → "cherry"
print(len(fruits))                # length → 2
print("mango" in fruits)          # membership check → True
fruits.sort()                       # sorts alphabetically in place
print(fruits)