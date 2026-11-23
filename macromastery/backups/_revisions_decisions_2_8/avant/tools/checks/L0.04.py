def run(c):
    # §4.4 / Ex1
    c('spread petit', round(1.0802-1.0800, 4)/0.0001, 2); c('spread grand', round(1.0803-1.0799, 4)/0.0001, 4)
    c('coût 1 lot', 2*10*1, 20); c('coût 50M', 4*10*(50_000_000/100_000), 20000); c('par M petit', 20/0.1, 200); c('par M grand 50M', 20000/50, 400)
    c('Ex1 20M lots', 20_000_000/100_000, 200); c('Ex1 coût 20M', 4*10*200, 8000); c('Ex1 par M', 8000/20, 400)
    # pip
    c('pip EURUSD', 0.0001*100000, 10); c('pip USDCHF CHF', 0.0001*100000, 10); c('pip USDCHF USD', 10/0.9, 11.11); c('pip USDJPY JPY', 0.01*100000, 1000)
    c('pip USDJPY 150', 1000/150, 6.67); c('pip USDJPY 160', 1000/160, 6.25)
    # Ex B, C, D
    c('B risque', 10000*0.01, 100); c('B lots', 100/(25*10), 0.4); c('B perte', 25*0.4*10, 100)
    c('C notionnel', 40000*1.0802, 43208); c('C marge', 43208*0.02, 864.16); c('C levier', 43208/864.16, 50); c('C levier effectif', 43208/10000, 4.3208, 0.0001)
    c('D lots', 100/(60*(1000/150)), 0.25)
    # Ex3
    c('Ex3 risque', 5000*0.02, 100); c('Ex3 lots EURUSD', 100/(40*10), 0.25); c('Ex3 lots USDJPY', 100/(60*1000/150), 0.25)
    c('Ex3 perte EURUSD', 40*0.25*10, 100); c('Ex3 perte USDJPY', 60*0.25*1000/150, 100)
    # Ex4
    c('Ex4 notionnel', 25000*1.0802, 27005); c('Ex4 marge 2', 27005*0.02, 540.10); c('Ex4 marge 5', 27005*0.05, 1350.25)
    c('Ex4 levier 2', 1/0.02, 50); c('Ex4 levier 5', 1/0.05, 20); c('Ex4 effectif', 27005/5000, 5.401); c('Ex4 risque', 25000*0.0040, 100)
    # CME et BRI
    c('CME tick', 125000*0.00005, 6.25)
    c('BRI parts centres', 37.77+18.59+11.83+7.03, 75.22, 0.01)
    # Ex5 sessions (UTC)
    c('hiver chevauch début', 13, 13); c('hiver durée', 17-13, 4); c('hiver Bénin début', 13+1, 14); c('hiver Bénin fin', 17+1, 18)
    c('été chevauch début', 12, 12); c('été Londres UTC', 8-1, 7); c('été NY UTC', 8+4, 12); c('été fin Londres', 17-1, 16); c('été Bénin', 12+1, 13)
    c('hiver NY UTC', 8+5, 13); c('hiver NY fin UTC', 17+5, 22)
    # Ex6
    c('Ex6 coût/lot', 1*10, 10); c('Ex6 total', 50*10, 500); c('Ex6 moyenne', 500/100, 5)
    # quiz
    c('Q4', 10/0.9, 11.11); c('Q5 risque', 10000*0.02, 200); c('Q5 lots', 200/(50*10), 0.4); c('Q6 notionnel', 50000*1.08, 54000); c('Q6 marge', 54000*0.02, 1080); c('Q6 levier', 54000/1080, 50)
