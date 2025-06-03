# Prédiction des Risques de Maladies Cardiovasculaires

Mini-projet réalisé dans le cadre de la matière **PYTHON - CALCUL SCIENTIFIQUE** (Doctorat – FST) – 2024-2025.

## Objectif

L’objectif de ce projet est de prédire les risques de développer une maladie cardiovasculaire à partir d’un ensemble de données issues du système BRFSS (Behavioral Risk Factor Surveillance System). Pour ce faire, nous appliquons plusieurs algorithmes de classification supervisée avec Python.

## Méthodologie

Le projet suit l’approche classique du machine learning :

1. Compréhension des données
2. Nettoyage et traitement
3. Transformation et normalisation
4. Modélisation et validation
5. Évaluation sur un jeu de test

## Données

- Source : Enquête BRFSS (États-Unis)
- Taille : 308 854 lignes, 19 colonnes
- Variable cible : `Heart_Disease`

### Principaux attributs

- Données démographiques : âge, sexe
- Comportements : tabagisme, consommation d’alcool, exercice
- Antécédents médicaux : diabète, cancer, dépression
- Données nutritionnelles : fruits, légumes, frites
- IMC, taille, poids

## Environnement et technologies

- Langage : Python 3
- Notebook : Jupyter
- Librairies :
  - Manipulation : `pandas`, `numpy`
  - Visualisation : `matplotlib`, `seaborn`
  - Machine learning : `scikit-learn`

## Modèles de classification utilisés

- k-Nearest Neighbors (`KNeighborsClassifier`)
- Arbre de Décision (`DecisionTreeClassifier`)
- Régression Logistique (`LogisticRegression`)
- Support Vector Machine (`SVC`)

### Évaluation des performances

- Accuracy
- Précision
- Recall
- F1-score
- Visualisation :
  - Matrices de confusion (heatmap)
  - Courbes ROC-AUC et Précision-Rappel

## Validation croisée et optimisation

Chaque modèle a été optimisé avec une validation croisée et recherche d’hyperparamètres (`GridSearchCV`), avec les paramètres suivants :

| Modèle               | Hyperparamètres                                   |
|----------------------|---------------------------------------------------|
| k-NN                 | `n_neighbors`, `metric`                           |
| Decision Tree        | `criterion`                                       |
| Logistic Regression  | `solver`, `max_iter`                              |
| SVM                  | `kernel`, `C`                                     |

## Résultats finaux

Le modèle le plus performant a été sélectionné en fonction de ses performances sur l’ensemble de validation, puis testé sur un jeu de test (25 %).

Les mesures affichées :
- Matrice de confusion
- Accuracy
- Précision
- Rappel
- F1-score


## Avertissement

Ce projet est à but strictement pédagogique et ne doit pas être utilisé à des fins médicales ou commerciales sans validation professionnelle.
