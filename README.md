# SeqScope — Analyse de séquences ADN

## Description

SeqScope est un projet Python de bioinformatique permettant d'analyser des séquences ADN à partir d'un fichier FASTA.

## Fonctionnalités

- Lecture de fichiers FASTA avec Biopython.
- Validation des séquences ADN.
- Calcul de la longueur et du nombre de chaque nucléotide.
- Calcul du pourcentage GC.
- Comparaison de séquences deux à deux.
- Export des résultats dans des fichiers CSV.
- Visualisation du pourcentage GC avec Matplotlib.
- Tests automatisés avec pytest.

## Technologies utilisées

- Python
- Biopython
- Matplotlib
- CSV
- pytest

## Structure du projet

```text
seqscope/
├── data/
│   └── example.fasta
├── results/
│   ├── statistiques.csv
│   ├── comparaisons.csv
│   └── pourcentage_gc.png
├── tests/
│   └── test_analysis.py
├── main.py
├── statistiques.py
├── comparaison.py
├── graphique.py
├── validation.py
└── README.md
```

## Installation

Installer les dépendances :

```bash
python -m pip install biopython matplotlib pytest
```

## Utilisation

Exécuter les scripts depuis le dossier principal du projet :

```bash
python main.py
python statistiques.py
python comparaison.py
python graphique.py
python validation.py
```

## Objectif pédagogique

Ce projet permet de mettre en pratique Python, la manipulation de séquences biologiques, l'analyse de données et la visualisation de résultats en bioinformatique.