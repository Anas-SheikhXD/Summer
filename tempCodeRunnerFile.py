from collections import deque

customers = deque(['Ali ' , 'ahmed','Umar', 'Zain'])

while customers:
    current_customer = customers.popleft()
    print("Serving: ", current_customer)