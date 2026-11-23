import statistics as s
def run(c):
    x=[-1.40,-0.94,1.30,0.38,-0.60]
    c('r1',(4012/4000-1)*100,0.30,0.001); c('r2',(3996/4000-1)*100,-0.10,0.001); c('r3',(4040/4000-1)*100,1.00,0.001)
    c('mean',s.mean(x),-0.252,1e-9); c('med',s.median(x),-0.60,1e-9); c('sd',s.stdev(x),1.086,0.0005); c('rng',max(x)-min(x),2.70,1e-9)
    c('abs',s.mean([abs(v) for v in x]),0.924,1e-9)
    conf=[-1.40,-0.94,0.38,-0.60]; c('conf',s.mean(conf),-0.64,1e-9); c('ecart',1.30-s.mean(conf),1.94,1e-9)
    d=[abs(v-s.mean(x[:i]+x[i+1:])) for i,v in enumerate(x)]; c('maxj',d.index(max(d)),2,0); c('p',sum(1 for v in d if v>=d[2]-1e-12)/5,0.20,1e-9)
    c('sA',-0.6/5,-0.12,1e-9); c('sB',0.2/-2,-0.10,1e-9); c('rap',(-0.6/5)/(0.2/-2),1.2,1e-9)
    c('impl',4310.10/1.0038,4293.8,0.05); c('e',0.38*25,9.5,1e-9); c('oct',0.094*25,2.35,1e-9); c('n',len(x),5,0)
