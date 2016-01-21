# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

list=[]
list.append([75])
list.append([95,64])
list.append([17,47,82])
list.append([18,35,87,10])
list.append([20,4,82,47,65])
list.append([19,1,23,75,3,34])
list.append([88,2,77,73,7,63,67])
list.append([99,65,4,28,6,16,70,92])
list.append([41,41,26,56,83,40,80,70,33])
list.append([41,48,72,33,47,32,37,16,94,29])
list.append([53,71,44,65,25,43,91,52,97,51,14])
list.append([70,11,33,28,77,73,17,78,39,68,17,57])
list.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
list.append([63,66,4,68,89,53,67,30,73,16,69,87,40,31])
list.append([4,62,98,27,23,9,70,98,73,93,38,53,60,4,23])

for x in range(len(list)-1,0,-1):
    for y in range(len(list[x])-1,0,-1):
        if list[x][y]>list[x][y-1]:
            list[x-1][y-1]=(list[x-1][y-1])+list[x][y]
        else:
            list[x-1][y-1]=list[x-1][y-1]+list[x][y-1]
            
print list[0]
print (edu.time()-ts0)