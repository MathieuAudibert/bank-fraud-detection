# Vitrine de mes capacités SQL/Python dans un contexte bancaire 💳
<p align='center'>
    <a href="README.md"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg/2560px-Flag_of_the_United_Kingdom_%283-5%29.svg.png" title="GB" alt="GB" width="70" height="50"/></a> 
    <a href="README_es.md"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/1280px-Flag_of_Spain.svg.png" title="ES" alt="ES" width="70" height="50"/></a> 
</p>

##
## A propos du projet 
>[IMPORTANT]\
>Ce repo est un projet-vitrine qui utilise SQL, Python et Jupyter Notebooks dans une simulation bancaire. L'objectif principal est d'analyser les mouvements du compte afin de detecter des activités frauduleuses et en générer des statistiques. 

## Fonctionnalités 💎
- **Création de base de données** : Script de création des tables de la banque avec des comptes, des transactions et des clients.
- **Détection de fraude** : Scripts Python et SQL pour identifier les transactions potentiellement frauduleuses.
- **Analyse statistique** : Générer des statistiques sur les occurrences de fraude, telles que le pourcentage de transactions frauduleuses et le montant total d'argent impliqué.
- **Automatisation** : Workflow GitHub Actions pour automatiser l'exécution des scripts et mettre à jour les résultats régulièrement.

## Structure du dépôt 📁
- `data/` Ensemble de données d'exemple et scripts SQL pour la création de la base de données.
- `notebooks/` Jupyter Notebooks pour l'analyse des données et la détection de fraude.
- `scripts/` Scripts Python pour le traitement et l'analyse des données.
- `.github/workflows/` Workflow GitHub Actions pour l'automatisation.
- `README.md` Documentation du projet.

## Pour commencer

### Prérequis 🔨
- Python 3.12
- Jupyter Notebook
- SQL (SQLite, PostgreSQL, MySQL)
- Git

### Installation
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/yourusername/bank-fraud-detection.git
    cd bank-fraud-detection
    ```

2. Installez les dépendances Python :
    ```bash
    pip install -r requirements.txt
    ```

3. Configurez la base de données :
    ```bash
    cd data
    # Exécutez les scripts SQL pour créer et peupler la base de données
    ```

### Utilisation

1. Ouvrez les Jupyter Notebooks dans le répertoire `notebooks/` pour explorer les données et exécuter les analyses de détection de fraude :
    ```bash
    jupyter notebook
    ```

2. Exécutez les scripts Python dans le répertoire `scripts/` pour le traitement et l'analyse automatisés des données :
    ```bash
    python scripts/analyze_fraud.py
    ```

### Automatisation avec GitHub Actions
Le dépôt comprend des flux de travail GitHub Actions qui automatisent l'exécution des scripts de détection de fraude. Ces flux de travail se trouvent dans le répertoire `.github/workflows/`. Pour activer l'automatisation :
1. Poussez le dépôt sur GitHub.
2. Accédez à l'onglet GitHub Actions sur la page de votre dépôt pour surveiller les exécutions de flux de travail.

## Contribuer
Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request pour toute amélioration ou nouvelle fonctionnalité.

## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact 
![Gmail](https://img.shields.io/badge/mathieu.audibert27@gmail.com-white?style=for-the-badge&logo=gmail&logoColor=white&logoSize=auto&color=C11E1E)
![Outlook](https://img.shields.io/badge/mathieu.audibert@efrei.net-white?style=for-the-badge&logo=microsoft-outlook&logoColor=white&logoSize=auto&color=0072C6)