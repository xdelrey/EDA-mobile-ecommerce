import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time



# ========== CARGA Y EXPLORACIÓN DE DATOS DATASET 1 ==========

df_1 = pd.read_csv('data/user_behavior_dataset.csv')

# descripción del dataset 1
df_1.head()

df_1.info()

df_1.describe()

#comprobamos si hay datos nulos
print('Valores nulos en el Dataset 1:\n',
      df_1.isnull().sum()
      )

#comprobando si hay datos duplicados
print('Valores duplicados en el Dataset 1:',
      df_1.duplicated().sum()
      )

# CORRECCIÓN DE DATOS Y ESTANDARIZACIÓN
# comprobamos los tipos de las diferentes variables
df_1.dtypes

# Columnas tipo object
objetos = df_1.select_dtypes(include='object')
print(objetos.info())

# Revisamos los valores únicos de los objetos
print('\nValores únicos:')
for col in objetos:
    print('\n', col, '→', df_1[col].nunique(), ':\n', df_1[col].unique())

#Convertimos los Object con pocos valores diferentes al tipo category
df_1['Operating System'] = df_1['Operating System'].astype('category')
df_1['Gender'] = df_1['Gender'].astype('category')

# revisamos los tipos de las columnas
df_1.info()

# Seleccionamos solo las columnas numéricas
numeric_cols = df_1.select_dtypes(include='number').columns

# Creamos un boxplot por cada variable numérica
plt.figure(figsize=(14, 10))

for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df_1[col])
    plt.title(col)
    #plt.tight_layout()

plt.savefig('grafico_celda_10.png')
plt.close()

# ========== CARGA Y EXPLORACIÓN DE DATOS DATASET 2 ==========

df_2 = pd.read_csv('data/E-commerce Dataset.csv')
df_2.head()

# descripción del dataset 2
print('Total registros:', len(df_2))
print('Usuarios únicos:', df_2['Customer_Id'].nunique())

print('\nRegistros mobile:', len(df_2[df_2['Device_Type'] == 'Mobile']))
print('Usuarios únicos + móvil:', df_2[df_2['Device_Type'] == 'Mobile']['Customer_Id'].nunique())

df_2.info()

df_2.describe()

#comprobamos si hay datos nulos
nulos = df_2.isnull().sum()[df_2.isnull().sum() > 0]

# e imprimimos dónde se encuentran
print('Valores nulos en el Dataset 2:\n', nulos)

#comprobando si hay datos duplicados
print('Valores duplicados en el Dataset 2:',
      df_2.duplicated().sum()
      )

# comprobamos los tipos de las diferentes variables
df_2.dtypes

# Columnas tipo object
objetos_2 = df_2.select_dtypes(include='object')
print(objetos_2.info())

# Revisamos los valores únicos de los objetos
print('\nValores únicos:')
for col in objetos_2:
    print('\n', col, '→', df_2[col].nunique(), ':\n', df_2[col].unique())

#Convertimos los Object con pocos valores diferentes al tipo category
df_2['Gender'] = df_2['Gender'].astype('category')
df_2['Device_Type'] = df_2['Device_Type'].astype('category')
df_2['Customer_Login_type'] = df_2['Customer_Login_type'].astype('category')
df_2['Product_Category'] = df_2['Product_Category'].astype('category')
df_2['Order_Priority'] = df_2['Order_Priority'].astype('category')
df_2['Payment_method'] = df_2['Payment_method'].astype('category')

# revisamos los tipos de las columnas
df_2.info()

# Seleccionamos solo las columnas numéricas
numeric_cols_2 = df_2.select_dtypes(include='number').columns

# Creamos un boxplot por cada variable numérica
plt.figure(figsize=(14, 10))

for i, col in enumerate(numeric_cols_2, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df_2[col])
    plt.title(col)
    #plt.tight_layout()

plt.savefig('grafico_celda_20.png')
plt.close()

# TIPOS FECHA/HORA
# convierto Order_Date en tipo datetime
df_2['Order_Date'] = pd.to_datetime(df_2['Order_Date'], errors='coerce')

# convierto Time en tipo datetime (HH:MM:SS)
df_2['Time'] = pd.to_datetime(df_2['Time'], format='%H:%M:%S', errors='coerce').dt.time

# comprobamos los cambios
print(type(df_2['Order_Date'][0]))
print(type(df_2['Time'][0]))

# elimino los registros que contengan algún dato nulo
df_2 = df_2.dropna()

# muestro la información del Dataframe 2 limpio
df_2.info()


# ========== ESTANDARIZACIÓN DE COLUMNAS Y VALORES DE LAS CATEGORÍAS  ==========

