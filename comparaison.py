

import csv
from Bio import SeqIO
from main import comparer_sequences

fasta_path = "data/example.fasta"
csv_path = "results/comparaisons.csv"

sequences = []

# Lire les séquences du fichier FASTA
for record in SeqIO.parse(fasta_path, "fasta"):
    sequence = str(record.seq).upper()
    sequences.append((record.id, sequence))

# Comparer les séquences deux à deux
with open(csv_path, "w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier, delimiter=";")

    writer.writerow([
        "Sequence 1",
        "Sequence 2",
        "Longueur",
        "Similarite (%)"
    ])

    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            id1, seq1 = sequences[i]
            id2, seq2 = sequences[j]

            if len(seq1) == len(seq2):
                similarite = comparer_sequences(seq1, seq2)

                writer.writerow([
                    id1,
                    id2,
                    len(seq1),
                    similarite
                ])

            else:
                writer.writerow([
                    id1,
                    id2,
                    "Longueurs différentes",
                    "Non calculée"
                ])

print(f"Résultats enregistrés dans {csv_path}")
