#!/usr/bin/env python3
"""Mesure la taille des chapitres du mémoire à partir de main.toc (après compilation).

Repères (voir memoire-conventions, « Taille et équilibre des chapitres ») :
  - chapitre numéroté entre 0,5 et 1,5 fois la moyenne des chapitres ;
  - chapitre des résultats pas le plus court ;
  - introduction générale de 5 à 8 pages, conclusion générale de 2 à 4 pages ;
  - corps (introduction → conclusion) de 60 à 90 pages environ ;
  - répartition cible propre à ce mémoire (colonne « Cible »), prioritaire.

Usage : python equilibre_chapitres.py [main.toc]
"""
import re
import sys
from pathlib import Path

INTRO = (5, 8)
CONCLUSION = (2, 4)
CORPS = (60, 90)
RATIO_MIN, RATIO_MAX = 0.5, 1.5

# Répartition cible d'OntoPlantMedBF (choix de l'auteur, 2026-11-16).
CIBLES = {
    "intro": (6, 7),
    "I": (15, 17),
    "II": (16, 19),
    "III": (17, 20),
    "IV": (14, 17),
    "conclusion": (2, 3),
}


def cle_cible(titre: str, num: str):
    if num:
        return num
    bas = titre.lower()
    if bas.startswith("introduction g"):
        return "intro"
    if bas.startswith("conclusion g"):
        return "conclusion"
    return None


def lire_toc(chemin: Path):
    """Renvoie la liste (titre, numéro, page) des entrées de niveau chapitre en pagination arabe."""
    entrees = []
    for ligne in chemin.read_text(encoding="utf-8", errors="replace").splitlines():
        if not ligne.startswith("\\contentsline {chapter}"):
            continue
        m = re.match(r"\\contentsline \{chapter\}\{(.*)\}\{([^{}]*)\}\{[^{}]*\}%?\s*$", ligne)
        if not m:
            continue
        titre, page = m.group(1), m.group(2)
        if not page.isdigit():
            continue  # pièces liminaires en chiffres romains
        num = re.search(r"\\numberline \{([^}]*)\}", titre)
        titre = re.sub(r"\\numberline \{[^}]*\}", "", titre)
        titre = re.sub(r"\\[a-zA-Z]+\s*", "", titre).replace("{", "").replace("}", "").strip()
        entrees.append((titre, num.group(1) if num else "", int(page)))
    return entrees


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    chemin = Path(sys.argv[1] if len(sys.argv) > 1 else "main.toc")
    if not chemin.exists():
        print(f"{chemin} introuvable : compile d'abord le mémoire (latexmk -pdf main.tex).")
        sys.exit(2)
    entrees = lire_toc(chemin)
    if len(entrees) < 2:
        print("Pas assez d'entrées de chapitre dans la table des matières.")
        sys.exit(2)

    # Taille = page de début de l'entrée suivante - page de début (la dernière entrée,
    # en général la bibliographie, sert de borne et n'est pas mesurée).
    parties = []
    for (titre, num, page), (_, _, suivante) in zip(entrees, entrees[1:]):
        parties.append((titre, num, page, max(suivante - page, 1)))

    alertes = []
    chapitres = [p for p in parties if p[1]]
    moyenne = sum(p[3] for p in chapitres) / len(chapitres) if chapitres else 0

    print(f"{'Partie':<52} {'Début':>6} {'Pages':>6} {'Cible':>8}  Rapport")
    for titre, num, page, n in parties:
        nom = f"{num} {titre}".strip()
        rapport = f"{n / moyenne:.2f} × moy." if num and moyenne else ""
        cible = CIBLES.get(cle_cible(titre, num))
        txt_cible = f"{cible[0]}-{cible[1]}" if cible else ""
        print(f"{nom[:52]:<52} {page:>6} {n:>6} {txt_cible:>8}  {rapport}")
        if cible and not cible[0] <= n <= cible[1]:
            sens = "au-dessus" if n > cible[1] else "en dessous"
            alertes.append(f"{nom} : {n} p., {sens} de la cible {cible[0]}-{cible[1]} p.")
        bas = titre.lower()
        if num:
            if n > RATIO_MAX * moyenne:
                alertes.append(f"{nom} : {n} p., plus de {RATIO_MAX} fois la moyenne ({moyenne:.1f} p.) → alléger, déplacer en annexe")
            if n < RATIO_MIN * moyenne:
                alertes.append(f"{nom} : {n} p., moins de la moitié de la moyenne ({moyenne:.1f} p.) → étoffer sans remplissage")
        elif not cible and bas.startswith("introduction g"):
            if not INTRO[0] <= n <= INTRO[1]:
                alertes.append(f"Introduction générale : {n} p. (repère {INTRO[0]} à {INTRO[1]})")
        elif not cible and bas.startswith("conclusion g"):
            if not CONCLUSION[0] <= n <= CONCLUSION[1]:
                alertes.append(f"Conclusion générale : {n} p. (repère {CONCLUSION[0]} à {CONCLUSION[1]})")

    resultats = [p for p in chapitres if "sultat" in p[0].lower()]
    if resultats and chapitres:
        plus_court = min(chapitres, key=lambda p: p[3])
        if resultats[0][3] <= plus_court[3]:
            alertes.append(f"Le chapitre des résultats ({resultats[0][3]} p.) est le plus court des chapitres numérotés")

    corps = [p for p in parties if p[1] or p[0].lower().startswith(("introduction g", "conclusion g"))]
    total = sum(p[3] for p in corps)
    print(f"\nCorps du mémoire (introduction → conclusion) : {total} pages ; moyenne des chapitres : {moyenne:.1f} p.")
    if not CORPS[0] <= total <= CORPS[1]:
        alertes.append(f"Corps de {total} p. (ordre de grandeur attendu {CORPS[0]} à {CORPS[1]})")

    print(f"\n{len(alertes)} écart(s) aux repères")
    for a in alertes:
        print(f"  - {a}")
    print("\nNote : la taille d'une partie est comptée jusqu'au début de la suivante (±1 page).")


if __name__ == "__main__":
    main()
