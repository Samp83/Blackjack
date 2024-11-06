# Blackjack_Cassandra_Sami_Owen
 
## Table of Contents
1. [Description](#description)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Lancement](#lancement)
5. [Repartition](#repartition)

# Description
***
Jeu de Blackjack simplifié en utilisant uniquement des dés avec 4 joueurs.
Projet réalisé par: Sami, Cassandra et Owen.

# Technologies
***
**Backend:** 
* Django version 5.1.3 (ORM)
* Django Ninja version 1.3.0

**Frontend:**
* Vite version 5.4.10 pour du React.js

# Installation
***
Au préalable, nous créons un environnement virtuel pour notre **Backend** en urilisant [Mini Conda](https://docs.anaconda.com/miniconda/#miniconda-latest-installer-links): 
En prenant au moins, une version utilisant Python 3.11 ou plus et en utilisant de préférence la console de conda **Anaconda Prompt**.
```
conda create -n <env_name>
conda activate <env_name>
```
Puis nous installons Django:
```
pip  install django          
pip  install django-ninja

 # alternative
py -m pip  install django          
py -m pip  install django-ninja
```
Consernant le **Frontend**, vérifier si vous avec bien [Node](https://nodejs.org/fr), 
ici nous allons l'utiliser conjointement avec [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating),
un gestionnaire de pour les différentes versions de Node.js possibles. ***/!\ Choisisez la version adaptée à votre système d'exploitation.*** 
```
nvm list
nvm use X.X.X
```
# Lancement
***
Pour lancer le **Front**
```
cd Frontend
npm run dev
```
Pour lancer le **Back**
```
cd backend
python manage.py migrate
python manage.py runserver
```
# Repartition
***
Sami c'est principalement occupé du back, Owen du front et moi j'ai aidé des 2 côtés.
Due à certains soucis la pluspart de nos commits on était fais par Sami.
