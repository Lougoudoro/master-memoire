#!/usr/bin/env python3
"""Contrôle de style du mémoire (fichiers LaTeX en français).

Signale, ligne par ligne :
  - les phrases de plus de 25 mots (ALERTE au-delà de 30) ;
  - les deux-points dans la prose (hors liste introduite et étiquettes de puces) ;
  - les paragraphes contenant plus d'une parenthèse ;
  - les formules typiques des textes générés par IA ;
  - les connecteurs répétés en tête de phrases consécutives ;
  - les tirets cadratins.

Usage : python verifier_style.py fichier.tex [autres.tex ...]
Code de sortie 1 s'il y a au moins une ALERTE.
"""
import re
import sys
from pathlib import Path

MAX_MOTS = 25
MAX_MOTS_ALERTE = 30

FORMULES_IA = [
    r"il est important de (noter|souligner|rappeler)",
    r"il convient de (noter|souligner|rappeler)",
    r"force est de constater",
    r"jou\w* un r[ôo]le (crucial|essentiel|cl[ée]|majeur|central|d[ée]terminant)",
    r"dans un monde en (constante )?[ée]volution",
    r"[àa] l'[èe]re (du num[ée]rique|de l'intelligence artificielle)",
    r"\bv[ée]ritable\b",
    r"enjeu majeur",
    r"pierre angulaire",
    r"\blevier\b",
    r"\ben somme\b",
    r"\ben d[ée]finitive\b",
    r"non seulement .{1,80} mais (aussi|[ée]galement)",
    r"s'inscri\w* dans une (d[ée]marche|dynamique|logique)",
    r"solution (innovante|novatrice|robuste)",
    r"\b(r[ée]volutionn\w*|r[ée]volutionnaire)\b",
    r"\bexceptionnel\w*\b",
    r"de mani[èe]re (significative|cons[ée]quente|holistique)",
    r"\bholistique\b",
    r"\bsynergie\b",
    r"\bparadigme\b",
    r"ouvr\w* la voie",
    r"\bcrucial\w*\b",
    r"\bincontournable\w*\b",
    r"\bfondamental\w*\b.{0,40}\bfondamental\w*\b",
    r"cela (montre|souligne|d[ée]montre) l'importance",
    r"tirer parti",
    r"au c(œ|oe)ur de",
    r"en constante [ée]volution",
    r"\bdivers(es)? et vari[ée]e?s\b",
]

CONNECTEURS = [
    "ainsi", "en effet", "de plus", "par ailleurs", "en outre", "cependant",
    "toutefois", "de ce fait", "enfin", "également", "donc", "or",
]

ENV_IGNORES = ("table", "tabular", "figure", "equation", "align", "verbatim",
               "lstlisting", "longtable", "tikzpicture", "minted")

ABREV = ["et al.", "p.~", "p. ", "pp. ", "Dr.", "Pr.", "M.", "Mme.", "etc.", "cf.",
         "vol.", "n°.", "fig.", "Fig.", "éd.", "op. cit.", "i.e.", "e.g.", "c.-à-d."]


def nettoyer(texte: str) -> str:
    """Retire les commandes LaTeX en gardant le texte lisible."""
    t = re.sub(r"(?<!\\)%.*", "", texte)
    t = re.sub(r"\$[^$]*\$", " X ", t)
    t = re.sub(r"\\(cite|ref|label|eqref|autoref|pageref|url|href)\*?(\[[^\]]*\])*\{[^}]*\}", "", t)
    t = re.sub(r"\\(textit|textbf|emph|texttt|enquote|textsc|underline|mbox)\{([^}]*)\}", r"\2", t)
    t = re.sub(r"\\(og|fg)\{\}", '"', t)
    t = t.replace("~", " ").replace("\\,", " ").replace("\\%", "%")
    t = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?", " ", t)
    t = t.replace("{", "").replace("}", "")
    return re.sub(r"[ \t]+", " ", t)


def paragraphes(lignes):
    """Regroupe les lignes en paragraphes de prose, hors environnements ignorés."""
    para, debut, profondeur = [], None, 0
    for num, ligne in enumerate(lignes, 1):
        brut = ligne.strip()
        m_debut = re.match(r"\\begin\{(\w+)\*?\}", brut)
        m_fin = re.match(r"\\end\{(\w+)\*?\}", brut)
        if m_debut and m_debut.group(1).startswith(ENV_IGNORES):
            profondeur += 1
        if profondeur:
            if m_fin and m_fin.group(1).startswith(ENV_IGNORES):
                profondeur -= 1
            continue
        if not brut or brut.startswith("%") or re.match(r"\\(sub)*section|\\chapter|\\paragraph|\\phantomsection|\\addcontentsline|\\begin|\\end|\\vspace|\\noindent\\textbf\{(Mots|Keywords)", brut):
            if para:
                yield debut, para
            para, debut = [], None
            continue
        if debut is None:
            debut = num
        para.append((num, ligne))
    if para:
        yield debut, para


