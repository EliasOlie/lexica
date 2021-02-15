lista = ['amar', 'animo']
newlist = []

for i in lista:
    if i[-1] == 'r':
        i = f'{i}, verbo'
    else:
        i = f'{i}, substantivo'
    newlist.append(i)

print(newlist)