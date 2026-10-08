s = set()
s.add('uno')
s.add('dos')
s.add('tres')
s.add('cuatro')
s.add('cinco')

print(s)
b = 'tres' not in s
s.add('tres')
print(f'permite elementos duplicados? {b}')
print(s)

for n in s:
    print(n, end=' ')

print()
for element in sorted(s):
    print(element)

for i, element in enumerate(s):
    print(f'{i}: {element}')

list_ordered = sorted(s)
print(list_ordered)

print(list_ordered[1])

set_to_list = list(s)
print(set_to_list[0])
