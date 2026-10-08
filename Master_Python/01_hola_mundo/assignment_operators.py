
i = 5
j = i + 4

print(f'i = {i + j}')

i += 2 # i = i + 2
print(f'i = {i}')

i += 5 # i = i + 5
print(f'i = {i}')

j -= 4 # j = j - 4
print(f'j = {j}')

j *= 3 # j = j * 3
print(f'j = {j}')

j /= 3 # j = j / 3
print(f'j = {j}')

sql_str = 'select * from users as u'
sql_str += ' where u.name=:name'
sql_str += ' and u.active=1'
print(f'sql_str = {sql_str}')