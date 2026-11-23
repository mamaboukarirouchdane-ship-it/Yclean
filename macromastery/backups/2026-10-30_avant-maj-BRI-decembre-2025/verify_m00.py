from decimal import Decimal as D, getcontext
import json, re, glob, os, sys
getcontext().prec=28
def r(x,n=2): return round(x,n)
ok=True
def chk(label, got, exp, tol=0.005):
    global ok
    good = abs(float(got)-float(exp))<=tol
    ok &= good
    print(("OK  " if good else "FAIL"), label, float(got), "attendu", exp)

print("== L0.01 ==")
chk("A primaire 100000*20", 100000*20, 2_000_000)
chk("A secondaire 1000*22", 1000*22, 22000)
chk("B spread", 100.10-99.90, 0.20)
chk("B mid", (99.90+100.10)/2, 100.00)
chk("B achat 500*100.10", 500*100.10, 50050)
chk("B revente 500*99.90", 500*99.90, 49950)
chk("B perte", 500*100.10-500*99.90, 100)
chk("B pct", 100/50050*100, 0.20, 0.01)
chk("C reçus", 1000*0.06, 60); chk("C versés",1000*0.02,20); chk("C marge",60-20,40); chk("C perte 5%",1000*0.05,50); chk("C résultat",40-50,-10)
chk("Ex1a 50000*40", 50000*40, 2_000_000); chk("Ex1b 1000*45",1000*45,45000)
chk("Ex2 achat 400*25.05", 400*25.05, 10020); chk("Ex2 revente 400*24.95",400*24.95,9980); chk("Ex2 perte",10020-9980,40)
chk("Ex2 pct perte/achat",40/10020*100,0.40,0.01); chk("Ex2 spread/mid",0.10/25.00*100,0.40,0.001)
chk("Ex3 reste",100-49-35,16)
chk("Ex4 A",10000*0.0005,5); chk("Ex4 B",10000*0.02,200); chk("Ex4 ratio",200/5,40)
chk("Ex5 reçus",2000*0.07,140); chk("Ex5 versés",2000*0.02,40); chk("Ex5 marge",100,100); chk("Ex5 seuil",100/2000*100,5)
chk("Q5 perte 100*(50.10-49.90)",100*50.10-100*49.90,20); chk("Q4 mid",(49.90+50.10)/2,50.00)


print("== L0.01 révision 2 ==")
chk("Rév2 Ex1e 20000*50",20000*50,1_000_000)
chk("Rév2 BCE prêts %",16813/34395*100,48.9,0.05)
chk("Rév2 BCE titres+cotées",8430+3747,12177); chk("Rév2 BCE titres %",12177/34395*100,35.4,0.05)
chk("Rév2 BCE reste (dép+pens+autres)",256+349+4801,5406); chk("Rév2 BCE reste %",5406/34395*100,15.7,0.05)
chk("Rév2 BCE somme lignes - total",16813+8430+3747+256+349+4801-34395,1)
chk("Rév2 BCE MFI+autres = prêts",11006+5807,16813)
chk("Rév2 Ex D 1000*100.10",1000*100.10,100100); chk("Rév2 Ex D 2000*100.20",2000*100.20,200400); chk("Rév2 Ex D 2000*100.35",2000*100.35,200700)
chk("Rév2 Ex D total",100100+200400+200700,501200); chk("Rév2 Ex D prix moyen",501200/5000,100.24); chk("Rév2 Ex D surcoût",501200-5000*100.10,700)
chk("Rév2 Ex6 500*50",500*50.00,25000); chk("Rév2 Ex6 1000*50.10",1000*50.10,50100); chk("Rév2 Ex6 500*50.30",500*50.30,25150)
chk("Rév2 Ex6 total",25000+50100+25150,100250); chk("Rév2 Ex6 moyen",100250/2000,50.125,0.0001)
chk("Rév2 Ex6 surcoût",100250-2000*50.00,250); chk("Rév2 Ex6 %",250/100000*100,0.25,0.0001)
import math
chk("Rév2 seuil quiz L0.01 (7/8)",math.ceil(0.8*8),7)

