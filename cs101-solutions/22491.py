h=int(input())
m=int(input())
time=2*h-0.5*m
sc=[]
for i in range(0,m):
    sc.append(list(map(float,input().split())))
sc.sort(key=lambda x:x[0]*x[1],reverse=True)
i=0
sc_sum=0
while time>0 and i<m:
    time-=5/sc[i][0]
    sc_sum+=5*sc[i][1]
    i+=1
if time<0:
    sc_sum+=time*sc[i-1][0]*sc[i-1][1]
print("%.1f"%sc_sum)