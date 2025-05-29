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
   | ID | Hipótesis |
   |----|-----------|
   | H1 | **Confianza del comprador** – Los usuarios que compran desde el móvil previamente han comprado desde Desktop |
   | H2 | **Confianza del comprador** – Hay relación entre plazos de entrega previos y la repetición de compra? |
   | H3 | **Perfil** - Hay diferencias de género entre los compradores 'mobile' recurrentes? |
   | H4 | **Oferta** Hay categorías de producto que destaquen para la primera compra móvil? |
   | H5 | **Compras impulsivas** Tienen más efecto los descuentos en las compras móviles que en las Desktop? |
   | H6 | **Sincronía horaria de uso y compra** Se solapan las horas de mayor actividad en el móvil con las horas pico de compra online? |


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
