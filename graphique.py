
import csv
import matplotlib.pyplot as plt

identifiants = []
pourcentages_gc = []

with open("results/statistiques.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=";")

    for ligne in lecteur:
        identifiants.append(ligne["Identifiant"])
        pourcentages_gc.append(float(ligne["Pourcentage GC"]))

plt.figure(figsize=(9, 5))

plt.bar(identifiants, pourcentages_gc)

plt.title("Pourcentage GC des séquences ADN")
plt.xlabel("Séquences")
plt.ylabel("GC (%)")

plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("results/pourcentage_gc.png")
plt.show()
