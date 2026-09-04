import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="Autoavaliação de Accountability: Liderança por Contexto",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS Customizado
st.markdown("""
    <style>
    .main {
        background-color: #F8F9FA;
    }
    .stTitle {
        color: #1E1E1E;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 800;
    }
    .card-baixo {
        background-color: #FDF2E9;
        border-left: 5px solid #EA5B0C;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 10px;
    }
    .card-alto {
        background-color: #FEF9E7;
        border-left: 5px solid #F3B200;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 10px;
    }
    .metric-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #E0E0E0;
    }
    .perspective-box {
        background-color: #EBF5FB;
        border-left: 5px solid #2980B9;
        padding: 20px;
        border-radius: 6px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Dados do Modelo de Liderança por Contexto (Baseado nas Fontes)
elementos = [
    {
        "id": "abordagem",
        "nome": "1. Abordagem Resolutiva",
        "baixo_comportamento": "Temos um problema, mas demoramos para comunicá-lo. Rolamos ele até alguém considerar alarmante.",
        "alto_comportamento": "Quando temos um problema, atuamos de forma rápida para comunicá-lo e resolvê-lo!",
        "recomendacao": "Foque em criar canais rápidos e seguros para comunicação de desvios. Estimule a cultura de que identificar e reportar problemas cedo é melhor do que postergar soluções. Estabeleça rituais simples para reportar barreiras antes que se tornem críticas."
    },
    {
        "id": "resultado",
        "nome": "2. Responsável pela integralidade do Resultado",
        "baixo_comportamento": "Somos ágeis para encontrar justificativas, culpados e transferir responsabilidades.",
        "alto_comportamento": "Somos ágeis para encontrar em qual área/etapa aconteceu e o respectivo Responsável integral pelo resultado.",
        "recomendacao": "Redirecione o foco de 'quem errou' para 'como resolvemos'. Defina claramente os proprietários de ponta a ponta de cada processo e incentive parcerias multifuncionais para eliminar silos e transferências de culpa."
    },
    {
        "id": "causas",
        "nome": "3. Causas Sistêmicas",
        "baixo_comportamento": "A Liderança CC imprime unilateralidade, focando apenas o sujeito, não a Liderança e o Sistema Organizacional.",
        "alto_comportamento": "A Liderança por Contexto exemplifica Responsabilidade Mútua (Sujeito-Líder-Sistema Organizacional) e busca Causas Sistêmicas.",
        "recomendacao": "Pratique a responsabilidade mútua (Líder-Liderado-Sistema). Ao invés de focar apenas no erro individual, mapeie gargalos operacionais, nível de clareza das metas e se o suporte e recursos da liderança foram adequadamente fornecidos."
    },
    {
        "id": "autoridade",
        "nome": "4. Autoridade para Solucionar e Implementar",
        "baixo_comportamento": "Mesmo com a Solução, as barreiras feudais e burocráticas, irracionais, impedem a implementação efetiva e ágil.",
        "alto_comportamento": "Quando há Solução, o responsável possui autorização e condição racional para implementar de forma efetiva e ágil.",
        "recomendacao": "Identifique e reduza barreiras burocráticas ou 'feudos' organizacionais. Delegue autonomia de decisão real aos responsáveis diretos pelas entregas, garantindo que tenham legitimidade e ferramentas para agir rapidamente."
    },
    {
        "id": "aprendizagem",
        "nome": "5. Alta Aprendizagem do Sistema Organizacional",
        "baixo_comportamento": "Após erros importantes, a empresa não melhora o sistema operacional. Os aprendizados não são incorporados na forma de trabalhar.",
        "alto_comportamento": "Após erros importantes, a empresa melhora o sistema operacional. Os aprendizados são incorporados rapidamente na forma de trabalhar!",
        "recomendacao": "Institua rituais pós-incidente ou análises pós-morte (post-mortems) de forma não punitiva. Garanta que cada falha importante gere uma revisão documentada no processo ou ferramenta de trabalho para evitar reincidência."
    },
    {
        "id": "cultura",
        "nome": "6. Cultura de Responsabilidade e Confiança",
        "baixo_comportamento": "Os profissionais criam desconfiança porque vários líderes não respondem por suas responsabilidades e consequências.",
        "alto_comportamento": "Os profissionais confiam que todos respondem por suas responsabilidades e consequências.",
        "recomendacao": "Promova a transparência radical. Líderes devem ser os primeiros a assumir a responsabilidade e as consequências por suas decisões e resultados. Alinhe combinados e responsabilidades publicamente para gerar confiança mútua."
    }
]

# Título Principal e Header do App
st.title("🎯 LIDERANÇA POR CONTEXTO")
st.subheader("Modelo Resolutivo de Alto Accountability — Autoavaliação")

st.markdown("""
Este aplicativo interativo permite avaliar o nível de **Accountability** da sua liderança ou organização com base no modelo resolutivo de Eduardo Carmello. 
Abaixo, selecione para cada um dos 6 elementos a nota de **1 a 10** que melhor representa o seu cenário atual, considerando os extremos descritos à esquerda (baixo) e à direita (alto).
""")

# Barra Lateral com Informações Teóricas das Fontes
st.sidebar.image("https://raw.githubusercontent.com/streamlit/streamlit/master/lib/streamlit/static/favicon.png", width=50) # Placeholder para logo se houver
st.sidebar.title("Sobre o Accountability")
st.sidebar.markdown("""
**Alto Accountability:** 
Gera efetividade, agilidade e aceleração de resultados. Foca em reconhecer, assumir e agir sobre os desafios.

**Baixo Accountability:**
Gera apatia, desculpas e manutenção da medianidade. Foca em transferência de culpas e justificativas.

*Modelo baseado no material de Eduardo Carmello (Liderança por Contexto).*
""")

# Divisão em duas colunas: Esquerda para Inputs, Direita para Gráficos e Resultados
col_input, col_results = st.columns([1.1, 0.9])

valores_selecionados = {}

with col_input:
    st.markdown("### 📋 Avalie os 6 Elementos")
    
    for item in elementos:
        st.write("---")
        st.markdown(f"#### {item['nome']}")
        
        # Grid para mostrar os dois lados do comportamento
        col_b, col_a = st.columns(2)
        with col_b:
            st.markdown(f"<div class='card-baixo'><b>Baixo Accountability (1):</b><br>{item['baixo_comportamento']}</div>", unsafe_allow_html=True)
        with col_a:
            st.markdown(f"<div class='card-alto'><b>Alto Accountability (10):</b><br>{item['alto_comportamento']}</div>", unsafe_allow_html=True)
        
        # Slider de 1 a 10
        valor = st.slider(
            "Selecione o nível atual:",
            min_value=1,
            max_value=10,
            value=5,
            key=item['id']
        )
        valores_selecionados[item['id']] = valor

# Processamento e Gráficos na Coluna da Direita
with col_results:
    st.markdown("### 📊 Resultado da Avaliação")
    
    # Cálculo da pontuação total
    total_score = sum(valores_selecionados.values())
    max_possible = len(elementos) * 10
    
    # Classificação conforme as faixas de pontos especificadas no Carmello Accountability resolutivo.pdf
    classificacao = ""
    cor_faixa = ""
    descricao_faixa = ""
    
    if 57 <= total_score <= 60:
        classificacao = "Alto Accountability Organizacional"
        cor_faixa = "#2ECC71" # Verde
        descricao_faixa = "A responsabilidade tornou-se parte da cultura. Os resultados deixam de depender de heróis."
    elif 51 <= total_score <= 56:
        classificacao = "Liderança por Contexto Fortalecida"
        cor_faixa = "#27AE60" # Verde-escuro
        descricao_faixa = "A Liderança por Contexto já fortalece significativamente a execução. Os líderes criam clareza, responsabilidade e aprendizagem."
    elif 43 <= total_score <= 50:
        classificacao = "Práticas Isoladas / Variabilidade"
        cor_faixa = "#F39C12" # Laranja
        descricao_faixa = "Existem boas práticas isoladas. O accountability varia conforme cada gestor. O sistema ainda produz ambiguidades."
    else:
        classificacao = "Operação por Cobrança / Baixo Accountability"
        cor_faixa = "#C0392B" # Vermelho
        descricao_faixa = "A empresa opera predominantemente por cobrança. O accountability depende do esforço individual. Grande tendência à transferência de responsabilidades."
        
    # KPI Box
    st.markdown(f"""
        <div class='metric-box'>
            <span style='font-size: 16px; color: #7F8C8D; font-weight: bold; text-transform: uppercase;'>Pontuação Total</span>
            <h1 style='font-size: 64px; color: {cor_faixa}; margin: 10px 0;'>{total_score} <span style='font-size: 20px; color: #BDC3C7;'>/ {max_possible}</span></h1>
            <h3 style='color: {cor_faixa}; margin-top: 0;'>{classificacao}</h3>
            <p style='font-size: 14px; color: #555; font-style: italic; margin-bottom: 0;'>"{descricao_faixa}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # Gráfico de Gauge com Plotly
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = total_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Velocímetro de Accountability", 'font': {'size': 18}},
        gauge = {
            'axis': {'range': [0, 60], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': cor_faixa},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 42], 'color': '#FDEDEC'},
                {'range': [42, 50], 'color': '#FEF5E7'},
                {'range': [50, 56], 'color': '#E8F8F5'},
                {'range': [56, 60], 'color': '#D4EFDF'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 57
            }
        }
    ))
    fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_gauge, use_container_width=True)
    
    # Gráfico de Barras dos Elementos
    df_scores = pd.DataFrame({
        "Elemento": [item["nome"].split(". ")[1] for item in elementos],
        "Pontuação": [valores_selecionados[item["id"]] for item in elementos],
        "Cor": ["#F3B200" if valores_selecionados[item["id"]] >= 8 else "#EA5B0C" for item in elementos]
    })
    
    fig_bars = px.bar(
        df_scores,
        x="Pontuação",
        y="Elemento",
        orientation="h",
        title="Pontuação por Dimensão",
        range_x=[0, 10],
        color="Pontuação",
        color_continuous_scale=["#EA5B0C", "#F39C12", "#F3B200", "#2ECC71"]
    )
    fig_bars.update_layout(
        height=320,
        margin=dict(l=20, r=20, t=40, b=20),
        coloraxis_showscale=False,
        yaxis=dict(autorange="reversed")
    )
    st.plotly_chart(fig_bars, use_container_width=True)

