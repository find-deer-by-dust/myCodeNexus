import numpy as np

tab = [[78, 521, 602, 2863],
       [144, -600, -521, 2245],
       [95, -457, 468, -1283],
       [69, 596, 695, 1054],
       [190, 527, 691, 2051],
       [101, 403, 470, 2487],
       [146, 413, 435, 2571], ]

for i in range(len(tab[0])):
    minNum = tab[0][i]
    maxNum = tab[0][i]
    for j in range(len(tab)):
        if tab[j][i] > maxNum:
            maxNum = tab[j][i]
        if tab[j][i] < minNum:
            minNum = tab[j][i]
    for j in range(len(tab)):
        tab[j][i] = (tab[j][i] - minNum) / (maxNum - minNum) * (1 - 0) + 0

print(np.round(tab, 2))
