import matplotlib.pyplot as plt
import numpy as np

port = []
x=[]
ind=0
with open("port.log") as f:
    lines = f.readlines()
    for l in lines:
        c = ""
        a = l.split(' ')
        if len(a) > 2:
            b = a[2].split('.')
            if len(b) > 4:
                c = b[4]
                #print(c)
                x.append(ind)
                ind+=1
                port.append(int(c))

print(port)

""" n = int(lines[0])
    x = []
    y = []
    for i in range(n):
        line = lines[i+1].split(" ")
        x.append(int(line[0]))
        y.append(int(line[1]))
"""

#                   记号形状       颜色           点的大小    设置标签
plt.scatter(x, port, marker = '.',color = 'red', s = 40 ,label = 'First')
plt.legend(loc = 'best')    # 设置 图例所在的位置 使用推荐位置
plt.show()