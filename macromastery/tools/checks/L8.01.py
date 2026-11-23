import datetime as d
def run(c):
    c('p_a',0.05*40,2.0,1e-9); c('p_b',0.40*5,2.0,1e-9); c('p_c',0.08*25,2.0,1e-9); c('p_d',0.20*10,2.0,1e-9)
    c('base_fev22',1910/1.06,1802,0.5); c('base_fev22_lo',1910/1.065,1793,0.5); c('base_fev22_hi',1910/1.055,1810,0.5)
    c('base_oct23',1997/1.068,1870,0.5)
    c('dir_delai',(d.date(2023,5,19)-d.date(2022,2,24)).days,449,0)
    c('wgc_fev_pub',(d.date(2022,3,7)-d.date(2022,2,28)).days,7,0)
    c('wgc_oct_pub',(d.date(2023,11,7)-d.date(2023,10,31)).days,7,0)
    c('brent_ecart',100-75,25,0); c('brent_h2',85-78,7,0)
    c('ecart_etf_t',38-37,1,0)
    c('comex_net',87+84,171,0)
