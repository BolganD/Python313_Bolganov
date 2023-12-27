month = ['January', 'February', 'March']
total = [52000.00, 51000.00, 48000.00]
pc = [46800.00, 45900.00, 43200.00]
for m, n1, n2 in zip(month, total, pc):
    print('Чистая прибыль в', m, '=', n1 - n2)
