
def calcul_moyenne(donnees: list[float]) -> float | None:
    if not donnees:
        return None
    return sum(donnees) / len(donnees)