# creo una función para eliminar espacios en blanco y otros caracteres especiales, y poner los nombres en minúsculas
def estandarizar_columnas(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('(', '', regex=False)
        .str.replace(')', '', regex=False)
        .str.replace('/', '_', regex=False)
    )
    return df

# Aplicamos a los dataframes
df_1 = estandarizar_columnas(df_1)
df_2 = estandarizar_columnas(df_2)

df_1.info()


# creo una función para estandarizar los valores de las variables categóricas

# Columnas categóricas en df_1
cat_cols_df1 = ['device_model', 'operating_system', 'gender']

# Columnas categóricas en df_2
cat_cols_df2 = ['gender', 'device_type', 'customer_login_type', 'product_category', 'order_priority', 'payment_method']

# Función para limpiar valores de texto/categoría
def limpiar_categorias(df, columnas):
    for col in columnas:
        if df[col].dtype.name in ['object', 'category']:
            df[col] = df[col].str.strip().str.lower() # al aplicarle métodos de string se convierte en tipo object
            df[col] = df[col].astype('category') # volvemos a convertir a category (no es lo óptimo) :-/
    return df

# Aplicamos a los dos dataframes
df_1 = limpiar_categorias(df_1, cat_cols_df1)
df_2 = limpiar_categorias(df_2, cat_cols_df2)



# ==========  GUARDADO DE DATASETS LIMPIOS  ==========

# Guardamos el Dataframe 1 como copia limpia del Dataset 1

df_1.to_csv('data/cleaned_user_behavior.csv', index=False)

# Guardamos el Dataframe 2 como copia limpia del Dataset 2
df_2.to_csv('data/cleaned_ecommerce.csv', index=False)



# ========== CONSTANTES  ==========

# Constantes
AZUL_X = '#4292c6'




# ========== ANÁLISIS EXPLORATORIO GENERAL  ==========


# ========== DATASET 1  ==========

# Carga del Dataset 1 previamente limpiado
df_1c = pd.read_csv('data/cleaned_user_behavior.csv')
df_1c.info()


# Gráfico descriptivo sobre la representación que tiene cada 'clase de comportamiento' en el Dataset

paleta_clases = sns.color_palette("Blues", n_colors=5)

plt.figure(figsize=(8, 5))
sns.countplot(data=df_1c, x='user_behavior_class', palette= paleta_clases)
plt.title('Distribución de Clases de Comportamiento del Usuario')
plt.xlabel('Clase de Comportamiento')
plt.ylabel('Número de Usuarios')
plt.savefig('grafico_celda_31.png')
plt.close()


# Gráfico descriptivo sobre la distribución de Edad y Género según la 'Clase de comportamiento'
 
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df_1c,
    x='user_behavior_class',
    y='age',
    palette='Blues',
    hue='gender'
    )
plt.title('Distribución de Edad según Clase de Comportamiento, para ambos Géneros')
plt.xlabel('Clase de Comportamiento del Usuario')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylabel('Edad')
plt.legend(title= 'Género', loc=2, bbox_to_anchor=(1, 1))
plt.savefig('grafico_celda_32.png')
plt.close()


# Gráfico descriptivo sobre la distribución por puntos de la Edad según la 'Clase de comportamiento'

plt.figure(figsize=(10, 6))
sns.swarmplot(
    data=df_1c,
    x='user_behavior_class',
    y='age',
    palette='Blues',
    size=5
    )

sns.stripplot(
    data=df_1c,
    x='user_behavior_class',
    y='age',
    color='black',
    alpha=0.3,
    jitter=True
    )

plt.title('Edad según Clase de Comportamiento')
plt.xlabel('Clase de Comportamiento')
plt.ylabel('Edad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('grafico_celda_33.png')
plt.close()



# ========== DATASET 2  ==========

df_2c = pd.read_csv('data/cleaned_ecommerce.csv')
df_2c.info()


# Gráfico descriptivo sobre la distribución de pedidos por Tipo de Dispositivo utilizado 

plt.figure(figsize=(6, 4))

sns.countplot(
    data=df_2c,
    x='device_type',
    palette='Blues')

plt.title('Número de pedidos por Tipo de Dispositivo utilizado')
plt.xlabel('Tipo de Dispositivo')
plt.ylabel('Número de Pedidos')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('grafico_celda_35.png')
plt.close()


# Gráfico descriptivo con el Número de pedidos por Tipo de dispositivo y por Género.
g = sns.catplot(
    data=df_2c,
    kind='count',
    x='gender',
    col='device_type',
    palette='Blues',
    height=5,
    aspect=0.8,
    sharey = False
)

g.fig.subplots_adjust(top=0.8)
g.fig.suptitle('Número de Pedidos por Género y Tipo de Dispositivo', fontsize=14)
g.set_axis_labels("Género", "Número de Pedidos")
g.set_titles("Dispositivo: {col_name}")


# Gráfico descriptivo de las Ventas (en Euros) por Categoría de Producto

categorias = df_2c.groupby('product_category')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))

