import numpy as np

tab = [[78, 521, 602, 2863],
       [144, -600, -521, 2245],
       [95, -457, 468, -1283],
       [69, 596, 695, 1054],
       [190, 527, 691, 2051],
       [101, 403, 470, 2487],
       [146, 413, 435, 2571], ]

for i in range(len(tab[0])):
    max = tab[0][i]
    max = 1.0
    for j in range(len(tab)):
        if (tab[j][i] > max):
            max = tab[j][i]
    print(max)
    tmp = 0
    while (max > 0):
        tmp = tmp+1
        max = max/10.0
    print(tmp)
    for j in range(len(tab)):
        tab[j][i] = tab[j][i]/(10**tmp)


print(np.round(tab, 4))
