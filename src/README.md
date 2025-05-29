# Mobile-Driven Purchase Behavior Analysis

Exploratory Data Analysis (EDA) to understand how mobile device usage shapes online purchasing behavior.

---

## 🎯 Goal

Quantify and visualize the impact of mobile usage habits on e‑commerce conversion and customer segments to inform product decisions, personalization tactics, and notification strategy.

---

## 📦 Datasets Used

| # | Dataset | Source | Key Fields |
|---|---------|--------|-----------|
| 1 | **E‑commerce Transactions** | Kaggle ([link](https://www.kaggle.com/datasets/mervemenekse/ecommerce-dataset/data)) | Order‐level records (order ID, timestamp, product, price, quantity, device, etc.) |
| 2 | **Mobile Device Usage & User Behavior** | Kaggle ([link](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)) | Daily app usage time, number of notifications, installed apps, age, gender, OS |

---

## 🛠️ Workflow

1. **Data Cleaning & Standardization**  
   * Eliminación de duplicados y nulos  
   * Conversión de formatos de fecha y hora (UTC → local)  
   * Estandarización de nombres de columnas y categorías

2. **General EDA**  
   * Estadísticos descriptivos de órdenes, dispositivos y demografía  
   * Detección de outliers y distribución de variables clave  
   * Observaciones generales sobre calidad y sesgos de los datos  

3. **Hypothesis‑Driven Analysis**  
   | ID | Hipótesis | Métricas y Visualizaciones |
   |----|-----------|---------------------------|
   | H1 | **Confianza multicanal** – Los usuarios que compran en móvil lo han hecho antes en desktop | Secuencia de dispositivos, ratios móvil ↔ desktop, heatmap temporal |
   | H2 | **Conversión por género** – Existen diferencias en la tasa de compra recurrente móvil según género | Gráficos de barras apiladas, test de proporciones |
   | H3 | **Tiempo en apps de compras ↔ nº compras** | Scatter + regresión lineal, buckets de percentiles |
   | H4 | **Notificaciones diarias ↔ conversión** | Violín + boxplot, correlación de Spearman |


---

## 📂 Project Layout

```
├── data/               # Raw & cleaned CSV files
├── notebooks/          # Jupyter drafts & exploratory work
├── main.py             # Reproducible script: loads data, runs EDA & saves charts / CSVs
├── memoria.ipynb       # Narrative notebook with full analysis & commentary
└── README.md           # You are here
```

---

## 🚀 How to Reproduce

```bash
# 1) Clone repo & create env

# 2) Install dependencies

# 3) Run analysis
python main.py  # guarda gráficos en /outputs y CSVs intermedios en /data
```

> Para mayor detalle de cada paso, consulta **memoria.ipynb** .

---

## ✍️ Author

Proyecto elaborado por **Xabi del Rey** (Product Manager → Data Science) © 2025