categorias.plot(
    kind='barh',
    color = AZUL_X
    )

plt.title('Ventas (€) por Categoría')
plt.xlabel('Ventas Totales (€)')
plt.ylabel('Categoría de Producto')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().invert_yaxis()
plt.savefig('grafico_celda_37.png')
plt.close()


# Gráfico descriptivo que relaciona las Ventas (€) con el Beneficio

# Convierto order_date en un 'pandas datetime object'.
df_2c['order_date'] = pd.to_datetime(df_2c['order_date'])

# Añado una columna 'month' con año/mes
df_2c['month'] = df_2c['order_date'].dt.to_period('M')

# Agrupamos por mes y sumar el beneficio
monthly_summary = df_2c.groupby('month').agg(
    ventas=('sales', 'sum'),
    beneficio=('profit', 'sum')
).reset_index()

# gráficas
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_summary['month'].astype(str),
    monthly_summary['ventas'],
    marker='o',
    label='Ventas (€)',
    color='C0'
    )

plt.plot(
    monthly_summary['month'].astype(str),
    monthly_summary['beneficio'],
    marker='o',
    label='Beneficio (€)',
    color='orange'
    )

plt.title('Evolución Mensual de Ventas y Beneficio')
plt.xlabel('Mes')
plt.ylabel('€')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_celda_38.png')
plt.close()


# Gráfico de correlaciones para mapa de calor

# Filtramos las variables numéricas
variables_correlacion = ['sales', 'quantity', 'discount', 'profit', 'shipping_cost', 'aging']
corr_data = df_2c[variables_correlacion]

# Calculamos la matriz de correlación
corr_matrix = corr_data.corr()

# Mostramos el mapa de calor / heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    corr_matrix, 
    annot=True, 
    cmap='Blues', 
    fmt='.2f', 
    linewidths=0.5
    )
plt.title('Matriz de Correlaciones entre Variables Numéricas')
plt.savefig('grafico_celda_39.png')
plt.close()




# ========== ANÁLISIS ESPECÍFICOS DE HIPÓTESIS  ==========

# ################### HIPÓTESIS 1  ###################

# 1. Filtramos los usuarios que hayan comprado al menos una vez por móvil.

# 1.1 Primero creamos una columna nueva que unifica fecha y hora y sea de tipo datetime
df_2c['order_datetime'] = pd.to_datetime(df_2c['order_date'].astype(str) + ' ' + df_2c['time'].astype(str))

# 1.2 filtramos a un dataframe las compras hechas desde el móvil
mobile_sales_df = df_2c[df_2c['device_type'] == 'mobile']

# 1.3. guardamos los IDs únicos de quienes han comprado vía móvil
mobile_customers = mobile_sales_df['customer_id'].unique()

total_purchases = len(df_2c)
print('# compras:', total_purchases)
total_mobile_purchases = len(mobile_sales_df)
print('# compras desde móvil:', total_mobile_purchases)
total_mobile_users = len(mobile_customers)
print('# compradores únicos desde móvil:', total_mobile_users)

# 2. Para cada usuario, identificamos la fecha de su primera compra móvil.

# 2.1. Ordenamos por usuario y datetime
mobile_sales_df = mobile_sales_df.sort_values(['customer_id', 'order_datetime'])

# 2.2. Seleccionamos la primera compra móvil de cada usuario
first_mobile_purchase = mobile_sales_df.drop_duplicates(subset=['customer_id'], keep='first')

# 3. Comprobamos si antes de esa fecha el usuario había comprado por Desktop.

# 3.1. Guardamos en un dataframe solo las compras desde la 'web' (Desktop)
desktop_sales_df = df_2c[df_2c['device_type'] == 'web']
total_desktop_purchases = len(desktop_sales_df)
print('# compras desde web:', total_desktop_purchases)

# 3.2. Hacemos merge para asociar la fecha de primera compra móvil a cada usuario
merged_df = pd.merge(
    first_mobile_purchase[['customer_id', 'order_datetime']],
    desktop_sales_df,
    on='customer_id',
    suffixes=('_mobile', '_desktop')
)
total_desktop_mobile_purchases = len(merged_df)
print('# compras web de usuarios que también han comprado vía móvil:', total_desktop_mobile_purchases)

