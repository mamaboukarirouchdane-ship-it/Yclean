"""Règle R1 des seuils de quiz (décision 3 du 31/10/2026, étendue à tous les quiz le 23/11/2026).

requiredCorrect = ⌈0,8 × n⌉ (entier) ; passThreshold = requiredCorrect / n ; passRule écrite à partir de requiredCorrect.
Seule source de la règle pour les générateurs (make_quiz.py, make_assessment_m00.py à m08.py) : aucun seuil de quiz ne doit
être écrit en dur. Chargement depuis un générateur (compatible avec python3 -I) :
    spec = importlib.util.spec_from_file_location('r1', f'{root}/tools/r1.py'); r1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r1)
    d = dict(lessonId=..., title=..., **r1.seuil(len(qs)), note=..., ...)
Les examens (EX0 à EX8) ne relèvent pas de R1 : leur seuil est en points.
"""
import math

PLANCHER = 0.8


def required_correct(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f'nombre de questions invalide : {n!r}')
    return math.ceil(PLANCHER * n - 1e-9)


def seuil(n):
    """Clés de seuil d'un quiz de n questions, dans l'ordre où elles sont stockées."""
    rc = required_correct(n)
    return {'passThreshold': rc / n, 'requiredCorrect': rc,
            'passRule': f'{rc} bonnes réponses sur {n} (règle R1 : ⌈0,8 × {n}⌉ = {rc} ; seuil pédagogique provisoire)'}
