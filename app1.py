# dashboard_ecommerce.py

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Titre et mise en page
st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")
st.title("📦 Tableau de Bord - E-commerce")

# 2. Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce_data.csv", encoding='ISO-8859-1')  # adapte le nom du fichier
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Total'] = df['Quantity'] * df['UnitPrice']
    return df

df = load_data()

# 3. Filtres
st.sidebar.header("Filtres")
countries = st.sidebar.multiselect("Pays", options=df['Country'].unique(), default=["United Kingdom"])
date_range = st.sidebar.date_input("Plage de dates", [df['InvoiceDate'].min(), df['InvoiceDate'].max()])

# Application des filtres
df_filtered = df[
    (df['Country'].isin(countries)) &
    (df['InvoiceDate'].dt.date >= date_range[0]) &
    (df['InvoiceDate'].dt.date <= date_range[1])
]

# 4. KPI
total_sales = df_filtered['Total'].sum()
total_orders = df_filtered['InvoiceNo'].nunique()
avg_order = total_sales / total_orders if total_orders > 0 else 0

st.markdown("### 🔢 Indicateurs Clés")
col1, col2, col3 = st.columns(3)
col1.metric("💰 Chiffre d'affaires", f"${total_sales:,.2f}")
col2.metric("🧾 Nombre de commandes", f"{total_orders}")
col3.metric("🛒 Panier moyen", f"${avg_order:,.2f}")

# 5. Graphiques
st.markdown("### 📈 Ventes par Mois")
df_filtered['Month'] = df_filtered['InvoiceDate'].dt.to_period("M").astype(str)
monthly_sales = df_filtered.groupby('Month')['Total'].sum().reset_index()
fig1 = px.line(monthly_sales, x='Month', y='Total', title="Évolution des ventes mensuelles")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 🏷️ Top Produits")
top_products = df_filtered.groupby('Description')['Total'].sum().nlargest(10).reset_index()
fig2 = px.bar(top_products, x='Total', y='Description', orientation='h', title="Top 10 Produits")
st.plotly_chart(fig2, use_container_width=True)
