import streamlit as st
import pandas as pd

# Configuração do título da página
st.title("Análise de Receita e Comissão")

# 1. Preparando os dados
data = {
    "Quantidade pedidos": [10000, 20000, 30000, 40000, 50000],
    "Receita Assinatura": [12000.00, 18000.00, 24000.00, 30000.00, 36000.00],
    "Valor Comissão": [7480.00, 14960.00, 22440.00, 29920.00, 37400.00]
}

df = pd.DataFrame(data)

# Definindo a quantidade de pedidos como o índice (eixo X do gráfico)
df.set_index("Quantidade pedidos", inplace=True)

# 2. Exibindo os dados em formato de tabela (opcional)
st.subheader("Dados da Tabela 1")
st.table(df)

# 3. Criando o gráfico de linhas
st.subheader("Gráfico de Evolução: Receita vs Comissão")
st.line_chart(df)

# Exibindo uma breve legenda/explicação
st.info("O gráfico acima mostra a relação entre o volume de pedidos e os valores financeiros.")


