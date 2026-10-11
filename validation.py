
from pathlib import Path
from Bio import SeqIO
from main import valider_sequence


def verifier_fasta(chemin):
    """Vérifie que le fichier FASTA existe et contient des séquences."""

    chemin = Path(chemin)

    if not chemin.is_file():
        raise FileNotFoundError(
            f"Le fichier {chemin} n'existe pas."
        )

    sequences = list(SeqIO.parse(chemin, "fasta"))

    if not sequences:
        raise ValueError(
            "Le fichier FASTA est vide ou ne contient aucune séquence."
        )

    for record in sequences:
        sequence = str(record.seq)

        if not valider_sequence(sequence):
            raise ValueError(
                f"La séquence {record.id} contient des caractères invalides."
            )

    return sequences


if __name__ == "__main__":
    try:
        sequences = verifier_fasta("data/example.fasta")
        print(f"Fichier valide : {len(sequences)} séquences trouvées.")

    except (FileNotFoundError, ValueError) as erreur:
        print(f"Erreur : {erreur}")
