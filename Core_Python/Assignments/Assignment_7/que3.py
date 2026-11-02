# 1
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,6):
        if j == 1:
            print(1,end=" ")
        elif i == 5:
            print(j,end=" ")
        elif i == j:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()