import datetime as d
def run(c):
    D=d.date
    c('j_168',(D(1991,1,17)-D(1990,8,2)).days,168,0)
    for k,x in enumerate((D(2022,3,3),D(2022,3,26),D(2022,5,25))): c(f'h22_{k}',(D(2022,2,24)+d.timedelta((7,30,90)[k])-x).days,0,0)
    for k,x in enumerate((D(2001,9,18),D(2001,10,11),D(2001,12,10))): c(f'h01_{k}',(D(2001,9,11)+d.timedelta((7,30,90)[k])-x).days,0,0)
    for k,x in enumerate((D(1990,8,9),D(1990,9,1),D(1990,10,31))): c(f'h90_{k}',(D(1990,8,2)+d.timedelta((7,30,90)[k])-x).days,0,0)
    c('p40_22',40/22-1,0.8182,0.0001); c('p28_22',28/22-1,0.2727,0.0001); c('p20_40',20/40-1,-0.5,1e-9)
    c('w28_21',28/21-1,0.3333,0.0001); c('w46_21',46/21-1,1.1905,0.0001)
    c('or9091',362/383-1,-0.0548,0.0001)
    c('dec',275.30/278.60-1,-0.01184,0.00001)
    c('j_6311',(D(2001,11,13)-D(2001,9,11)).days,63,0); c('j_6611',(D(2001,11,16)-D(2001,9,11)).days,66,0)
    c('or_a',2069/1910-1,0.0832,0.0001); c('or_b',1942/2069-1,-0.0614,0.0001); c('or_c',1672/1942-1,-0.1390,0.0001); c('or_d',1672/2069-1,-0.1919,0.0001)
    c('j_28',(D(2022,2,28)-D(2022,2,24)).days,4,0); c('j_08',(D(2022,3,8)-D(2022,2,24)).days,12,0); c('j_31',(D(2022,3,31)-D(2022,2,24)).days,35,0); c('j_30s',(D(2022,9,30)-D(2022,2,24)).days,218,0)
    c('achats',1135.7/450.1-1,1.5232,0.0001)
    c('sim_a',104/100-1,0.04,1e-9); c('sim_b',112/100-1,0.12,1e-9); c('sim_j',(D(2022,6,10)-D(2022,3,10)).days,92,0)
    # Règle de couverture avec tolérance (décision 6, 23/11/2026) : 2 = couvert, 1 = partiel, 0 = non couvert.
    # h = 0 désigne la réaction immédiate (jours 0 à 4). Fenêtre partielle : ± floor(0,2 × h) jours.
    def cls(h, jour):
        if h == 0: return 2 if 0 <= jour <= 4 else 0
        if jour == h: return 2
        return 1 if abs(jour - h) <= int(0.2 * h) else 0
    cas = [  # (horizon, jour lu, classement écrit dans le module, où)
        (0, 1, 2, 'L8.06 6.6 et EX8-A4'), (0, 4, 2, 'frise 8.3, 2022'),
        (7, 14, 0, 'L8.06 6.6'), (7, 12, 0, 'L8.06 ex. 1, quiz Q2, C8.3-Q4, EX8-A4'), (7, 15, 0, 'synthèse 8.3'),
        (30, 12, 0, 'L8.06 ex. 1'), (30, 35, 1, 'frise 8.3 et EX8-A4'),
        (90, 92, 1, 'L8.06 6.6'), (90, 94, 1, 'synthèse 8.3'), (90, 66, 0, 'C8.3-Q2 et EX8-A4'), (90, 63, 0, 'frise 8.3, 2001')]
    for h, j, att, ou in cas: c(f'couverture h{h} jour {j} ({ou})', cls(h, j), att, 0)
    c('fenêtres ± 1, ± 6, ± 18 jours', [int(0.2 * h) for h in (7, 30, 90)] == [1, 6, 18], True, 0)
