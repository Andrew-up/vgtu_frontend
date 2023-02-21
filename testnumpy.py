import numpy as np

a = np.array([[[197, 239]], [[191, 245]]])

print(a)
res = []
for i in a:
    for j in i:
        a, b = j
        res.append(a)
        res.append(b)

print(res)