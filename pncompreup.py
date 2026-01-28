import streamlit as st
import pandas as pd



# Configuração da Página
st.set_page_config(page_title="CompreUp - Modelo de Negócio", layout="wide")

# --- SIDEBAR: SIMULADOR DE FATURAMENTO ---
st.sidebar.header("🛠️ Simulador de Escala")
st.sidebar.markdown("Ajuste os valores para projetar o cenário financeiro.")

# num_clientes = st.sidebar.slider("Quantidade de Clientes", min_value=1, max_value=15000, value=1160)
ticket_mensal = st.sidebar.number_input("Valor da Assinatura (R$)", value=600.0)
num_clientes = st.sidebar.number_input("Quantidade de Clientes", min_value=1)

# Cálculos do Simulador
receita_mensal = num_clientes * ticket_mensal
impostos = receita_mensal * 0.06
custos_variaveis = receita_mensal * 0.10
custos_fixos = receita_mensal * 0.15
lucro_operacional = receita_mensal - (impostos + custos_variaveis + custos_fixos)

# --- SIDEBAR: SIMULADOR DE COMPARATIVO DE MODELOS DE RECEITA ---
st.sidebar.header("Simulador Comparativo Modelos de Receita")

# 1. Inputs de Produto e Negociação
st.sidebar.subheader("Produto & Taxas")
valor_produto = st.sidebar.number_input("Valor do Produto (R$)", value=17.0, step=0.05)

taxa_negociacao = st.sidebar.number_input("Taxa de Negociação (%)", min_value = 10) / 100
#taxa_negociacao = st.sidebar.slider("Taxa de Negociação (%)", min = 0.05) / 100

#taxa_remuneracao = st.sidebar.slider("Taxa de Remuneração (%)", 0, 100, 5) / 100
taxa_remuneracao = st.sidebar.number_input("Taxa de Remuneração (%)", min_value = 5) / 100

# 2. Inputs de Volume e Assinatura
st.sidebar.subheader("Volume & Assinaturas")
# Aqui permitimos simular uma progressão (como as fases da planilha) ou um valor único
fases = ['Fase 1', 'Fase 2', 'Fase 3', 'Fase 4', 'Fase 5', 'Fase 6']
volumes_input = [10000, 20000, 30000, 40000, 50000, 60000] # Padrão da planilha
assinantes_input = [20, 30, 40, 50, 60, 70] # Padrão da planilha
# valor_assinatura = st.sidebar.number_input("Valor da Assinatura (R$)", value=600.0)

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
    receita_assinatura = ass_ajustado * ticket_mensal
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


# --- CORPO PRINCIPAL ---
st.title("📊 Modelo de Negócio: CompreUp")
st.markdown("---")

# NOVA SEÇÃO: DADOS DE MERCADO (Início da Página)
st.header("📌 Análise de Mercado e Público-Alvo")
col_m1, col_m2 = st.columns(2)

with col_m1:
    st.subheader("Público-Alvo (PMEs)")
    st.write("""
    O foco está em pequenas e médias empresas do **setor alimentício** que sofrem com baixo poder de negociação.
    - **Perfis Principais:** Padarias, mercados de bairro, restaurantes e lanchonetes.
    - **Dor Central:** Compras descentralizadas e falta de previsibilidade de preços[cite: 2].
    """)

with col_m2:
    st.subheader("Potencial de Mercado")
    st.write("""
    - **TAM (Brasil):** ~1,16 milhão de empresas no setor alimentício.
    - **SAM (Foco Inicial):** Empresas que faturam entre R$ 360k e R$ 4,8M/ano[cite: 86].
    - **Meta de Penetração:** Alcançar 1% do mercado (aprox. 11.600 clientes) em 5 anos[cite: 87].
    """)

st.success(f"**Insight:** O cenário atual de {num_clientes} clientes representa {((num_clientes/1160000)*100):.4f}% do mercado total brasileiro.")
st.markdown("---")

