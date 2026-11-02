# A
# A B
# A B C
# A B C D
# A B C D E

for i in range(1,6):
    #num = 65
    for j in range(i):
        print(chr(65+j),end=' ')
        #num += 1
    print()