print("== L0.02 ==")
chk("A 2M/1.08", 2_000_000/1.08, 1851851.85)
chk("A 2M/1.12", 2_000_000/1.12, 1785714.29)
chk("A perte", 2_000_000/1.08-2_000_000/1.12, 66137.57)
chk("A 2M/1.04", 2_000_000/1.04, 1923076.92)
chk("A gain", 2_000_000/1.04-2_000_000/1.08, 71225.07)
chk("A forward 2M/1.082", 2_000_000/1.082, 1848428.84)
chk("B achat", 1_000_000*1.08, 1_080_000); chk("B gain",1_000_000*1.09-1_000_000*1.08,10000); chk("B perte",1_000_000*1.08-1_000_000*1.07,10000)
chk("B pct", 10000/1_080_000*100, 0.93, 0.01)
chk("C client", 1_000_000*1.0802, 1_080_200); chk("C rachat",1_000_000*1.0798,1_079_800); chk("C revenu",1_000_000*(1.0802-1.0798),400)
chk("Ex2a 500k/1.08",500_000/1.08,462962.96); chk("Ex2b 500k/1.04",500_000/1.04,480769.23); chk("Ex2b extra",500_000/1.04-500_000/1.08,17806.27)
chk("Ex2c 500k/1.12",500_000/1.12,446428.57); chk("Ex2c éco",500_000/1.08-500_000/1.12,16534.39)
chk("BIS somme parts",46+50+5,101); chk("BIS 4.4+4.8",4.4+4.8,9.2); chk("BIS reste 0.4/9.6 %",0.4/9.6*100,4.17,0.01); chk("BIS écart 9,6-9,2",9.6-9.2,0.4,0.001); chk("BIS 5 % de 9,6",0.05*9.6,0.48,0.001); chk("COT jours mardi->vendredi (ven=5, mar=2)",5-2,3)
chk("Q3 300000/1.2",300_000/1.2,250000)

print("== L0.03 ==")
chk("A spread pips",(1.0802-1.0798)/0.0001,4); chk("A achat",100000*1.0802,108020); chk("A revente",100000*1.0798,107980); chk("A perte",108020-107980,40)
chk("B pips",(1.0850-1.0800)/0.0001,50); chk("B gain",200000*0.0050,1000); chk("B pip val",200000*0.0001,20)
chk("C pips",(149.20-150.00)/0.01,-80); chk("C yen",100000*(149.20-150.00),-80000); chk("C usd",80000/149.20,536.19)
chk("D EURJPY",1.08*150,162.0); chk("D EURGBP",1.08/1.26,0.857143,0.000001); chk("D EURGBP2",1.08/1.30,0.830769,0.000001)
chk("E croissance",9.6/7.5-1,0.28,0.0001); chk("E swaps 42%",0.42*9.6,4.03,0.01); chk("E spot 31%",0.31*9.6,2.976,0.001)
chk("E instruments somme",42+31+19+7+2,101); chk("E places",38+19+11.8+7.0,75.8)
chk("Ex1b 50000*1.26",50000*1.26,63000); chk("Ex1c",50000*1.27,63500); chk("Ex1c pct",500/63000*100,0.79,0.01)
chk("Ex2 spread pips",(0.6503-0.6500)/0.0001,3); chk("Ex2 coût",100000*0.0003,30); chk("Ex2 direct",100000*0.6503-100000*0.6500,30)
chk("Ex3 pips",(151-150)/0.01,100); chk("Ex3 yen",100000*1,100000); chk("Ex3 usd",100000/151,662.25)
chk("Ex6 pct",2040/2000-1,0.02,0.0001)
chk("Q3 pips 150.50",(150.50-150.00)/0.01,50); chk("Q4 EURJPY",1.08*150,162)
named=89.2+28.9+16.8+10.2+8.5+6.4+6+6+3.8+2
print("info: devises nommées somme =",round(named,1),"; reste jusqu'à 200 =",round(200-named,1))

print("== Quiz JSON ==")
base="./content/m00/quiz/"
for f in sorted(glob.glob(base+"*.json")):
    d=json.load(open(f,encoding="utf-8"))
    qs=d["questions"]
    ids=set()
    for q in qs:
        o={x["id"] for x in q["options"]}
        good = q["correct"] in o and q["id"] not in ids and len(o)==len(q["options"]) and q["explanation"].strip()
        ids.add(q["id"]); ok &= bool(good)
        if not good: print("FAIL", f, q["id"])
    from collections import Counter
    print(os.path.basename(f), len(qs),"questions", Counter(q["correct"] for q in qs))

