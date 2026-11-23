import statistics as s, math, datetime as d
def run(c):
    def last4(y,m):
        x=d.date(y+(m==12),(m%12)+1,1)-d.timedelta(days=1); out=[]
        while len(out)<3:
            if x.weekday()<5: out.append(x)
            x-=d.timedelta(days=1)
        return out
    exp={3:(31,27),4:(30,28),6:(30,26),8:(31,27),9:(30,28),10:(30,28),12:(31,29)}
    for m,(a,b) in exp.items():
        t=last4(2026,m); c('last%d'%m,t[0].day,a,0); c('third%d'%m,t[2].day,b,0)
        nb=sum(1 for i in range((t[0]-t[2]).days) if (t[2]+d.timedelta(days=i+1)).weekday()<5)
        c('gap%d'%m,nb,2,0)
    c('wd_sep28',d.date(2026,9,28).weekday(),0,0); c('wd_sep30',d.date(2026,9,30).weekday(),2,0); c('wd_dec29',d.date(2026,12,29).weekday(),1,0)
    # rééquilibrage
    w=[60*0.94,35*1.01,5*0.92]; T=sum(w)
    c('T',T,96.35,1e-9); c('wg',w[2]/T*100,4.77,0.005); c('wa',w[0]/T*100,58.54,0.005); c('wo',w[1]/T*100,36.69,0.005)
    c('buy',0.05*T-w[2],0.2175,1e-9); c('bn',0.2175/100*1000,2.175,1e-9); c('shr',2.175/430*100,0.51,0.005)
    w2=[60*1.04,35,5*1.20]; T2=sum(w2); c('T2',T2,103.4,1e-9); c('wg2',w2[2]/T2*100,5.80,0.005); c('sell',w2[2]-0.05*T2,0.83,0.005)
    c('b500',0.83/100*500,4.15,1e-9); c('s500',4.15/430*100,0.97,0.005)
    # échantillons
    ME=[0.4,-0.2,0.9,0.1,-0.3,0.6,0.2,1.1,-0.5,0.3,0.7,-0.1]
    OR=[0.1,-0.3,0.2,0.0,-0.4,0.5,-0.1,0.3,-0.2,0.1,0.4,-0.5,0.2,-0.1,0.0,0.3,-0.3,0.1,-0.2,0.2]
    c('nme',len(ME),12,0); c('nor',len(OR),20,0)
    c('mme',s.mean(ME),0.267,0.0005); c('medme',s.median(ME),0.25,1e-9); c('sdme',s.stdev(ME),0.496,0.0005)
    c('mor',s.mean(OR),0.015,1e-9); c('medor',s.median(OR),0.05,1e-9); c('sdor',s.stdev(OR),0.274,0.0005)
    diff=s.mean(ME)-s.mean(OR); c('diff',diff,0.252,0.0005)
    se=math.sqrt(s.variance(ME)/12+s.variance(OR)/20); c('t',diff/se,1.62,0.005)
    q=[ME[2],ME[5],ME[8],ME[11]]; c('q',s.mean(q),0.225,1e-9); c('qmed',s.median(q),0.25,1e-9); c('qsd',s.stdev(q),0.6397,0.0005)
    cp=sorted(ME)[-4:]; c('cp',s.mean(cp),0.825,1e-9); c('cpx',s.mean(cp)/s.mean(ME),3.09,0.01)
    # open interest
    oi=[582664,577454,571291,541982,527641,526276]
    for i,(e,p) in enumerate([(-5210,-0.89),(-6163,-1.07),(-29309,-5.13),(-14341,-2.65),(-1365,-0.26)]):
        c('doi%d'%i,oi[i+1]-oi[i],e,0); c('poi%d'%i,(oi[i+1]/oi[i]-1)*100,p,0.005)
    c('oit',(oi[-1]/oi[0]-1)*100,-9.7,0.05)
    c('sim_gain',4092/4000-1,0.023,1e-9)
