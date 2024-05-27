import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import openpyxl
st.set_page_config(page_title="Educação", page_icon="⚡")
st.markdown("# 1° Exemplo de codigo Temperatura ")
st.markdown("## Digite um valor entre 0 e 20 ")
st.sidebar.header("Profissional")
data =("0","15","20","30")
data_list = list(data)
data_counts = pd.Series(data_list).value_counts()
x = data_counts.index.to_numpy()
y = data_counts.to_numpy()

col1,col2,col3 = st.columns(3) 
with col1:
     # Crie a figura
    fig, ax = plt.subplots()

# Crie o gráfico de barras
    ax.bar(x, y)

# Defina títulos e rótulos
    ax.set_title("Temperatura")
    ax.set_xlabel("Valores")
    ax.set_ylabel("Frequência")

# Mostre o gráfico no Streamlit
    st.pyplot(fig)
     

with col2:
     temp = st.number_input("Enter your temperature ")
     col1 = st.write(f"Hello, the temperature now is , {temp}°C !")

if temp <= 4.99:

    st.write("gelo")

elif temp <= 12 :

        st.write ("ameno")

elif temp <=27:

    st.write("quente")

else :

    st.write ("hot")

    st.write(temp)
#****************************************************************************************************************************
st.markdown("# 2° Exemplo de codigo(Em Construção)")

df1 = pd.read_excel("Plan_vendas.xlsx",
                 sheet_name="Plan",
                 usecols="A:K",
                 header=0)

# Converter a coluna "Date" para o formato de data
df1["Data Emissão Pedido"] = pd.to_datetime(df1["Data Emissão Pedido"])
df1 = df1.sort_values("Data Emissão Pedido")
# Criar uma nova coluna "Month" que contém o ano e o mês
df1["Data Emissão Pedido"] = df1["Data Emissão Pedido"].apply(lambda x: str(x.year) + "-" + str(x.month))
print (df1)
col1,col2,col3  = st.columns(3) # Primeira linha com duas colunas
col5,col4,col6 = st.columns(3) # Segunda linha com três colunas
#*******************************************************************************************************************************
month = st.sidebar.selectbox("Selecione Produto", df1["Produto"].unique())

#*******************************************************************************************************************************
# Filtrar os dados com base no mês selecionado
df_filtered = df1[df1["Data Emissão Pedido"] == month]
# Criar uma nova coluna "Month" que contém o ano e o mês
df_filtered = df1[df1["Produto"] == month]
# Exibir o DataFrame filtrado
st.write(df_filtered)
col1,col2,  = st.columns(2) # Primeira linha com duas colunas
col3,col4, = st.columns(2) # Segunda linha com três colunas
col5 = st.columns(1) # Segunda linha com três colunas
# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Data Emissão Pedido", y="Canal de Vendas", color="Valor", title="Pedido")
# Exibir o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)
#---------------------------------------------------------------------------------------------------------------------------#
# Criar o gráfico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Data Emissão Pedido", y="Canal de Vendas", 
                  color="Estado", title="Vendas Estado",
                  orientation="h")
# Exibir o gráfico na segunda coluna
col2.plotly_chart(fig_prod, use_container_width=True)
#---------------------------------------------------------------------------------------------------------------------------#
# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Canal de Vendas", y="Valor", color="Data Emissão Pedido", title="Vendas por Empresa")

# Exibir o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)

