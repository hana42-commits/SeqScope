
import csv
from Bio import SeqIO
from main import analyser_sequence

fasta_path = "data/example.fasta"
csv_path = "results/statistiques.csv"

with open(csv_path, "w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier, delimiter=";")

    writer.writerow([
        "Identifiant",
        "Longueur",
        "Nombre A",
        "Nombre T",
        "Nombre G",
        "Nombre C",
        "Pourcentage GC"
    ])

    for record in SeqIO.parse(fasta_path, "fasta"):
        resultat = analyser_sequence(record)

        writer.writerow([
            resultat["identifiant"],
            resultat["longueur"],
            resultat["nombre_A"],
            resultat["nombre_T"],
            resultat["nombre_G"],
            resultat["nombre_C"],
            resultat["pourcentage_GC"]
        ])

print(f"Statistiques enregistrées dans {csv_path}")
