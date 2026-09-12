a = [1, 2, 3]
b = a              # ALIAS — same list, two names
c = a.copy()       # COPY — independent list

b.append(99)
print(a)   # [1, 2, 3, 99]  ← changed, because b IS a
print(c)   # [1, 2, 3]       ← unaffected, c is a separate list