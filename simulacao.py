import streamlit as st
import pandas as pd
import altair as alt

# Configuração da Página
st.set_page_config(page_title="Simulador de Negócios", layout="wide")

st.title("📊 Simulador de Cenários de Receita")

# --- BARRA LATERAL (INPUTS) ---
st.sidebar.header("Parâmetros da Simulação")

# 1. Inputs de Produto e Negociação
st.sidebar.subheader("Produto & Taxas")
valor_produto = st.sidebar.number_input("Valor do Produto (R$)", value=17.0, step=0.05)

taxa_negociacao = st.sidebar.number_input("Taxa de Negociação (%)") / 100
#taxa_negociacao = st.sidebar.slider("Taxa de Negociação (%)", 0, 100, 12) / 100

#taxa_remuneracao = st.sidebar.slider("Taxa de Remuneração (%)", 0, 100, 5) / 100
taxa_remuneracao = st.sidebar.number_input("Taxa de Remuneração (%)") / 100

# 2. Inputs de Volume e Assinatura
st.sidebar.subheader("Volume & Assinaturas")
# Aqui permitimos simular uma progressão (como as fases da planilha) ou um valor único
fases = ['Fase 1', 'Fase 2', 'Fase 3', 'Fase 4', 'Fase 5', 'Fase 6']
volumes_input = [10000, 20000, 30000, 40000, 50000, 60000] # Padrão da planilha
assinantes_input = [20, 30, 40, 50, 60, 70] # Padrão da planilha
valor_assinatura = st.sidebar.number_input("Valor da Assinatura (R$)", value=600.0)

# Opção para customizar o volume base (multiplicador para simulação)
fator_crescimento = st.sidebar.slider("Fator de Crescimento do Volume de Pedidos(x)", 0.5, 3.0, 1.0)

# --- CÁLCULOS ---
# Cálculos Unitários
valor_negociado = valor_produto * (1 - taxa_negociacao)
valor_remuneracao_unit = valor_negociado * taxa_remuneracao

# Construção do DataFrame de Cenários
dados = []
for i, fase in enumerate(fases):
    vol_ajustado = volumes_input[i] * fator_crescimento
    valor_remuneracao_total = valor_negociado * vol_ajustado * taxa_remuneracao

    # ass_ajustado = assinantes_input[i] # Mantendo fixo ou poderia aplicar fator também
    ass_ajustado = assinantes_input[i] * fator_crescimento

    valor_total_pedido = valor_negociado * vol_ajustado
    receita_assinatura = ass_ajustado * valor_assinatura
    #receita_total = valor_total_pedido + receita_assinatura
    
    dados.append({
        "Fase": fase,
        "Volume": vol_ajustado,
        "Assinante": ass_ajustado,
        "Total Pedidos (R$)": valor_total_pedido,
        "Receita Assinaturas (R$)": receita_assinatura,
        "Valor Remuneração Unitaria (R$)": valor_remuneracao_unit,
        "Valor Total da Remuneração (R$)": valor_remuneracao_total
    })

df_resultado = pd.DataFrame(dados)

# --- VISUALIZAÇÃO ---

# 1. KPIs do Cenário Atual (Baseado na Fase 1 como exemplo ou média)
col1, col2, col3 = st.columns(3)
col1.metric("Valor Negociado (Unit)", f"R$ {valor_negociado:.2f}")
col2.metric("Remuneração (Unit)", f"R$ {valor_remuneracao_unit:.2f}")
col3.metric("Ticket Assinatura", f"R$ {valor_assinatura:.2f}")

# st.divider()

# 2. Tabela de Resultados
st.subheader("Projeção por Fases")
st.dataframe(df_resultado.style.format({
    "Volume":" {:,.0f}",
    "Total Pedidos (R$)": "R$ {:,.2f}",
    "Receita Assinaturas (R$)": "R$ {:,.2f}",
    "Assinante": "{:.0f}",
    "Valor Remuneração Unitaria (R$)": "R$ {:,.2f}",
    "Valor Total da Remuneração (R$)":"R$ {:,.2f}"
}))

# 3. Gráficos
# st.subheader("Evolução Gráfica")
# chart_data = df_resultado.melt('Fase', value_vars=['Total Pedidos (R$)', 'Receita Assinaturas (R$)'], var_name='Tipo', value_name='Valor')

# chart = alt.Chart(chart_data).mark_bar().encode(
#     x='Fase',
#     y='Valor',
#     color='Tipo',
#     tooltip=['Fase', 'Tipo', 'Valor']
# ).interactive()
#st.altair_chart(chart, use_container_width=True)



st.subheader("Comparativo de Modelos")
#chart_data = df_resultado("Valor Total da Remuneração (R$)")


# Definindo a quantidade de pedidos como o índice (eixo X do gráfico)
df_resultado.set_index("Fase", inplace=True)
df_selecao = df_resultado[['Receita Assinaturas (R$)' , "Valor Total da Remuneração (R$)"]]
st.line_chart(df_selecao)

# fim do arquivo
