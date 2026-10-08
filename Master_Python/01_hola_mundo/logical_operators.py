
i = 3
j = 3
k = 0.00127e-7
l = 3.1415e3
m = False

b1 = i == j and k < l and m == True
print(f'b1 = {b1}')

b2 = i == j or k < l
print(f'b2 = {b2}')

b3 = (i == j and k < l) or m == True
print(f'b3 = {b3}')

print(not (5 > 3))
print(not i == j)

b4 = i == j or k < l and m == True
print(f'b4 = {b4}')

b5 = True or (True and False)
print(f'b5 = {b5}')

b6 = (True or (False and False)) or False
print(f'b6 = {b6}')

b7 = ((True or False) and False) or False
print(f'b7 = {b7}')

b8 = True or (False and (False or False))
print(f'b8 = {b8}')