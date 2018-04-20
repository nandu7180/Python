res = []

for i in range(1, 20):
    if i % 2 == 0:
        pass
    else:
        res.append(i)

print res

result = [i for i in range(1, 20) if not i % 2 == 0]
print result

combibnations = []

for i in [1, 2, 3]:
    for j in [3, 4, 1]:
        if i == j:
            combibnations.append((i, j))

print combibnations

comb = [(x, y) for x in [1, 2, 3] for y in [3, 4, 1] if x != y]
print comb

matrix1 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]

matrix = [[row[i] for row in matrix1] for i in range(4)]
print matrix