print("== Cohérence quiz / leçon / seuils ==")
for f in sorted(glob.glob(base+"*.json")):
    d=json.load(open(f,encoding="utf-8")); n=len(d["questions"]); need_ok=math.ceil(d["passThreshold"]*n-1e-9)
    lesson=open("./content/m00/"+d["lessonId"]+".mdx",encoding="utf-8").read()
    m=re.search(r"au moins (\d+) bonnes réponses sur (\d+)",lesson)
    good = bool(m) and int(m.group(1))==need_ok and int(m.group(2))==n
    ok &= good
    print("OK  " if good else "FAIL", d["lessonId"], "seuil", d["passThreshold"], "x", n, "=> min", need_ok, "| leçon:", m.groups() if m else None)
dq=json.load(open(base+"L0.02.quiz.json",encoding="utf-8"))
chk("L0.02 nombre de questions",len(dq["questions"]),10)
chk("L0.02 seuil 8/10",math.ceil(dq["passThreshold"]*10-1e-9),8)
defined_ids=set(re.findall(r"\| (S-[A-Z]+-\d+) \|",open("./content/sources.md",encoding="utf-8").read()))
bad=[]
for q in dq["questions"]:
    for k in ("skill","difficulty","sources","lessonRefs"):
        if k not in q: bad.append((q["id"],"champ manquant",k))
    for sid in q.get("sources",[]):
        if sid not in defined_ids: bad.append((q["id"],"source non définie",sid))
q6=[q for q in dq["questions"] if q["id"]=="L0.02-Q6"][0]
if not (q6.get("volatile") is True and q6.get("review_when")): bad.append(("Q6","marque volatile/review_when manquante"))
if "calendrier traditionnel" not in q6["prompt"]: bad.append(("Q6","calendrier traditionnel non nommé"))
q4=[q for q in dq["questions"] if q["id"]=="L0.02-Q4"][0]
if any(re.search(r"\d",o["text"]) for o in q4["options"]): bad.append(("Q4","chiffre dans une option"))
print("Contrôles de forme L0.02 :", "OK" if not bad else bad); ok &= not bad
longest=[]
for q in dq["questions"]:
    L={o["id"]:len(o["text"]) for o in q["options"]}
    if q["id"] in ("L0.02-Q%d"%i for i in range(4,11)):
        longest.append(max(L,key=L.get)==q["correct"] and sorted(L.values())[-1]>sorted(L.values())[-2])
print("Q4-Q10 : bonne réponse strictement la plus longue dans",sum(longest),"questions sur 7 (info)")
chk("L0.02 bonne réponse la plus longue (max toléré 2 sur 7)",min(sum(longest),2),sum(longest),0)

print("== Structure MDX ==")
need=["Objectifs d'apprentissage","Prérequis","Explication intuitive","Développement technique","Définitions essentielles","Exemples chiffrés","Application au Forex","Erreurs courantes","Limites de l'interprétation","Exercices pratiques","Quiz","Résumé","Critères de maîtrise","Sources et références"]
src=open("./content/sources.md",encoding="utf-8").read()
defined=set(re.findall(r"\| (S-[A-Z]+-\d+) \|",src))
for f in sorted(glob.glob("./content/m00/L0.0*.mdx")):
    t=open(f,encoding="utf-8").read()
    miss=[n for n in need if n not in t]
    nex=len(re.findall(r"\*\*Exercice \d",t)); ncor=t.count("<summary>Correction")
    cited=set(re.findall(r"S-[A-Z]+-\d+",t))
    print(os.path.basename(f),"sections manquantes:",miss,"| exercices",nex,"corrections",ncor,"| sources citées non définies:",cited-defined,"| déclarées mais non citées dans le corps:",
      [s for s in re.findall(r'sources: \[(.*?)\]',t)[0].replace('"','').split(', ') if t.count(s)<2])
    ok &= not miss and 3<=nex<=6 and nex==ncor and not (cited-defined)
print("\nRÉSULTAT GLOBAL:", "OK" if ok else "ÉCHECS À CORRIGER")
