import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="CompreUp - Modelo de Negócio", layout="wide")

# --- SIDEBAR: SIMULADOR DE FATURAMENTO ---
st.sidebar.header("🛠️ Simulador de Escala")
st.sidebar.markdown("Ajuste os valores para projetar o cenário financeiro.")

# num_clientes = st.sidebar.slider("Quantidade de Clientes", min_value=1, max_value=15000, value=1160)
ticket_mensal = st.sidebar.number_input("Valor da Assinatura (R$)", value=600.0)
num_clientes = st.sidebar.number("Quantidade de Clientes", min_value=1)


# Cálculos do Simulador
receita_mensal = num_clientes * ticket_mensal
impostos = receita_mensal * 0.06
custos_variaveis = receita_mensal * 0.10
custos_fixos = receita_mensal * 0.15
lucro_operacional = receita_mensal - (impostos + custos_variaveis + custos_fixos)

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

# Seção 3: Estrutura de Custos (Dados do PDF)
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

# Seção 4: Indicadores de Viabilidade
st.header("4. Indicadores de Viabilidade")
v1, v2, v3 = st.columns(3)
with v1: st.write("**EBITDA:** Positivo no 1º ano [cite: 99]")
with v2: st.write("**Payback Estimado:** ~1,6 anos [cite: 100]")
with v3: st.write("**ROI (5 anos):** ~496% [cite: 101]")

st.markdown("---")
st.caption("Documento de Referência: Modelo de Negócio CompreUp - Tecnologia em Compras B2B[cite: 1].")