def couper_phrases(texte):
    protege = texte
    for i, a in enumerate(ABREV):
        protege = protege.replace(a, a.replace(".", f"§{i}§"))
    morceaux = re.split(r"(?<=[.!?])\s+(?=[A-ZÀÂÉÈÊÎÔÙÇ«\"])", protege)
    res = []
    for m in morceaux:
        for i, a in enumerate(ABREV):
            m = m.replace(a.replace(".", f"§{i}§"), a)
        if m.strip():
            res.append(m.strip())
    return res


def ligne_de(fragment, para):
    """Retrouve la ligne source approximative d'un fragment de phrase."""
    debut = re.sub(r"\s+", " ", fragment)[:30].strip()
    for num, ligne in para:
        if debut[:15] and debut[:15] in re.sub(r"\s+", " ", nettoyer(ligne)):
            return num
    return para[0][0]


def analyser(chemin: Path):
    lignes = chemin.read_text(encoding="utf-8").splitlines()
    alertes, remarques = [], []

    for num, ligne in enumerate(lignes, 1):
        if "—" in ligne and not ligne.lstrip().startswith("%"):
            remarques.append((num, "tiret cadratin « — » : reformuler avec une virgule ou un point"))

    for debut, para in paragraphes(lignes):
        brut = " ".join(l for _, l in para)
        texte = nettoyer(brut)
        if not texte.strip():
            continue

        # Parenthèses par paragraphe
        n_par = len(re.findall(r"\(", texte))
        if n_par > 1:
            remarques.append((debut, f"{n_par} parenthèses dans le paragraphe (1 au maximum)"))

        # Deux-points dans la prose
        for num, ligne in para:
            sans_etiquette = re.sub(r"\\item\s*\[[^\]]*\]", "", ligne)
            sans_etiquette = re.sub(r"\\(texttt|verb)\{[^}]*\}", "", sans_etiquette)
            propre = nettoyer(sans_etiquette)
            # Étiquette de puce ou de rubrique en tête de ligne (« \item \textbf{Limites :} … »)
            if re.match(r"\s*(\\item\b|\\textbf\{|\\textit\{)", ligne):
                propre = re.sub(r"^\s*[^:.]{0,70}?\s*:\s?", "", propre, count=1)
            propre = re.sub(r"https?://\S+", "", propre)
            propre = re.sub(r"\d:\d", "", propre)
            if ":" in propre:
                suivante = lignes[num].strip() if num < len(lignes) else ""
                # « : » final qui introduit une liste, un code ou une figure : toléré
                if propre.rstrip().endswith(":") and suivante.startswith("\\begin{"):
                    continue
                alertes.append((num, "deux-points dans la prose : remplacer par un point, « car », « donc »…"))

        # Phrases
        phrases = couper_phrases(texte)
        prec_connecteur = None
        for ph in phrases:
            mots = re.findall(r"[\wÀ-ÿ'’-]+", ph)
            n = len(mots)
            num = ligne_de(ph, para)
            extrait = ph[:70] + ("…" if len(ph) > 70 else "")
            if n > MAX_MOTS_ALERTE:
                alertes.append((num, f"phrase de {n} mots (max {MAX_MOTS_ALERTE}) : « {extrait} »"))
            elif n > MAX_MOTS:
                remarques.append((num, f"phrase de {n} mots (cible ≤ {MAX_MOTS}) : « {extrait} »"))
            tete = ph.lower().lstrip("« \"")
            connecteur = next((c for c in CONNECTEURS if re.match(rf"{re.escape(c)}\b", tete)), None)
            if connecteur and prec_connecteur:
                remarques.append((num, f"connecteurs en tête de deux phrases de suite (« {prec_connecteur} », « {connecteur} »)"))
            prec_connecteur = connecteur

        # Formules IA
        bas = texte.lower()
        for motif in FORMULES_IA:
            for m in re.finditer(motif, bas):
                num = ligne_de(texte[m.start():m.start() + 40], para)
                alertes.append((num, f"formule typique de l'IA : « {texte[m.start():m.end()]} »"))

        # « permet de » répété
        n_permet = len(re.findall(r"\bpermet(tent|tant)? (de|d')", bas))
        if n_permet > 1:
            remarques.append((debut, f"« permet de » employé {n_permet} fois dans le paragraphe"))

    return alertes, remarques


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total_alertes = 0
    for arg in sys.argv[1:]:
        chemin = Path(arg)
        alertes, remarques = analyser(chemin)
        total_alertes += len(alertes)
        print(f"\n=== {chemin} : {len(alertes)} alerte(s), {len(remarques)} remarque(s)")
        for num, msg in sorted(alertes):
            print(f"  ALERTE    {chemin.name}:{num}  {msg}")
        for num, msg in sorted(remarques):
            print(f"  remarque  {chemin.name}:{num}  {msg}")
    sys.exit(1 if total_alertes else 0)


if __name__ == "__main__":
    main()
