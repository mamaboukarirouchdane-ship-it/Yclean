import statistics as s
def q(v,p):
    v=sorted(v); k=p*(len(v)-1); f=int(k); return v[f]+(k-f)*(v[min(f+1,len(v)-1)]-v[f])
def run(c):
    ref=[-18,-15,-12,-10,-8,-6,-5,-3,-2,0,1,2,4,5,7,8,10,12,15,20]
    c('q1',q(ref,.25),-6.5,1e-9); c('q3',q(ref,.75),7.25,1e-9); c('n',len(ref),20,0)
    dr=[12,8,-10,-6,15,-14,3,-9,11,-4,7,-12]; dd=[1.0,-0.4,-1.2,0.6,1.5,-0.9,0.2,-0.5,-0.8,0.3,1.1,-1.5]; R=[-2.1,-0.8,3.0,0.4,-3.2,2.2,0.5,1.1,-0.3,-0.2,-1.4,2.6]
    cl=lambda x,t: 1 if x>=t else (-1 if x<=-t else 0)
    reg=[]
    for a,b in zip(dr,dd):
        u,v=cl(a,5),cl(b,0.5); reg.append('A' if (u,v)==(1,1) else 'B' if (u,v)==(-1,-1) else 'C' if (u,v)==(1,-1) else 'D' if (u,v)==(-1,1) else 'M')
    g=lambda k:[x for x,y in zip(R,reg) if y==k]
    c('nA',len(g('A')),3,0); c('nB',len(g('B')),4,0); c('nC',len(g('C')),1,0); c('nD',len(g('D')),1,0); c('nM',len(g('M')),3,0)
    c('mA',s.mean(g('A')),-2.233,0.0005); c('mB',s.mean(g('B')),2.225,0.0005); c('medB',s.median(g('B')),2.4,1e-9); c('sdA',s.stdev(g('A')),0.907,0.0005); c('sdB',s.stdev(g('B')),0.818,0.0005)
    c('mM',s.mean(g('M')),-0.167,0.0005); c('medM',s.median(g('M')),-0.2,1e-9); c('sdM',s.stdev(g('M')),0.651,0.0005)
    c('opp',sum(1 for a,r in zip(dr,R) if a*r<0),10,0)
    mx=s.mean(dr); my=s.mean(R); sxy=sum((x-mx)*(y-my) for x,y in zip(dr,R)); sxx=sum((x-mx)**2 for x in dr); syy=sum((y-my)**2 for y in R)
    c('b',sxy/sxx,-0.164,0.0005); c('r2',sxy**2/(sxx*syy),0.815,0.0005)
    c('dr4',2.67-2.64,0.03,1e-9); c('dm',2.64-2.40,0.24,1e-9); c('vix',17.20-19.45,-2.25,1e-9); c('or',(4035.48/4137.94-1)*100,-2.48,0.005); c('sens',(4035.48/4137.94-1)*100/3,-0.83,0.005)
    c('j1',(4310.10/4290.52-1)*100,0.46,0.005); c('j2',(4035.48/4310.10-1)*100,-6.37,0.005); c('j3',(4035.48/4290.52-1)*100,-5.94,0.005)
    c('sA',-2.1-3.2-1.4,-6.7,1e-9)
