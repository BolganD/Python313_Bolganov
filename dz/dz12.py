d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
d1 = {'name': d['name'], 'salary': d['salary']}

del d['name'], d['salary']

print(d)
print(d1)
