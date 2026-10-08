
from array import array

a = array('i', [1, 2, 3, 4, 5, 6])
print(a[0])
print(a[-1])
a.append(7)

print(a)
a.pop(2)
for value in a:
    print(value, end=' ')

s = array('w', ['a', 'b', 'c'])
print(s)