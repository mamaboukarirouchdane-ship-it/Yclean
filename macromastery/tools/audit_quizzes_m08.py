"""Audit des quiz du module 8 (structure, biais de position, biais de longueur, doublons, réserves 8.4)."""
import json, glob, re, collections
rows=[]; bad=0
def audit(path, thr_expected):
    global bad
    d=json.load(open(path,encoding='utf-8'))
    qs=d['questions']; out={'f':path.split('/')[-1],'n':len(qs),'thr':d.get('passThreshold'),'issues':[]}
    pos=collections.Counter(q['correct'] for q in qs)
    longest=0; sumratio=0
    prompts=set()
    for q in qs:
        L={o['id']:len(o['text']) for o in q['options']}
        if max(L,key=L.get)==q['correct']: longest+=1
        others=[v for k,v in L.items() if k!=q['correct']]
        sumratio+=L[q['correct']]/(sum(others)/len(others))
        if len(q['explanation'])<60: out['issues'].append(q['id']+' explication courte')
        if q['prompt'] in prompts: out['issues'].append(q['id']+' doublon')
        prompts.add(q['prompt'])
        if len(q['options'])!=4: out['issues'].append(q['id']+' options!=4')
    out['pos']=dict(sorted(pos.items())); out['longest']=longest
    out['ratio']=round(sumratio/len(qs),2)
    if thr_expected and d.get('passThreshold')!=thr_expected: out['issues'].append('seuil inattendu')
    if len(qs)<6: out['issues'].append('moins de 6 questions')
    if max(pos.values())>len(qs)/2: out['issues'].append('position dominante')
    if longest/len(qs)>=0.5 : out['issues'].append('biais de longueur (bonne réponse la plus longue %d/%d)'%(longest,len(qs)))
    return out
for p in sorted(glob.glob('content/m08/assessments/chap_*.quiz.json')): rows.append(audit(p,5/6))
for p in sorted(glob.glob('content/m08/quiz/L8.*.quiz.json')): rows.append(audit(p,0.875))
for r in rows:
    print(r['f'],r['n'],r['thr'],r['pos'],'plus longue=%d'%r['longest'],'ratio=%s'%r['ratio'],r['issues'])
