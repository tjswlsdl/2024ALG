xlst = []
ylst = []
x = 0
y = 0
for _ in range(3):
    x, y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)
    
for i in range(3):
    if xlst.count(xlst[i]) ==1:
        x = xlst[i]
    if ylst.count(ylst[i]) ==1:
        y = ylst[i]
        
print(x,y)
    