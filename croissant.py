x=[8,3,12.5,25.5,52,1]
y=[]
i=0
while i in range(5):
    if x[i]==min(x):
        y=y.append(x[i])
        x=x.remove(x[i])
    else:
        x=x
        y=y
    i=i+1
    print(y)
    
