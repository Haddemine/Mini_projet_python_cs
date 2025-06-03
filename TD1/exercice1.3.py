def gene_plus_exprime(donnees: dict) -> str:
    return max(donnees, key=donnees.get)

donnees = {"BRCA1": 5200, "TP53": 3400, "EGFR": 4100}
print(gene_plus_exprime(donnees))  # Résultat : BRCA1
