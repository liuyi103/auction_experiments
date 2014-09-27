import numpy as np
import bisect as bi
m=10
mm=10
data=[sorted(np.random.uniform(size=mm),reverse=True) for i in range(m)]
#data=[[0.98253093336882713, 0.4701652427647186, 0.41437836542249018, 0.23499094360627093], [0.59344844333653934, 0.57270905343016709, 0.53730247567712441, 0.460399155602221]]
pre={0:-1,1:0}
opt={0:0,1:0}
band=np.r_[max([max(i)for i in data])+0.12:0:-0.01]
n=len(band)
tsum={}
pre={i:0 for i in range(n)}
def bib(a,x):
    s=list(a)
    s.reverse()
    return mm-bi.bisect(s,x)
for i in range(1,n):
    tsum[i]=sum([data[j][1]>=band[i] and band[i] or 0 for j in range(m)])
for i in range(2,n):
    for j in range(1,i):
        tmp=0
        for u in range(m):
            if bib(data[u], band[i])<=1:
                continue
            if bib(data[u],band[j])>=2:
                continue
            if bib(data[u],band[j])==0:
                tmp+=band[i]
                continue
            cnt=bib(data[u],band[i])-bib(data[u],band[j])
            tmp+=(cnt*band[j]+band[i])/(1.0+cnt)
        if i==30:
            print j,tmp+tsum[j]
        if tsum[i]<tsum[j]+tmp:
            tsum[i]=tsum[j]+tmp
            pre[i]=j
t=n-1
level=[]
while t:
    level+=[band[t]]
    t=pre[t]
level+=[band[0]]
data=[sorted(np.random.uniform(size=mm),reverse=True) for i in range(m)]
print 'secnd price',sum([data[i][1] for i in range(m)])
print 'discrete second price',sum([level[bi.bisect(level,data[i][1])-1] for i in range(m)])
ans=0
for i in range(m):
    x=bi.bisect(level,data[i][1])-1
    t1=bib(data[i],level[x])
    t2=bib(data[i],level[x+1])
    t=t1-t2
    ans+=(t*level[x+1]+level[x])/(t+1.0)
print 'final answer',ans
print 'level',level
    