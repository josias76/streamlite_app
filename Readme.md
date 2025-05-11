

![e_commerce](https://github.com/user-attachments/assets/fed80e22-2cdc-4d13-8704-d8f92e26e7a0)

# 📦 Dashboard E-Commerce avec Streamlit

Ce projet est une application web interactive construite avec **Streamlit** permettant d’analyser les ventes d’un site de commerce électronique. Le tableau de bord propose des visualisations dynamiques, des filtres interactifs et des indicateurs clés de performance.

## 🔧 Fonctionnalités

- 🔍 Filtrage des ventes par pays et par période
- 💰 Affichage des KPI : chiffre d’affaires, nombre de commandes, panier moyen
- 📈 Graphiques dynamiques :
  - Évolution mensuelle des ventes
  - Top 10 des produits les plus vendus
- 📦 Données simulées sur 10 000 transactions

## 🗃️ Fichier de données

Le fichier de données simulé est fourni dans ce projet :  
**`ecommerce_data.csv`**

Colonnes :
- `InvoiceNo` : Identifiant unique de la commande
- `Description` : Produit vendu
- `Quantity` : Quantité achetée
- `UnitPrice` : Prix unitaire
- `InvoiceDate` : Date de la commande
- `Country` : Pays du client
- `CustomerID` : Identifiant client

## 🚀 Lancer l'application

### 1. Installer les dépendances

```bash
pip install streamlit pandas plotly
