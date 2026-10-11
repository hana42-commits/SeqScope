

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import calculer_gc, valider_sequence, comparer_sequences


def test_gc_50_pourcent():
    assert calculer_gc("ATGC") == 50.0


def test_gc_100_pourcent():
    assert calculer_gc("GGCC") == 100.0


def test_gc_0_pourcent():
    assert calculer_gc("ATAT") == 0.0


def test_sequence_vide():
    assert calculer_gc("") == 0.0


def test_minuscules():
    assert calculer_gc("atgc") == 50.0
from main import calculer_gc, valider_sequence

def test_sequence_adn_valide():
    assert valider_sequence("ATGC") is True


def test_sequence_en_minuscules():
    assert valider_sequence("atgc") is True


def test_sequence_caractere_invalide():
    assert valider_sequence("ATGB") is False


def test_sequence_vide_invalide():
    assert valider_sequence("") is False

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

from validation import verifier_fasta


def test_fasta_valide():
    sequences = verifier_fasta("data/example.fasta")
    assert len(sequences) == 5


def test_fasta_introuvable():
    import pytest

    with pytest.raises(FileNotFoundError):
        verifier_fasta("data/fichier_inexistant.fasta")

