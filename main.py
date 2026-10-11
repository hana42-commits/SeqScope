

from Bio import SeqIO

def calculer_gc(sequence):
    """Calcule le pourcentage de G et de C."""
    sequence = sequence.upper()

    if len(sequence) == 0:
        return 0.0

    nombre_g = sequence.count("G")
    nombre_c = sequence.count("C")

    return (nombre_g + nombre_c) / len(sequence) * 100


def valider_sequence(sequence):
    """Vérifie qu'une séquence contient uniquement A, T, G et C."""
    sequence = sequence.upper()
    alphabet_adn = set("ATGC")

    if len(sequence) == 0:
        return False

    for nucleotide in sequence:
        if nucleotide not in alphabet_adn:
            return False

    return True


def analyser_sequence(record):
    """Calcule les statistiques d'une séquence ADN."""
    sequence = str(record.seq).upper()

    if not valider_sequence(sequence):
        raise ValueError(f"Séquence invalide : {record.id}")

    resultat = {
        "identifiant": record.id,
        "longueur": len(sequence),
        "nombre_A": sequence.count("A"),
        "nombre_T": sequence.count("T"),
        "nombre_G": sequence.count("G"),
        "nombre_C": sequence.count("C"),
        "pourcentage_GC": round(calculer_gc(sequence), 2),
    }

    return resultat


if __name__ == "__main__":
    fasta_path = "data/example.fasta"

    for record in SeqIO.parse(fasta_path, "fasta"):
        resultat = analyser_sequence(record)
        print(resultat)

def comparer_sequences(seq1, seq2):
    """Compare deux séquences ADN de même longueur."""
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    if not valider_sequence(seq1) or not valider_sequence(seq2):
        raise ValueError("Une des séquences ADN est invalide.")

    if len(seq1) != len(seq2):
        raise ValueError(
            "Les deux séquences doivent avoir la même longueur."
        )

    identiques = 0

    for nucleotide1, nucleotide2 in zip(seq1, seq2):
        if nucleotide1 == nucleotide2:
            identiques += 1

    pourcentage = identiques / len(seq1) * 100

    return round(pourcentage, 2)
print(comparer_sequences("ATGC", "ATGA"))

def test_sequences_identiques():
    assert comparer_sequences("ATGC", "ATGC") == 100.0


def test_sequences_partiellement_identiques():
    assert comparer_sequences("ATGC", "ATGA") == 75.0


def test_sequences_differentes():
    assert comparer_sequences("AAAA", "TTTT") == 0.0


def test_longueurs_differentes():
    import pytest

    with pytest.raises(ValueError):
        comparer_sequences("ATGC", "ATG")