# Seção de Perspectivas de Melhoria (Abaixo das colunas para ter largura total)
st.write("---")
st.markdown("### 🚀 Perspectivas de Melhoria & Plano de Ação")

# Recomendações personalizadas baseadas em pontuações baixas (< 8)
recomendacoes_ativas = []
for item in elementos:
    if valores_selecionados[item["id"]] < 8:
        recomendacoes_ativas.append(item)

if len(recomendacoes_ativas) > 0:
    st.markdown(f"Como você possui dimensões com nota inferior a **8**, aqui estão ações estratégicas para elevar o nível de Accountability nessas áreas:")
    for rec in recomendacoes_ativas:
        with st.expander(f"💡 Melhorando: {rec['nome']} (Nota Atual: {valores_selecionados[rec['id']]})"):
            st.markdown(f"**Cenário Atual Redutor:** *{rec['baixo_comportamento']}*")
            st.markdown(f"**Ação Recomendada:** {rec['recomendacao']}")
else:
    st.balloons()
    st.success("🎉 **Excelente!** Todas as suas dimensões estão com alta pontuação (8 ou mais). Continue promovendo e sustentando esse alto nível de Accountability na cultura organizacional!")

st.markdown("""
---
<p style='text-align: center; color: #7F8C8D; font-size: 12px;'>
Desenvolvido com 🧠 Gemini Notebook baseado no modelo Liderança por Contexto de Eduardo Carmello.
</p>
""", unsafe_allow_html=True)