# Seção 1: Fontes de Receita
st.header("1. Fontes de Receita")
st.write("A estratégia de monetização da CompreUp foca na recorrência e transparência[cite: 63].")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Assinatura Mensal", value=f"R$ {ticket_mensal:,.2f}", delta="Por Cliente")
    st.caption("Principal fonte de receita atual[cite: 64].")
with col2:
    st.metric(label="Venda de Dados", value="Fase Futura")
    st.caption("Inteligência estratégica de mercado[cite: 65].")
with col3:
    st.metric(label="BPO de Compras", value="Fase Futura")
    st.caption("Terceirização de processos operacionais[cite: 66].")

st.info("**Diferencial Inovador:** A comissão do fornecedor é 100% revertida em desconto para o cliente[cite: 28].")

st.markdown("---")

# Seção 2: Simulador de Resultados Dinâmicos
st.header("2. Simulação de Modelo de Receita")
m1, m2, m3, m4 = st.columns(4)

m1.metric("Receita Bruta Mensal", f"R$ {receita_mensal:,.2f}")
m2.metric("Impostos (6%)", f"- R$ {impostos:,.2f}")
m3.metric("Custos (Var/Fixos)", f"- R$ {(custos_variaveis + custos_fixos):,.2f}")
m4.metric("Lucro Operacional", f"R$ {lucro_operacional:,.2f}", delta=f"{(lucro_operacional/receita_mensal)*100:.0f}% Margem")

st.subheader("Distribuição Financeira da Operação (R$)")
df_simulacao = pd.DataFrame({
    "Categoria": ["Impostos", "Custos Variáveis", "Custos Fixos", "Lucro Operacional"],
    "Valores": [impostos, custos_variaveis, custos_fixos, lucro_operacional]
})
st.bar_chart(data=df_simulacao, x="Categoria", y="Valores")

st.markdown("---")

# Seção 4: Estrutura de Custos (Dados do PDF)
# --- VISUALIZAÇÃO ---

# 1. KPIs do Cenário Atual (Baseado na Fase 1 como exemplo ou média)
col1, col2, col3 = st.columns(3)
col1.metric("Valor Negociado (Unit)", f"R$ {valor_negociado:.2f}")
col2.metric("Remuneração (Unit)", f"R$ {valor_remuneracao_unit:.2f}")
col3.metric("Ticket Assinatura", f"R$ {ticket_mensal:.2f}")

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


st.subheader("Comparativo de Modelos")
#chart_data = df_resultado("Valor Total da Remuneração (R$)")


# Definindo a quantidade de pedidos como o índice (eixo X do gráfico)
df_resultado.set_index("Fase", inplace=True)
df_selecao = df_resultado[['Receita Assinaturas (R$)' , "Valor Total da Remuneração (R$)"]]
st.line_chart(df_selecao)


# Seção 4: Estrutura de Custos (Dados do PDF)
st.header("3. Estrutura de Custos e Eficiência")
dados_custos = {
    "Categoria": ["Impostos", "Custos Variáveis", "Custos Fixos", "Margem Operacional"],
    "Percentual": [6, 10, 15, 69]
}
df_custos = pd.DataFrame(dados_custos)

col_graf, col_txt = st.columns([2, 1])
with col_graf:
    st.bar_chart(data=df_custos, x="Categoria", y="Percentual", color="Categoria")
with col_txt:
    st.subheader("Detalhamento [%]")
    for index, row in df_custos.iterrows():
        st.write(f"- **{row['Categoria']}:** {row['Percentual']}%")
    st.success("O modelo apresenta uma **Alta Margem Operacional**[cite: 71].")

st.markdown("---")

# Seção 5: Indicadores de Viabilidade
st.header("4. Indicadores de Viabilidade")
v1, v2, v3 = st.columns(3)
with v1: st.write("**EBITDA:** Positivo no 1º ano [cite: 99]")
with v2: st.write("**Payback Estimado:** ~1,6 anos [cite: 100]")
with v3: st.write("**ROI (5 anos):** ~496% [cite: 101]")

st.markdown("---")
st.caption("Documento de Referência: Modelo de Negócio CompreUp - Tecnologia em Compras B2B[cite: 1].")