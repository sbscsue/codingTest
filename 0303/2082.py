import sys
from turtle import ondrag 


#숫자 세팅
s0 = "###  ..#  ###  ###  #.#  ###  ###  ###  ###  ###1#.#  ..#  ..#  ..#  #.#  #..  #..  ..#  #.#  #.#1#.#  ..#  ###  ###  ###  ###  ###  ..#  ###  ###1#.#  ..#  #..  ..#  ..#  ..#  #.#  ..#  #.#  ..#1###  ..#  ###  ###  ..#  ###  ###  ..#  ###  ### "
s1 = s0.split("1")



def oneDimensionNum(n,s1):
    num = []
    [num.append([]) for _ in range(n)]


    for row in s1:
        s2 = row.split(" ")
        for i in s2:
            if i == "":
                s2.remove("")

        for i in range(len(s2)):
            num[i].append(list(s2[i]))
    return num

nums = oneDimensionNum(10,s1)




#입력 숫자 
data  =[] 
[data.append(sys.stdin.readline().rstrip()) for _ in range(5)]


data = oneDimensionNum(4,data)





result = []

for d in data:
    print(d)
    index = 0
    flag = -1
    while (flag == -1):
        for j in range(5):
            for x in range(3):
                if(d[j][x]=="#"):
                    if(nums[index][j][x]=="."):
                        
                        
    result.append(index)

print(result)