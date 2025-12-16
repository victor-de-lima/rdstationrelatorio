import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(
    page_title="Relatório de Migração - Marketing & Atendimento",
    page_icon="🚀",
    layout="wide"
)

# --- DADOS ---
# Cenário Atual
custos_atual = {
    "Chatguru": 703,
    "Gupshup": 1000,
    "Make": 45,
    "RD Station": 529
}
total_atual = sum(custos_atual.values())

# Cenário Proposto
custo_novo = 2700
ferramentas_novas = "RD Station + Gupshup (Integrados)"

# --- CABEÇALHO ---
st.title("🚀 Apresentação de Novo Projeto: Unificação de Atendimento")
st.markdown("---")

# --- SIDEBAR (Navegação) ---
st.sidebar.header("Navegação")
page = st.sidebar.radio("Ir para:", ["Visão Geral & Custos", "Análise Comparativa", "Conclusão"])

if page == "Visão Geral & Custos":
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔴 Cenário Atual (Fragmentado)")
        st.write(f"**Custo Mensal Total:** R$ {total_atual:,.2f}")
        
        # Exibindo os custos detalhados
        df_atual = pd.DataFrame(list(custos_atual.items()), columns=['Ferramenta', 'Custo (R$)'])
        st.dataframe(df_atual, hide_index=True, use_container_width=True)

        st.error("**Principais Desvantagens:**")
        st.markdown("""
        - ❌ **Sem ROI:** Não sabemos a efetividade dos disparos.
        - ❌ **Silos:** Uso exclusivo do Comercial (1 segmento).
        - ❌ **Complexidade:** Pagamento de 4 serviços diferentes.
        - ❌ **Dados:** Ausência de base unificada de clientes/leads.
        """)

    with col2:
        st.subheader("🟢 Cenário Proposto (Unificado)")
        st.write(f"**Custo Mensal Total:** R$ {custo_novo:,.2f}")
        st.info(f"**Ferramenta:** {ferramentas_novas}")
        
        st.success("**O que ganhamos com isso?**")
        st.markdown("""
        - ✅ **Base Unificada:** Centralização de clientes e leads.
        - ✅ **Inteligência:** Dashboards e painéis interativos em tempo real.
        - ✅ **Automação:** Chatbots avançados e fluxos automáticos.
        - ✅ **Escalabilidade:** Possibilidade de expansão para outros setores.
        """)

elif page == "Análise Comparativa":
    st.header("📊 Análise Financeira vs. Valor Agregado")
    
    # Preparando dados para gráficos
    diff = custo_novo - total_atual
    
    col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
    col_metrics1.metric("Investimento Atual", f"R$ {total_atual}")
    col_metrics2.metric("Investimento Proposto", f"R$ {custo_novo}")
    col_metrics3.metric("Diferença (Investimento)", f"R$ {diff}", delta=f"- R$ {diff} (Aumento)", delta_color="inverse")

    st.markdown("---")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Composição do Custo Atual")
        fig_pie = px.pie(values=list(custos_atual.values()), names=list(custos_atual.keys()), hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_chart2:
        st.subheader("Comparativo Direto")
        dados_comp = pd.DataFrame({
            "Cenário": ["Atual", "Proposto"],
            "Custo": [total_atual, custo_novo],
            "Benefícios Chave": ["4 Ferramentas Isoladas", "Plataforma Unificada"]
        })
        fig_bar = px.bar(dados_comp, x="Cenário", y="Custo", color="Cenário", text="Custo",
                         color_discrete_map={"Atual": "#EF553B", "Proposto": "#00CC96"})
        fig_bar.update_traces(texttemplate='R$ %{text:.2f}', textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)

elif page == "Conclusão":
    st.header("🎯 Veredito do Projeto")
    
    st.markdown(f"""
    ### O investimento vale a pena?
    
    Embora haja um aumento de **R$ {custo_novo - total_atual:.2f}** no custo mensal, a transição resolve as dores críticas da operação:
    
    1. **Fim da "Cegueira" de Dados:** Deixamos de gastar dinheiro sem saber o retorno (ROI).
    2. **Otimização de Processos:** Eliminamos a gestão de 4 faturas e conectores (como o Make) para ter tudo nativo.
    3. **Expansão:** O modelo atual limita o atendimento ao comercial. O novo modelo permite que o Suporte e Financeiro também utilizem a ferramenta no futuro.
    
    > **Recomendação:** Aprovação imediata para migração e setup do RD Station + Gupshup.
    """)