# 3.3. Buscamos compras Desktop previas a la primera compra móvil de cada usuario
merged_df = merged_df[merged_df['order_datetime_desktop'] < merged_df['order_datetime_mobile']]
total_desktop_purchases_prior_mobile = len(merged_df)
print('# compras web anteriores a la primera compra móvil:', total_desktop_purchases_prior_mobile)

################### RESULTADO DE LA HIPÓTESIS 1 ###################

# 4.1. Guardamos aquellos usuarios que han comprado en Desktop antes que en móvil
users_with_prior_desktop = merged_df['customer_id'].unique()
total_users_with_prior_desktop = len(users_with_prior_desktop)

# 4.2. Cálculo del % que cumplen la hipótesis
percent_with_prior_desktop = (total_users_with_prior_desktop / total_mobile_users) * 100

print('\n\t- Número de compradores únicos desde móvil:', total_mobile_users)
print('\t- Número de personas que compraron vía desktop antes que vía móvil:', total_users_with_prior_desktop)
print(f'\t- Porcentaje de personas que compran desde desktop antes de comprar desde móvil: {percent_with_prior_desktop:.2f} %')


################### VISUALIZACIONES HIPÓTESIS 1 ###################

# Diagrama de tarta con porcentajes

### Datos
labels = ['Compró antes en Desktop', 'No había comprado antes en Desktop']
sizes = [total_users_with_prior_desktop, total_mobile_users - total_users_with_prior_desktop]  # 821 sí, 2736 no

### Estilo
colors = plt.cm.Blues([0.5, 0.8])
explode = (0.05, 0)  # Para resaltar la primera porción

plt.figure(figsize=(6, 6))
plt.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    explode=explode, 
    autopct='%1.1f%%',
    shadow=True
)
plt.title('Hipótesis 1. ¿Los compradores móviles habían comprado antes en Desktop?')
plt.axis('equal')  # Círculo perfecto

plt.savefig('grafico_celda_44.png')
plt.close()


# Diagrama de barras secuenciales

### Datos
etapas = [
    'Compradores móviles únicos',
    'Compras web de\nusuarios que han comprado móvil',
    'Compras web anteriores\na primera móvil',
    'Personas que compraron\nweb antes que móvil'
]
valores = [total_mobile_users, total_desktop_mobile_purchases, total_desktop_purchases_prior_mobile, total_users_with_prior_desktop]

plt.figure(figsize=(10, 6))
bars = plt.bar(
    etapas, 
    valores, 
    color=plt.cm.Blues([0.8, 0.6, 0.4, 0.2]))

plt.ylabel('Número de usuarios/compras')
plt.title('Compras y compradores móviles')

### Añade los valores encima de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 30,
        int(yval),
        ha='center',
        va='bottom'
        )

plt.tight_layout()
plt.savefig('grafico_celda_45.png')
plt.close()


# ################### HIPÓTESIS 2 ###################

# Filtra solo compras hechas desde móvil
df_mobile = df_2c[df_2c['device_type'] == 'mobile']
print(len(df_mobile))

# Cuenta el número de compras por usuario en móvil
compras_mobile = df_mobile.groupby('customer_id').size().reset_index(name='compras_mobile')
print(len(compras_mobile))

# Selecciona solo los usuarios con más de una compra en móvil (recurrentes)
usuarios_recurrentes = compras_mobile[compras_mobile['compras_mobile'] > 1]
print(len(usuarios_recurrentes))

# Únelos con el DataFrame original para recuperar info de género
df_recurrentes_mobile = df_mobile[df_mobile['customer_id'].isin(usuarios_recurrentes['customer_id'])]
print(len(df_recurrentes_mobile))

# Gráfico de barras por género para usuarios recurrentes en móvil

df_recurrentes_mobile['gender'].value_counts().plot(kind='bar', color='C0')

plt.title('Distribución de Género entre Compradores Recurrentes Mobile')
plt.xlabel('Género')
plt.ylabel('Nº de usuarios')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('grafico_celda_47.png')
plt.close()

################### RESULTADO DE LA HIPÓTESIS ###################

# Total de usuarios recurrentes en móvil
total_recurrentes = len(df_recurrentes_mobile['customer_id'].unique())

# Número de recurrentes por género
genero_counts = df_recurrentes_mobile.groupby('gender')['customer_id'].nunique()

# Porcentaje por género
porcentajes = (genero_counts / total_recurrentes * 100).round(2)

print("Porcentaje de usuarios recurrentes en móvil por género:")
print(porcentajes)